import os
import sys
import stat
import platform
from datetime import datetime

print("\n==============================")
print("System Call Demonstration (Linux)")
print("==============================\n")

# 1️⃣ getpid()
print("1. getpid() - Current Process ID:")
print("PID:", os.getpid())

# 2️⃣ fork()
print("\n2. fork() - Creating a child process...")
pid = os.fork()

if pid == 0:
    # Child process
    print(f"Child Process Created! PID = {os.getpid()}, Parent PID = {os.getppid()}")

    # 3️⃣ exec() - Replace process with another program
    print("\n3. exec() - Replacing current process with 'ls -l'...")
    os.execlp("ls", "ls", "-l")
else:
    # Parent process
    os.wait()  # Wait for child to finish

    # 4️⃣ pipe()
    print("\n4. pipe() - Communication between processes")
    r, w = os.pipe()

    msg = b"Message sent through pipe!"
    os.write(w, msg)
    os.close(w)

    output = os.read(r, 1024)
    os.close(r)
    print("Message received from pipe:", output.decode())

    # 5️⃣ open() and close()
    print("\n5. open() & close() - Opening and closing a file")
    file_name = "demo_file.txt"
    fd = os.open(file_name, os.O_CREAT | os.O_WRONLY)
    os.write(fd, b"Hello! This file is created using open() system call.\n")
    os.close(fd)
    print(f"File '{file_name}' created and closed successfully.")

    # 6️⃣ stat()
    print("\n6. stat() - File information")
    info = os.stat(file_name)
    print(f"File Size: {info.st_size} bytes")
    print(f"Permissions: {oct(info.st_mode)}")
    print("Last Modified:", datetime.fromtimestamp(info.st_mtime))

    # 7️⃣ uname()
    print("\n7. uname() - System Information")
    sys_info = os.uname()
    print("System Name:", sys_info.sysname)
    print("Node Name:", sys_info.nodename)
    print("Release:", sys_info.release)
    print("Version:", sys_info.version)
    print("Machine:", sys_info.machine)

    # 8️⃣ exit()
    print("\n8. exit() - Terminating parent process gracefully")
    sys.exit(0)
