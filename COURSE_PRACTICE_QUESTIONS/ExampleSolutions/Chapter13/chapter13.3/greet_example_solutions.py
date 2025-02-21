#!/usr/bin/env python3

import sys
from datetime import datetime

# Get script name from sys.argv[0]
script_name = sys.argv[0]

# Get your name from sys.argv[1]
# Remember: Check if a name was provided!
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "Unknown"

# Get current time (use the hint provided above)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print the three required lines
print(f"This script is: {script_name}")
print(f"It was run at: {current_time}")
print(f"Hello {name}!")