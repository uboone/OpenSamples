import numpy as np

def nplanes():
    return 3

def nwires(p):
    if p==0: return 2400
    elif p==1: return 2400
    elif p==2: return 3456
    else: raise RuntimeError('plane %i is out of range'%p)

def ntimeticks():
    return 6400

def nopdets():
    return 32

def wireStartPosPlane0(w):
    if w<0 or w>=2400: raise RuntimeError('wire %i is out of range'%w)
    return [0,np.maximum(117.153-0.34641*w,-115.505),np.maximum(-402.941+0.6*w,0.0352608)]

def wireEndPosPlane0(w):
    if w<0 or w>=2400: raise RuntimeError('wire %i is out of range'%w)
    return [0,np.minimum(715.8006-0.34640*w,117.445),np.minimum(0.541+0.6*w,1036.96)]

def wireStartPosPlane1(w):
    if w<0 or w>=2400: raise RuntimeError('wire %i is out of range'%w)
    return [-0.3,np.minimum(-115.213+0.34641*w,117.445),np.maximum(-402.941+0.6*w,0.0352608)]

def wireEndPosPlane1(w):
    if w<0 or w>=2400: raise RuntimeError('wire %i is out of range'%w)
    return [-0.3,np.maximum(-713.8606+0.34640*w,-115.505),np.minimum(0.541+0.6*w,1036.96)]

def wireStartPosPlane2(w):
    if w<0 or w>=3456: raise RuntimeError('wire %i is out of range'%w)
    return [-0.6,-115.53,0.25+0.3*w]

def wireEndPosPlane2(w):
    if w<0 or w>=3456: raise RuntimeError('wire %i is out of range'%w)
    return [-0.6,117.47,0.25+0.3*w]

def wireStartPos(p,w):
    if p==0: return wireStartPosPlane0(w)
    elif p==1: return wireStartPosPlane1(w)
    elif p==2: return wireStartPosPlane2(w)
    else: raise RuntimeError('plane %i is out of range'%p)

def wireEndPos(p,w):
    if p==0: return wireEndPosPlane0(w)
    elif p==1: return wireEndPosPlane1(w)
    elif p==2: return wireEndPosPlane2(w)
    else: raise RuntimeError('plane %i is out of range'%p)

def doWiresCross(p1,w1,p2,w2):
    if p1==p2: return False

    s1 = wireStartPos(p1,w1)
    e1 = wireEndPos(p1,w1)
    s2 = wireStartPos(p2,w2)
    e2 = wireEndPos(p2,w2)

    if s1[2]<s2[2] and s1[2]<e2[2] and e1[2]<s2[2] and e1[2]<e2[2]: return False
    if s1[2]>s2[2] and s1[2]>e2[2] and e1[2]>s2[2] and e1[2]>e2[2]: return False
        
    return True

# from https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
def wireCrossingYZ(p1,w1,p2,w2):

    if p1==p2: raise RuntimeError('Wires on same plane do not cross. Please check if they cross with doWiresCross().')
    
    s1 = wireStartPos(p1,w1)
    e1 = wireEndPos(p1,w1)
    s2 = wireStartPos(p2,w2)
    e2 = wireEndPos(p2,w2)

    if s1[2]<s2[2] and s1[2]<e2[2] and e1[2]<s2[2] and e1[2]<e2[2]: 
        raise RuntimeError('Wires do not cross within the detector volume. Please check if they cross with doWiresCross().')
    if s1[2]>s2[2] and s1[2]>e2[2] and e1[2]>s2[2] and e1[2]>e2[2]: 
        raise RuntimeError('Wires do not cross within the detector volume. Please check if they cross with doWiresCross().')

    a1 = np.array([s1[1],s1[2]])
    a2 = np.array([e1[1],e1[2]])
    b1 = np.array([s2[1],s2[2]])
    b2 = np.array([e2[1],e2[2]])
    
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = np.empty_like(da)
    dap[0] = -da[1]
    dap[1] = da[0]
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )
    return ((num / denom.astype(float))*db + b1).tolist()

def isPosInActiveVolume(x,y,z):
    #approximated
    if x<0 or x>255: return False
    if y<-116 or y>116: return False
    if z<10 or z>1036: return False
    return True

def tpcTimeToX(t):
    time2cm=0.0548965 #accounts for sampling and drift velocity
    trigOffset=800
    return (t-trigOffset)*time2cm

def barycenter(x,w):
    return (x*w).sum()/w.sum()

def width(x,w):
    return np.sqrt(((w*x*x).sum()*w.sum() - (w*x).sum()*(w*x).sum()))/w.sum()

import enum
class category(enum.Enum):
    pion = 0
    muon = 1
    kaon = 2
    proton = 3
    electron = 4
    michel = 5
    delta = 6
    other = 7
    photon = 8
