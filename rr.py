# Round Robin CPU Scheduling Algorithm (with Arrival Time)
# Proper version that avoids infinite loops and handles arrival times correctly

def round_robin(n, arrival_time, burst_time, quantum):
    processes = [i + 1 for i in range(n)]
    remaining_bt = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    current_time = 0
    ready_queue = []
    visited = [False] * n
    completed = 0

    while completed < n:
        # Add processes that have arrived
        for i in range(n):
            if arrival_time[i] <= current_time and not visited[i]:
                ready_queue.append(i)
                visited[i] = True

        if not ready_queue:
            current_time += 1
            continue

        idx = ready_queue.pop(0)

        # Execute current process
        if remaining_bt[idx] > quantum:
            current_time += quantum
            remaining_bt[idx] -= quantum
        else:
            current_time += remaining_bt[idx]
            remaining_bt[idx] = 0
            completion_time[idx] = current_time
            turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
            completed += 1

        # Add any newly arrived processes during this time
        for i in range(n):
            if (arrival_time[i] <= current_time and not visited[i]):
                ready_queue.append(i)
                visited[i] = True

        # If current process is not done, put it back at the end
        if remaining_bt[idx] > 0:
            ready_queue.append(idx)

    total_wt = sum(waiting_time)
    total_tat = sum(turnaround_time)

    print("\n--- Round Robin Scheduling ---")
    print("+-----------+--------------+-------------+--------------+----------------+")
    print("| ProcessID | Arrival Time | Burst Time  | Waiting Time | Turnaround Time|")
    print("+-----------+--------------+-------------+--------------+----------------+")
    for i in range(n):
        print(f"| P{processes[i]:^8} | {arrival_time[i]:^12} | {burst_time[i]:^11} | {waiting_time[i]:^12} | {turnaround_time[i]:^14} |")
    print("+-----------+--------------+-------------+--------------+----------------+")
    print(f"\nAverage Waiting Time     = {total_wt / n:.2f}")
    print(f"Average Turnaround Time  = {total_tat / n:.2f}")


# Driver code
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    arrival_time, burst_time = [], []
    for i in range(n):
        arrival_time.append(int(input(f"Enter Arrival Time for Process P{i+1}: ")))
        burst_time.append(int(input(f"Enter Burst Time for Process P{i+1}: ")))
    quantum = int(input("Enter Time Quantum: "))

    round_robin(n, arrival_time, burst_time, quantum)
