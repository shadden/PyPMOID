import numpy as np
from ctypes import cdll,c_double,byref,POINTER
_libpath = "/Users/shadden/Projects/00_Codes_And_Data/MOID/PyMOID/"
clibmoid = cdll.LoadLibrary(_libpath + "libmoid.so")

_moid = clibmoid.moid_
_moid.restype = c_double
_moid.argtypes = [POINTER(c_double) for _ in range(10) ]

_myfunc = clibmoid.myfunc_
_myfunc.restype = c_double
_myfunc.argtypes = [POINTER(c_double)]

def myfunc(x):
    return _myfunc(byref(x))

def moid(saxisA,eccenA,argpeA,omegaA,incliA,saxisB,eccenB,argpeB,omegaB,incliB):
    """
    Calculate the minimum orbit intersection distance for a pair of orbits.
    
    Arguments
    ---------
    saxisA : float
      semi-major axis of body A
    eccenA : float
      eccentricity of body A
    argpeA : float
      Argument of pericenter for body A
    omegaA : float
      Longitude of ascending node for body A
    incliA : float
      Inclination of body A
    saxisB : float
      semi-major axis of body B
    eccenB : float
      eccentricity of body B
    argpeB : float
      Brgument of pericenter for body B
    omegaB : float
      Longitude of ascending node for body B
    incliB : float
      Inclination of body B

    Returns
    -------
    moid : float
     Value of the minimum orbit intersection distance.
    """
    try:
        aA,eA,omegaA,OmegaA,IA=[c_double(x) for x in (saxisA,eccenA,argpeA,omegaA,incliA)]
        aB,eB,omegaB,OmegaB,IB=[c_double(x) for x in (saxisB,eccenB,argpeB,omegaB,incliB)]
        val = _moid(aA,eA,omegaA,OmegaA,IA,aB,eB,omegaB,OmegaB,IB)
        return val
    except:
        raise ValueError("MOID failed.")

def moid_from_simulation(sim,indexA=1,indexB=2):
    """
    Calculate MOID for a pair of rebound particles.

    Arguments
    ---------
    sim : rebound.Simulation
      Simulation object with particles.
    indexA : int
      Index of particle A for MOID calculation
    indexB : int
      Index of particle B for MOID calculation

    Returns
    -------
    moid : float
     Value of the minimum orbit intersection distance.
    """
    star = sim.particles[0]
    pA,pB = sim.particles[indexA], sim.particles[indexB] 
    oA = pA.calculate_orbit(primary=star)
    oB = pB.calculate_orbit(primary=star)
    aA,eA,omegaA,OmegaA,IA = oA.a, oA.e, oA.omega, oA.Omega, oA.inc
    aB,eB,omegaB,OmegaB,IB = oB.a, oB.e, oB.omega, oB.Omega, oB.inc
    return moid(aA,eA,omegaA,OmegaA,IA,aB,eB,omegaB,OmegaB,IB)
