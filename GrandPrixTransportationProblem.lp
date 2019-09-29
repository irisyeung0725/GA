\* Grand_Prix_Transportation *\
Minimize
Sum_of_Shipping_Costs: 131 vars(Plant1)(Region1) + 218 vars(Plant1)(Region2)
 + 266 vars(Plant1)(Region3) + 120 vars(Plant1)(Region4)
 + 250 vars(Plant2)(Region1) + 116 vars(Plant2)(Region2)
 + 263 vars(Plant2)(Region3) + 278 vars(Plant2)(Region4)
 + 178 vars(Plant3)(Region1) + 132 vars(Plant3)(Region2)
 + 122 vars(Plant3)(Region3) + 188 vars(Plant3)(Region4)
Subject To
Sum_of_Products_into_Region_Region1: vars(Plant1)(Region1)
 + vars(Plant2)(Region1) + vars(Plant3)(Region1) >= 450
Sum_of_Products_into_Region_Region2: vars(Plant1)(Region2)
 + vars(Plant2)(Region2) + vars(Plant3)(Region2) >= 200
Sum_of_Products_into_Region_Region3: vars(Plant1)(Region3)
 + vars(Plant2)(Region3) + vars(Plant3)(Region3) >= 300
Sum_of_Products_into_Region_Region4: vars(Plant1)(Region4)
 + vars(Plant2)(Region4) + vars(Plant3)(Region4) >= 300
Sum_of_Products_out_of_Plant_Plant1: vars(Plant1)(Region1)
 + vars(Plant1)(Region2) + vars(Plant1)(Region3) + vars(Plant1)(Region4)
 <= 450
Sum_of_Products_out_of_Plant_Plant2: vars(Plant2)(Region1)
 + vars(Plant2)(Region2) + vars(Plant2)(Region3) + vars(Plant2)(Region4)
 <= 600
Sum_of_Products_out_of_Plant_Plant3: vars(Plant3)(Region1)
 + vars(Plant3)(Region2) + vars(Plant3)(Region3) + vars(Plant3)(Region4)
 <= 500
Bounds
0 <= vars(Plant1)(Region1)
0 <= vars(Plant1)(Region2)
0 <= vars(Plant1)(Region3)
0 <= vars(Plant1)(Region4)
0 <= vars(Plant2)(Region1)
0 <= vars(Plant2)(Region2)
0 <= vars(Plant2)(Region3)
0 <= vars(Plant2)(Region4)
0 <= vars(Plant3)(Region1)
0 <= vars(Plant3)(Region2)
0 <= vars(Plant3)(Region3)
0 <= vars(Plant3)(Region4)
Generals
vars(Plant1)(Region1)
vars(Plant1)(Region2)
vars(Plant1)(Region3)
vars(Plant1)(Region4)
vars(Plant2)(Region1)
vars(Plant2)(Region2)
vars(Plant2)(Region3)
vars(Plant2)(Region4)
vars(Plant3)(Region1)
vars(Plant3)(Region2)
vars(Plant3)(Region3)
vars(Plant3)(Region4)
End
