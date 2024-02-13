import time
import random

print("Welcome to the Cyberpunk 2077 Hacking Minigame Solver! 🥳\n")
print("Made by Thea Josephine 13522012 :>\n")
print("Do you want to use an input file or customized random tokens? (1/2)\n")
print("1. Input file (.txt)\n")
print("2. Customized and randomized (CLI)\n")
#  Ensure use inputs a positive int
def positive_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Value has to be bigger than 0")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
while True:
    byCLI_or_file = input("=> ")
    if byCLI_or_file == "1":
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
                for i in range(0, num_of_sequences):
                    list_of_sequences.append(list(map(str, file.readline().split())))
                    points.extend([int(x) for x in file.readline().split()])
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
                buffer_size = positive_input(f"{prompt}: ")
            elif "num_of_sequences" in key:
                num_of_sequences = positive_input(f"{prompt}: ")
            elif "seq_max_size" in key:
                seq_max_size = positive_input(f"{prompt}: ")



        # Randomized matrix
        matrix = [[None for _ in range(cols)] for _ in range(rows)]

        for i in range (rows):
            for j in range (cols):
                matrix[i][j] = random.choice(tokens.copy())

        print("Randomized matrix:\n")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

        # Randomized list of seq
        print(f"There is {num_of_sequences} amount of sequences:")
        list_of_sequences = []
        for i in range (num_of_sequences):
            seq =  random.sample(tokens, k=random.randint(2, seq_max_size))
            list_of_sequences.append(seq)
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in list_of_sequences]))
        
        # Randomized list of points
        points = []
        for i in range (num_of_sequences):
            pts = random.choice([-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100])
            points.append(pts)
        print("Points: ",points)

        break
    else:
        print("Wrong input, try again.\n")



# Display reading file inputs
print("\nBuffer size:", buffer_size)
print("Row:", rows)
print("Col:", cols)
print("\nMatrix:")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
print("\nSequences:", num_of_sequences)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in list_of_sequences]))
print("Points",points)
print("")

# Check if there is a token seq in there -> boolean
def check_vertical_initial(idcol,token,matrix,sumrow):  # special for first token in a seq
    for i in range (0,sumrow):
        if (matrix[i][idcol] == token):
            return True
    return False
def check_next_vertical(idrow,idcol,token,matrix,sumrow):
    for i in range (sumrow):
        if (matrix[i][idcol] == token) :
           return True
    return False
def check_next_horizontal(idrow,idcol,token,matrix,sumcol):
    for i in range (0,sumcol):
        if (matrix[idrow][i] == token):
            return True
    return False

# count total points from a buffer
def count_points(buffer,arr_of_seq,arr_of_points):
    res = 0
    for i in range (len(arr_of_seq)):
        if sublist(buffer,arr_of_seq[i]):
            res+=arr_of_points[i]
    return res

# To know if a sublist is a part of main_list
def sublist(main_list, sublist):
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False

def find_optimum_points (sets_of_buffer,arr_of_seq,arr_of_points):
    final_buffer = []
    final_points = 0
    for i in range (len(sets_of_buffer)):
        temp = count_points(sets_of_buffer[i],arr_of_seq,arr_of_points)
        if temp>final_points:
            final_points = temp
            final_buffer = sets_of_buffer[i]
    return final_points,final_buffer

# Decide to change the max point or not
def max_point(curr_buffer,curr_coords,list_of_sequences,points,final_points,final_buffer,final_coords):
    curr_points = count_points(curr_buffer,list_of_sequences,points) 
    if final_points < curr_points:
        final_points = curr_points
        final_coords = curr_coords
        final_buffer = curr_buffer
    return final_points,final_buffer,final_coords

def check_seq(curr_buffer,list_of_sequences):
    count=0
    for i in range (len(list_of_sequences)):
        if sublist(curr_buffer,list_of_sequences[i]):
            count+=1
    if count==len(list_of_sequences):
        return True
    return False 

# for last token needed
def last_token(curr_buffer,final_points,list_of_sequences,token,points,final_buffer,final_coords,curr_coords):
    curr_buffer.append(token)
    final_points, final_buffer,final_coords = max_point(curr_buffer,curr_coords,list_of_sequences,points,final_points,final_buffer,final_coords)
    return final_buffer,final_points,final_coords

# for last token needed, check if the last token is there or not
def check_next_withindex(matrix,token,cols,rows,id,type):
    if type == 0:       # check horizontal
        for i in range (cols):
            if matrix[id][i]==token:
                return True,i
        return False,0
    else:               # check vertical
        for i in range (rows):
            if matrix[i][id]==token:
                return True,i
        return False,0

