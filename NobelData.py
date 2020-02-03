# Author: Mahtab Zilaie
# Date: January 31 2020
# Description: class, NobelData, reads from json file, nobels.json, that allows user to
# search data and get the surnames of the winners from a year and category

import json

class NobelData:

    """class NobelData with an init method that reads the nobels.json file """

    def __init__(self):
        with open('nobels.json', 'r') as infile:
            self.restored_list = json.load(infile)

    def search_nobel(self, year, category):

        """method search_nobel that takes parameters year and category and returns a sorted list
        of the surnames of the winners"""
        winner_info = []     # set winner_info to list
        dic = len(self.restored_list['prizes'])
        for i in range(0, dic):                 # loops through dictionary
            if self.restored_list['prizes'][i]['year'] == year and self.restored_list['prizes'][i]['category'] == category:
                winner_info = self.restored_list['prizes'][i]["laureates"] # sets winner_info to "laureates" index

        surnames = []       # set surnames to list
        for i in range(0, len(winner_info)):   # loops through every index in winner_info
            surnames.append(winner_info[i]['surname'])          # adds all surnames to list
        surnames.sort()
        return surnames             # returns sorted list of surnames
