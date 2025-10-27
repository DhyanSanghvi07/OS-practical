# Priority CPU Scheduling (Non-Preemptive)

def priority_scheduling(n, arrival_time, burst_time, priority):
    processes = [i + 1 for i in range(n)]
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    current_time = 0
    completed_count = 0

    while completed_count < n:
        idx = -1
        highest_priority = float('inf')

        for i in range(n):
            if arrival_time[i] <= current_time and not completed[i]:
                if priority[i] < highest_priority:
                    highest_priority = priority[i]
                    idx = i

        if idx == -1:
            current_time += 1
            continue

        current_time += burst_time[idx]
        completion_time[idx] = current_time
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        completed[idx] = True
        completed_count += 1

    total_wt = sum(waiting_time)
    total_tat = sum(turnaround_time)

    print("\n--- Priority Scheduling (Non-Preemptive) ---")
    print("+-----------+--------------+-------------+-----------+--------------+----------------+")
    print("| ProcessID | Arrival Time | Burst Time  | Priority  | Waiting Time | Turnaround Time|")
    print("+-----------+--------------+-------------+-----------+--------------+----------------+")
    for i in range(n):
        print(f"| P{processes[i]:^8} | {arrival_time[i]:^12} | {burst_time[i]:^11} | {priority[i]:^9} | {waiting_time[i]:^12} | {turnaround_time[i]:^14} |")
    print("+-----------+--------------+-------------+-----------+--------------+----------------+")
    print(f"\nAverage Waiting Time     = {total_wt / n:.2f}")
    print(f"Average Turnaround Time  = {total_tat / n:.2f}")


# Driver
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    arrival_time, burst_time, priority = [], [], []
    for i in range(n):
        arrival_time.append(int(input(f"Enter Arrival Time for Process P{i+1}: ")))
        burst_time.append(int(input(f"Enter Burst Time for Process P{i+1}: ")))
        priority.append(int(input(f"Enter Priority for Process P{i+1} (lower number = higher priority): ")))
    priority_scheduling(n, arrival_time, burst_time, priority)
