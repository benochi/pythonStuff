import fcntl
import os

# Open the device file corresponding to the hard drive you want to modify
device_file = '/dev/sda'
device_fd = os.open(device_file, os.O_RDONLY)

# Define the command to change the device status
# The command to set the read-only mode is 0x4d, and the parameter is 1 to enable read-only mode
cmd = 0x4d
param = 1

# Send the command to the device driver using the ioctl system call
fcntl.ioctl(device_fd, cmd, param)

# Close the device file
os.close(device_fd)
