lst=input("enter alist of words(space separated): ").split()
maxlenght=max(len(word) for word in lst)
lg_word=[word for word in lst if len(word)==maxlenght]

print(f"largest word:{lg_word},size:{maxlenght}")
