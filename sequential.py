# Sequential File Allocation Method in Python

n = int(input("Enter total number of blocks: "))
blocks = [0] * n  # 0 = free, 1 = allocated

print("\nEnter number of files:")
num_files = int(input())

for i in range(num_files):
    start = int(input(f"\nEnter starting block of file {i+1}: "))
    length = int(input(f"Enter length of file {i+1}: "))

    # Check if all blocks in range are free
    if start + length > n:
        print("Error: File exceeds disk size!")
        continue

    if any(blocks[j] == 1 for j in range(start, start + length)):
        print("Error: Some blocks already allocated!")
        continue

    for j in range(start, start + length):
        blocks[j] = 1

    print(f"File {i+1} allocated from block {start} to {start + length - 1}")

print("\nFinal Block Status:")
for i in range(n):
    print(f"Block {i}: {'Allocated' if blocks[i] else 'Free'}")
