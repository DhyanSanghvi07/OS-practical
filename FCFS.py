# FCFS CPU Scheduling Algorithm (with Arrival Time)
# Calculates Waiting Time, Turnaround Time, and their Averages

def find_avg_time(processes, n, arrival_time, burst_time):
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes by arrival time (to simulate FCFS)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arrival_time[i] > arrival_time[j]:
                arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                processes[i], processes[j] = processes[j], processes[i]

    # Calculate Completion, Turnaround, and Waiting times
    for i in range(n):
        if i == 0:
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            if arrival_time[i] > completion_time[i - 1]:
                completion_time[i] = arrival_time[i] + burst_time[i]
            else:
                completion_time[i] = completion_time[i - 1] + burst_time[i]

        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    total_wt = sum(waiting_time)
    total_tat = sum(turnaround_time)

    # Display results
    print("\n+-----------+--------------+-------------+--------------+-----------------+")
    print("| ProcessID | Arrival Time | Burst Time  | Waiting Time | Turnaround Time |")
    print("+-----------+--------------+-------------+--------------+-----------------+")
    for i in range(n):
        print(f"| {"P"+(str)(processes[i]):^9} | {arrival_time[i]:^12} | {burst_time[i]:^11} | {waiting_time[i]:^12} | {turnaround_time[i]:^15} |")
    print("+-----------+--------------+-------------+--------------+-----------------+")

    print(f"\nAverage Waiting Time     = {total_wt / n:.2f}")
    print(f"Average Turnaround Time  = {total_tat / n:.2f}")


# Driver code
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = [i + 1 for i in range(n)]
    arrival_time = []
    burst_time = []

    for i in range(n):
        at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
        bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
        arrival_time.append(at)
        burst_time.append(bt)

    find_avg_time(processes, n, arrival_time, burst_time)