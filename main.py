#program intended to calculate the efg and the shot distribution within the corner three, non corner
#three, and two point ranges for two teams using a diagram of the court and a shots_data.csv file

import pandas
import math
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

try:
    logging.info("Program started")
    atwop = 0
    ancthree = 0
    acthree = 0
    btwop = 0
    bncthree = 0
    bcthree = 0

    # Read the Team Data
    data = pandas.read_csv("shots_data.csv")
    data_dict = data.to_dict()  # convert to dictionary for further usage

    team_a_shots = len(data[data["team"] == "Team A"])  # A Team total shots
    team_b_shots = len(data[data["team"] == "Team B"])  # B Team total Shots

    logging.info("team_a_shots" + str(team_a_shots))  # print(team_a_shots)
    logging.info("team_b_shots" + str(team_b_shots))  # print(team_b_shots)

    a_data = data[data.team == "Team A"]  # A Team data
    b_data = data[data.team == "Team B"]  # B Team data

    #initialize variables
    a_made_two = 0
    a_made_nc3 = 0
    a_made_c3 = 0

    b_made_two = 0
    b_made_nc3 = 0
    b_made_c3 = 0

    # for loop to iterate through each row of data
    for index, row in data.iterrows():
        #calculate shot len for 3 pointers
        len = (data["x"].values[index] * data["x"].values[index]) + (data["y"].values[index] * data["y"].values[index])
        shotlen = math.sqrt(len)
        #check for corner threes
        if data["team"].values[index] == "Team A":
            if data["x"].values[index] > 22:
                if data["y"].values[index] < 7.8:
                    acthree += 1
                    if data["fgmade"].values[index] == 1:
                        a_made_c3 += 1
            elif data["x"].values[index] < -22:
                if data["y"].values[index] < 7.8:
                    acthree += 1
                    if data["fgmade"].values[index] == 1:
                        a_made_c3 += 1
            #check for non corner threes
            elif shotlen > 23.75:
                if data["y"].values[index] > 7.8:
                    ancthree += 1
                    if data["fgmade"].values[index] == 1:
                        a_made_nc3 += 1
            #else it is a two pointer
            else:
                atwop += 1
                if data["fgmade"].values[index] == 1:
                    a_made_two += 1
        #repeat same process for team B
        else:
            if data["x"].values[index] > 22:
                if data["y"].values[index] < 7.8:
                    bcthree += 1
                    if data["fgmade"].values[index] == 1:
                        b_made_c3 += 1
            elif data["x"].values[index] < -22:
                if data["y"].values[index] < 7.8:
                    bcthree += 1
                    if data["fgmade"].values[index] == 1:
                        b_made_c3 += 1
            elif shotlen > 23.75:
                if data["y"].values[index] > 7.8:
                    bncthree += 1
                    if data["fgmade"].values[index] == 1:
                        b_made_nc3 += 1
            else:
                btwop += 1
                if data["fgmade"].values[index] == 1:
                    b_made_two += 1
    # Calculating the Team A percents
    a_two_percent = atwop / team_a_shots
    a_nc3_percent = ancthree / team_a_shots
    a_c3_percent = acthree / team_a_shots
    a_efg_2 = a_made_two / atwop
    a_efg_nc3 = (a_made_nc3 + (.5 * a_made_nc3)) / ancthree
    a_efg_c3 = (a_made_c3 + (.5 * a_made_c3)) / acthree
    logging.info("Team A C3 Percent = {0} %".format(a_c3_percent * 100))
    logging.info("Team A NC3 Percent = {0} %".format(a_nc3_percent * 100))
    logging.info("Team A two point goal  Percent = {0} %".format(a_two_percent * 100))
    logging.info("Team A efg c3 = {0} %".format(a_efg_c3 * 100))
    logging.info("Team A efg nc3 = {0} %".format(a_efg_nc3 * 100))
    logging.info("Team A efg 2 = {0} %".format(a_efg_2 * 100))

    # print(a_nc3_percent)
    # print(a_two_percent)
    # print(a_efg_c3)
    # print(a_efg_nc3)
    # print(a_efg_2)
    # Calculating the Team B percents
    b_two_percent = btwop / team_b_shots
    b_nc3_percent = bncthree / team_b_shots
    b_c3_percent = bcthree / team_b_shots
    b_efg_2 = b_made_two / btwop
    b_efg_nc3 = (b_made_nc3 + (.5 * b_made_nc3)) / bncthree
    b_efg_c3 = (b_made_c3 + (.5 * b_made_c3)) / bcthree
    # print(b_c3_percent)
    # print(b_nc3_percent)
    # print(b_two_percent)
    # print(b_efg_c3)
    # print(b_efg_nc3)
    # print(b_efg_2)
    logging.info("Team B C3 Percent = {0} %".format(b_c3_percent * 100))
    logging.info("Team B NC3 Percent = {0} %".format(b_nc3_percent * 100))
    logging.info("Team B two point goal  Percent = {0} %".format(b_two_percent * 100))
    logging.info("Team B efg c3 = {0} %".format(b_efg_c3 * 100))
    logging.info("Team B efg nc3 = {0} %".format(b_efg_nc3 * 100))
    logging.info("Team B efg 2 = {0} %".format(b_efg_2 * 100))
except Exception as e:  # error handling
    logging.error(e)
