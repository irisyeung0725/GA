#!/usr/bin/python

#Copyright 2019, Gurobi Optimization, LLC


from gurobipy import *


try:

    #Create a new model
    m = Model("mip1")

    # Create variables
    xw = m.addVar(name="xw")
    xc = m.addVar(name="xc")
    xb = m.addVar(name="xb")

    #Create a dictionary with the keys of requirements for each senarios
    y = {}

    for i in range(1,6): #Create 5 senarios
        for j in range(1,7): #Create 6 elements for each scnario
            #Set variable names
            y[i,j] = m.addVar(name="y(%s)(%s)"%(i,j)) #y[1,1] means senario 1 element 1 


    #As an alternative way, we can create a dictionary within a dictionary:
    #for i in range(1,6):
        # temp = {}
        # for j in range(1,7):
        #     y[i][j] = m.addVar(name="y(%s)(%s)"%(i,j))
        # y[i] = temp

    # Set objective
    obj = (150 * xw + 230 * xc + 260 * xb + 47.6* y[1,1] - 34 * y[1,2] + 42 * y[1,3] 
        - 30 * y[1,4] - 7.2 * y[1,5] - 2 * y[1,6] + 47.6 * y[2,1] - 34 * y[2,2] 
        + 42 * y[2,3] - 30 * y[2,4] - 7.2 * y[2,5] - 2 * y[2,6] + 71.4 * y[3,1] 
        - 51 * y[3,2] + 63 * y[3,3] - 45 * y[3,4] - 10.8 * y[3,5] - 3 * y[3,6] 
        + 35.7 * y[4,1] - 25.5 * y[4,2] + 31.5 * y[4,3] - 22.5 * y[4,4] - 5.4 * y[4,5] 
        - 1.5 * y[4,6] + 35.7 * y[5,1] - 25.5 * y[5,2] + 31.5 * y[5,3] - 22.5 * y[5,4] 
        - 5.4 * y[5,5] - 1.5 * y[5,6])

    m.setObjective(obj, GRB.MINIMIZE)


    #first-stage land allocation
    m.addConstr(xw + xc + xb <= 500, "c0") 
    #second-stage "scen 1" wheat requirements
    m.addConstr(1.75 * xw + y[1,1] - y[1,2] >= 200, "c1")
    #second-stage "scen 1" corn requirements
    m.addConstr(2.1 * xc + y[1,3] - y[1,4] >= 240, "c2")
    #second-stage "scen 1" sugar beet growth restrictions
    m.addConstr(-14 * xb + y[1,5] + y[1,6] <= 0, "c3")
    #second-stage "scen 1" favorable price sugar beet sale restrictions (from quota)
    m.addConstr(y[1,5] <= 5000, "c4")
    #second-stage "scen 2" wheat requirements
    m.addConstr(2 * xw + y[2,1] - y[2,2] >= 200, "c5")
    #second-stage "scen 2" corn requirements
    m.addConstr(2.4 * xc + y[2,3] - y[2,4] >= 240, "c6")
    #second-stage "scen 2" sugar beet growth restrictions
    m.addConstr(-16 * xb + y[2,5] + y[2,6] <= 0, "c7")
    #second-stage "scen 2" favorable price sugar beet sale restrictions (from quota)
    m.addConstr(y[2,5] <= 5500, "c8")
    #second-stage "scen 3" wheat requirements
    m.addConstr(2.5 * xw + y[3,1] - y[3,2] >= 200, "c9")
    #second-stage "scen 3" corn requirements
    m.addConstr(3 * xc + y[3,3] - y[3,4] >= 240, "c10")
    #second-stage "scen 3" sugar beet growth restrictions
    m.addConstr(-20 * xb + y[3,5] + y[3,6] <= 0, "c11")
    #second-stage "scen 3" favorable price sugar beet sale restrictions (from quota)
    m.addConstr(y[3,5] <= 6000, "c12")
    #second-stage "scen 4" wheat requirements
    m.addConstr(3.125 * xw + y[4,1] - y[4,2] >= 200, "c13")
    #second-stage "scen 4" corn requirements
    m.addConstr(3.75 * xc + y[4,3] - y[4,4] >= 240, "c14")
    #second-stage "scen 4" sugar beet growth restrictions
    m.addConstr(-25 * xb + y[4,5] + y[4,6] <= 0, "c15")
    #second-stage "scen 4" favorable price sugar beet sale restrictions (from quota)
    m.addConstr(y[4,5] <= 7000, "c16")
    #second-stage "scen 5" wheat requirements
    m.addConstr(3.375 * xw + y[5,1] - y[5,2] >= 200, "c17")
    #second-stage "scen 5" corn requirements
    m.addConstr(4.05 * xc + y[5,3] - y[5,4] >= 240, "c18")
    #second-stage "scen 5" sugar beet growth restrictions
    m.addConstr(-27 * xb + y[5,5] + y[5,6] <= 0, "c19")
    #second-stage "scen 5" favorable price sugar beet sale restrictions (from quota)
    m.addConstr(y[5,5] <= 7500, "c20")
    



    m.optimize()
    m.write('StochFarmers5Scens.lp')

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))
except AttributeError:
    print('Encountered an attribute error')


