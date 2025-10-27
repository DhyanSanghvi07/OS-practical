# LRU Page Replacement Algorithm in Python

def lru_page_replacement(pages, capacity):
    memory = []
    recent = []
    faults = 0
    total = len(pages)

    print("\nPage\tMemory State")
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Find the least recently used page
                lru_page = recent.pop(0)
                memory.remove(lru_page)
                memory.append(page)
            faults += 1
        else:
            recent.remove(page)  # Move to most recent
        recent.append(page)
        print(f"{page}\t{memory}")

    print("\nTotal Page Faults:", faults)
    print("Fault Percentage:",round((faults)/total* 100,2), "%")
    print("Total Page Hits:", total-faults)
    print("Hit Percentage:", round((total-faults)/total * 100,2), "%")


# ---------- Main Program ----------
pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
capacity = int(input("Enter frame capacity: "))
lru_page_replacement(pages, capacity)
