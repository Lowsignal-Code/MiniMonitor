# System Monitor

A lightweight, terminal-based system monitoring tool written in Python. It displays real-time CPU, RAM, disk, and network usage, along with the top processes consuming CPU resources, all in a continuously refreshing dashboard directly in your terminal.

The tool is built entirely on top of [psutil](https://pypi.org/project/psutil/) and the standard library, with no external UI framework required, making it easy to read, modify, and extend.

## Table of Contents

- [Features](#features)
- [Preview](#preview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)
- [Contributing](#contributing)

## Features

- Real-time CPU usage percentage
- RAM usage percentage and used/total memory
- Disk usage percentage and used/total space
- Live upload and download network speed
- Top 5 processes sorted by CPU usage (PID, name, CPU%, RAM%)
- Auto-refreshing display with configurable refresh rate
- Human-readable byte formatting (B, KB, MB, GB, TB, PB)
- Cross-platform screen clearing (Windows and Unix-based systems)

## Preview

```
============================================================
                  SYSTEM MONITOR
============================================================
CPU Usage      :   12.4%
RAM Usage      :   58.7%
RAM Used       : 9.15 GB / 15.60 GB
Disk Usage     :   71.2%
Disk Used      : 214.30 GB / 300.00 GB
------------------------------------------------------------
NETWORK
Upload Speed   : 12.45 KB/s
Download Speed : 340.10 KB/s
------------------------------------------------------------
TOP PROCESSES BY CPU
PID     PROCESS                  CPU       RAM
------------------------------------------------------------
1234    chrome                   18.2      6.3%
5678    python                   9.5       1.1%
9012    explorer                 3.0       0.8%
3456    code                     2.7       2.4%
7890    system                   1.1       0.2%
============================================================
Press Ctrl+C to exit
```

The exact numbers will vary depending on your system's current load.

## Requirements

- Python 3.7 or newer
- [psutil](https://pypi.org/project/psutil/), a cross-platform library for retrieving process and system utilization information
- A terminal or command-line environment (Windows Command Prompt/PowerShell, macOS Terminal, or a Linux shell)

## Installation

Clone the repository:

```bash
git clone https://github.com/<honeyspyder>/<MiniMonitor>.git
cd <MiniMonitor>
```

It is recommended to use a virtual environment to keep dependencies isolated:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

Install the required dependency:

```bash
pip install psutil
```

Alternatively, if a `requirements.txt` file is included in the repository:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the terminal:

```bash
python Main.py
```

On startup, the script takes an initial network snapshot, then enters a loop that:

1. Waits for the configured refresh interval.
2. Recalculates CPU, RAM, disk, and network statistics.
3. Clears the terminal screen.
4. Redraws the dashboard with the updated values.

The monitor will keep refreshing automatically until interrupted. Press `Ctrl+C` at any time to stop it gracefully; the script catches the interrupt, clears the screen, and prints a shutdown message instead of raising a traceback.

**Note:** On some operating systems, retrieving accurate per-process CPU percentages may require running the script with administrator/root privileges, since `psutil` may not be able to access information for processes owned by other users otherwise.

## Configuration

The refresh interval can be adjusted by changing the `REFRESH_RATE` constant (in seconds) near the top of the script:

```python
REFRESH_RATE = 1
```

Increasing this value reduces CPU overhead from the monitor itself and produces smoother average network speed readings, at the cost of a less "live" feel. Decreasing it makes the dashboard update more frequently but increases the script's own resource usage.

Other aspects of the script that can be easily customized include:

- The number of top processes displayed, by changing the slice `processes[:5]` in `get_top_processes()`.
- The sorting criterion for the process list, by changing the `key` used in the `sort()` call (for example, sorting by memory usage instead of CPU usage).
- The width and formatting of the printed tables, by adjusting the `f-string` field widths in `display_system_info()`.

## Project Structure

```
.
├── system_monitor.py   # Main application script
└── README.md
```

## How It Works

- **CPU, RAM, and disk statistics** are gathered using `psutil.cpu_percent()`, `psutil.virtual_memory()`, and `psutil.disk_usage()`, respectively. Disk usage is measured for the system's root path, resolved with `os.path.abspath(os.sep)` so the script works correctly on both Windows and Unix-based systems.
- **Network speed** is not read directly from `psutil`, since it only exposes cumulative byte counters. Instead, the script takes two snapshots of `psutil.net_io_counters()` a fixed interval apart, computes the difference in bytes sent and received, and divides by the elapsed time to derive an upload and download rate in bytes per second.
- **Top processes** are collected with `psutil.process_iter()`, which iterates over all currently running processes. Each process's PID, name, CPU percentage, and memory percentage are extracted, and processes that raise `psutil.NoSuchProcess` or `psutil.AccessDenied` (for example, due to insufficient permissions or a process that exited mid-iteration) are silently skipped. The resulting list is sorted by CPU usage in descending order, and only the top five entries are kept.
- **Byte formatting** is handled by `get_size()`, which converts a raw byte count into a human-readable string by repeatedly dividing by 1024 and stepping through the units B, KB, MB, GB, TB, and PB.
- **The display loop** clears the terminal on every cycle using the platform-appropriate command (`cls` on Windows, `clear` on Unix-based systems) and reprints the full dashboard, which creates the effect of a continuously updating, in-place monitor.

## Limitations

- CPU usage percentages, particularly for individual processes, may be less accurate on the very first refresh cycle, since `psutil` needs a baseline measurement to compare against.
- Network speed reflects total system-wide traffic across all interfaces, not per-application usage.
- Disk usage is reported only for the root/system drive; additional mounted drives or partitions are not shown.
- Accessing information for processes owned by other users may be restricted by the operating system unless the script is run with elevated privileges.
- The dashboard is designed for standard terminal widths; extremely narrow terminal windows may cause the layout to wrap or misalign.

## Roadmap

Potential future improvements include:

- Support for monitoring multiple disks and network interfaces individually.
- A configurable number of displayed processes, exposed as a command-line argument.
- Logging of historical usage data to a file for later analysis.
- An option to sort the process list by memory usage instead of CPU usage.
- A curses-based or `rich`-based interface for smoother rendering without a full screen clear.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or submit an issue.
