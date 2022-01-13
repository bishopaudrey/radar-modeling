#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:42:24 2021

@author: dcargill
"""
import Helper
import numpy as np



class Logging:
    
    def __init__(self,logFile, Helper):
        
        self.logFile = logFile
        self.entries = []
        self.help = Helper
                
    def LogDetection(self, time, measurement, snr, probOfDet, targetPos):
        
        loggingType = 1
        
        measurementENU       = self.help.convertRAE2ENU1d(measurement)
    
        azimuthMeasurement   = measurement[0]
        elevationMeasurement = measurement[1]
        rangeMeasurement     = measurement[2]
        eastMeasurement      = measurementENU[0]
        northMeasurement     = measurementENU[1]
        upMeasurement        = measurementENU[2]
        
        targetPosAER         = self.help.convertENU2RAE1d(targetPos)
        
        azimuthTarget    = targetPosAER[0]
        elevationTarget  = targetPosAER[1]
        rangeTarget      = targetPosAER[2]
        eastTarget       = targetPos[0]
        northTarget      = targetPos[1]
        upTarget         = targetPos[2]
        
        
        entry = [loggingType,time,azimuthMeasurement,
                             elevationMeasurement,
                             rangeMeasurement,
                             eastMeasurement,
                             northMeasurement,
                             upMeasurement,
                             snr,probOfDet,
                             azimuthTarget,
                             elevationTarget,
                             rangeTarget,
                             eastTarget,
                             northTarget,
                             upTarget]
        
        self.Log(entry)

        
    def LogFalseAlarm(self, time, measurement, snr, probOfDet, targetPos):
        
        loggingType = 2
        
        measurementENU       = self.help.convertRAE2ENU1d(measurement)
    
        azimuthMeasurement   = measurement[0]
        elevationMeasurement = measurement[1]
        rangeMeasurement     = measurement[2]
        eastMeasurement      = measurementENU[0]
        northMeasurement     = measurementENU[1]
        upMeasurement        = measurementENU[2]
        
        targetPosAER         = self.help.convertENU2RAE1d(targetPos)
        
        azimuthTarget    = targetPosAER[0]
        elevationTarget  = targetPosAER[1]
        rangeTarget      = targetPosAER[2]
        eastTarget       = targetPos[0]
        northTarget      = targetPos[1]
        upTarget         = targetPos[2]
    
        entry = [loggingType,time,azimuthMeasurement,
                             elevationMeasurement,
                             rangeMeasurement,
                             eastMeasurement,
                             northMeasurement,
                             upMeasurement,
                             snr,probOfDet,
                             azimuthTarget,
                             elevationTarget,
                             rangeTarget,
                             eastTarget,
                             northTarget,
                             upTarget]
        
        self.Log(entry)
            
            
        
    def LogMiss(self, time, snr, probOfDet, targetPos):
        
        loggingType = 3
            
        azimuthMeasurement   = 0
        elevationMeasurement = 0
        rangeMeasurement     = 0
        eastMeasurement      = 0
        northMeasurement     = 0
        upMeasurement        = 0
                
        targetPosAER         = self.help.convertENU2RAE1d(targetPos)
        
        azimuthTarget    = targetPosAER[0]
        elevationTarget  = targetPosAER[1]
        rangeTarget      = targetPosAER[2]
        eastTarget       = targetPos[0]
        northTarget      = targetPos[1]
        upTarget         = targetPos[2]
    
        entry =[loggingType,time,azimuthMeasurement,
                             elevationMeasurement,
                             rangeMeasurement,
                             eastMeasurement,
                             northMeasurement,
                             upMeasurement,
                             snr,probOfDet,
                             azimuthTarget,
                             elevationTarget,
                             rangeTarget,
                             eastTarget,
                             northTarget,
                             upTarget]
        self.Log(entry)


        
        
    def Log(self,entry):
        
        if len(self.entries) == 0:
            self.entries = [entry]
        else:
            self.entries.append(entry)
        
        

    def PrintLog(self):
        
        print(self.entries)
        
    def WriteLog(self):
        np.savetxt(self.logFile, np.array(self.entries), fmt='%6.16f',
                                                    delimiter=' ', 
                                                    newline='\n', 
                                                    header= '',#fileHeader,                                                                 footer='',
                                                    comments='', 
                                                    encoding=None)