# list all possible sequences 
def new_seq(sequences, curr_sequence=None, remaining_sequences=None, size_limit=None, all_sequences=None):
    if curr_sequence is None:
        curr_sequence = []
    if remaining_sequences is None:
        remaining_sequences = sequences.copy()
    if all_sequences is None:
        all_sequences = []

    if curr_sequence and len(curr_sequence) <= size_limit:
        all_sequences.append(curr_sequence.copy())
    if len(curr_sequence) >= size_limit:
        return

    for i, seq in enumerate(remaining_sequences):
        overlap_len = find_overlap(curr_sequence, seq)
        if overlap_len > 0:
            new_sequence = curr_sequence + seq[overlap_len:]
            new_remaining = remaining_sequences[:i] + remaining_sequences[i + 1:]
            new_seq(sequences, new_sequence, new_remaining, size_limit, all_sequences)
        else:
            new_sequence = curr_sequence + seq
            new_remaining = remaining_sequences[:i] + remaining_sequences[i + 1:]
            new_seq(sequences, new_sequence, new_remaining, size_limit, all_sequences)
    return all_sequences

# count the number of tokens overlapping
def find_overlap(seq1, seq2):
    for i in range(1, min(len(seq1), len(seq2)) + 1):
        if seq1[-i:] == seq2[:i]:
            return i
    return 0

# Base variables
curr_coords = []        # array of array of kumpulan koordinat posible ans
final_points = 0        # didapat dari mencari poin terbesar dan optimum
final_buffer = []       # didapat dari mencari buffer teroptimum
final_coords = []
seq = 0
old_seq = list_of_sequences
old_point = points
checklist = [True for _ in range (len(list_of_sequences))]
counter = 0

start_time = time.time()


print("＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊ All Sequences ＊˚*•̩̩͙✩•̩̩͙*˚＊˚*•̩̩͙✩•̩̩͙*˚＊")
list_of_sequences = new_seq(list_of_sequences, size_limit=buffer_size)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in list_of_sequences]))
points = [0 for _ in range (len(list_of_sequences))]
for j in range (len(old_point)):
    for i in range (len(list_of_sequences)):
        if list_of_sequences[i]==old_seq[j] and checklist[j]==True:
            points[i] = old_point[j]
            checklist[j] = False
            
print(points)
num_of_sequences = len(list_of_sequences)


