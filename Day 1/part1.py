left_list = []
right_list = []

def read_input(filename):
    with open(filename, 'r') as f:
        content = f.readlines()

        for lignes in content:
            lignes = lignes.strip()
            left, right = map(int,lignes.split("   "))

            left_list.append(left)
            right_list.append(right)


read_input("Day 1\\Inputs\\input_part1.txt")

#print(left_list)

left_list.sort()
right_list.sort()

sum = 0

for i in range(0, len(left_list)):
    diff = left_list[i]-right_list[i]
    sum += abs(diff)

print(sum)