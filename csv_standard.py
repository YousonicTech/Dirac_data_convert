import os
import pandas as pd
import numpy as np
path = "D:/YouSonic/extract_t60/Finished_File"
csv_list = os.listdir(path)
total_csv = pd.read_csv("D:/YouSonic/extract_t60/total_csv.csv")
import csv

for name in csv_list:
    data = pd.read_csv(path+ '/'+ name)

    Mic_config = name[:-4]
    index = (data['0']=='T60')#找出T60对应的列号
    for i in range (len(index)):
        if index[i]==True:
            Room = data['0'][i-4]
            Room_decode = Room
            Room_Config = 'b-format'
            t60_31 = data['2'][i]
            t60_63 = data['3'][i]
            t60_125 = data['4'][i]
            t60_250 = data['5'][i]
            t60_500 = data['6'][i]
            t60_1000 = data['7'][i]
            t60_2000 = data['8'][i]
            t60_4000 = data['9'][i]
            t60_8000 = data['10'][i]
            with open("D:/YouSonic/extract_t60/total_csv.csv", 'a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([Mic_config,Room,Room_decode,Room_Config,1,0,0,0,0,25.11886,0,0,0,0,31.6227766,t60_31,t60_31,0,0,39.81072
            ,0,0,0,0,50.11872,0,0,0,0,63.09573,t60_63,t60_63,0,0,79.43282,0,0,0,0,100,0,0,0,0,125.8925,t60_125,t60_125,0,0,158.4893,0,0,0,0,199.5262,0,0,0,0,251.1886,t60_250,t60_250,0,0,316.2278,0,0,0,0,398.1072,0,0,0,0,501.1872,t60_500,t60_500,0,0,630.9573,0,0,0,0,794.3282,0,0,0,0,1000,t60_1000,t60_1000,0,0,1258.925,0,0,0,0,1584.893,0,0,0,0,1995.262,t60_2000,t60_2000,0,0,2511.886,0,0,0,0,3162.278,0,0,0,0,3981.072,t60_4000,t60_4000,0,0,5011.872,0,0,0,0,6309.573,0,0,0,0,7943.282,t60_8000,t60_8000,0,0,10000,0,0,0,0,12589.25,0,0,0,0,15848.93,0,0,0,0,19952.62,0,0,0,0])




