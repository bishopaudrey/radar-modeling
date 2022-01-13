import numpy as np

class Helper:
    
    def __init__(self):
        pass
    
    def ENU (self, data):
        self.east=data[:,1]
        self.north=data[:,2]
        self.up=data[:,3]
        ENU = [self.east, self.north, self.up]
        return ENU
    
    def ENU2RAE (self):
        self.range=np.sqrt(self.east**2 + self.north**2 + self.up**2)
        self.azimuth=np.arctan2(self.east,self.north) * 180/np.pi
        self.elevation=np.arctan(self.up/np.sqrt(self.east**2+self.north**2)) * 180/np.pi
        RAE = [self.range, self.azimuth, self.elevation]
        return RAE
    
    def convertENU2RAE(self, ENU):
        
        self.range=np.sqrt(ENU[:,0]**2 + ENU[:,1]**2 + ENU[:,2]**2)
        self.azimuth=np.arctan2(ENU[:,0],ENU[:,1]) * 180/np.pi
        self.elevation=np.arctan(ENU[:,2]/np.sqrt(ENU[:,0]**2+ENU[:,1]**2)) * 180/np.pi
        RAE = [self.range, self.azimuth, self.elevation]
        return RAE
    
    def convertENU2RAE1d(self, ENU): # Coming out degrees
        
        self.range=np.sqrt(ENU[0]**2 + ENU[1]**2 + ENU[2])
        self.azimuth=np.arctan2(ENU[0],ENU[1]) * 180/np.pi
        self.elevation=np.arctan(ENU[2]/np.sqrt(ENU[0]**2+ENU[1]**2)) * 180/np.pi
        RAE = [self.range, self.azimuth, self.elevation]
        return RAE
    
    def convertRAE2ENU(self, RAE):
        
        self.east = RAE[:,0] * np.sin(RAE[:,1])*np.cos(RAE[:,2])
        self.north = RAE[:,0] * np.cos(RAE[:,1])* np.cos(RAE[:,2])
        self.up = RAE[:,0] * np.sin(RAE[:,2])
        
    def convertRAE2ENU1d(self, RAE):
        
        self.east = RAE[0] * np.sin(RAE[1])*np.cos(RAE[2])
        self.north = RAE[0] * np.cos(RAE[1])* np.cos(RAE[2])
        self.up = RAE[0] * np.sin(RAE[2])
        ENU = [self.east, self.north, self.up]
        return ENU
        
    def WavelengthCalculation (frequency_hz):
        return spc.c/frequency_hz      
    
    def GetMaxandMin_Deg (RAE):
        azimuth_min = azimuth.min()
        azimuth_max = azimuth.max()
        elevation_min = elevation.min()
        elevation_max = elevation.max()
        return [azimuth_min, azimuth_max, elevation_min, elevation_max]

    def GetMaxandMin_Rad (RAE_deg):
        azimuth_min = np.deg2rad(azimuth_min_deg)
        azimuth_max = np.deg2rad(azimuth_max_deg)
        elevation_min = np.deg2rad(elevation_min_deg)
        elevation_max = np.deg2rad(elevation_max_deg)
        return [azimuth_min, azimuth_max, elevation_min, elevation_max] 
    
    def GetRange (self, ENU):
        return np.sqrt(ENU[0]**2 + ENU[1]**2 + ENU[2]**2)
