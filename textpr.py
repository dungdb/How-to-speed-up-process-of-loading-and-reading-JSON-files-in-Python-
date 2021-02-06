file_object = open('DeviceSolar.txt', 'r')
data = file_object.read()
data_text = data.split('"')
# result = data.count('E_today') 
leng = len(data_text)
print (leng) 
# print (float(data_text[3]))
# i=0
# data_1 = data_text[0].split(':')
# leng = len(data_1)
# print (float(data_1[0]))
# print (float(data_1[1]))
i=0
for x in range(len(data_text)):
# 	data_1[i] = x.split(':')
	# print (data_text[x].find('E_today'))
	if (data_text[x].find('E_today')==0):
		# print(x)
		# print(float(data_text[x+2]))
		if (float(data_text[x+2])>1000):
			print(float(data_text[x+2])/3600000)
			fp=format(float(data_text[x+2])/3600000, '.2f')
			data_text[x+2] = str(fp)
			i=i+1

	if (data_text[x].find('SLLK')==0):
		# print(x)
		# print(float(data_text[x+2]))
		if (float(data_text[x+2])>1000):
			print(float(data_text[x+2])/3600000)
			fp=format(float(data_text[x+2])/3600000, '.2f')
			data_text[x+2] = str(fp)
			i=i+1

	if (data_text[x].find('TTGHD')==0):
		# print(x)
		# print(float(data_text[x+2]))
		if (float(data_text[x+2])>1000):
			print(float(data_text[x+2])/3600000)
			fp=format(float(data_text[x+2])/3600000, '.2f')
			data_text[x+2] = str(fp)
			i=i+1

	# x.find('E_today')
	# data_text_arr=data_text[x].split(':')
	# print (data_text_arr)

makeitastring = '"'.join(map(str, data_text))
print('ok')
print(i)
file = open("DeviceSolar1.txt", "w") 
file.write(makeitastring) 
file.close() 

# for x in range(len(data_text)):
# 	print(data_text[x])

file_object.close()
