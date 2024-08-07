import random
from itertools import permutations
def tsp(distance):
    n=len(distance)
    best_route=[]
    cost=float("inf")
    for route in permutations(range(n)):
        c=0
        for i in range(n-1):
            c+=distance[route[i]][route[i+1]]
            c+=distance[route[-1]][route[0]]
            if c<cost:
                best_route=route
                cost=c
    return best_route,cost
distance=[[0,10,15,20],[10,0,30,5],[15,30,0,25],[20,5,25,0]]
route,c=tsp(distance)
print("The best route is ",route)
print("The total cost is ",c)

