#!/bin/bash
# ==========================================================
# Experiment: Basic Memory Management Commands in Linux
# Commands: df, free, vmstat, /proc/meminfo, htop
# ==========================================================

clear
echo "==================================================="
echo "Basic Memory Management Commands in Linux"
echo "==================================================="

# 1. df - Display disk space usage
echo -e "\n[1] Displaying disk space usage using 'df -h':"
df -h

# 2. free - Show system memory usage
echo -e "\n[2] Displaying system memory status using 'free -h':"
free -h

# 3. vmstat - Display system performance statistics
echo -e "\n[3] Displaying system performance statistics using 'vmstat 1 5':"
vmstat 1 5

# 4. /proc/meminfo - View detailed memory information
echo -e "\n[4] Displaying detailed memory information from '/proc/meminfo':"
head -15 /proc/meminfo

# 5. htop - Interactive process and memory viewer (auto closes after 10 seconds)
echo -e "\n[5] Displaying 'htop' :"
htop

echo -e "\n==================================================="
echo "End of Basic Memory Management Commands Demonstration"
echo "==================================================="
