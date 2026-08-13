import os
import time
import psutil


REFRESH_RATE = 1


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_size(bytes_value):
    units = ["B", "KB", "MB", "GB", "TB"]

    size = float(bytes_value)

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def get_network_speed(previous_sent, previous_recv, interval):
    current = psutil.net_io_counters()

    upload = (current.bytes_sent - previous_sent) / interval
    download = (current.bytes_recv - previous_recv) / interval

    return upload, download, current.bytes_sent, current.bytes_recv


def get_top_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append(
                {
                    "pid": info["pid"],
                    "name": info["name"] or "Unknown",
                    "cpu": info["cpu_percent"] or 0,
                    "memory": info["memory_percent"] or 0,
                }
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda process: process["cpu"], reverse=True)

    return processes[:5]


def display_system_info(upload, download):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    print("=" * 60)
    print("                  SYSTEM MONITOR")
    print("=" * 60)

    print(f"CPU Usage      : {cpu:>6.1f}%")
    print(f"RAM Usage      : {ram.percent:>6.1f}%")
    print(
        f"RAM Used       : "
        f"{get_size(ram.used)} / {get_size(ram.total)}"
    )

    print(
        f"Disk Usage     : {disk.percent:>6.1f}%"
    )
    print(
        f"Disk Used      : "
        f"{get_size(disk.used)} / {get_size(disk.total)}"
    )

    print("-" * 60)

    print("NETWORK")

    print(f"Upload Speed   : {get_size(upload)}/s")
    print(f"Download Speed : {get_size(download)}/s")

    print("-" * 60)

    print("TOP PROCESSES BY CPU")

    processes = get_top_processes()

    print(f"{'PID':<8}{'PROCESS':<25}{'CPU':<10}{'RAM'}")
    print("-" * 60)

    for process in processes:
        print(
            f"{process['pid']:<8}"
            f"{process['name'][:23]:<25}"
            f"{process['cpu']:<10.1f}"
            f"{process['memory']:.1f}%"
        )

    print("=" * 60)
    print("Press Ctrl+C to exit")


def main():
    previous_network = psutil.net_io_counters()

    previous_sent = previous_network.bytes_sent
    previous_recv = previous_network.bytes_recv

    try:
        while True:
            time.sleep(REFRESH_RATE)

            (
                upload,
                download,
                previous_sent,
                previous_recv,
            ) = get_network_speed(
                previous_sent,
                previous_recv,
                REFRESH_RATE,
            )

            clear_screen()

            display_system_info(upload, download)

    except KeyboardInterrupt:
        clear_screen()
        print("System Monitor stopped.")


if __name__ == "__main__":
    main()