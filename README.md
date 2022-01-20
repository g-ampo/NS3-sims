# NS3-sims
A note-taking repository to help me document my PhD research.

# Installing NS3
(Assuming linux installation)

Navigate to the [nsnam latest releases](https://www.nsnam.org/releases/latest/) website.

As of the time I am writing this document, the latest version is 3.35.

![image](https://user-images.githubusercontent.com/71447362/148080055-c8776752-a3b6-454a-84a4-8b5884f76f55.png)

Download the `ns-allinone-3.35.tar.bz2` file locally.

Extract the `.tar.bz2` file.

cd inside the newly extracted `ns3-allinone-3.35` folder.

`./build.py --enable-examples --enable-test`

cd to the `ns-3.28` folder, which is inside the `ns3-allinone-3.35` folder.

`./waf --build-profile=debug --enable-examples --enable-tests configure`

`./waf`

`./test.py -c core`

`./waf --run hello-simulator`

Congrats, ns3 is successfully installed.

## Manet routing protocol comparison

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

`cd ~/ns-allinone-3.35/ns-3.35`

Run the simulation:

`./waf --run scratch/manet-routing-compare` (random waypoint mobility model)

or:

`./waf --run scratch/manet-routing-compare-v3` (gaus markov mobility model)

## Simulation Outputs

After running the simulation, in the directory /ns-allinone-3.35/ns-3.35 there should have been created the following files:

1. manet-routing.output.csv
2. manet-routing.output.flowmon
3. manet-routing.output.mob

Lets visualise the flow statistics of our simulation.

Copy the contents of the "Simulation results processing" folder inside the directory containing the 3 files mentioned above.

We will use the flow.py script and the manet-routing.output.flowmon file mentioned above.

run:

`python3 flow.py manet-routing.output.flowmon`

In the same directory, a new file "results.pdf" will be created.
