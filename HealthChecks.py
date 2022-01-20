#!/usr/bin/env python3
import psutil
import shutil


def check_disk_usage(disk):
    du = shutil.disk_usage("/")  # In bytes.
    free = du.free / du.total * 100  # In percentage
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)  # Interval of 1.0 second, check overall usage.
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():  # Use conditional if and logical not.
    print("ERROR!")
else:
    print("Everything OK!")
