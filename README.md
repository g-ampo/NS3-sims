# NS3-sims
A note-taking repository to help me document my PhD research. It concerns legacy-layer routing protocols, and cross-layer routing protocols alike. The cross-layer metrics I focus on is ETX.

# Installing NS3
(Assuming linux installation)

Install dependencies:
`sudo apt install g++ python3 python3-dev pkg-config sqlite3 cmake python3-setuptools git qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools gir1.2-goocanvas-2.0 python3-gi python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython3 openmpi-bin openmpi-common openmpi-doc libopenmpi-dev autoconf cvs bzr unrar gsl-bin libgsl-dev libgslcblas0 wireshark tcpdump sqlite sqlite3 libsqlite3-dev  libxml2 libxml2-dev libc6-dev libc6-dev-i386 libclang-dev llvm-dev automake python3-pip libxml2 libxml2-dev libboost-all-dev`

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
