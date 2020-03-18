names={'Tom Zhang':'He is a little bit shy.','Mary Wang':'She is very cute.',
       'Jimmy Tang':'He is very rich.','William Fang':'He is very handsome.'}
for key,value in names.items(): #use names.items(） to bind key and value,
    # then we do the loop of key and value in the same time
    print('Name:{}    saying;{}'.format(key,value))


