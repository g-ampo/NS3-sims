# NS3-sims
A note-taking repository to help me document my PhD research. It concerns legacy-layer routing protocols, and cross-layer routing protocols alike. The cross-layer metrics I focus on is ETX.

# Installing NS3
(Assuming linux installation)

Navigate to the [nsnam latest releases](https://www.nsnam.org/releases/latest/) website.

As of the time I am writing this document, the latest version is 3.35.

![image](https://user-images.githubusercontent.com/71447362/148080055-c8776752-a3b6-454a-84a4-8b5884f76f55.png)

Download the ns-allinone-3.35.tar.bz2 file locally.

Extract the .tar.bz2 file.

cd inside the newly extracted `ns3-allinone-3.35` folder.

`./build.py --enable-examples --enable-test`

cd to the `ns-3.28` folder, which is inside the `ns3-allinone-3.35` folder.

`./waf --build-profile=debug --enable-examples --enable-tests configure`

`./waf`

`./test.py -c core`

`./waf --run hello-simulator`

Congrats, ns3 is successfully installed.
