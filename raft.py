[sheep_count, courses] = [int(x) for x in input("Enter sheep count and number of courses: ").split(' ')]
sheep = [int(x) for x in input("Enter each sheep weight: ").split(' ')]

# sheep_count = 6
# courses = 2
# sheep = [26, 7, 10, 30, 5, 4]

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
    print(f"--CURRENT COURSES: {current_courses}--")
    for s in sheep:
        print(f"Segashna ovca: {s}, Exceeds: {w + s > current_weight}, Izpolzvana li e ovca: {s in used_sheep}, Izpolvani ovce: {used_sheep}, courses: {current_courses}, w: {w}, current_weight: {current_weight}")
            
        if w + s > current_weight or s in used_sheep: 
            continue
        w += s
        used_sheep.append(s)
        # print(used_sheep, w)
    if current_courses == courses and len(used_sheep) == len(sheep):
        break
    if current_courses > courses:
        # print(f"kolko pati vlizam tuka: {current_courses}")
        used_sheep = []
        w = 0
        current_courses = 0
        current_weight += 1
        continue
    # print(current_courses, len(used_sheep))

print(current_weight, current_courses, i)
