#tuple
from site import abs_paths


punto = (1,2,3,4)
print(f"La coordinata x del punto p è:{punto[0]}")
triangolo = [(1,2,3,4),(5,6,7,8),(8,9,3,1)]
print(f"la coordinata y del secondo vertice è {triangolo[1][1]}")



area = 1/2 *abs([triangolo[0][0]*triangolo[1][1]]+[triangolo[1][0]*triangolo[2][0]]+[triangolo[1][0]*triangolo[2][1]]-[triangolo[2][0]*triangolo[1][1]]-[triangolo[2][1]*triangolo[0][0]]-[triangolo[1][0]*triangolo[1][1]])
print(area)