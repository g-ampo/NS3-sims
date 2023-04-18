import csv
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 18})

######################################
dps = []
time_HTCP = []
i = 0
with open('drop_TcpHtcp.csv', 'r') as TcpHtcp:
    reader = csv.reader(TcpHtcp, delimiter=' ')
    for row in reader:
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        timestamp = float(row[0])
        time_HTCP.append(timestamp)
        dps.append(drops/timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_HTCP = dps
######################################
dps = []
time_SHTCP = []
i = 0
with open('drop_TcpShtcp.csv', 'r') as TcpShtcp:
    reader = csv.reader(TcpShtcp, delimiter=' ')
    for row in reader:
        drops = int(row[1]) #value of the second column's row (the drops value in the csv)
        timestamp = float(row[0])
        time_SHTCP.append(timestamp)
        dps.append(drops/timestamp)
        print("-----------------------")
        print("drops per second:", dps[i])
        print("-----------------------")
        i+=1
dps_SHTCP = dps
######################################


plt.plot(time_HTCP, dps_HTCP, label = "HTCP")
plt.plot(time_SHTCP, dps_SHTCP, label = "S-HTCP")

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
