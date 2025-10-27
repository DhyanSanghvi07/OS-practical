# FIFO Page Replacement Algorithm in Python

def fifo_page_replacement(pages, capacity):
    memory = []
    total = len(pages)
    faults = 0

    print("\nPage\tMemory State")
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)  # Remove the oldest page
                memory.append(page)
            faults += 1
        print(f"{page}\t{memory}")

    print("\nTotal Page Faults:", faults)
    print("Fault Percentage:",round((faults)/total* 100,2), "%")
    print("Total Page Hits:", total-faults)
    print("Hit Percentage:", round((total-faults)/total * 100,2), "%")


# ---------- Main Program ----------
pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
capacity = int(input("Enter frame capacity: "))
fifo_page_replacement(pages, capacity)
