eyes = float(input())

if eyes >= 1.0:
    result = "High"
elif eyes >= 0.5:
    result = "Middle"
else:
    result = "Low"

print(result)