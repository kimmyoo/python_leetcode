l = [3, 46, 4, 2, 1, 0, 99]

left, right = 3, 6

left -= 1
right -= 1

l[left:right] = l[left:right][::-1]

print(l)