import numpy as np

class IsInBeam:

    def __init__(self):
        pass

    def IsTargetInBeam(self, boresightAzimuth, boresightElevation, SetBeamAzimuthDefractionAngle, SetBeamElevationDefractionAngle, targetPositionENU):

        # cos(theta) = a/a (dot) b/b
    
        # convert target position to 
        targetPosNorm = np.linalg.norm(targetPositionENU)
        targetPosNormVector = targetPositionENU/targetPosNorm
    
        # forming the boresight unit vector 
        eastBoresight = 1.0 * np.sin(boresightAzimuth) * np.cos(boresightElevation)       # 1.0 = rad so no normalize necessary
        northBoresight = 1.0 * np.cos(boresightAzimuth) * np.cos(boresightElevation)
        upBoresight = 1.0 * np.sin(boresightElevation)
        boresightVector = np.array([eastBoresight, northBoresight, upBoresight])
    
        # calc the angle (we have to take dot and arccos)
        theta = np.arccos(targetPosNormVector.dot(boresightVector))
    
        # Compare to beam angle (compare to the smaller of the two angles?)    
        # Return true or false
        beamAngle = min(SetBeamAzimuthDefractionAngle,SetBeamElevationDefractionAngle)
    
        if (theta < beamAngle/2.0) :
            isInBeam = True
        else:
            isInBeam = False
        
        return isInBeam    

    def IsTargetInRange(self, targetRange, Rmin, Rmax):
        if (targetRange < Rmax and targetRange > Rmin):
            isInRange = True
        else:
            isInRange = False
        return isInRange   