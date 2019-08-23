# L1 = [1,2,3]
L1 = [1, 2, 3, 0]
L2 = [3, 2, 1]
# L2 = [3,2,1, 0]

print([i for i in zip(L1, L2)])

nums = ['flower', 'flow', 'flight']
for i in zip(*nums):
    print(i)
