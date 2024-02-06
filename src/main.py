import os
print("Welcome to the Cyberpunk 2077 Hacking Minigame Solver! 🥳\n")
name = input("Enter input file name (ex: input.txt) => ")
try:
    with open(name, 'r') as file:
        buffer_size = int(file.readline().strip())
        dimensions_line = file.readline().strip()
        rows, cols = map(int, dimensions_line.split())
        matrix = []
        for i in range(0, rows):
            matrix.append(list(map(str, file.readline().split()[:cols])))
        num_of_sequences = int(file.readline().strip())
        list_of_sequences = []
        points = []
        for i in range (0,num_of_sequences):
            list_of_sequences.append(list(map(str,file.readline().split())))
            points.append(list(map(int,file.readline().split())))

except FileNotFoundError:
    print(f"The input file named '{name}' was not found.")

print("Buffer size:", buffer_size)
print("Row:", rows)
print("Col:", cols)
print("Matrix:", matrix)
print("Sequences:", num_of_sequences)
print(points)
print(list_of_sequences)
