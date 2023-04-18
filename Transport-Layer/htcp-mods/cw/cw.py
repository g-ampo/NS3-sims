import csv
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})

####################################################
x = list(range(0, 100)) # time
y = list(range(0, 100)) # abs cwnd variance
i = 0

with open('cw_TcpHtcp.csv', 'r') as TcpHtcp:
    reader = csv.reader(TcpHtcp, delimiter=' ')
    prev_timestamp = 0
    prev_cw = 55700 #value just brefore the 1st second
    for row in reader:
        timestamp = int(float(row[0])) #value of the first column's row (the time value in the csv)
        cw = int(row[1]) #value of the second column's row (the cw value in the csv)
        if timestamp != prev_timestamp:
            print("-----------------------")
            print("curr:", timestamp, "prev:", prev_timestamp)
            print("cw:", cw, "prev cw:", prev_cw)
            print("abs prev - curr:", abs(cw-prev_cw))
            print("-----------------------")
            y[i] = abs(cw-prev_cw)            
            i += 1
            prev_timestamp = timestamp
            prev_cw = cw

abs_cwnd_avg = y
window_size = 1
j = 0
moving_averages_HTCP = []
while j < len(abs_cwnd_avg) - window_size + 1:
    this_window = abs_cwnd_avg[j : j + window_size]
    window_average = sum(this_window) / window_size
    moving_averages_HTCP.append(window_average)
    j += 1
    window_size += 1
####################################################
x = list(range(0, 100)) # time
y = list(range(0, 100)) # abs cwnd variance
i = 0

with open('cw_TcpShtcp.csv', 'r') as TcpShtcp:
    reader = csv.reader(TcpShtcp, delimiter=' ')
    prev_timestamp = 0
    prev_cw = 2680 #value just brefore the 1st second
    for row in reader:
        timestamp = int(float(row[0])) #value of the first column's row (the time value in the csv)
        cw = int(row[1]) #value of the second column's row (the cw value in the csv)
        if timestamp != prev_timestamp:
            print("-----------------------")
            print("curr:", timestamp, "prev:", prev_timestamp)
            print("cw:", cw, "prev cw:", prev_cw)
            print("abs prev - curr:", abs(cw-prev_cw))
            print("-----------------------")
            y[i] = abs(cw-prev_cw)
            i += 1
            prev_timestamp = timestamp
            prev_cw = cw

abs_cwnd_avg = y
window_size = 1
j = 0
moving_averages_SHTCP = []
while j < len(abs_cwnd_avg) - window_size + 1:
    this_window = abs_cwnd_avg[j : j + window_size]
    window_average = sum(this_window) / window_size
    moving_averages_SHTCP.append(window_average)
    j += 1
    window_size += 1

plt.plot(moving_averages_HTCP, label = "HTCP")
plt.plot(moving_averages_SHTCP, label = "S-HTCP")

plt.legend()
plt.legend(ncol=2)
plt.xlim([0.5, 49])
plt.ylabel("Cumulative Moving Avg. of Abs. CWND Difference (MSS)")
plt.xlabel("Simulation Time (seconds)")
#plt.yscale("log")

ax = plt.gca() # to hide the x axis text
ax.axes.xaxis.set_ticklabels([0, 20, 40, 60, 80])

plt.show()

#plt.plot(x, y)
#plt.xlabel("Seconds")
#plt.ylabel("|CWND variance|")
#plt.show()
