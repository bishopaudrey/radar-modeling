import numpy as np 
import scipy as sp
import scipy.constants as spc

def db2Lin(x):
    return 10**(x/10)

class RadarInputs:

    def __init__(self):

        self.Radarfrequency = 2e9 #Hz
        self.Wavelength = spc.c/self.Radarfrequency
        self.DutyCycle = .10 # 10%
        self.AveragePower = 100 #Watts
        self.PeakPower = self.AveragePower/self.DutyCycle
        self.PulseWidth = 1e-6 #sec
        self.PulseRepInterval = 10000*self.PulseWidth/self.DutyCycle
        self.PulseRepFrequency = 1/self.PulseRepInterval
        self.AntennaGain_db = 40 #unitless
        self.AntennaGain = db2Lin(self.AntennaGain_db)
        self.AtmosphericLoss = 0.02 
        self.ProbabilityOfFalse_Alarm = 10e-6 
        self.DetectionProbability = 0.85
        self.EffectiveSystemTemperature = 987 #Kelvin
        self.AntennaWidth = 3.0 # m
        self.AntennaHeight = 5.5 # m
        self.ProcessingTime = 0.01 # sec
        self.Target_RCS_dBsm = -5 #-10 - -5 #dBsm # Radar Cross Section
        self.Target_RCS = db2Lin(self.Target_RCS_dBsm)
        # self.Target_RCS_sm = 0.1 # m**2
        self.StandardTemperature = 290 #T(0) and Kelvin
        self.NoiseFigure = self.EffectiveSystemTemperature/self.StandardTemperature  # F 
        self.BandwidthOfPulse = 1/self.PulseWidth  # B(p)

    
