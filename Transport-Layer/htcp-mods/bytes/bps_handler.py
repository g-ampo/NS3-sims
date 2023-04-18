import csv
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})

######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpHtcp.csv', 'r') as TcpHtcp:
    reader = csv.reader(TcpHtcp, delimiter=' ')
    prev_timestamp = 0
    prev_bytes = 0
    for row in reader:
        timestamp = int(float(row[0])) #value of the first column's row (the time value in the csv)
        bytes = int(row[1]) #value of the second column's row (the bytes value in the csv)
        if timestamp != prev_timestamp:
            bps[i] = (bytes-prev_bytes)
            print("-----------------------")
            print("curr:", timestamp, "prev:", prev_timestamp)
            print("bytes:", bytes, "prev bytes:", prev_bytes)
            print("bytes per second:", bps[i])
            print("-----------------------")
            prev_timestamp = timestamp
            prev_bytes = bytes
            i+=1
bps_HTCP = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpShtcp.csv', 'r') as TcpShtcp:
    reader = csv.reader(TcpShtcp, delimiter=' ')
    prev_timestamp = 0
    prev_bytes = 0
    for row in reader:
        timestamp = int(float(row[0])) #value of the first column's row (the time value in the csv)
        bytes = int(row[1]) #value of the second column's row (the bytes value in the csv)
        if timestamp != prev_timestamp:
            bps[i] = (bytes-prev_bytes)
            print("-----------------------")
            print("curr:", timestamp, "prev:", prev_timestamp)
            print("bytes:", bytes, "prev bytes:", prev_bytes)
            print("bytes per second:", bps[i])
            print("-----------------------")
            prev_timestamp = timestamp
            prev_bytes = bytes
            i+=1
bps_SHTCP = bps
######################################
plt.plot(time, bps_HTCP, label = "HTCP")
plt.plot(time, bps_SHTCP, label = "S-HTCP")
plt.legend()
plt.legend(ncol=2)
#plt.yscale("log")
plt.xlim([0, 100])

plt.ylabel("Bytes per Second")
plt.xlabel("Simulation Time (seconds)")

plt.show()
