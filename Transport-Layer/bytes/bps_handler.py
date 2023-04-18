import csv
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})

######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpNewReno.csv', 'r') as TcpNewReno:
    reader = csv.reader(TcpNewReno, delimiter=' ')
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
bps_NR = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpVegas.csv', 'r') as TcpVegas:
    reader = csv.reader(TcpVegas, delimiter=' ')
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
bps_VE = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpBic.csv', 'r') as TcpBic:
    reader = csv.reader(TcpBic, delimiter=' ')
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
bps_B = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpCubic.csv', 'r') as bytes_TcpCubic:
    reader = csv.reader(bytes_TcpCubic, delimiter=' ')
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
bps_C = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpHighSpeed.csv', 'r') as bytes_TcpHighSpeed:
    reader = csv.reader(bytes_TcpHighSpeed, delimiter=' ')
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
bps_HS = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpIllinois.csv', 'r') as bytes_TcpIllinois:
    reader = csv.reader(bytes_TcpIllinois, delimiter=' ')
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
bps_I = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpScalable.csv', 'r') as bytes_TcpScalable:
    reader = csv.reader(bytes_TcpScalable, delimiter=' ')
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
bps_SC = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpVeno.csv', 'r') as bytes_TcpVeno:
    reader = csv.reader(bytes_TcpVeno, delimiter=' ')
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
bps_VE = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpYeah.csv', 'r') as bytes_TcpYeah:
    reader = csv.reader(bytes_TcpYeah, delimiter=' ')
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
bps_YE = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpWestwoodPlus.csv', 'r') as bytes_TcpWestwoodPlus:
    reader = csv.reader(bytes_TcpWestwoodPlus, delimiter=' ')
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
bps_WE = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpHtcp.csv', 'r') as bytes_TcpHtcp:
    reader = csv.reader(bytes_TcpHtcp, delimiter=' ')
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
bps_HT = bps
######################################
bps = list(range(0, 100))
time = list(range(0, 100))
i = 0
with open('bytes_TcpHybla.csv', 'r') as bytes_TcpHybla:
    reader = csv.reader(bytes_TcpHybla, delimiter=' ')
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
bps_HY = bps
######################################
plt.plot(time, bps_NR, label = "New Reno")
plt.plot(time, bps_HY, label = "Hybla")
plt.plot(time, bps_HS, label = "High Speed")
plt.plot(time, bps_HT, label = "HTCP")
plt.plot(time, bps_VE, label = "Vegas")
plt.plot(time, bps_SC, label = "Scalable")
plt.plot(time, bps_VE, label = "Veno")
plt.plot(time, bps_B, label = "BIC")
plt.plot(time, bps_YE, label = "YeAH")
plt.plot(time, bps_C, label = "CUBIC")
plt.plot(time, bps_WE, label = "Westwood Plus")
plt.plot(time, bps_I, label = "Illinois")
plt.legend()
plt.legend(ncol=2)
#plt.yscale("log")
plt.xlim([0, 100])

plt.ylabel("Bytes per Second")
plt.xlabel("Simulation Time (seconds)")

plt.show()
