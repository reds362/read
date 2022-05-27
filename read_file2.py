data =[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		
		data.append(line)
		count += 1
		if count % 10000 ==0:
			print(count)

print(len(data))
#print(data[0])
ch_sum = 0
for d in data:
	ch_sum += len(d)
print(ch_sum)

print('平均每筆有', ch_sum / len(data), '個字母')

