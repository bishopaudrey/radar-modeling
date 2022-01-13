#!/usr/bin/env python
# coding: utf-8


import os      
import sys
import numpy as np


class Target:
    
    def __init__(self,pathToTargetFile):
        self.targetStateData = np.loadtxt(pathToTargetFile)
        (self.numberOfPoints,self.sizeOfState) = np.shape(self.targetStateData)
        
        self.time   = self.targetStateData[:,0]
        self.East   = self.targetStateData[:,1]
        self.North  = self.targetStateData[:,2]
        self.Up     = self.targetStateData[:,3]
        self.VEast  = self.targetStateData[:,4]
        self.VNorth = self.targetStateData[:,5]
        self.VUp    = self.targetStateData[:,6]
        self.AEast  = self.targetStateData[:,7]
        self.ANorth = self.targetStateData[:,8]
        self.AUp    = self.targetStateData[:,9]
        

    def GetState(self,time):
        state = np.zeros((self.sizeOfState,))
        for index in np.arange(self.sizeOfState):
            state[index] = np.interp(time, self.time, self.targetStateData[:,index])
            
        return np.append(np.array([time]),state)



    def IsTargetInBeam(self, boresightAzimuth,boresightElevation, diffractionAngleBeamAz, diffractionAngleBeamEl, targetPositionENU, debug):
        
        # From class and notes, the strat is to use cos(angle) = a/|a| (dot) b/|b|
        
        # convert target position to 
        targetPosNorm = np.linalg.norm(targetPositionENU)
        targetPosNormENUVector = targetPositionENU/targetPosNorm
        
        if debug:
            print("This should be 1.0: {}".format(np.linalg.norm(targetPosNormENUVector)))
        
        # forming the boresigth unit vector 
        eastBoresight   = 1.0 * np.sin(boresightAzimuth) * np.cos(boresightElevation)
        northBoresight  = 1.0 * np.cos(boresightAzimuth) * np.cos(boresightElevation)
        upBoresight     = 1.0 * np.sin(boresightElevation)
        boresightVector = np.array([eastBoresight,northBoresight,upBoresight])
        
        if debug:
            print("This should be 1.0: {}".format(np.linalg.norm(boresightVector)))
            print("Boresight East: {}, Boresight North {}, Boresigth Up {}".format(boresightVector[0],boresightVector[1],boresightVector[2]))
        
        # calulate the angle
        theta = np.arccos(np.dot(targetPosNormENUVector,boresightVector))
            
        if debug:
            print("Theta is: {}".format(theta))
        
        # compare to beam angle
        beamAngle = np.min(np.array([diffractionAngleBeamAz,diffractionAngleBeamEl]))
        if debug:
            print("Half of beamangle is: {}".format(beamAngle/2.0))
        
        
        if (theta < beamAngle/2.0):
            isInBeam = True
        else:
            isInBeam = False
            
        return isInBeam 

    def IsTargetInRange(self,PositionENU, PulseDuration, PRI):
        if (Detection.TargetRange < Detection.Rmax and Detection.TargetRange > Detection.Rmin):
            isInRange = True
        else:
            isInRange = False
        return isInRange   