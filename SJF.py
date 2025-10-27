# ==========================================================
# EXPERIMENT: CPU SCHEDULING ALGORITHM - SHORTEST JOB FIRST
# TYPE: NON-PREEMPTIVE (ONCE A PROCESS STARTS, IT RUNS FULLY)
# LANGUAGE: PYTHON
# ==========================================================

# Function to perform Shortest Job First (Non-Preemptive) scheduling
def sjf_scheduling(n, arrival_time, burst_time):
    # ------------------------------------------------------
    # n               → Total number of processes
    # arrival_time[]  → Stores when each process arrives
    # burst_time[]    → Stores how much CPU time each process needs
    # ------------------------------------------------------

    processes = [i + 1 for i in range(n)]       # Process IDs: P1, P2, P3, ...
    completed = [False] * n                     # Keeps track of which process is completed
    waiting_time = [0] * n                      # Waiting time for each process
    turnaround_time = [0] * n                   # Turnaround time for each process
    completion_time = [0] * n                   # Time when each process finishes execution

    current_time = 0                            # Tracks the current CPU time
    completed_count = 0                         # Counts how many processes are completed

    # ---------------- MAIN SCHEDULING LOOP ----------------
    # Runs until all processes are completed
    while completed_count < n:
        idx = -1                                # Will store index of the selected process
        min_bt = float('inf')                   # Initialize with a large number for comparison

        # Find the process with the shortest burst time among all arrived & incomplete processes
        for i in range(n):
            # Process must have arrived and not be completed
            if arrival_time[i] <= current_time and not completed[i]:
                # Choose the one with the smallest burst time
                if burst_time[i] < min_bt:
                    min_bt = burst_time[i]
                    idx = i

        # If no process has arrived yet, just move time forward by 1 unit
        if idx == -1:
            current_time += 1
            continue

        # ---------------------------------------------
        # Execute the selected process
        # ---------------------------------------------
        current_time += burst_time[idx]         # CPU runs this process till completion
        completion_time[idx] = current_time     # Record when it finished
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]  # Total time taken
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]       # Time spent waiting
        completed[idx] = True                   # Mark process as completed
        completed_count += 1                    # Increase completed count

    # ---------------- RESULT CALCULATIONS ----------------
    total_wt = sum(waiting_time)                # Total waiting time
    total_tat = sum(turnaround_time)            # Total turnaround time

    # ---------------- DISPLAY OUTPUT ----------------
    print("\n--- Shortest Job First (Non-Preemptive) Scheduling ---")
    print("+-----------+--------------+-------------+--------------+----------------+")
    print("| ProcessID | Arrival Time | Burst Time  | Waiting Time | Turnaround Time|")
    print("+-----------+--------------+-------------+--------------+----------------+")

    # Display table for all processes
    for i in range(n):
        print(f"| P{processes[i]:^8} | {arrival_time[i]:^12} | {burst_time[i]:^11} | {waiting_time[i]:^12} | {turnaround_time[i]:^14} |")

    print("+-----------+--------------+-------------+--------------+----------------+")
    print(f"\nAverage Waiting Time     = {total_wt / n:.2f}")
    print(f"Average Turnaround Time  = {total_tat / n:.2f}")

# ---------------- DRIVER CODE ----------------
# Accepts input from user and calls the scheduling function
if __name__ == "__main__":
    print("===============================================")
    print("Shortest Job First (Non-Preemptive) Scheduling")
    print("===============================================")

    # Input number of processes
    n = int(input("\nEnter number of processes: "))

    arrival_time, burst_time = [], []           # Initialize lists

    # Take arrival and burst times from user
    for i in range(n):
        print(f"\nProcess P{i+1}:")
        arrival = int(input("Enter Arrival Time: "))
        burst = int(input("Enter Burst Time: "))
        arrival_time.append(arrival)
        burst_time.append(burst)

    # Call the SJF scheduling function
    sjf_scheduling(n, arrival_time, burst_time)
