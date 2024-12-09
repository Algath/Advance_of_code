rapport = []
def read_input(filename):
    with open(filename, 'r') as f:
        content = f.readlines()

        for lignes in content:
            nombres = list(map(int, lignes.strip().split()))
            rapport.append(nombres)

read_input("Day 2\\Input\\input.txt")

#print(rapport)

safe = False
count = 0
        
def analyze_sequence(lst):
    count = 0
    if len(lst) < 2:
        count += 1
    
    increases = 0
    decreases = 0
    
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            increases += 1
        elif lst[i] < lst[i-1]:
            decreases += 1
    

    for x in range(0, len(lst)-1):
        diff = lst[x]-lst[x+1]
        #print(f"{lst[x]}-{lst[x+1]}: {diff}")
        if (1 <= diff <= 3) or (-3 <= diff <= -1):
            safe = True
        else:
            safe = False
            break

    total_changes = increases + decreases
    
    if increases == total_changes and safe:
        count += 1
        #print("Strictly increasing")
    elif decreases == total_changes and safe:
        count += 1
        #print("Strictly decreasing")
    return count

for i in rapport:
    count += analyze_sequence(i)

print(count)