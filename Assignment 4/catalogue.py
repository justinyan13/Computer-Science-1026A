# Justin Yan
# jyan388
# Computer Science 1026A Assignment 4
# 12/03/2020

from country import *


class CountryCatalogue:
    def __init__(self, countryFile):
        self.file = open(countryFile, "r")
        self.countryFile = countryFile
        self.countryCat = {}

        self.file.readline()
        for line in self.file:
            line = line.replace("\n", "|").split("|")  # creates list of each line
            self.countryCat[line[0]] = Country(line[0], line[2], line[3], line[1])  # creates country object out of each line

        self.file.close()

    def setPopulationOfCountry(self, name, value):  # setter
        if name.title() in self.countryCat:
            self.countryCat[name].setPopulation(value)
        else:
            print("You can not change the population because {} does not exist in the database".format(name))

    def setAreaOfCountry(self, name, area):  # setter
        if name.title() in self.countryCat:
            self.countryCat[name].setArea(area)
        else:
            print("You can not change the area because {} does not exist in the database".format(name))

    def setContinentOfCountry(self, name, continent):  # setter
        if name.title() in self.countryCat:
            self.countryCat[name].setContinent(continent)
        else:
            print("You can not change the continent because {} does not exist in the database".format(name))

    def findCountry(self, name):  # searches for country
        if name in self.countryCat:
            return self.countryCat[name]
        else:
            return None

    def addCountry(self, name, pop, area, continent):  # adds country given all attributes
        if name.title() in self.countryCat:
            return False
        else:
            self.countryCat[name] = Country(name.title(), pop, area, continent.title())
            return True

    def printCountryCatalogue(self):
        for i in self.countryCat:
            print(repr(self.countryCat[i]))  # uses repr method from Country

    def saveCountryCatalogue(self, fileName):  # saves country to desired file when complete
        file = open(fileName, 'w')
        file.write("Country|Continent|Population|Area\n")
        # writeFile = False
        for i in sorted(self.countryCat):
            output = self.countryCat[i].getName() + "|" + self.countryCat[i].getContinent() + "|" + (
                self.countryCat[i].getPopulation()) + "|" + (
                         self.countryCat[i].getArea()) + "\n"
            file.write(output)
        return len(self.countryCat)
        return -1
        file.close()
