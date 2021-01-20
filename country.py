# Justin Yan
# jyan388
# Computer Science 1026A Assignment 4
# 12/03/2020

class Country:
    def __init__(self, name, pop, area, continent):  # constructor
        self.name = name  # setting
        self.pop = pop  # setting
        self.area = area  # setting
        self.continent = continent  # setting

    def getName(self):  # getters
        return self.name

    def getPopulation(self):  # getters
        return self.pop

    def getArea(self):  # getters
        return self.area

    def getContinent(self):  # getters
        return self.continent

    def setPopulation(self, population):  # setters
        self.pop = population

    def setArea(self, area):  # setters
        self.area = area

    def setContinent(self, continent):  # setters
        self.continent = continent

    def __repr__(self):  # customized print
        return '{} (pop: {}, size: {}) in {}'.format(self.name, self.pop, self.area, self.continent)
