N = int(input())

if N >= 80:
    print("pass")
else:
    needed = 80 - N
    print(f"{needed} more score")