
def three_sum (input_li):
	input_li.sort()
	ans = []
	for i in range (len(input_li)-2):
		if i == 0 or i > 0 and input_li[i-1] != input_li[i]:
			left = i + 1
			right = len(input_li) - 1
			while left < right:
				sum = input_li[i] + input_li [left] + input_li[right]
				if sum == 0:
					ans.append([input_li[i], input_li[left], input_li[right]])
					left += 1
					right -= 1
					while left < right and input_li[left] == input_li[left-1]:
						left+=1
					while right > left and input_li[right+1] == input_li[right]:
						right-=1
				elif sum < 0:
					left +=1
				else:
					right -= 1
	return ans
					

input_list = [9, 9, -9, 0, 100, -50, -50, 2, 1, 99, -99]
result = three_sum(input_list)
print (result)
