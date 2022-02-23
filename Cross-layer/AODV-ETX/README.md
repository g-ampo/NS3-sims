# ns3-aodv-etx
This project implements ETX metric in AODV routing protocol in NS3 simulator.
Project is work in progress. Updated to work with 3.28 release.

To try how it works, you should do the following:
1) Delete all files from folder /ns-3.28/src/aodv/model in your ns-3 instalation (save these files if you want to restore them later);
2) Then copy all files from folder aodv/model from this repository to folder /ns-3.28/src/aodv/model in your ns-3 instalaltion;
3) Do the same with file wscript from folder aodv from this repository to folder /ns-3.28/src/aodv in your ns-3 instalaltion;
4) Write a script that uses aodv routing protocol and you are ready to go. You can use script file provided for you in folder scratch. Put it in your scratch folder and run.

You can use the scripts located in the scratch folder, and the process will be the same as in the legacy-layer routing protols:

Download the contents of the "scratch" folder in this github repo, and place them inside the `/ns-allinone-3.35/ns-3.35/scratch` folder of your NS3 installation.

### Running the simulation

By default, the simulations run with following parameters:
1. number of nodes: 50
2. Number of sinks: 10
3. Propagation Model: ConstantSpeedPropagationDelay
4. Propagation Loss Model: Friis
5. Position Allocator: RandomRectangularPositionAllocator
6. MAC: AdhocWifiMAC
7. MAC Standard: 802.11b
8. Throughput: 2kbps
9. Total simulation time: 200 sec
10. Node velocity: 20m/s
11. Node pause time: 0
12. Protocol: OLSR/AODV/DSDV/DSR

The original version of this script uses the Random Waypoint Mobility Model.

The 'v3' version of this script has been modified to use the Gauss Markov Mobility Model.

Set `m_protocol` inside the code (line 113) to various values to control the routing protocol:

`m_protocol (1)`: OLSR

`m_protocol (2)`: AODV

`m_protocol (3)`: DSDV

`m_protocol (4)`: DSR

Open a terminal and navigate to the ns-3.35 folder:

`cd ~/ns-allinone-3.28.1/ns-3.28.1`

Run the simulation:

`./waf --run scratch/manet-routing-compare` (random waypoint mobility model)

or:

`./waf --run scratch/manet-routing-compare-v3` (gaus markov mobility model)

Run the simulation twice: once for e.g., AODV, and once for OLSR. Do not neglect to change the output file name by setting it anew at `m_CSVfileName ("manet-routing-compare-v3.csv")`, at line 117.

## Simulation Outputs

After running the simulation, in the directory /ns-allinone-3.35/ns-3.35 there should have been created the following files:

1. manet-routing.output.csv
2. manet-routing.output.flowmon
3. manet-routing.output.mob

### Flow statistics

Lets visualise the flow statistics of our simulation.

Copy the contents of the "Simulation results processing" folder inside the directory containing the 3 files mentioned above.

We will use the flow.py script and the manet-routing.output.flowmon file mentioned above.

run:

`python3 flow.py manet-routing.output.flowmon`

repeat this for both your AODV and OLSR files.

In the same directory, a new file "results.pdf" will be created.

![image](https://user-images.githubusercontent.com/71447362/150393845-96709b52-78d3-43fb-ad46-2f999e9238e2.png)

### Receive rate

For the packet receive rate, we will use the script found in the "Simulation results processing" folder:

```
set terminal pdf 
set output "Packetrate.pdf"
set title "Receive Rate"
set xlabel "Simulated Seconds"
set ylabel "Receive Rate"
plot "GNUPLOT-manet-routing.output.csv" using 1:2 with lines title "AODV", "OLSR.csv" using 1:2 with lines title "OLSR"

set title "Packets Received"
set xlabel "Simulated Seconds"
set ylabel "No of Packets Received"
plot "AODV.csv" using 1:3 with lines title "AODV", "OLSR.csv" using 1:3 with lines title "OLSR"
```

PUBLICATIONS:
1. Telfor Journal, http://journal.telfor.rs/Published/Vol10No1/Vol10No1_A4.pdf
2. Telfor conference, https://ieeexplore.ieee.org/document/8249315, DOI: 10.1109/TELFOR.2017.8249315
