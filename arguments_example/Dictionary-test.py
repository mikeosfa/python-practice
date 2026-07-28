list_of_animals = ['cat','dog','tiger','elephant','honey badger']


my_dict = {}
for number, animal in enumerate(list_of_animals, start=1):
    my_dict[animal] = number

print(my_dict)