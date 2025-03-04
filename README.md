


# RAFT Distributed Key-Value Store

This project implements a simplified version of the RAFT consensus algorithm in a distributed key-value store. RAFT is a consensus algorithm that is designed to be easy to understand and provides a way to manage a replicated log. It's used to ensure consistency across a cluster of nodes in a distributed system.

## Features

- Leader election
- Log replication
- Heartbeats for maintaining authority
- Follower and candidate modes
- Dynamic timeout to handle partitions and recover from leader failures

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.x installed on your system to run this project. No external libraries are required as the project uses standard libraries that come with Python 3.

```bash
python3 --version
```

### Installing

Clone the repository to your local machine:

```bash
git clone https://yourrepositorylink.com
cd your-repository-folder
```

### Running the Server

To run a single node of the RAFT server, you can use the following command:

```bash
make run all
```

This command starts the RAFT server with default settings. Modify the `Makefile` to change the default configuration such as `PORT`, `NODE_ID`, and `OTHER_NODES`.



## Issues Faced and Solutions Implemented

### 1. Leader Election Issues

**Problem Description:**  
One of the primary challenges in implementing the RAFT consensus algorithm was ensuring reliable leader election. We encountered issues where leaders were not being elected due to network delays, improper handling of election timeouts, and conflicts arising from simultaneous candidate promotions.

**Solutions Implemented:**
- **Dynamic Election Timeouts:** We adjusted the election timeouts dynamically based on the network conditions to reduce collisions in leader elections.
- **Heartbeat Mechanism Enhancement:** Improved the heartbeat mechanism to ensure timely heartbeats, helping followers stay updated with the leader's status, thereby preventing unnecessary transitions to candidate status.
- **Term Validation:** Ensured that nodes only vote for candidates from either the same or a higher term, which helped in maintaining a single, consistent leader per term as intended.

### 2. Issues with Appending Entries

**Problem Description:**  
Entries were not being consistently appended to the logs of all followers, primarily due to network partitions or followers temporarily going offline, leading to an inconsistent state across the cluster.

**Solutions Implemented:**
- **Robust Log Matching:** Implemented a more robust log matching check before appending new entries. If mismatches are detected, followers truncate their logs to the last known agreed-upon entry and request refills from the leader.
- **Batching of Append Entries:** Introduced batching in the append entries mechanism to handle high throughput and reduce the overhead of frequent log replication, especially useful in high-latency networks.
- **Failure Recovery Mechanism:** Developed a recovery mechanism where followers can request missing entries after detecting gaps in their logs during heartbeat checks.

### 3. Managing Redundancy Between Replicas

**Problem Description:**  
Ensuring redundancy and data consistency across replicas was challenging, especially in scenarios involving network failures or partitions, where some replicas might end up isolated.

**Solutions Implemented:**
- **Replication Policies:** Introduced policies to control the replication process, such as ensuring that data is replicated to a majority of nodes before it is considered committed.
- **Frequent State Checks:** Implemented frequent state checks and reconciliations among nodes to ensure all replicas stay consistent with the leader. This was particularly crucial after resolving network partitions.
- **Enhanced Logging and Monitoring:** Improved logging and monitoring of state changes across nodes to quickly identify and resolve discrepancies in data replication.

### Additional Insights

The challenges faced during the implementation highlighted the importance of robust testing, especially in a distributed system where network issues and node failures are common. Simulating various network conditions and node behaviors in a test environment was crucial in identifying and fixing the issues related to leader election, log replication, and redundancy management. Future improvements may include more sophisticated algorithms for dynamic adjustment of parameters based on ongoing system performance and further optimizations in the log compaction process to enhance the overall efficiency and reliability of the system.

# Distributed-KeyValue-Store
