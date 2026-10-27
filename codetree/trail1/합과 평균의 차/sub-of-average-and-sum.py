num_list = list(map(int, input().split()))

t_sum = sum(num_list)
t_avg = t_sum//len(num_list)

print(t_sum)
print(t_avg)
print(t_sum-t_avg)