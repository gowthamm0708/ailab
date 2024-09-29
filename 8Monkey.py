def monkey(n):
    climb = 0
    banana = 0
    hungry = True

    for i in range(n):
        if hungry:
            climb += 1
            banana += 1
            hungry = False
        else:
            climb += 1

    return climb, banana

n = 10
climb, banana = monkey(n)
print(f"The monkey made {climb} climbs and got {banana} bananas.")


