#include "ns3/point-to-point-module.h"
#include "ns3/ipv4-global-routing-helper.h"
#include <fstream>
#include <string>
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/applications-module.h"
#include "ns3/mobility-module.h"
#include "ns3/config-store-module.h"
#include "ns3/wifi-module.h"
#include "ns3/aodv-module.h"
#include "ns3/olsr-module.h"
#include "ns3/dsdv-module.h"
#include "ns3/dsr-module.h"
#include "ns3/flow-monitor-module.h" //!

#include "ns3/aodv-helper.h"
#include "ns3/internet-module.h"
#include "ns3/netanim-module.h"
#include "ns3/yans-wifi-helper.h"

using namespace ns3;
NS_LOG_COMPONENT_DEFINE ("Mob");

int main (int argc, char *argv[])
{
  CommandLine cmd;
  cmd.Parse (argc, argv);

  NodeContainer c;
  c.Create (20); //20 wireless nodes

//!!!
 WifiHelper wifi;
 wifi.SetStandard (WIFI_STANDARD_80211b);
//80211a, 80211b, 80211n, 2.4g and 5G, 80211ac, 80211ax is also supported.80211p (VANETs, WAVE)
//!!!!

  WifiMacHelper mac;
  mac.SetType ("ns3::AdhocWifiMac");
  //AdhocWifiMac, StaWifiMac, ApWifiMac
  wifi.SetRemoteStationManager ("ns3::ConstantRateWifiManager",
                                "DataMode", StringValue ("OfdmRate54Mbps"));
  //YansWifiPhyHelper wifiPhy = YansWifiPhyHelper::Default (); //!
  YansWifiPhyHelper wifiPhy; //!
  wifiPhy.SetErrorRateModel ("ns3::NistErrorRateModel");
  YansWifiChannelHelper wifiChannel = YansWifiChannelHelper::Default ();
  wifiChannel.SetPropagationDelay ("ns3::ConstantSpeedPropagationDelayModel");
  wifiChannel.AddPropagationLoss ("ns3::FriisPropagationLossModel");
  wifiPhy.SetChannel (wifiChannel.Create ());
  NetDeviceContainer cDevices = wifi.Install (wifiPhy, mac, c);
 //
  NS_LOG_INFO ("Enabling AODV routing on all backbone nodes");
  AodvHelper aodv;
  OlsrHelper olsr;
  DsdvHelper dsdv;
  DsrHelper dsr;
  //AODV protocol is being using FANETs.
  InternetStackHelper internet;
  //internet.SetRoutingHelper (aodv); // has effect on the next Install ()
  internet.SetRoutingHelper (olsr);
  internet.Install (c);

  //
  // Assign IPv4 addresses to the device drivers (actually to the associated
  // IPv4 interfaces) we just created.
  //
  Ipv4AddressHelper ipAddrs;
  ipAddrs.SetBase ("192.168.0.0", "255.255.255.0");
  Ipv4InterfaceContainer cInterfaces;
  cInterfaces=ipAddrs.Assign (cDevices);

 /*
//Mobility Model - 2D
MobilityHelper mobility;

mobility.SetPositionAllocator ("ns3::GridPositionAllocator",
  "MinX", DoubleValue (0.0),
  "MinY", DoubleValue (0.0),
  "DeltaX", DoubleValue (5.0),
  "DeltaY", DoubleValue (10.0),
  "GridWidth", UintegerValue (3),
  "LayoutType", StringValue ("RowFirst"));

mobility.SetMobilityModel ("ns3::RandomWalk2dMobilityModel",  "Bounds", RectangleValue (Rectangle (-100, 100, -100, 100)));
mobility.Install (c);
 */

 //Mobility Model -3D
 MobilityHelper mobility;
/*
mobility.SetMobilityModel ("ns3::GaussMarkovMobilityModel",
  "Bounds", BoxValue (Box (0, 100, 0, 100, 0, 100)),
  "TimeStep", TimeValue (Seconds (0.5)),
  "Alpha", DoubleValue (0.85),
  "MeanVelocity", StringValue ("ns3::UniformRandomVariable[Min=800|Max=1200]"),
  "MeanDirection", StringValue ("ns3::UniformRandomVariable[Min=0|Max=6.283185307]"),
  "MeanPitch", StringValue ("ns3::UniformRandomVariable[Min=0.05|Max=0.05]"),
  "NormalVelocity", StringValue ("ns3::NormalRandomVariable[Mean=0.0|Variance=0.0|Bound=0.0]"),
  "NormalDirection", StringValue ("ns3::NormalRandomVariable[Mean=0.0|Variance=0.2|Bound=0.4]"),
  "NormalPitch", StringValue ("ns3::NormalRandomVariable[Mean=0.0|Variance=0.02|Bound=0.04]"));
mobility.SetPositionAllocator ("ns3::RandomBoxPositionAllocator",
  "X", StringValue ("ns3::UniformRandomVariable[Min=0|Max=100]"),
  "Y", StringValue ("ns3::UniformRandomVariable[Min=0|Max=100]"),
  "Z", StringValue ("ns3::UniformRandomVariable[Min=0|Max=100]"));
  */
  int64_t streamIndex = 0; // used to get consistent mobility across scenarios
  std::stringstream ss2;
  int nodeSpeed = 20; //in m/s
  int nodePause = 0.25; //in s
  ss2 << nodeSpeed;
  std::string sNodeSpeed = ss2.str ();

  std::stringstream ss3;
  ss3 << nodePause;
  std::string sNodePause = ss3.str ();
  ObjectFactory pos;
  pos.SetTypeId ("ns3::RandomRectanglePositionAllocator");
  pos.Set ("X", StringValue ("ns3::UniformRandomVariable[Min=0.0|Max=300.0]"));
  pos.Set ("Y", StringValue ("ns3::UniformRandomVariable[Min=0.0|Max=1500.0]"));

  Ptr<PositionAllocator> taPositionAlloc = pos.Create ()->GetObject<PositionAllocator> ();
  streamIndex += taPositionAlloc->AssignStreams (streamIndex);

  std::stringstream ssSpeed;
  ssSpeed << "ns3::UniformRandomVariable[Min=0.0|Max=" << nodeSpeed << "]";
  std::stringstream ssPause;
  ssPause << "ns3::ConstantRandomVariable[Constant=" << nodePause << "]";

  mobility.SetMobilityModel ("ns3::RandomWaypointMobilityModel",
                                  "Speed", StringValue (ssSpeed.str ()),
                                  "Pause", StringValue (ssPause.str ()),
                                  "PositionAllocator", PointerValue (taPositionAlloc));
 mobility.Install (c);

 UdpEchoServerHelper echoServer (9);

  ApplicationContainer serverApps = echoServer.Install (c.Get(0));
  serverApps.Start (Seconds (1.0));
  serverApps.Stop (Seconds (120.0));

 UdpEchoClientHelper echoClient (cInterfaces.GetAddress(0), 9);
  echoClient.SetAttribute ("MaxPackets", UintegerValue (1));
  echoClient.SetAttribute ("Interval", TimeValue (Seconds (1.0)));
  echoClient.SetAttribute ("PacketSize", UintegerValue (1024));

  ApplicationContainer clientApps = echoClient.Install (c.Get(1));
  clientApps.Start (Seconds (2.0));
  clientApps.Stop (Seconds (120.0));

wifiPhy.EnablePcapAll ("Fanet3D"); //Packet Capture.
//Network Animation using NetAnim.
AnimationInterface anim("Fanet3D.xml");
//Ascii Trace Metrics can be processed using Tracemetrics Software.
AsciiTraceHelper ascii;
wifiPhy.EnableAsciiAll(ascii.CreateFileStream("Fanet3D.tr"));

  Simulator::Stop (Seconds (120.0));
  Simulator::Run ();
  Simulator::Destroy ();
  return 0;
}
