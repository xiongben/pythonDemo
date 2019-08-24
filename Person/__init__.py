#coding=utf-8

class Person:
    name = "xiongben"
    age = 26

    def __init__(self, sport, level):
        super().__init__()
        self.sport = sport
        self.level = level
        self.__weight = 158

    def eat(self):
        self.__knowWeight()
        print("like eat meat")

    @classmethod
    def drink(cls,drinkType):
        print('like drink : {0}'.format(drinkType))

    @staticmethod
    def occupation(profession):
        print('occupation : {0}'.format(profession))

    def __knowWeight(self):
        print('privilate weight: {0}'.format(self.__weight))

    @property
    def weight(self):
        return self.__weight

    @weight.setter 
    def weight(self, weight):
        self.__weight = weight

    


    

    