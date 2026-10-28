A_scores = list(map(int, input().split()))
B_scores = list(map(int, input().split()))

if A_scores[0] > B_scores[0] and A_scores[1] > B_scores[1]:
    print(1)
else:
    print(0)