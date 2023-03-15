import os

# Open the device file corresponding to the hard drive you want to modify
device_file = '\\\\.\\PhysicalDrive0'
device_fd = os.open(device_file, os.O_RDWR | os.O_BINARY)

# Define the new status value as a bytes object
new_status = b'\xF7\xFF\x00\x00'

# Define the buffer size for each write operation
buffer_size = 4096

# Seek to the start of the device file
os.lseek(device_fd, 0, os.SEEK_SET)

# Loop through each block on the hard drive and overwrite it with zeros
while True:
    buffer = b'\x00' * buffer_size
    bytes_written = os.write(device_fd, buffer)
    if bytes_written == 0:
        break

# Seek to the offset where the status value is located
os.lseek(device_fd, 0x1C2, os.SEEK_SET)

# Write the new status value to the device file
os.write(device_fd, new_status)

# Close the device file
os.close(device_fd)
