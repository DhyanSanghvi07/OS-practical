#!/bin/bash
# ==========================================================
# Experiment: Communication and Shared Memory Commands in Linux
# Commands: who, wall, write, mesg, cat, ipcs
# ==========================================================

clear
echo "==================================================="
echo "Linux Communication and Shared Memory Commands"
echo "==================================================="

# a) Sending Messages to Logged-in Users
echo -e "\n-------------------------------------------"
echo "PART A: Sending Messages to Logged-in Users"
echo "-------------------------------------------"

# 1. who - List all logged-in users
echo -e "\n[1] Displaying currently logged-in users using 'who':"
who || echo "No users currently logged in."

# 2. wall - Send a broadcast message
echo -e "\n[2] Sending a broadcast message using 'wall':"
echo "System maintenance will start in 5 minutes. Please save your work." | wall

# 3. mesg - Control message permissions
echo -e "\n[3] Checking message permission using 'mesg':"
mesg

echo -e "\nTo disable message reception:  mesg n"
echo "To enable message reception again: mesg y"

# 4. write - Send a private message (manual demo)
echo -e "\n[4] Demonstrating 'write' command (manual test):"
echo "To send a message to a specific user, type:"
echo "  write <username>"
echo "Then type your message and press Ctrl+D to send."
echo "Example: write dhyan"

# 5. cat - Display or send a message from a file
echo -e "\n[5] Using 'cat' to display contents of a message file:"
echo "Hello, this is a system-wide test message!" > message.txt
cat message.txt

# b) Shared Memory Segment Commands
echo -e "\n-------------------------------------------"
echo "PART B: Shared Memory Commands"
echo "-------------------------------------------"

# 6. ipcs - Show System V IPC facilities
echo -e "\n[6] Listing shared memory segments using 'ipcs -m':"
ipcs -m

echo -e "\nUse 'ipcs -s' to view semaphores."
ipcs -s

echo "Use 'ipcs -q' to view message queues."
ipcs -q

echo -e "\n==================================================="
echo "End of Communication and Shared Memory Demonstration"
echo "==================================================="