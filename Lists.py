Names = ['Murtaza', 'Abeera', 'Umer', 'Hassan', 'Hashir']

print(len(Names))

print()

for name in Names:
    print(name)

print()

print(Names)

print(Names[1:4])

print()

# find largest number in a list
numbers = [2, 23, 11, 15, 6]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i

print(f"Largest number: {largest}")

print()

# useful functions (append, pop, insert(index, number), clear, remove, index, count, sort, reverse)