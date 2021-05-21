

vals = [1, 2, 4, 4, 4, 5, 6, 7]

target = 4

i = 0
j = len(vals)-1


while i <= j:
    m = (i+j)//2
    if vals[m] < target:
        i = m + 1
    else:
        j = m - 1

print(vals)
print(i, j, vals[j], target)

