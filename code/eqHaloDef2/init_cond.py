# Slightly more advanced initial conditions.
# Goal is to correct last eqHaloDef test and create stars by increasing the particle count 
# and hopefully the density
from pyICs.density_profiles import *
from pyICs.am_profiles import *
from pyICs.equilibrium_halos import *
from pyICs.tools import *

sim = EquilibriumHalo(fname = "halo2.out", n_particles = 1e7)
sim.make_halo()
sim.finalize()