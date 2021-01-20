# Justin Yan
# jyan388
# Computer Science 1026A Assignment 4
# 12/03/2020
from country import *
from catalogue import *


def processUpdates(cntryFileName, updateFileName):  # process updates given country data & updates data
    z = False
    while not z:  # process cntryFileName
        try:
            open(cntryFileName, 'r')
            z = True  # ends loop once valid file is found
            catalog = CountryCatalogue(cntryFileName)  # creates country catalog object out of provided file

        except IOError:  # handles exception
            quit_input = input("Do you want to quit? Y = yes, N = no\n")
            if quit_input == "N":
                cntryFileName = input("Enter a new country file:\n")
            else:
                quit_file = open('output.txt', 'w')
                quit_file.write('Update Unsuccessful\n')
                quit_file.close()
                return False
                exit()

        except ValueError:  # handles exception
            quit_input = input("Do you want to quit? Y = yes, N = no\n")
            if quit_input == "N":
                cntryFileName = input("Enter a new country file:\n")
            else:
                quit_file = open('output.txt', 'w')
                quit_file.write('Update Unsuccessful\n')
                quit_file.close()
                return False
                exit()

        except RuntimeError as error:  # handles exception
            quit_input = input("Do you want to quit? Y = yes, N = no\n")
            if quit_input == "N":
                cntryFileName = input("Enter a new country file:\n")
            else:
                quit_file = open('output.txt', 'w')
                quit_file.write('Update Unsuccessful\n')
                quit_file.close()
                return False
                exit()

    y = False
    while not y:
        try:
            open_update_file = open(updateFileName, 'r')
            pop_validity = False  # checks that population update is valid
            area_validity = False  # checks that area update is valid
            continent_validity = False  # checks that continent update is valid
            list_of_continents = ['Africa', 'Antarctica', 'Arctic', 'Asia', 'Europe', 'North America', 'South America']  # list of valid continent updates

            for line in open_update_file:
                try:
                    line = line.replace("\n", "").replace("=", ";").split(";")  # separates each line into list
                    if line[0] in catalog.countryCat:  # processes update if country pre-exists in catalog(from provided data file)
                        for i in range(len(line)):
                            if line[i].strip() == 'P':  # process population updates
                                new_line_list = line[i + 1].split(",")
                                for element in new_line_list:  # checks validity; no greater than 3 digits separated by commas
                                    if len(element) > 3:
                                        pop_validity = False
                                        raise ValueError  # raises exception if invalid, skips entire line, ignoring any updates before it or after
                                    else:
                                        pop_validity = True
                                if pop_validity:
                                    new_pop = line[i + 1]  # assigns population update to variable
                            elif line[i].strip() == 'A':  # process area updates; identicial to population
                                new_line_list = line[i + 1].split(",")
                                for element in new_line_list:
                                    if len(element) > 3:
                                        area_validity = False
                                        raise ValueError
                                    else:
                                        area_validity = True
                                if area_validity:
                                    new_area = line[i + 1]
                            elif line[i].strip() == 'C':  # process continent updates
                                new_continent = str.title(" ".join(line[i + 1].split()))
                                if new_continent in list_of_continents:
                                    new_con_temp = new_continent
                                    continent_validity = True
                                else:
                                    continent_validity = False
                                    raise ValueError
                        if pop_validity:  # updates country population if valid value
                            catalog.setPopulationOfCountry(line[0], new_pop)
                            pop_validity = False
                        if area_validity:
                            catalog.setAreaOfCountry(line[0], new_area)
                            area_validity = False
                        if continent_validity:
                            catalog.setContinentOfCountry(line[0], new_con_temp)
                            continent_validity = False
                    elif line[0] not in catalog.countryCat:  # process updates for brand new countries
                        for i in range(len(line)):
                            if line[i].strip() == 'P':
                                new_line_list = line[i + 1].split(",")
                                for element in new_line_list:
                                    if len(element) > 3:
                                        pop_validity = False
                                        raise ValueError
                                    else:
                                        pop_validity = True
                                if pop_validity:
                                    new_pop = line[i + 1]
                            elif line[i].strip() == 'A':
                                new_line_list = line[i + 1].split(",")
                                for element in new_line_list:
                                    if len(element) > 3:
                                        area_validity = False
                                        raise ValueError
                                    else:
                                        area_validity = True
                                if area_validity:
                                    new_area = line[i + 1]
                            elif line[i].strip() == 'C':
                                new_continent = str.title(" ".join(line[i + 1].split()))
                                if new_continent in list_of_continents:
                                    new_con_temp = new_continent
                                    continent_validity = True
                                else:
                                    continent_validity = False
                                    raise ValueError
                        if pop_validity:
                            if line[0] not in catalog.countryCat:  # creates new item if country does not exist
                                catalog.addCountry(line[0], new_pop, '', '')
                                pop_validity = False
                            elif line[0] in catalog.countryCat:  # updates existing item(occurs if it is after the first update for a new country)
                                catalog.setPopulationOfCountry(line[0], new_pop)
                                pop_validity = False
                        if area_validity:
                            if line[0] not in catalog.countryCat:
                                catalog.addCountry(line[0], '', new_area, '')
                                area_validity = False
                            elif line[0] in catalog.countryCat:
                                catalog.setAreaOfCountry(line[0], new_area)
                                area_validity = False
                        if continent_validity:
                            if line[0] not in catalog.countryCat:
                                catalog.addCountry(line[0], '', '', new_con_temp)
                                continent_validity = False
                            elif line[0] in catalog.countryCat:
                                catalog.setContinentOfCountry(line[0], new_con_temp)
                                continent_validity = False

                    y = True

                except ValueError:
                    continue  # skips & ignores entire line

            catalog.saveCountryCatalogue("output.txt")  # saves catalog to output.txt
            return True
            exit()

        except IOError:
            quit_input = input("Do you want to quit? Y = yes, N = no\n")
            if quit_input == "N":
                updateFileName = input("Enter a new updates file:\n")
            else:
                quit_file = open('output.txt', 'w')
                quit_file.write('Update Unsuccessful\n')
                quit_file.close()
                return False
                exit()
