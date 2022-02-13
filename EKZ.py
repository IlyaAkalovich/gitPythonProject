# Задача 1

def credit(number):
    return "*" * 12 + number[-4::]
print(credit(input("Введите номер карты: " )))

# Задача 2

def is_polindrom(str):
    reversed_string = str[::-1]
    return str  == reversed_string
print(is_polindrom(input("Введите слово: ")))

# Задача 3

class Tomato:
    states = ["проростание","формирование стебля","появление листков","появление цветоноса","созревание плода"]
    def __init__(self,ind):
        self._index = ind
        self._state = self.states[0]
    def grow(self):
        index = self.states.index(self._state)
        if index != len(self.states) -1:
            self._state = self.states[index + 1]
    def is_ripe(self):
        return self._state == self.states[-1]
class TomatoBush:
    tomatos = []
    def __init__(self,count):
        self.tomatos = [Tomato(i) for i in range(count)]
    def grow_all(self):
        for tomato in self.tomatos:
            tomato.grow()
    def all_are_ripe(self):
        condition = True
        for tomato in self.tomatos:
            condition = condition and tomato.is_ripe()
        return condition
    def give_away_all(self):
        self.tomatos = []
class Gardener:
    def __init__(self,name,tomato_bush):
        self.name = name
        self._plant = tomato_bush
    def work(self):
        self._plant.grow_all()
    def harvest(self):
        print("попытка собрать урожай: ")
        all_grown = self._plant.all_are_ripe()
        if all_grown:
            print("... " + self.name + " собирает урожай")
            self._plant.give_away_all()
        else:
            print("... не все плоды созрели")
        return all_grown
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству помидоров")

Gardener.knowledge_base()
tomatobushobj = TomatoBush(3)
gardenerobj = Gardener("Илья",tomatobushobj)
gardenerobj.work()
succeeded = gardenerobj.harvest()
while succeeded == False:
    gardenerobj.work()
    succeeded = gardenerobj.harvest()









