# hackerrank

steps = int(input('Enter number of steps: '))
UD = input("Enter number Uphills and Downhills").strip().upper()
counter = 0
level = 0
prev_level = 0
for i in UD:
    if i == 'U':
        level +=1
    elif i == 'D':
        level -= 1
    if level == 0 and i == 'U':
        counter += 1

print(counter)

