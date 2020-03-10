names=['tom Zhang','Mary Wang','jimmy Tang','William fang']
caplized_names=[]
lower_names=[]
for name in names:
    caplized_names.append(name.title())
    lower_names.append(name.lower().replace(' ','_'))
print(caplized_names)
print(lower_names)
