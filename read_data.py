# read_data.py

data = []
count = 0
with open('reviews.txt','r') as file:
	for e_line in file:
		data.append(e_line)
		count =+ 1
		if count % 1000 ==0:
			print(len(data))

print(len(data))

print(data[0])
print('------------------')
print(data[1])
