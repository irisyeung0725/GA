#The Grand Prix Transportation Problem

#Import PuLP library
from pulp import *

#Input data
#Create a list plants
PLANTS = ["Plant1", "Plant2", "Plant3"]
#Create a list of regions
REGIONS = ["Region1", "Region2", "Region3", "Region4"]
#Create a dictionary of unit cost
shippingCost = { "Plant1" : {"Region1" : 131, "Region2" : 218, "Region3" : 266, "Region4" : 120},
          		 "Plant2" : {"Region1" : 250, "Region2" : 116, "Region3" : 263, "Region4" : 278},
          		 "Plant3" : {"Region1" : 178, "Region2" : 132, "Region3" : 122, "Region4" : 188}}
#Set contraints
#Create a dictionary of constraints of supply
supply = {"Plant1": 450,
          "Plant2": 600,

          "Plant3": 500}
#Create a dictionary of constraints of demand
demand = {"Region1": 450,
          "Region2": 200,
          "Region3": 300,
          "Region4": 300}
#Create "prob" instance to contain problem data, and set objective as "minimize"
prob = LpProblem("Grand_Prix_Transportation", LpMinimize)

#Create list of tuples (pairs) containing all possible routes for transport
#Note1: Route pairs are only for transportation problems;
#Note2: Other problems may use standard variables

#Routes = [(i,j) for i in PLANTS for j in REGIONS]
Routes = [] #Create an empty list
for i in PLANTS: #Two dimensional list
	for j in REGIONS:
		myTuple = (i, j)
		Routes.append(myTuple)

#Dictionary called "vars" is created to contain referenced variables (routes)
#These variables are precisely the amount of flow (units shipped) on each route
Vars = LpVariable.dicts("Route", (PLANTS,REGIONS), 0, None, LpInteger)


#The objective function is added to "prob" first

# prob += lpSum([Vars[i][j]*shippingCost[i][j] for (i,j) in Routes]), "Sum_of_Shipping_Costs"
sumList = [] #Create an empty list 
for (i,j) in Routes:
	combinations = Vars[i][j]*shippingCost[i][j]
	#Use append() function to append new element to a list that was created earlier. For more information visit https://docs.python.org/3/library/array.html?highlight=append#array.array.append
	sumList.append(combinations) #A list of tuples
prob += lpSum(sumList), "Sum_of_Shipping_Costs"


# Upper "supply" bounds are added to "prob" for each supply node i (plant)

#for i in PLANTS:
#    prob += lpSum([Vars[i][j] for j in REGIONS]) <= supply[i], "Sum_of_Products_out_of_Plant_%s"%i
for i in PLANTS:
	supplyList = [] #Create a list for each plant containing 4 regions
	for j in REGIONS:
		supplyList.append(Vars[i][j])
	prob += lpSum(supplyList) <= supply[i], "Sum_of_Products_out_of_Plant_%s"%i
	print(type(lpSum(supplyList) <= supply[i]))
	print(type(prob))


#Lower "demand" bounds are added to "prob" for each demand node j (region)
#NOTE: This could also be done strictly as equality constraint "=="

# for j in REGIONS:
#     prob += lpSum([Vars[i][j] for i in PLANTS]) == demand[j], "Sum_of_Products_into_Region_%s"%j
for j in REGIONS:
	demandList = [] #Create a list for each region cotaining 3 plants
	for i in PLANTS:
		demandList.append(Vars[i][j])
	prob += lpSum(demandList) >= demand[j], "Sum_of_Products_into_Region_%s"%j
                   

#The problem data is written to an .lp file, so it is human-readable :)
prob.writeLP("GrandPrixTransportationProblem.lp")

prob.solve() #The problem is solved using PuLP's choice of Solver (usually CBC)
#prob.solve(COIN_CMD(msg=1)) #Solve using CBC with logging
#prob.solve(GUROBI_CMD()) #Solve using Gurobi (if installed) with no logging
#prob.solve(CPLEX_CMD()) #Solve using Gurobi (if installed) with no logging
#Other solvers, such a GUROBI (not GUROBI_CMD) will only work with the "Python (external)" language

#The status of the solution is printed to the screen
print("Status: ", LpStatus[prob.status])


print("--------FINAL SOLUTION---------") #Print the line "--------FINAL SOLUTION---------"
#The optimal objective function value is printed to the screen  
print("Total Cost of Transportation = $" + str(value(prob.objective)))
#Each of the variables is printed with it's optimal value
for v in prob.variables():
	if v.varValue: #When the value is not 0 (0 equals to False in Python)
		print("Ship %d" % v.varValue + " to %s" % v.name)
