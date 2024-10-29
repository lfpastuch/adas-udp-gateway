# ADAS UDP Gateway

## Overview

This repository contains a set of modules designed to capture, transmit, and manipulate data for Advanced Driver Assistance Systems (ADAS) using UDP. The main components include a capture module, a UDP gateway, a fault injection module, and a main controller that orchestrates the entire process.

**WARNING: This project and its documentation are a work in progress.**

## Architecture Overview

- **Capture Module**: Captures images and point cloud data.
- **UDP Gateway**: Transmits data over UDP.
- **Fault Injection Module**: Injects faults and controls data flow.
- **Main Controller**: Orchestrates the capture, transmission, and fault injection.

## Modules

- **capture.py**: Captures images and point cloud data.
- **udp_gateway.py**: Handles UDP transmission.
- **fault_injection.py**: Injects faults and controls data flow.
- **main.py**: Main controller to integrate all modules.

## IEEE 802.3 Protocol

- Ensure data frames are structured according to the Ethernet frame format.
- Use appropriate headers and payloads for image and point cloud data.

## File Structure

- **capture.py**: Simulates capturing images and point cloud data at 10Hz.
- **udp_gateway.py**: Implements a UDP gateway to send data.
- **fault_injection.py**: Injects faults by dropping or modifying data frames.
- **main.py**: Integrates all modules, captures data, injects faults, and sends data via UDP.
- **udp_server.py**: Implements a simple UDP server that listens on `127.0.0.1:12345` and prints received messages.

## Running the gateway and checking transmitted data

### Create a UDP Server

1. Implement a UDP server that listens on the same IP and port as the UDP gateway.
2. Print the received messages to verify the data transmission.

### Run the UDP Server

- Run the UDP server in a separate terminal or process.

```sh
python udp_server.py
```

### Run the Main Controller

- Run the `main.py` script to start capturing and transmitting data.

```sh
python main.py
```

## Summary

This setup allows you to test the UDP gateway implementation and ensure that data is being transmitted correctly.