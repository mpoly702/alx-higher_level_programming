#!/usr/bin/env python3
import fabric

# Create a directory (i.e. folder)
run("mkdir /tmp/trunk/")

# Uptime
run("uptime")

# Hostname
run("hostname")

# Capture the output of "ls" command
result = run("ls -l /var/www")

# Check if command failed
result.failed
# Check if command succeeded
result.succeeded