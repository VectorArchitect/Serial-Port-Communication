# Serial Port Communication

**A Python-based experimental project for serial data exchange, packet integrity checks, and status monitoring.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Serial](https://img.shields.io/badge/Communication-Serial-0A7B83)
![Status](https://img.shields.io/badge/Project-Experimental-orange)

## Overview

This repository explores communication between a computer and an embedded device over a serial interface. It includes a command-line serial client, a CRC utility for packet checks, and an early Streamlit dashboard prototype for displaying decoded values and bit-level alarm/status information.

> **Project status:** Experimental. The command-line script is configured for a local serial port, while the current Streamlit dashboard uses sample data. The dashboard is not yet connected to the serial device.

## How it fits together

```text
 Embedded device
      │
      │  Serial data (UART / USB-to-Serial)
      ▼
 Python serial client  ──────►  CRC utility
      │                         │
      │                         └─ Append / verify CRC bytes
      ▼
 Received packet
      │
      ▼
 Decode values and status bits
      │
      ▼
 Streamlit dashboard prototype
```

## Repository contents

| File | Purpose |
|---|---|
| `main.py` | Command-line serial communication experiment. Configure the serial port before running. |
| `crc.py` | CRC calculation, packet CRC appending, and packet verification helpers. |
| `gui_try.py` | Streamlit dashboard prototype that currently displays simulated packet data. |
| `bitwise_alarm_system.py` | Small experiment for inspecting set bits in an integer. |
| `data_sent.txt` / `data_recieved.txt` | Placeholder files retained from the original experiment. |

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/VectorArchitect/Serial-Port-Communication.git
cd Serial-Port-Communication
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**
```powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the experiments

### Serial command-line client

1. Connect your device through a serial interface.
2. Open `main.py` and change `COM7` to the correct port for your machine (for example, `/dev/ttyUSB0` on Linux).
3. Confirm the baud rate and packet format match your device firmware.
4. Run:

```bash
python main.py
```

### Streamlit dashboard prototype

```bash
streamlit run gui_try.py
```

The current dashboard renders a hard-coded sample packet. It is useful for exploring the layout and decoding logic, but it does not currently read from the physical serial port.

## CRC utility

`crc.py` provides three main functions:

- `calcrc(data, ldata)` — calculates the CRC bytes for the supplied data.
- `append_crc(data_bytes)` — appends the calculated CRC bytes to a packet.
- `verify_packet(packet_bytes)` — checks the CRC included at the end of a packet.

The implementation is marked CRC-16 with polynomial `0xA001`. CRC variants differ in initialization, reflection, final XOR, and byte order; verify these settings against the embedded device protocol before using it in production.

## Run tests

The hardware-independent CRC regression tests use Python's standard library and do not require a connected serial device:

```bash
python -m unittest discover -s tests -v
```

The GitHub Actions workflow runs this suite on Python 3.10, 3.11, and 3.12 for pushes and pull requests. The serial hardware and Streamlit dashboard still require separate manual verification.

## Configuration notes

- Select the correct serial port and baud rate for your device.
- Ensure both endpoints agree on data bits, parity, stop bits, timeout, packet layout, and CRC convention.
- Do not connect to a port already being used by another application.
- The current scripts are prototypes and have not been validated against every serial device or operating system.

## Roadmap

- [ ] Move serial-port settings out of the source code and into runtime configuration.
- [ ] Connect the Streamlit dashboard to a real serial data source.
- [ ] Add packet-length and CRC validation before decoding incoming data.
- [ ] Add automated tests for serial response framing and payload parsing.
- [ ] Improve error handling, logging, and graceful serial-port cleanup.

## Contributing

Issues and focused pull requests are welcome. For hardware-specific changes, include the serial settings and packet format needed to reproduce the behaviour.

## Author

**SAV!NAV** · [@VectorArchitect](https://github.com/VectorArchitect)

---

*Built as an exploration of Python, serial communication, embedded systems, and data integrity.*
