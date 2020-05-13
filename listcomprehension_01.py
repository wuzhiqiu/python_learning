number_list_01=[number*number for number in range(1,7) if number%2==0]       # do square operation in range(1,7) and if it is even
number_list_02=[number*number
            if number%2==0
            else number+10
            for number in range(1,7)]
print(number_list_01,number_list_02)