def tower_of_hanoi(n,source,aux,des): 
    if n==0:
       return
    tower_of_hanoi(n-1,source,des,aux)
    print("Move disk",n," from source ",source," to ",des) 
    tower_of_hanoi(n-1,aux,source,des)
n=3 
tower_of_hanoi(n,"A","B","C")
