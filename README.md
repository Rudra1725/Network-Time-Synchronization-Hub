# ⏱️ Network Time Synchronization Hub


![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-1F6AA5?style=for-the-badge)
![TCP Sockets](https://img.shields.io/badge/Networking-TCP_Sockets-06B6D4?style=for-the-badge&logo=wireshark&logoColor=white)
![Threading](https://img.shields.io/badge/Engine-Multithreading-orange?style=for-the-badge)
![Time Sync](https://img.shields.io/badge/Function-Time_Exchange-F59E0B?style=for-the-badge&logo=clockify&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### A Python-Based TCP Client-Server Time Exchange Application

A desktop application built with **Python and CustomTkinter** that demonstrates network communication through a dual-panel interface. It allows users to start a time server, request timestamps from a client, measure approximate round-trip latency, and monitor network activity through live logs.

The project combines socket programming, multithreading, and GUI development in a tactical, dark-themed control panel.

## ✨ Features

- 🖥️ **Dual-Panel Interface** — Manage the time server and client from a single desktop window.
- 🌐 **TCP Client-Server Communication** — Exchange timestamp data using Python sockets.
- ⏱️ **Time Request and Response** — Request the server's current local date and time using a `GET_TIME` message.
- 📡 **Latency Measurement** — Measure the approximate round-trip time of a request in milliseconds.
- 📋 **Activity Logs** — Monitor server connections, client requests, timestamps, and errors.
- 🧵 **Multithreading** — Run network operations in background threads to keep the interface responsive.
- 🎨 **Dark Tactical UI** — CustomTkinter panels, recessed displays, status indicators, and a clean technical layout.
- ⚙️ **Configurable Connection** — Specify server and client IP addresses and port numbers.
- 🛡️ **Basic Error Handling** — Handle invalid ports, connection refusals, and socket timeouts.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| CustomTkinter | Graphical user interface |
| Socket | TCP network communication |
| Threading | Background network operations |
| Datetime | Timestamp generation and log timestamps |
| Time | Round-trip elapsed-time measurement |

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10 or newer recommended
- pip package manager

### 2. Clone the Repository

```bash
git clone https://github.com/Rudra1725/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace `YOUR-REPOSITORY` with your actual GitHub repository name.

### 3. Install Dependencies

```bash
pip install customtkinter
```

The other modules used by the application are included in Python's standard library.

### 4. Run the Application

Save the Python script as `main.py`, then execute:

```bash
python main.py
```

## 📖 How to Use

**Step 1: Start the Server**

- Keep the default bind address as `127.0.0.1` for local testing.
- Set the port to `8888` or another available port.
- Click **START SERVER** to begin listening for TCP requests.

**Step 2: Configure the Client**

- Enter the server's IP address.
- Enter the same port number configured on the server.

**Step 3: Request the Time**

- Click **SYNC CLOCK NOW**.
- The client connects to the server and sends a `GET_TIME` request.
- The server returns a timestamp.
- The client displays the received timestamp and approximate round-trip delay.

**Step 4: Monitor Activity**

Use the server and client logs to inspect connection attempts, successful responses, and errors.

## 🔄 How It Works

```text
       TIME CLIENT
            |
            | TCP Connection
            |
            v
       Send GET_TIME
            |
            v
       TIME SERVER
            |
            | Generate Timestamp
            |
            v
       Return Timestamp
            |
            v
       Update Client UI
            |
            v
       Display Time & Latency
```

## 🧠 Concepts Demonstrated

- Client-server architecture
- TCP socket programming
- Network request-response communication
- Multithreading and concurrent execution
- GUI development with Python
- Latency measurement
- Exception handling and connection management

## ⚠️ Important Notes

- This project is a **TCP-based time exchange simulator**, not a complete implementation of the Network Time Protocol (NTP).
- It displays the received timestamp but does not modify the operating system's clock.
- The server uses its own local system time, which may differ from the client's time zone or clock settings.
- The default address, `127.0.0.1`, is for communication on the same computer.
- For testing across two computers, use the server's reachable LAN IP address and configure firewall access appropriately.
- The displayed latency includes connection setup, request processing, and response time; it is not a pure network propagation measurement.

## 🔮 Future Improvements

- Implement the actual NTP protocol using its standard packet format.
- Add a continuously updating digital clock.
- Estimate clock offset using request and response timestamps.
- Add connection status indicators and improved error reporting.
- Support multiple simultaneous client requests with more robust connection management.
- Add timestamp history and latency statistics.

## 👨‍💻 Author

**Rudra1725**

Engineering student exploring Python development, networking, automation, and practical software projects.

🔗 GitHub: [Rudra1725](https://github.com/Rudra1725)

---

⭐ If you find this project useful for learning Python networking, consider starring the repository.

*Built to explore networking fundamentals through practical Python development.*
