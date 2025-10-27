# Banker's Algorithm in Python
# Determines if the system is in a Safe State and prints the Safe Sequence

def is_safe(n, m, alloc, max_need, avail):
    need = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_need[i][j] - alloc[i][j]

    finish = [False] * n
    safe_seq = []
    work = avail[:]

    print("\nNeed Matrix:")
    for i in range(n):
        print(f"P{i}: {need[i]}")

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for k in range(m):
                        work[k] += alloc[i][k]
                    safe_seq.append(f"P{i}")
                    finish[i] = True
                    found = True
        if not found:
            print("\nSystem is NOT in a safe state.")
            return

    print("\nSystem is in a SAFE STATE.")
    print("Safe Sequence:", " -> ".join(safe_seq))


# ---------------- Main Program ----------------
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resource types: "))

    print("\nEnter Allocation Matrix:")
    alloc = []
    for i in range(n):
        alloc.append(list(map(int, input(f"Allocation for P{i} (space separated): ").split())))

    print("\nEnter Maximum Need Matrix:")
    max_need = []
    for i in range(n):
        max_need.append(list(map(int, input(f"Max Need for P{i} (space separated): ").split())))

    print("\nEnter Available Resources (space separated):")
    avail = list(map(int, input().split()))

    is_safe(n, m, alloc, max_need, avail)
