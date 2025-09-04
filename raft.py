[sheep_count, courses] = [int(x) for x in input("Enter sheep count and number of courses: ").split(' ')]
sheep = [int(x) for x in input("Enter each sheep weight: ").split(' ')]

if len(sheep) != sheep_count:
    print('Invalid input')
    exit()

max_weight = sum(sheep)
capacity = max(sheep)
current_weight = capacity
used_sheep = []
sheep.sort(reverse = True)
w = 0
current_courses = 0

i = 0
while current_courses <= courses:
    i += 1
    current_courses += 1
    w = 0
    for s in sheep:
           
        if w + s > current_weight or s in used_sheep: 
            continue
        w += s
        used_sheep.append(s)
    if current_courses == courses and len(used_sheep) == len(sheep):
        break
    if current_courses > courses:
        used_sheep = []
        w = 0
        current_courses = 0
        current_weight += 1
        continue

print(current_weight)
