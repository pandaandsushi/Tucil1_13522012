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
            pts = random.choice([-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100])
            points.append(pts)
        print("Points: ",points)

        break
    else:
        print("Wrong input, try again.\n")



# Check if there is a token seq in there -> boolean
def check_vertical_initial(idcol,token,matrix,sumrow):
    count = 0
    for i in range (0,sumrow):
        # jika ada kemungkinan token muncul di pencarian vertikal nantinya,
        # token akan masuk ke curr buffer
        if (matrix[i][idcol] == token):
            count+=1
        if count!=0:
            return True
        else:
            return False
        
def check_next_vertical(idrow,idcol,token,matrix,sumrow):
    count = 0
    for i in range (sumrow):
        # jika ada kemungkinan token muncul di pencarian vertikal nantinya,
        # token akan masuk ke curr buffer
        if (matrix[i][idcol] == token) and (i!=idrow):
            count+=1
        if count!=0:
            return True
        else:
            return False
def check_next_horizontal(idrow,idcol,token,matrix,sumcol):
    for i in range (sumcol):
        if (matrix[idrow][i] == token) and (i!=idcol):
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

def count_points(buffer,arr_of_seq,arr_of_points):
    res = 0
    for i in range (len(arr_of_seq)):
        for j in range (len(buffer)):
            if (buffer[j]==arr_of_seq[i][0]):
                count = 1
                for k in range(len(arr_of_seq[i])-1):
                    if (buffer[k+j+1] == arr_of_seq[i][k+1]):
                        count += 1
                if count == len(arr_of_seq[i]):
                    res += arr_of_points[i]
                    break
    return res

def find_optimum_points (sets_of_buffer,arr_of_seq,arr_of_points):
    final_buffer = []
    final_points = 0
    for i in range (len(sets_of_buffer)):
        temp = count_points(sets_of_buffer[i],arr_of_seq,arr_of_points)
        if temp>final_points:
            final_points = temp
            final_buffer = sets_of_buffer[i]
    return final_points,final_buffer

def max_point(curr_buffer,list_of_sequences,points,final_points):
    curr_points = count_points(curr_buffer,list_of_sequences,points) 
    if final_points == None:
        final_points = curr_points
        final_buffer = curr_buffer
    elif final_points < curr_points:
        final_points = curr_points
        final_buffer = curr_buffer
    return final_points,final_buffer

def process(rows, cols, idcol, mused, matrix, list_of_sequences, curr_buffer, points, buffer_size, seq):
    i=0
    while len(curr_buffer) < buffer_size:
        # choose from vertical angle
        while i < rows:
            copy_mused = mused
            id_seq = len(curr_buffer)
            if check_next_horizontal(i,idcol,list_of_sequences[seq][id_seq],matrix,cols) and mused[i][idcol] != False:
                curr_buffer.append(matrix[i][idcol])
                mused[i][idcol] = False
                final_points, final_buffer = max_point(curr_buffer,list_of_sequences,points,final_points)
                # choose from horizontal angle
                j = 0
                while j < cols:
                    if len(curr_buffer) < buffer_size:
                        sec_copy_mused = mused
                        id_seq = len(curr_buffer)

                        if check_next_vertical(j, i, list_of_sequences[seq][id_seq], matrix, rows) and mused[j][i] != False:
                            curr_buffer.append(matrix[j][i])
                            mused[j][i] = False
                            final_points,final_buffer = max_point(curr_buffer, list_of_sequences, points, final_points)
                            i = 0  # Reset i to 0 in the next iteration
                            break

                        mused = sec_copy_mused
                    else:
                        break

                    j += 1
                mused = copy_mused
            i += 1

    return final_points,final_buffer

# def process(rows,cols,idcol,mused,matrix,list_of_sequences,curr_buffer,points,buffer_size,seq):
#     while (len(curr_buffer) < buffer_size):
#         # choose from vertical angle
#         for i in range(rows):
#             copy_mused = mused
#             id_seq = len(curr_buffer)
#             if (check_next_horizontal(i,idcol,list_of_sequences[seq][id_seq],matrix,cols) and mused[i][idcol]!=False): #ini masih versi pop yg bawah jg
#                 curr_buffer.append(matrix[i][idcol]) 
#                 mused[i][idcol] = False
#                 final_points,final_buffer = max_point(curr_buffer,list_of_sequences,points)
#                 # choose from vertical angle
#                 for j in range(cols):
#                     if len(curr_buffer)<buffer_size:
#                         sec_copy_mused = mused
#                         id_seq = len(curr_buffer)
#                         if(check_next_vertical(j,i,list_of_sequences[seq][id_seq],matrix,rows) and mused[j][i]!=False):
#                             curr_buffer.append(matrix[j][i])  
#                             mused[j][i] = False
#                             up_final_points,up_final_buffer = max_point(curr_buffer,list_of_sequences,points,final_points)
#                             # i should go to i loop again from
#                         mused = sec_copy_mused
#                     else:
#                         break
#             mused = copy_mused
#     return up_final_points,up_final_buffer


