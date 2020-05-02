x=[1,2,3]
y=[3,2,1]
order_time=['10:30','23:15','5:45']
id_names=['A','B','C']
datas=[]
for data in zip(id_names,x,y,order_time):
    datas.append('{}:{},{},{}'.format(*data))
print(datas)
a1=['Hello','World']
a2=['How', 'are','you']
print('{0} {1} {0}'.format(a1,a2))
