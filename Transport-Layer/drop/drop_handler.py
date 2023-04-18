import csv
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 18})

######################################
dps = []
time_NR = []
i = 0
with open('drop_TcpNewReno.csv', 'r') as TcpNewReno:
    reader = csv.reader(TcpNewReno, delimiter=' ')
    for row in reader:
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        timestamp = float(row[0])
        time_NR.append(timestamp)
        dps.append(drops/timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_NR = dps
######################################
dps = []
time_VG = []
i = 0
with open('drop_TcpVegas.csv', 'r') as TcpVegas:
    reader = csv.reader(TcpVegas, delimiter=' ')
    for row in reader:
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        timestamp = float(row[0])
        time_VG.append(timestamp)
        dps.append(drops/timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_VG = dps
######################################
dps = []
time_B = []
i = 0
with open('drop_TcpBic.csv', 'r') as TcpBic:
    reader = csv.reader(TcpBic, delimiter=' ')
    for row in reader:
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        timestamp = float(row[0])
        dps.append(drops/timestamp)
        time_B.append(timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_B = dps
######################################
dps = []
time_C = []
i = 0
with open('drop_TcpCubic.csv', 'r') as drop_TcpCubic:
    reader = csv.reader(drop_TcpCubic, delimiter=' ')
    for row in reader:
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        timestamp = float(row[0])
        time_C.append(timestamp)
        dps.append(drops/timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_C = dps
######################################
dps = []
time_HS = []
i = 0
with open('drop_TcpHighSpeed.csv', 'r') as drop_TcpHighSpeed:
    reader = csv.reader(drop_TcpHighSpeed, delimiter=' ')
    prev_timestamp = 0
    prev_drops = 0
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        dps.append(drops/timestamp)
        time_HS.append(timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_HS = dps
######################################
dps = []
time_I = []
i = 0
with open('drop_TcpIllinois.csv', 'r') as drop_TcpIllinois:
    reader = csv.reader(drop_TcpIllinois, delimiter=' ')
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        dps.append(drops/timestamp)
        time_I.append(timestamp)
        print("-----------------------")
        print("drops:", drops, "prev drops:", prev_drops)
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_I = dps
######################################
dps = []
time_SC = []
i = 0
with open('drop_TcpScalable.csv', 'r') as drop_TcpScalable:
    reader = csv.reader(drop_TcpScalable, delimiter=' ')
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        dps.append(drops/timestamp)
        time_SC.append(timestamp)
        print("-----------------------")
        print("drops:", drops, "prev drops:", prev_drops)
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_SC = dps
######################################
dps = []
time_VE = []
i = 0
with open('drop_TcpVeno.csv', 'r') as drop_TcpVeno:
    reader = csv.reader(drop_TcpVeno, delimiter=' ')
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        dps.append(drops/timestamp)
        time_VE.append(timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_VE = dps
######################################
dps = []
time_YE = []
i = 0
with open('drop_TcpYeah.csv', 'r') as drop_TcpYeah:
    reader = csv.reader(drop_TcpYeah, delimiter=' ')
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        dps.append(drops/timestamp)
        time_YE.append(timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_YE = dps
######################################
dps = []
time_WE = []
i = 0
with open('drop_TcpWestwoodPlus.csv', 'r') as drop_TcpWestwoodPlus:
    reader = csv.reader(drop_TcpWestwoodPlus, delimiter=' ')
    prev_drops = 0
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        dps.append(drops/timestamp)
        time_WE.append(timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_WE = dps
######################################
dps = []
time_HT = []
i = 0
with open('drop_TcpHtcp.csv', 'r') as drop_TcpHtcp:
    reader = csv.reader(drop_TcpHtcp, delimiter=' ')
    prev_drops = 0
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        dps.append(drops/timestamp)
        time_HT.append(timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_HT = dps
######################################
dps = []
time_HY = []
i = 0
with open('drop_TcpHybla.csv', 'r') as drop_TcpHybla:
    reader = csv.reader(drop_TcpHybla, delimiter=' ')
    prev_drops = 0
    for row in reader:
        timestamp = float(row[0]) #value of the first column's row (the time value in the csv)
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        time_HY.append(timestamp)
        dps.append(drops/timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_HY = dps
######################################

print(dps_HS)
plt.plot(time_NR, dps_NR, label = "New Reno")
plt.plot(time_HY, dps_HY, label = "Hybla")
plt.plot(time_HS, dps_HS, label = "High Speed")
plt.plot(time_HT, dps_HT, label = "HTCP")
plt.plot(time_VG, dps_VG, label = "Vegas")
plt.plot(time_SC, dps_SC, label = "Scalable")
plt.plot(time_VE, dps_VE, label = "Veno")
plt.plot(time_B, dps_B, label = "BIC")
plt.plot(time_YE, dps_YE, label = "YeAH")
plt.plot(time_C, dps_C, label = "CUBIC")
plt.plot(time_WE, dps_WE, label = "Westwood Plus")
plt.plot(time_I, dps_I, label = "Illinois")
plt.legend()
plt.legend(ncol=2)
#plt.yscale("log")
plt.xlim([0, 100])
plt.ylabel("Drops per Second")
plt.xlabel("Simulation Time (seconds)")
ax = plt.gca() # to hide the x axis text
#plt.xticks(np.arange(0, 100, 10))
#ax.axes.xaxis.set_ticklabels([])

plt.show()
