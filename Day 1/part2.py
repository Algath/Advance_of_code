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

similarity_score = 0
appear = 0

for i in left_list:
    for j in right_list:
        if i == j:
            appear += 1

    similarity_score += i*appear
    appear = 0

print(similarity_score)