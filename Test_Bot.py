# This is a simple ChatBot

import os
import time
import random

os.system('color 3f')  # sets the background to blue

def abil():# Displays it's functions
    print("I can perform the following tasks")
    print(*Functions, sep="\n")
    print("What's your choice")
    ch = input()
    if ch in menu:
        mess1()
    elif ch in bus:
        busS()
    elif ch in ttable:
        timet()

def mess1():#Shows the days for mess menu
    print("Here's the mess menu :")
    print(*days, sep="\n")
    ch1=input()
    mess2(ch1)


def busS():#Displays the bus schedule
    print(*days, sep="\n")

def timet():#Displays the student timetable
    print(*days, sep="\n")


def mess2(ch1):#Displays the timetable according to the user input
    if ch1 is '1':
        print(*time_mess, sep="\n")
        i1 = input()
        if i1 is '1':
            print("Poha, Jalebi, sprouts")
        elif i1 is '2':
            print("Plain Rice, Arhar dal, Lauki Chana")
        elif i1 is '3':
            print("Jeera Rice, Moong-Masoor Dal,Boondi Raita Chhole Bhature")

    if ch1 is '2':
        print(*time_mess, sep="\n")
        i1 = input()
        if i1 is '1':
            print("Uttapam, Sambhar, Coconut Chutney")
        elif i1 is '2':
            print("Plain Rice, Dal Tadka, Aloo Matar")
        elif i1 is '3':
            print("Fried Rice, Dal Fry,Seasonal Fruit Papaya,Veg Manchurian Gravy")

    if ch1 is '3':
        print(*time_mess, sep="\n")
        i1 = input()
        if i1 is '1':
            print("Pyaaz and Azwain Paratha, Aloo Sabji")
        elif i1 is '2':
            print("Peas Pulao, Chana dal, Rajma Masala")
        elif i1 is '3':
            print("Plain Rice, Arhar Dal,Pickle Chhachh Mix Veg")
    if ch1 is '4':
        print(*time_mess, sep="\n")
        i1 = input()
        if i1 is '1':
            print(" Idli / Fried Idli, Sambhar, Coconut Chutney")
        elif i1 is '2':
            print("Plain Rice, Kadhi-Pakoda Black Chana Masala")
        elif i1 is '3':
            print("Plain Rice, Moong Dal, Red Pumpkin, Rice Kheer")

    if ch1 is '5':
        print(*time_mess, sep="\n")
        i1 = input()
        if i1 is '1':
            print("Poori Sabji")
        elif i1 is '2':
            print(" Lemon Rice, Chana Dal, Bhindi Aloo")
        elif i1 is '3':
            print("Plain Rice, Dal Tadka,Banana#/Guava# Paneer / Egg Curry#, Ice Cream Cup#")
    if ch1 is '6':
        print(*time_mess, sep="\n")
        i1 = input()
        if i1 is '1':
            print(" Aloo Paratha, Dahi, Sauce, Pickle ")
        elif i1 is '2':
            print("Fried Rice, Urad Dal, Veg Kolhapuri")
        elif i1 is '3':
            print("Plain Rice, Dal Fry,Veg Kolhapuri Baingan Bharta, Boondi# / Boondi Laddu#")
    if ch1 is '7':
        print(*time_mess, sep="\n")
        i1 = input()
        if i1 is '1':
            print("Masala Dosa, Sambhar, Chutney")
        elif i1 is '2':
            print("Veg Biryani, Dal Fry, Paalak Aloo")
        elif i1 is '3':
            print(" Plain Rice, Dal Makhani,Cucumber Raita Paneer / Chicken, Gulab Jamun / Kala Jamun")



#Defined user keywords
ability = ['what can you do?', 'what can you do ?', 'use', 'perform']
Functions = ["1.Mess Menu", "2.Bus Schedule","3.Class Schedule"]
menu = ['1','menu','food menu','food']
days = ['1.Monday','2.Tuesday','3.Wednesday','4.Thursday','5.Friday','6.Saturday','7.Sunday']
bus = ['Bus Schedule','bus','bus schedule','karwad to mbm']
ttable = ['Time Table','class']
time_mess = ['breakfast', "lunch", "dinner"]



# start the conversation
print('Hi there, I am DevelUp Bot, the bot of the open source community at IIT JODHPUR. As of now I am a simple chatbot!')  # greeting

# keep going the conversation
print('Whats your name?')  # ask
Name = input()  # save answer
print('Im glad to meet you, ' + Name + '!!')  # reply

while True:
    i1=input()
    if i1 in ability:
        abil()
    elif i1 in menu:
        mess1()
    elif i1 in bus:
        busS()
    elif i1 in ttable:
        timet()
    else:
        print("Invalid Input.")
        break