for seq in range (num_of_sequences):
    finish = False
    id_seq = 0
    temp_seq = seq
    print("")
    print("Sequence ke-" + str(seq))
    print("☆*: .｡. oo .｡.:*☆")
    print("Here is the last optimal buffer rn:")
    print(final_buffer)
    if (len(list_of_sequences[seq])<=buffer_size):
        curr_buffer = []
        stop = False
        mainstop = False
        maincounterstop = 0
        checklist = [True for _ in range (num_of_sequences)]
        if mainstop:
            print("⋆ˊˎ-•̩̩͙-*̩̩̥͙ Untuk sequence ini tidak ada solusi\n\n")
            break
        if finish:
            break
        for idcol in range (cols):    # check mulai dr baris pertama
            if finish:
                break
            curr_buffer = []
            curr_coords = []
            mused = [[True for _ in range(cols)] for _ in range(rows)]
            cekveriini = check_vertical_initial(idcol,list_of_sequences[seq][0],matrix,rows)
            if maincounterstop==cols:
                mainstop=True
            if cekveriini==False:
                maincounterstop+=1
            # Only one buffer space available
            if ((buffer_size==1) or (len(list_of_sequences[seq])==1)):
                one_buffer,idcol = check_next_withindex(matrix,list_of_sequences[seq][0],cols,rows,0,0)
                if one_buffer:  # token exists on the first row
                    final_buffer,final_points,final_coords = last_token(curr_buffer,final_points,list_of_sequences,matrix[0][idcol],points,final_buffer,final_coords,curr_coords)
                    final_coords.append((0,idcol))
                    checklist[seq]=False
                    finish = True
                    break
                else:           # token wasn't found on the first row
                    mainstop=True
                    break
            if cekveriini:
                if (buffer_size==len(list_of_sequences[seq]) and matrix[0][idcol]==list_of_sequences[seq][0]) or (buffer_size!=len(list_of_sequences[seq])):
                    curr_buffer.append(matrix[0][idcol])
                    curr_coords.append((0,idcol))
                    id_seq+=1
                    mused[0][idcol] = False
                    i = 0
                    first = True
                    countstop = 0
                    id_seq = len(curr_buffer)
                    if curr_buffer[0]!=list_of_sequences[seq][0]:
                        id_seq-=1

                    # Choose from vertical 
                    while i < rows:
                        if finish:
                            break
                        if check_seq(curr_buffer,list_of_sequences) or len(curr_buffer)==buffer_size:
                            finish=True
                            break
                        if first:
                            copy_mused = mused
                            # Last spot to avoid getting id_seq indexing error (choosing from vertical)
                            if id_seq==len(list_of_sequences[seq])-1: # last spot
                                one_buffer,idx = check_next_withindex(matrix,list_of_sequences[seq][id_seq],cols,rows,idcol,1)
                                if one_buffer and mused[idx][idcol]!=False:
                                    curr_coords.append((idx,idcol))
                                    final_buffer,final_points,final_coords = last_token(curr_buffer,final_points,list_of_sequences,list_of_sequences[seq][id_seq],points,final_buffer,final_coords,curr_coords)
                                    checklist[seq]=False
                                    finish=True
                                    break
                                else:
                                    curr_buffer.pop(len(curr_buffer)-1)
                                    curr_coords.pop(len(curr_buffer))
                                    id_seq-=1
                                    break
                            cekhori = check_next_horizontal(i,idcol,list_of_sequences[seq][id_seq],matrix,cols)
                            if cekhori==False or matrix[i][idcol] != list_of_sequences[seq][id_seq]:
                                countstop+=1
                            if countstop==rows:
                                maincounterstop+=1
                                break
                            if cekhori and mused[i][idcol] != False and matrix[i][idcol] == list_of_sequences[seq][id_seq]:
                                curr_buffer.append(matrix[i][idcol])
                                curr_coords.append((i,idcol))
                                id_seq+=1
                                mused[i][idcol] = False
                                final_points, final_buffer, final_coords = max_point(curr_buffer,curr_coords,list_of_sequences,points,final_points,final_buffer,final_coords)
                            
                                j = 0
                                countstop=0
                                # Choose from horizontal
                                while j < cols:
                                    if check_seq(curr_buffer,list_of_sequences) or len(curr_buffer)==buffer_size:
                                        finish=True
                                        break
                                    if len(curr_buffer) < buffer_size:
                                        sec_copy_mused = mused
                                        # Last spot to avoid getting id_seq indexing error (choosing from horizontal)
                                        if id_seq==len(list_of_sequences[seq])-1: # last spot
                                            one_buffer,idx = check_next_withindex(matrix,list_of_sequences[seq][id_seq],cols,rows,i,0)
                                            if one_buffer:
                                                finish = True
                                                curr_coords.append((i,idx))
                                                final_buffer,final_points,final_coords = last_token(curr_buffer,final_points,list_of_sequences,list_of_sequences[seq][id_seq],points,final_buffer,final_coords,curr_coords)
                                                finish=True
                                                break
                                            else:
                                                curr_buffer.pop(len(curr_buffer)-1)
                                                curr_coords.pop(len(curr_buffer))
                                                id_seq-=1
                                                break
                                        cekveri = check_next_vertical(i, j, list_of_sequences[seq][id_seq], matrix, rows)
                                        if cekveri==False or matrix[i][j] != list_of_sequences[seq][id_seq]:
                                            countstop+=1
                                        if countstop==cols:
                                            stop = True
                                            break
                                        if cekveri and mused[i][j] != False and matrix[i][j] == list_of_sequences[seq][id_seq]:
                                            curr_buffer.append(matrix[i][j])
                                            curr_coords.append((i,j))
                                            id_seq+=1
                                            mused[i][j] = False
                                            final_points,final_buffer,final_coords = max_point(curr_buffer,curr_coords, list_of_sequences, points, final_points,final_buffer,final_coords)
                                            i = -1  # Reset i to 0 in the next iteration
                                            first = False
                                            break
                                        mused = sec_copy_mused
                                    else:
                                        break
                                    j += 1
                                mused = copy_mused
                            i += 1
                        else:
                            # Choose from vertical
                            countstop=0
                            while i < rows:
                                if finish:
                                    break
                                if check_seq(curr_buffer,list_of_sequences) or len(curr_buffer)==buffer_size:
                                    finish=True
                                    break
                                copy_mused = mused
                                # Last spot to avoid getting id_seq indexing error (choosing from vertical)
                                if id_seq==len(list_of_sequences[seq])-1: # last spot
                                    one_buffer,idx = check_next_withindex(matrix,list_of_sequences[seq][id_seq],cols,rows,j,1)
                                    if one_buffer:
                                        curr_coords.append((idx,j))
                                        final_buffer,final_points,final_coords = last_token(curr_buffer,final_points,list_of_sequences,list_of_sequences[seq][id_seq],points,final_buffer,final_coords,curr_coords)
                                        checklist[seq]=False
                                        finish=True
                                        break
                                    else:
                                        curr_buffer.pop(len(curr_buffer)-1)
                                        curr_coords.pop(len(curr_buffer))
                                        id_seq-=1
                                        break
                                cekhori = check_next_horizontal(i,idcol,list_of_sequences[seq][id_seq],matrix,cols)
                                if cekhori==False or matrix[i][idcol] != list_of_sequences[seq][id_seq]:
                                    countstop+=1
                                if countstop==rows:
                                    maincounterstop+=1
                                    break

                                if cekhori and mused[i][j] != False and matrix[i][j] == list_of_sequences[seq][id_seq]:
                                    curr_buffer.append(matrix[i][j])
                                    curr_coords.append((i,j))
                                    id_seq+=1
                                    mused[i][j] = False
                                    final_points, final_buffer, final_coords = max_point(curr_buffer,curr_coords,list_of_sequences,points,final_points,final_buffer,final_coords)
                                    j = 0
                                    countstop=0
                                    # Choose from horizontal
                                    while j < cols:
                                        if check_seq(curr_buffer,list_of_sequences) or len(curr_buffer)==buffer_size:
                                            finish=True
                                            break
                                        if len(curr_buffer) < buffer_size:
                                            sec_copy_mused = mused
                                            if id_seq==len(list_of_sequences[seq])-1: # last spot
                                                one_buffer,idx = check_next_withindex(matrix,list_of_sequences[seq][id_seq],cols,rows,i,0)
                                                if one_buffer:
                                                    curr_coords.append((i,idx))
                                                    final_buffer,final_points,final_coords = last_token(curr_buffer,final_points,list_of_sequences,list_of_sequences[seq][id_seq],points,final_buffer,final_coords,curr_coords)
                                                    checklist[seq]=False
                                                    finish=True
                                                    break
                                                else:
                                                    curr_buffer.pop(len(curr_buffer)-1)
                                                    curr_coords.pop(len(curr_buffer))
                                                    id_seq-=1
                                                    break
                                            cekveri = check_next_vertical(i, j, list_of_sequences[seq][id_seq], matrix, rows)
                                            if cekveri==False or matrix[i][j] != list_of_sequences[seq][id_seq]:
                                                countstop+=1
                                            if countstop==cols:
                                                stop = True
                                                break
                                            if cekveri and mused[j][i] != False and matrix[i][j] == list_of_sequences[seq][id_seq]:
                                                curr_buffer.append(matrix[i][j])
                                                curr_coords.append((i,j))
                                                id_seq+=1
                                                mused[i][j] = False
                                                final_points,final_buffer,final_coords = max_point(curr_buffer,curr_coords, list_of_sequences, points, final_points,final_buffer,final_coords)
                                                i = -1  # Reset i to 0 in the next iteration
                                                first = False
                                                break
                                            mused = sec_copy_mused
                                        else:
                                            break
                                        j += 1
                                    mused = copy_mused
                                i += 1
    print("")
                    
              
end_time = time.time()
elapsed_time = end_time - start_time

# Output on terminal
print("ˏ⸉ˋ‿̩͙‿̩̩̥͙̽‿̩͙ Results ‿̩̥̩‿̩̩̥͙̽‿̩͙ˊ⸊ˎ\n")
print("Points obtained: " + str(final_points))
if final_points==0:
    print("Not worth/no possible solution")
else:
    print("Final buffer:")
    print(' '.join(final_buffer))
    print("Final Coordinates:")
    print(final_coords)
print(str(elapsed_time) + " ms\n")

while(True):
    prompt = input("Do you want to save the result? (y/n) => ")
    if (prompt == "y"):
        output_name = input("Output file name? (ex: output.txt) => ")
        with open(output_name, "w") as output:
            output.write(str(final_points) + "\n")
            output.write(str(' '.join(final_buffer)) + "\n") 
            for c in final_coords:
                output.write(f"{c}\n")
            output.write(f"{elapsed_time} ms")
        output.close()
        print("Saved successfully.\n")
        break
    elif (prompt == "n"):
        print("You did not save the result.\n")
        break
    else:
        print("Wrong input, try again.\n")
print("Thank you for trying my program :>")

