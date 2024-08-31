#   module_5_1  #
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        a = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            while 1:
                if new_floor != 0:
                    new_floor -= 1
                    a += 1
                    print(a)
                else:
                    break

    #   module_5_2  #
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


#   module_5_1  #
print('-----module_5_1-----')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

#   module_5_2  #
print('-----module_5_2-----')
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
