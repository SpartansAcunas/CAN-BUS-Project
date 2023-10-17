# Verification Prototipe for ECUs with CAN BUS

This repository contains the codes used to create a verification prototype for Electronic Control Units (ECUs) using the CAN BUS communication protocol.

## Overview

In summary, this repository includes programs designed for communicating with an automotive module, specifically an Engine Control Unit (ECU). The purpose of this project was to retrieve information from the ECU without directly interfering with the internal components of the module. To achieve this, an interface was used.

The interface consisted of a low-cost embedded system, and a module attached to it. The module was designed in-house using Altium Designer.

## Repository Contents

The repository primarily contains the following components:

- **ReceptorCANBUS:** This is C++ code that was responsible for facilitating communication with the embedded system prepared for CAN BUS communication.

- **Visualizador:** This is Python code used for data collection.

- **Ejecutable:** This Python code acts as an executable program, invoking or calling the Visualizador program, and displaying the collected data in a table format.

- **DATOS:** This archive includes an example of a .txt file, which shows how the data collected by the embedded system is formatted. However, please note that the final presentation of the data in the table may differ when viewed in the executable.

## Contact Information

If you have any questions or comments regarding this project, feel free to contact me.

Thank you for visiting my repository!
