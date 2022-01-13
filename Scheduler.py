import numpy as np

class Antenna:
    
    def __init__(self, wavelength, length, width):
        
        self.wavelength = wavelength
        self.arraylength_m = length
        self.arraywidth_m = width
        
class Scheduler:
    
    def __init__(self, antenna, minEl, maxEl, minAz, maxAz):
        
        self.antenna = antenna 
        self.minEl_deg = minEl
        self.minEl_rad = np.deg2rad(minEl)
        
        self.maxEl_deg = maxEl
        self.maxEl_rad = np.deg2rad(maxEl)
        
        self.minAz_deg = minAz
        self.minAz_rad = np.deg2rad(minAz)
        
        self.maxAz_deg = maxAz
        self.maxAz_rad = np.deg2rad(maxEl)
         
    
        self.firstCall = True
        self.currentAzimuthIndex = 0
        self.currentElevationIndex = 0
        
        self.SetBeamElevationDiffractionAngle()
        self.DeltaElevation()
        self.SetNumberOfElevationPoints()
        self.SetElevationPoints() 

        self.SetBeamAzimuthDiffractionAngle()
        self.DeltaAzimuth()
        self.SetNumberOfAzimuthPoints()
        self.SetAzimuthPoints()
           
    def SetBeamElevationDiffractionAngle(self):
        self.beamElevationDefractionAngle_rad = 2 * self.antenna.wavelength/self.antenna.arraywidth_m   
        self.beamElevationDefractionAngle_deg = np.rad2deg(self.beamElevationDefractionAngle_rad)
        
    def DeltaElevation(self):
        self.DeltaElevation_deg = self.maxEl_deg - self.minEl_deg
        self.DeltaElevation_rad = self.maxEl_rad - self.minEl_rad
        
    def SetNumberOfElevationPoints(self):
        self.NumberOfElevationPoints = np.ceil(self.DeltaElevation_deg/self.beamElevationDefractionAngle_deg)
        
    def SetBeamAzimuthDiffractionAngle(self):
        self.beamAzimuthDefractionAngle_rad = 2 * self.antenna.wavelength/self.antenna.arraylength_m   
        self.beamAzimuthDefractionAngle_deg = np.rad2deg(self.beamAzimuthDefractionAngle_rad)
        
    def DeltaAzimuth(self):
        self.DeltaAzimuth_deg = self.maxAz_deg - self.minAz_deg
        self.DeltaAzimuth_rad = self.maxAz_rad - self.minAz_rad
        
    def SetElevationPoints(self):   #(e_k)
        k = int(self.NumberOfElevationPoints)
        self.ElevationPoints = []
        for i in range (1, k+1):
            e = self.minEl_rad + i * ( 2 * self.antenna.wavelength / self.antenna.arraywidth_m)
            self.ElevationPoints.append(e)
            
    def SetNumberOfAzimuthPoints(self):    #(j_ek)
        self.NumberOfAzimuthPoints = []
        for i in (self.ElevationPoints):
            self.NumberOfAzimuthPoints.append(np.ceil((self.DeltaAzimuth_rad*self.antenna.arraylength_m*np.cos(i))/(2*self.antenna.wavelength))) 

    def SetAzimuthPoints(self):     #(aj_ek)
        self.AzimuthPoints = []
        for j in (self.NumberOfAzimuthPoints):
            # print("NumberOfAzimuthPoints: {}".format(j))
            azimuthPointsAtElevation = []
            for k in np.arange(j):
                # print("AzIndex: {}".format(k))
                az = self.minAz_rad + k*((2 * self.antenna.wavelength)/(self.antenna.arraylength_m))
                azimuthPointsAtElevation.append(az)
            self.AzimuthPoints.append(azimuthPointsAtElevation)
    
    def GetNextPoint(self, debug):     # Carg
        
        if self.firstCall == True:
            self.firstCall = False
            if debug:
                print("current Az and El indicies: ({}, {})".format(self.currentAzimuthIndex, self.currentElevationIndex))
                return (self.AzimuthPoints[self.currentElevationIndex][self.currentAzimuthIndex], self.ElevationPoints[self.currentElevationIndex])
        
        else:
            if self.currentAzimuthIndex == self.NumberOfAzimuthPoints[self.currentElevationIndex]-1:
            # at last Az Index point
                self.currentAzimuthIndex = 0
            
                if self.currentElevationIndex == self.NumberOfElevationPoints-1:
                    # at last Az and last El Index point
                    self.currentElevationIndex = 0
                    
                else:
                    # at the last Az Index but not last El Index
                    self.currentElevationIndex = self.currentElevationIndex + 1
            else:
                # Not as last Az 
                self.currentAzimuthIndex = self.currentAzimuthIndex + 1

        if debug:
            print("current Az and El indicies: ({}, {})".format(self.currentAzimuthIndex, self.currentElevationIndex))
    
        return (self.AzimuthPoints[self.currentElevationIndex][self.currentAzimuthIndex], self.ElevationPoints[self.currentElevationIndex])  
            
            

        
