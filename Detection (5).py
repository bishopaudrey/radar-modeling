import numpy as np
import scipy as sp
import scipy.constants as spc
import scipy.special as sps

class RadarFormulas:
        
    def __init__(self, RadarInputs):
        self.RadarInputs = RadarInputs
        
    def SNR(self, R):    
        debug = False
        # Loss = np.power(10,self.RadarInputs.AtmosphericLoss*R/10000)
        Loss = (2*self.RadarInputs.AtmosphericLoss*R)
        self.Pr = self.RadarInputs.PeakPower*(self.RadarInputs.AntennaGain**2)*(self.RadarInputs.Wavelength**2)*self.RadarInputs.Target_RCS
        self.Pn = ((4*spc.pi)**3)*(R**4)*Loss*spc.Boltzmann*self.RadarInputs.StandardTemperature*self.RadarInputs.NoiseFigure*self.RadarInputs.BandwidthOfPulse
        
        if debug:
            print("Range to Target: {} \n".format(R))
            print("Atm loss calculated as: {} \n".format(Loss))
            print("Numerator calculated as: {} \n".format(self.Pr))
            print("Denominator calculated as : {}\n".format(self.Pn))
        
        return self.Pr/self.Pn
        
    def TargetRange (self):
        # PositionEast = PositionENU [:,1]
        # PositionNorth = PositionENU [:,2]
        # PositionUp = PositionENU [:,3]
        # TargetRange=np.sqrt(PositionEast**2 + PositionNorth**2 + PositionUp**2) * 180/math.pi
    
        self.RangeMinimum = (spc.c * (self.RadarInputs.PulseWidth))/2
        self.RangeMaximum = (spc.c * (self.RadarInputs.PulseRepInterval - self.RadarInputs.PulseWidth))/2
        self.RangeResolution = (spc.c * (self.RadarInputs.PulseRepInterval - self.RadarInputs.PulseWidth))/2
          
    
class Detection: 
    
    def __init__(self, RadarInputs, Helper):
        self.RadarInputs = RadarInputs
        self.Help = Helper
        
        self.rangeUncertanty = 0.5 * spc.c * self.RadarInputs.PulseWidth
        
        self.beamAzimuthDefractionAngle_rad = 2 * self.RadarInputs.Wavelength/self.RadarInputs.AntennaHeight   
        self.beamElevationDefractionAngle_rad = 2 * self.RadarInputs.Wavelength/self.RadarInputs.AntennaWidth   
        
        self.azimuthUncertanty = self.beamAzimuthDefractionAngle_rad
        self.elevationUncertanty = self.beamElevationDefractionAngle_rad
        
    def SetProbOfDetection(self, SNR):           
        argument = sps.erfi(1.0 - 2.0 * self.RadarInputs.ProbabilityOfFalse_Alarm - np.sqrt(SNR/2.0))
        self.probOfDetection = 0.5 * (1.0 - sps.erf(argument))
        
    def GetProbOfDetection(self, SNR):
        self.SetProbOfDetection(SNR)
        return self.probOfDetection
          
    def IsDetected(self, prob):
        sample = np.random.random_sample()
        # print(sample, prob)
        if sample < prob:
            detected = True
        else:
            detected = False
        return detected
          
    def GenerateMeasurement(self, targetPositionENU):
        targetPositionRAE = self.Help.convertENU2RAE1d(targetPositionENU)
        rangeError = self.rangeUncertanty * (np.random.random_sample() -0.5)
        azimuthError = self.azimuthUncertanty * (np.random.random_sample() -0.5)
        elevationError = self.elevationUncertanty * (np.random.random_sample() - 0.5)
              
        rangeSample = targetPositionRAE[0] + rangeError
        azimuthSample = targetPositionRAE[1] + azimuthError
        elevationSample = targetPositionRAE[2] + elevationError
        measurement = np.array([azimuthSample,elevationSample,rangeSample])
            
        return measurement
          
    def TestDetection(self,prob,numberOfSamples):
        samples = np.empty((numberOfSamples,1))
        for index in np.arange(numberOfSamples):
            samples[index] = self.IsDetected(prob)
        print("For Exact Prob: {}, Function Sample Prob is {}".format(prob,sum(samples)/numberOfSamples))

          