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

## Running a simulation

Download the contents of the "scratch" folder in this github repo, and place them inside the `/ns-allinone-3.35/ns-3.35/scratch` folder of your NS3 installation.

### Manet-routing-compare

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
