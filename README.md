01 // OVERVIEW

MiniMonitor is a lightweight terminal-based system monitoring tool written in Python.

The project uses psutil to collect real-time information about the local system and display it through a simple command-line interface.

The goal is to create a small, practical, and readable monitoring tool while exploring how Python can interact with operating-system resources.

02 // FEATURES

MiniMonitor provides real-time information about:

CPU usage
RAM usage
Total and used RAM
Disk usage
Total and used disk space
Network upload speed
Network download speed
Top processes by CPU usage
Process ID (PID)
Process memory usage
Automatic terminal refresh
Cross-platform terminal clearing
Graceful shutdown with Ctrl+C
03 // PREVIEW
============================================================
                  SYSTEM MONITOR
============================================================
CPU Usage      :   17.4%
RAM Usage      :   52.3%
RAM Used       :   8.41 GB / 16.00 GB
Disk Usage     :   61.7%
Disk Used      :   489.32 GB / 793.45 GB
------------------------------------------------------------
NETWORK
Upload Speed   : 125.32 KB/s
Download Speed : 2.41 MB/s
------------------------------------------------------------
TOP PROCESSES BY CPU
PID     PROCESS                  CPU       RAM
------------------------------------------------------------
4128    chrome.exe               8.2       4.3%
9216    python.exe               4.7       1.2%
3044    code.exe                 3.1       6.7%
============================================================
Press Ctrl+C to exit

The values shown above are examples. Actual values depend on the system running the application.

04 // HOW IT WORKS

MiniMonitor continuously collects system information using psutil.

Start
  │
  ▼
Collect system information
  │
  ├── CPU
  ├── RAM
  ├── Disk
  ├── Network
  └── Processes
  │
  ▼
Process & format data
  │
  ▼
Display information
  │
  ▼
Wait
  │
  ▼
Refresh
  │
  └───────────────► Repeat

The monitor continues running until the user stops it with:

Ctrl + C
05 // PROJECT STRUCTURE
MiniMonitor/
│
├── system_monitor.py
├── requirements.txt
└── README.md
system_monitor.py

The main application containing the system monitoring logic and terminal interface.

requirements.txt

Contains the Python dependencies required by the project.

README.md

Project documentation.

06 // REQUIREMENTS
Python 3.x
psutil

No additional monitoring software is required.

07 // INSTALLATION

Clone the repository:

git clone https://github.com/Lowsignal-Code/MiniMonitor.git

Enter the project directory:

cd MiniMonitor

Create a virtual environment.

Windows
python -m venv .venv

Activate it:

.venv\Scripts\activate
Linux / macOS
python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install the required dependency:

pip install -r requirements.txt
08 // RUN

Start the monitor:

python system_monitor.py

The application will continuously refresh the displayed information.

To stop the monitor:

Ctrl + C
09 // TECHNOLOGY
Language
└── Python

Library
└── psutil

Interface
└── Terminal / CLI

Development
├── Git
└── GitHub
10 // SYSTEM MONITORING

MiniMonitor collects information from several areas of the operating system.

CPU

Displays the current overall CPU utilization.

RAM

Displays:

Current memory usage percentage
Used memory
Total available memory
Disk

Displays:

Disk utilization percentage
Used disk space
Total disk space
Network

The application calculates approximate upload and download speeds by comparing network byte counters between consecutive measurements.

Current Bytes
      -
Previous Bytes
      =
Transferred Bytes

The transferred amount is then divided by the refresh interval to estimate the current transfer rate.

Processes

MiniMonitor retrieves running processes and collects information such as:

PID
Process name
CPU usage
Memory usage

Processes are sorted by CPU usage and the top five are displayed.

11 // CROSS-PLATFORM SUPPORT

MiniMonitor includes basic support for Windows, Linux, and macOS.

The terminal clearing command is selected according to the operating system:

os.system("cls" if os.name == "nt" else "clear")

This allows the terminal interface to refresh correctly across different environments.

12 // ERROR HANDLING

Processes can disappear or become inaccessible while the monitor is running.

For example, a process may terminate immediately after being detected.

The application handles common psutil exceptions such as:

NoSuchProcess
AccessDenied

This prevents an individual inaccessible process from terminating the entire application.

13 // PROJECT GOAL

MiniMonitor was created as a practical Python project focused on system interaction and monitoring.

The project explores how Python can retrieve information from the operating system and present it in a useful terminal interface.

It also provides practical experience with:

Python
│
├── Functions
├── Loops
├── Modules
├── Exceptions
├── Lists
├── Dictionaries
├── Sorting
├── Formatting
└── External Libraries
14 // FUTURE IMPROVEMENTS

Possible future improvements include:

[ ] CPU temperature monitoring
[ ] Battery information
[ ] Per-core CPU usage
[ ] Network interface selection
[ ] Process search
[ ] Process filtering
[ ] Configurable refresh rate
[ ] Configurable process count
[ ] Disk I/O monitoring
[ ] Network interface statistics
[ ] System uptime
[ ] Terminal colors
[ ] Interactive CLI
[ ] Configuration file
[ ] Logging

The project is intentionally kept lightweight and focused on the command line.

15 // DEVELOPMENT WORKFLOW
Idea
  ↓
Implementation
  ↓
Testing
  ↓
Debugging
  ↓
Improvement
  ↓
Documentation
  ↓
Git
  ↓
GitHub

The project is part of my ongoing journey of learning Python through practical projects.

16 // STATUS
Project      : MiniMonitor
Version      : 1.0
Language     : Python
Interface    : CLI
Status       : Active
17 // PHILOSOPHY
Observe.
Understand.
Build.
Break.
Debug.
Improve.
Repeat.

The interesting part is usually hidden underneath.

18 // DISCLAIMER

MiniMonitor is an educational and lightweight system monitoring tool.

It is not intended to replace professional system monitoring or infrastructure monitoring solutions.

19 // AUTHOR

Danial

Computer Programming Student interested in:

Python
Linux
Networking
Cybersecurity
Automation
Systems
$ ./minimonitor

Monitoring system...

Status: ONLINE
> exit
Connection closed.

The system keeps running...

⭐ If you find the project useful or interesting, feel free to star the repository.


