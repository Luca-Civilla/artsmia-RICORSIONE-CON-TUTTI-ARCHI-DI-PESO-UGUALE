from model.model import Model
myModel = Model()
myModel.buildGraph("Photograper")
nodi,archi = myModel.graphDetails()
print(nodi)
print(f"archi sono {archi}")