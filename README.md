# SDN Path Tracing Tool using POX & Mininet
## Problem Statement

The objective of this project is to design and implement a Software Defined Networking (SDN) based Path Tracing Tool using the POX controller and Mininet. 
The controller tracks and logs the path taken by packets across different switches in the network.

## Objectives
* To understand how an SDN controller communicates with switches.
* To track the path taken by packets in the network.
* To implement basic OpenFlow rules (match and action).
* To observe how the network behaves during normal and failure conditions.
* To analyze network performance using ping and iperf.

## Tools & Technologies
* Mininet (Network Emulator)
* POX Controller
* OpenFlow Protocol
* Python

## Network Topology
* A linear topology is used:
* h1 — s1 — s2 — s3 — h2
* h1, h2 → Hosts
* s1, s2, s3 → OpenFlow switches

## Setup & Execution
### Step 1: Start POX Controller
```
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 path_tracer
```
### Step 2: Start Mininet
```
sudo mn --topo linear,3 --controller=remote
```
## Test Scenarios
### Scenario 1: Normal Communication
```
h1 ping h2
```
**Expected Output:**
* Successful ping (0% packet loss)
* Path is displayed in controller logs

###  Scenario 2: Link Failure
```
link s2 s3 down
h1 ping h2
```

##  Performance Analysis
### Latency (Ping)
```
h1 ping h2
```
### Throughput (iperf)
```
iperf h1 h2
```
## Flow Table Inspection
To view flow rules installed in switches:
```
sudo ovs-ofctl dump-flows s1
```
## Proof of Execution
Screenshots included in the `/screenshots` folder:
* Controller logs showing path tracing
* Successful ping output
* Failure scenario (link down)
* Flow table entries
* iperf results

##  SDN Concepts Used
* Control Plane vs Data Plane separation
* OpenFlow protocol communication
* Packet_In event handling
* Flow rule installation (match–action)
* Dynamic path observation

##  Observations
* The controller successfully tracks packet paths across switches.
* When a link fails, packet delivery is affected, demonstrating dependency on topology.
* Flow rules are dynamically handled based on network traffic.

## References
* POX Controller Documentation
* Mininet Documentation
* OpenFlow Protocol Specification


