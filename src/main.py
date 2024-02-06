import time
print("Welcome to the Cyberpunk 2077 Hacking Minigame Solver! 🥳\n")
print("Do you want to use an input file or customized random tokens? (1/2)\n")
print("1. Input file (.txt)\n")
print("2. Customized (CLI)\n")
while(True):
    byCLI_or_file = input("=> ")
    if (byCLI_or_file == "1"):
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
                
                break
        except FileNotFoundError:
            print(f"The input file named '{name}' was not found.")  
    elif (byCLI_or_file == "2"):
        unique_tokens = int(input("Number of unique tokens: "))
        tokens = []
        # TESTING - MASIH SALAH BLM BS BACA IN ONE LINE
        for i in range (0,unique_tokens):
            ins = input()
            tokens.append(str(ins))
        buffer_size = int(input("Buffer size: "))
        ins = input("The size of the matrix rows x cols: ")
        inssplit = ins.split()
        rows = int(inssplit[0])
        cols = int(inssplit[1])
        num_of_sequences = input("How many sequence(s): ")
        seq_max_size = input("Sequence max size: ")
        # TESTING - add randomized
        break
    else:
        print("Wrong input, try again.\n")

# Base variables
points_obtained = 0
curr_buffer = []
coords = []

start_time = time.time()




end_time = time.time()
elapsed_time = end_time - start_time

# Output on terminal
print(points_obtained)
print(' '.join(curr_buffer))
print(coords)
print(str(elapsed_time) + " ms\n")
while(True):
    prompt = input("Do you want to save the result? (y/n) => ")
    if (prompt == "y"):
        output_name = input("Output file name? (ex: output.txt)=>")
        with open(output_name, "w") as output:
            output.write(str(points_obtained))
            output.write(str(' '.join(curr_buffer))) 
            
            output.write(f"{elapsed_time} ms")
        output.close()
        print("Saved successfully.\n")
        break
    elif (prompt == "n"):
        print("You did not save the result.\n")
        break
    else:
        print("Wrong input, try again.\n")


# TESTING reading file inputs
print("\nBuffer size:", buffer_size)
print("Row:", rows)
print("Col:", cols)
print("Matrix:", matrix)
print("Sequences:", num_of_sequences)
print(points)
print(list_of_sequences)
