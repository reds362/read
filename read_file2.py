data =[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		
		data.append(line)
		count += 1
		if count % 100000 ==0:
			print(count)

print(len(data))
#print(data[0])
ch_sum = 0
for d in data:
	ch_sum += len(d)
print(ch_sum)

print('平均每筆有', ch_sum / len(data), '個字母')


new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆資料小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'筆資料')
print(good[1])


bad = ['cool' for d in data if 'bad' in d]
print(len(bad))
print(bad)


bad =[]
for d in data:
	if 'bad' in d:
		bad.append(d)
print(len(bad))
print(bad)


