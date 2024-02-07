import time
import random
print("Welcome to the Cyberpunk 2077 Hacking Minigame Solver! 🥳\n")
print("Made by Thea Josephine 13522012 :>\n")
print("Do you want to use an input file or customized random tokens? (1/2)\n")
print("1. Input file (.txt)\n")
print("2. Customized and randomized (CLI)\n")
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
        def get_tokens():
            unique_tokens = int(input("Number of unique tokens: "))
            while True:
                tokens = list(map(str, input(f"Enter {unique_tokens} tokens separated by space: ").split()))
                if len(tokens) == unique_tokens:
                    return tokens
                else:
                    print(f"Please enter exactly {unique_tokens} number of unique tokens. Try again.")

        tokens = None
        matrix_values = None
        num_of_sequences = None
        seq_max_size = None
        buffer_size = None

        questions = [
            {"key": "tokens", "prompt": "Enter tokens", "values": None},
            {"key": "matrix", "prompt": "The size of the matrix rows x cols", "values": None},
            {"key": "num_of_sequences", "prompt": "How many sequence(s)", "values": None},
            {"key": "seq_max_size", "prompt": "Sequence max size", "values": None},
            {"key": "buffer_size", "prompt": "Buffer size", "values": None}
        ]

        random.shuffle(questions)
        for question in questions:
            key = question["key"]
            prompt = question["prompt"]
            if "tokens" in key:
                tokens = get_tokens()
            elif "matrix" in key:
                ins = input(f"{prompt}: ")
                inssplit = ins.split()
                rows = int(inssplit[0])
                cols = int(inssplit[1])
            elif "buffer_size" in key:
                buffer_size = int(input(f"{prompt}: "))
            elif "num_of_sequences" in key:
                num_of_sequences = int(input(f"{prompt}: "))
            elif "seq_max_size" in key:
                seq_max_size = int(input(f"{prompt}: "))

        # TESTING - Input by CLI
        print("Tokens:", tokens)
        print("Buffer Size:", buffer_size)
        print("Matrix Size (rows x cols):", rows, "x",cols)
        print("Number of Sequences:", num_of_sequences)
        print("Sequence Max Size:", seq_max_size)

        # Randomized matrix
        matrix = [[None for _ in range(cols)] for _ in range(rows)]
        mused = [[True for _ in range(cols)] for _ in range(rows)]

        for i in range (rows):
            for j in range (cols):
                matrix[i][j] = random.choice(tokens.copy())

        print("Randomized matrix:\n")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

        # Randomized list of seq
        print(f"There is {num_of_sequences} amount of sequences:")
        list_of_sequences = []
        for i in range (num_of_sequences):
            seq =  random.choices(tokens, k=random.randint(2, seq_max_size))
            list_of_sequences.append(seq)
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in list_of_sequences]))
        
        # Randomized list of points
        points = []
        for i in range (num_of_sequences):
            pts = random.choice([0,10,20,30,40,50,60,70,80,90,100])
            points.append(pts)
        print("Points",points)

        break
    else:
        print("Wrong input, try again.\n")

# Base variables
points_obtained = 0
coords = []

# Check if there is a token seq in there -> boolean
def check_next_vertical(row,col,token,matrix):
    for i in range (0,row):
        if (matrix[i][col] == token):
            return True
        else:
            return False
def check_next_horizontal(row,col,token,matrix):
    for i in range (0,col):
        if (matrix[row][i] == token):
            return True
        else:
            return False
        
# Check if current buffer could be connected to the seqarr to check on overlapping
def can_connect(curr_buffer,seqarr):
    for i in range (len(curr_buffer)):
        if (curr_buffer[i] == seqarr[0]):
            count=0
            for j in range (len(seqarr)-1):
                if(curr_buffer[j+i] == seqarr[j]):
                    count+=1
                if len(curr_buffer)-count==0:
                    return True
    return False

 

# starts dengan currbuffer kosong, bakal while loop hingga len(currbuffer) full
start_time = time.time()
for i in range (0,cols):
    curr_buffer = []
    while (len(curr_buffer) <= buffer_size):
        curr_buffer.append(matrix[0][i])
        # for j in range (rows-2):

end_time = time.time()
elapsed_time = end_time - start_time
# TESTING reading file inputs
print("\nBuffer size:", buffer_size)
print("Row:", rows)
print("Col:", cols)
print("\nMatrix:")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
print("\nSequences:", num_of_sequences)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in list_of_sequences]))
print("Points",points)

# Output on terminal
print(points_obtained)
print(' '.join(curr_buffer))
print(coords)
print(str(elapsed_time) + " ms\n")
while(True):
    prompt = input("Do you want to save the result? (y/n) => ")
    if (prompt == "y"):
        output_name = input("Output file name? (ex: output.txt) => ")
        with open(output_name, "w") as output:
            output.write(str(points_obtained) + "\n")
            output.write(str(' '.join(curr_buffer)) + "\n") 
            # TESTING - Save coords not yet implemented
            output.write(f"{elapsed_time} ms")
        output.close()
        print("Saved successfully.\n")
        break
    elif (prompt == "n"):
        print("You did not save the result.\n")
        break
    else:
        print("Wrong input, try again.\n")


