from pulp import *

# Creates a list of all the supply nodes
Warehouses = ["A","B"]

# Creates a dictionary for the number of units of supply for each supply node
supply = {"A": 1000,
        "B": 4000}

# Creates a list of all demand nodes
Bars = ["1", "2", "3", "4", "5"]

# Creates a dictionary for the number of units of demand for each demand node
demand = {"1": 500,
        "2": 900,
        "3": 1800,
        "4": 200,
        "5": 700}

# Creates a list of costs of each transportation path
costs = { "A" : {"1" : 2, "2" : 4, "3" : 5, "4" : 2, "5" : 1 },
          "B" : {"1" : 3, "2" : 1, "3" : 3, "4" : 2, "5" : 3 }}

# Creates the prob variable to contain the problem data
prob = LpProblem("Beer Distribution Problem",LpMinimize)


# Creates a list of tuples containing all the possible routes for transport
Routes = [(w,b) for w in Warehouses for b in Bars]
# print(Routes)

# A dictionary called route_vars is created to contain the referenced variables (the routes)
route_vars = LpVariable.dicts("Route",(Warehouses,Bars),0,None,LpInteger)
# for (w,b) in Routes:
	# print(costs[w][b])
# The objective function is added to prob first
prob += lpSum([route_vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum of Transporting Costs"
# print(prob)

# The supply maximum constraints are added to prob for each supply node (warehouse)
for w in Warehouses:
    prob += lpSum([route_vars[w][b] for b in Bars]) <= supply[w], "Sum of Products out of Warehouse %s"%w
print(supply[w])

# The demand minimum constraints are added to prob for each demand node (bar)
for b in Bars:
	print(b)
	# print(type(b))
	for w in Warehouses:
		print(lpSum([route_vars[w][b] for w in Warehouses]))
		print(demand[b])


    # prob += lpSum([route_vars[w][b] for w in Warehouses]) >= demand[b], "Sum of Products into Bars %s"%b
    # print(demand[b])

print(lpSum([route_vars[w][b] for w in Warehouses]))

