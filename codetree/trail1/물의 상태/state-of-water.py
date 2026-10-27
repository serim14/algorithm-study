n = int(input())

if n < 0:
    result = "ice"
elif n >= 100:
    result = "vapor"
else:
    result = "water"

print(result)