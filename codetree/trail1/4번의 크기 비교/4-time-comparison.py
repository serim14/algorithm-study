A = int(input())

num_list = list(map(int, input().split()))

for num in num_list:
    print(1 if A > num else 0)