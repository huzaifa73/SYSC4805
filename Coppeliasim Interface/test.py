import time
import zmq

client = RemoteAPIClient()
sim = client.getobject('sim')
client.setstepping(True)

sim.startSimulation()
while (t := sim.getSimulationTime()) < 3:
    s = f'Simulation time: {t:.2f} [s]'
    print(s)
    client.step()
sim.stopSimulation()