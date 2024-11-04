sentence=[word for word in input("enter a string:").lower().split()]
freq_dict={}
for word in sentence:
	if word in freq_dict:
		freq_dict[word]+=1
	else:
		freq_dict[word]=1
print("character occurance:")
for key,value  in freq_dict.items():
	print(f"{key}:{value}")

