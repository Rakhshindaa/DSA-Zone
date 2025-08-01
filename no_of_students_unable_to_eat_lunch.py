students = list(map(int, input().split()))
sandwiches = list(map(int, input().split()))
count = 0
while students and count < len(students):
    if students[0] == sandwiches[-1]:
        students.pop(0)
        sandwiches.pop()
        count = 0  # Reset since we made a successful match
    else:
        students.append(students.pop(0))  # Rotate
        count += 1
# Output how many students couldn't eat
print(len(students))
