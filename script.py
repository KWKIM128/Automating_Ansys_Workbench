# Finding the failing stress
# copy paste this code to ansys script

Model = ExtAPI.DataModel.Project.Model
Geometry = Model.Geometry
Material = Model.Materials
CS = Model.CoordinateSystems
Mesh = Model.Mesh
Static_Sol = Analysis.Solution
UTS = 45 # in MPa. 

# inital force
Force = -700 # change to the force to the value you found but don't change the negative sign
Fmax = -2000

# Do not change code below
while(Force < Fmax):
    Load = Analysis.AddForce()
    Load.Location = ExtAPI.DataModel.GetObjectsByName("Load")[0]
    Load.DefineBy = LoadDefineBy.Components
    Load.XComponent.Output.SetDiscreteValue(0, Quantity(Force, "N"))
   
    Eqv = Static_Sol.AddEquivalentStress()
    Static_Sol.Solve(True)
