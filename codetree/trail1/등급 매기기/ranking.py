N = int(input())

if N >= 90:
    grade = 'A'
elif N >= 80:
    grade = 'B'
elif N >= 70:
    grade = 'C'
elif N >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)