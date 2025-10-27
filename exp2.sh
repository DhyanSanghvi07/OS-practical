#!/bin/bash
# ==========================================================
# Experiment: Process Related Commands in Linux
# Commands: top, ps, kill, wait, sleep, nice, renice, bg, fg
# ==========================================================

echo "==============================================="
echo "Process Related Commands Demonstration (Linux)"
echo "==============================================="

# 1️⃣ ps - Show list of processes
echo -e "\n1. Showing all current running processes using 'ps -e':"
ps -e | head -10

# 2️⃣ top - Real-time process monitoring
echo -e "\n2. Displaying system processes with 'top' (press 'q' to quit):"
top -n 1

# 3️⃣ sleep - Pause the process for given time
echo -e "\n3. Demonstrating 'sleep' command (pauses execution for 5 seconds):"
sleep 5
echo "Sleep complete!"

# 4️⃣ background (&) and fg/bg
echo -e "\n4. Running a command in the background using '&':"
sleep 30 &
PID=$!
echo "Background process started with PID: $PID"
echo "Check background jobs using: jobs"

echo -e "\nYou can move background jobs to foreground using 'fg %job_number' manually if suspended with Ctrl+Z."

# 5️⃣ wait - Wait for process to complete
echo -e "\n5. Using 'wait' to wait for background process to finish:"
wait $PID
echo "Background process $PID has completed."

# 6️⃣ nice - Start a process with modified priority
echo -e "\n6. Starting a process with 'nice' (lower priority):"
nice -n 10 sleep 5 &
NICE_PID=$!
echo "Started 'sleep 5' with PID: $NICE_PID and nice value of +10"
wait $NICE_PID

# 7️⃣ renice - Change priority of a running process
echo -e "\n7. Changing process priority using 'renice':"
sleep 60 &
REPID=$!
echo "New process started with PID: $REPID"
renice +15 $REPID
echo "Priority of process $REPID changed to +15"
kill $REPID

# 8️⃣ kill - Terminate a process
echo -e "\n8. Demonstrating 'kill' command:"
sleep 100 &
KILLPID=$!
echo "Process started with PID: $KILLPID"
kill $KILLPID
echo "Process $KILLPID terminated using kill command."

echo -e "\n==============================================="
echo "End of Process Commands Demonstration"
echo "==============================================="
