#!/usr/bin/env python3

import os

uptime = os.popen("uptime -p").read().strip()
print(f"System Uptime: {uptime}")
