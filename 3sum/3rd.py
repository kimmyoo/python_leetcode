# 3rd attempt on 3sum
def three_sum (input_list):
	input_list.sort()
	res = []
	for i in range (len(input_list) -2):
		if i == 0 or (i > 0 and input_list[i] != input_list [i+1]):
			left = i+1
			right = len(input_list) -1
			while left < right:
				sum = input_list[i] + input_list[left] + input_list[right]
				if sum == 0:
					res.append([input_list[i], input_list[left], input_list[right]])
					left+= 1
					right-=1
					while left < right and input_list[left] == input_list[left-1]:
						left+=1
					while left < right and input_list[right] == input_list[right+1]:
						right-=1
				elif sum < 0:
					left+=1
				else:
					right-=1
	return res

input_list = [9, 9, -9, 0, 100, -50, -50, 2, 1, 99, -99]
result = three_sum(input_list)
print (result)
