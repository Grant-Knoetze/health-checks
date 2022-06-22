#!/usr/bin/env python3
import psutil
import shutil


def check_disk_usage(disk):
    du = shutil.disk_usage("/")  # In bytes.
    free = du.free / du.total * 100  # In percentage
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(10)  # Interval of 10 seconds, check overall usage.
    return usage < 70


if not check_disk_usage("/") or not check_cpu_usage():  # Use conditional if and logical not.
    print("ERROR!")
else:
    print("Everything OK!")
