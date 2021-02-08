import rebound as rb
from PyMOID import moid_from_simulation

# Mercury-Venus MOID
sim = rb.Simulation()
sim.add('Sun')
sim.add('Mercury')
sim.add('Venus')
sim.move_to_com()
moid_val = moid_from_simulation(sim)
print("Mercury-Venus MOID value is {} AU".format(moid_val))