# Base variables
curr_coords = []             # array of array of kumpulan koordinat posible ans
final_points = None        # didapat dari mencari poin terbesar dan optimum
final_buffer = []       # didapat dari mencari buffer teroptimum
final_coords = []
start_time = time.time()
for seq in range (num_of_sequences):
    curr_buffer = []
    print("Sequence ke-" + str(seq))
    mused = [[True for _ in range(cols)] for _ in range(rows)]
    for idcol in range (cols):    # check mulai dr baris pertama
        print("tes")
        copy_seq = list_of_sequences[seq]   # copy sequence ke seq
        if check_vertical_initial(idcol,list_of_sequences[seq][0],matrix,rows):
            if (matrix[0][idcol] == list_of_sequences[seq][0]):
                curr_buffer.append(matrix[0][idcol])
                mused[0][idcol] = False
            i=0
            while len(curr_buffer) < buffer_size:
                # choose from vertical angle
                while i < rows:
                    copy_mused = mused
                    id_seq = len(curr_buffer)
                    if check_next_horizontal(i,idcol,list_of_sequences[seq][id_seq],matrix,cols) and mused[i][idcol] != False:
                        curr_buffer.append(matrix[i][idcol])
                        mused[i][idcol] = False
                        final_points, final_buffer = max_point(curr_buffer,list_of_sequences,points,final_points)
                        # choose from horizontal angle
                        j = 0
                        while j < cols:
                            if len(curr_buffer) < buffer_size:
                                sec_copy_mused = mused
                                id_seq = len(curr_buffer)

                                if check_next_vertical(j, i, list_of_sequences[seq][id_seq], matrix, rows) and mused[j][i] != False:
                                    curr_buffer.append(matrix[j][i])
                                    mused[j][i] = False
                                    final_points,final_buffer = max_point(curr_buffer, list_of_sequences, points, final_points)
                                    i = 0  # Reset i to 0 in the next iteration
                                    break

                                mused = sec_copy_mused
                            else:
                                break

                            j += 1
                        mused = copy_mused
                    i += 1

                # final_points,final_buffer = process(rows,cols,idcol,mused,matrix,list_of_sequences,curr_buffer,points,buffer_size,seq)
                # cek vertikal dulu
                # for i in range(rows):
                #     if (check_next_horizontal(i,idcol,list_of_sequences[seq][0],matrix,cols) and mused[i][idcol]!=False): #ini masih versi pop yg bawah jg
                #         curr_buffer.append(matrix[i][idcol]) 
                #         mused[i][idcol] = False
                #         # cek horizontal
                #         for j in range(cols):
                #             if(check_next_vertical(j,i,list_of_sequences[seq][0],matrix,rows) and mused[j][i]!=False):
                #                 curr_buffer.append(matrix[j][i])  
                #                 mused[j][i] = False
            # curr_points = count_points(curr_buffer,list_of_sequences,points) 
            # if final_points == None:
            #     final_points = curr_points
            #     final_buffer = curr_buffer
            # elif final_points < curr_points:
            #     final_points = curr_points
            #     final_buffer = curr_buffer
                    
# final_points, final_buffer = find_optimum_points(sets_of_buffer, list_of_sequences, sets_of_points)

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
print("---------------- Results:\n")
print("Points obtained: " + str(final_points))
print(' '.join(final_buffer))
print(final_coords)
print(str(elapsed_time) + " ms\n")
while(True):
    prompt = input("Do you want to save the result? (y/n) => ")
    if (prompt == "y"):
        output_name = input("Output file name? (ex: output.txt) => ")
        with open(output_name, "w") as output:
            output.write(str(final_points) + "\n")
            output.write(str(' '.join(final_buffer)) + "\n") 
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


