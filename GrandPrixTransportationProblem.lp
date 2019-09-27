\* Grand_Prix_Transportation *\
Minimize
Sum_of_Shipping_Costs: 131 Route_Plant1_Region1 + 218 Route_Plant1_Region2
 + 266 Route_Plant1_Region3 + 120 Route_Plant1_Region4
 + 250 Route_Plant2_Region1 + 116 Route_Plant2_Region2
 + 263 Route_Plant2_Region3 + 278 Route_Plant2_Region4
 + 178 Route_Plant3_Region1 + 132 Route_Plant3_Region2
 + 122 Route_Plant3_Region3 + 188 Route_Plant3_Region4
Subject To
Sum_of_Products_into_Region_Region1: Route_Plant1_Region1
 + Route_Plant2_Region1 + Route_Plant3_Region1 >= 450
Sum_of_Products_into_Region_Region2: Route_Plant1_Region2
 + Route_Plant2_Region2 + Route_Plant3_Region2 >= 200
Sum_of_Products_into_Region_Region3: Route_Plant1_Region3
 + Route_Plant2_Region3 + Route_Plant3_Region3 >= 300
Sum_of_Products_into_Region_Region4: Route_Plant1_Region4
 + Route_Plant2_Region4 + Route_Plant3_Region4 >= 300
Sum_of_Products_out_of_Plant_Plant1: Route_Plant1_Region1
 + Route_Plant1_Region2 + Route_Plant1_Region3 + Route_Plant1_Region4 <= 450
Sum_of_Products_out_of_Plant_Plant2: Route_Plant2_Region1
 + Route_Plant2_Region2 + Route_Plant2_Region3 + Route_Plant2_Region4 <= 600
Sum_of_Products_out_of_Plant_Plant3: Route_Plant3_Region1
 + Route_Plant3_Region2 + Route_Plant3_Region3 + Route_Plant3_Region4 <= 500
Bounds
0 <= Route_Plant1_Region1
0 <= Route_Plant1_Region2
0 <= Route_Plant1_Region3
0 <= Route_Plant1_Region4
0 <= Route_Plant2_Region1
0 <= Route_Plant2_Region2
0 <= Route_Plant2_Region3
0 <= Route_Plant2_Region4
0 <= Route_Plant3_Region1
0 <= Route_Plant3_Region2
0 <= Route_Plant3_Region3
0 <= Route_Plant3_Region4
Generals
Route_Plant1_Region1
Route_Plant1_Region2
Route_Plant1_Region3
Route_Plant1_Region4
Route_Plant2_Region1
Route_Plant2_Region2
Route_Plant2_Region3
Route_Plant2_Region4
Route_Plant3_Region1
Route_Plant3_Region2
Route_Plant3_Region3
Route_Plant3_Region4
End
