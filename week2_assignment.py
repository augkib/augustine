
my_list=[]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list[1]=15
print(my_list)

my_list2=[50,60,70]

my_list.extend(my_list2)

print(my_list)

my_list.sort()

print('The sorted list is ',my_list)

print('The index of 30 is ',my_list.index(30))


