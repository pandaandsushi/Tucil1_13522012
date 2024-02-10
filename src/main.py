import time
import random

print("Welcome to the Cyberpunk 2077 Hacking Minigame Solver! 🥳\n")
print("Made by Thea Josephine 13522012 :>\n")
print("Do you want to use an input file or customized random tokens? (1/2)\n")
print("1. Input file (.txt)\n")
print("2. Customized and randomized (CLI)\n")

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


# TESTING reading file inputs
print("\nBuffer size:", buffer_size)
print("Row:", rows)
print("Col:", cols)
print("\nMatrix:")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
print("\nSequences:", num_of_sequences)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in list_of_sequences]))
print("Points",points)

# Check if there is a token seq in there -> boolean
def check_vertical_initial(idcol,token,matrix,sumrow):
    count = 0
    for i in range (0,sumrow):
        # print("Matriks",matrix[i][idcol])
        # print("Token",token)
        if (matrix[i][idcol] == token):
            count+=1
        # print("Count",count)
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
    print("Count",count)
    if count!=0:
        return True
    else:
        return False
def check_next_horizontal(idrow,idcol,token,matrix,sumcol):
    count = 0
    for i in range (0,sumcol):
        if (matrix[idrow][i] == token) and (i!=idcol):
            count+=1
    print("Count",count)
    if count!=0:
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
                    return True,count
    return False,0

def count_points(buffer,arr_of_seq,arr_of_points):
    res = 0
    for i in range (len(arr_of_seq)):
        remaindertocheck = len(buffer)
        for j in range (len(buffer)):
            remaindertocheck-=1
            if (buffer[j]==arr_of_seq[i][0]):
                count = 0
                if len(buffer)>=len(arr_of_seq[i]):
                    for k in range(len(arr_of_seq[i])):
                        if remaindertocheck+1<len(arr_of_seq[i]):
                            return 0
                        if (buffer[k+j] == arr_of_seq[i][k]):
                            count += 1
                    if count == len(arr_of_seq[i]):
                        res = arr_of_points[i] + res
                        break
                else:
                    return 0
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

def max_point(curr_buffer,list_of_sequences,points,final_points,final_buffer):
    curr_points = count_points(curr_buffer,list_of_sequences,points) 
    if final_points == None:
        final_points = curr_points
        final_buffer = curr_buffer
    elif final_points < curr_points:
        final_points = curr_points
        final_buffer = curr_buffer
    return final_points,final_buffer


# Base variables
curr_coords = []             # array of array of kumpulan koordinat posible ans
final_points = None        # didapat dari mencari poin terbesar dan optimum
final_buffer = []       # didapat dari mencari buffer teroptimum
final_coords = []

start_time = time.time()
for seq in range (num_of_sequences):
    print("Sequence ke-" + str(seq))
    if (len(list_of_sequences[seq])<=buffer_size):
        curr_buffer = []
        stop=False
        mainstop = False
        maincounterstop=0
        while len(curr_buffer) < buffer_size:
            print(maincounterstop)
            if mainstop:
                break
            for idcol in range (cols):    # check mulai dr baris pertama
                curr_buffer = []
                curr_coords = []
                mused = [[True for _ in range(cols)] for _ in range(rows)]
                cekveriini = check_vertical_initial(idcol,list_of_sequences[seq][0],matrix,rows)
                if maincounterstop==cols:
                    mainstop=True
                if cekveriini==False:
                    maincounterstop+=1
                print("LAST")
                print("MainCounterstop:", maincounterstop)
                if cekveriini:
                    curr_buffer.append(matrix[0][idcol])
                    curr_coords.append((0,idcol))
                    mused[0][idcol] = False
                    # choose from vertical 
                    i = 0
                    first = True
                    id_seq = len(curr_buffer)
                    countstop = 0
                    while i < rows:
                        if first:
                            print("Final point", final_points)
                            print("------------------Masuk ke vertical sec (FIRST)\n")
                            copy_mused = mused
                            
                            print("Curr coord: ",curr_coords)
                            print("Curr buffer ",curr_buffer)
                            print("TESSSS",matrix[i][idcol])
                            id_seq = len(curr_buffer)
                            print("Next tokennn: ",list_of_sequences[seq][id_seq])
                            print("Nilai i:",i)
                            print("Nilai idcol:",idcol)


                            # TESTING UNTUK CONT STLH KETEMU 1 SEQ
                            # if id_seq >= len(list_of_sequences[seq]):
                                # connect,overlap = can_connect(curr_buffer,list_of_sequences[seq])
                                # if connect:
                                #     for secseq in range (num_of_sequences):
                                #         if secseq!=seq and len(list_of_sequences[secseq]-overlap)<=(buffer_size-len(curr_buffer)):
                                #             while i < rows:
                                #                 copy_mused = mused
                                                
                                #                 print("Curr coord: ",curr_coords)
                                #                 print("----final pts:",final_points)
                                #                 print("Curr buffer ",curr_buffer)
                                #                 print("TESSSS",matrix[i][j])
                                #                 id_seq = len(curr_buffer)
                                #                 # print("Next token: ",list_of_sequences[seq][id_seq])
                                #                 print(mused[i][j])
                                #                 print("Nilai i:",i)
                                #                 print("Nilai j:",j)
                                #                 if check_next_horizontal(i,j,list_of_sequences[seq][id_seq],matrix,cols) and mused[i][j] != False and matrix[i][j] == list_of_sequences[seq][id_seq-1]:
                                #                     curr_buffer.append(matrix[i][j])
                                #                     curr_coords.append((i,j))
                                #                     mused[i][j] = False
                                #                     final_points, final_buffer = max_point(curr_buffer,list_of_sequences,points,final_points,final_buffer)
                                #                     print("Final points vertical",final_points)
                                #                     print(curr_buffer)
                                #                     print("")
                                #                     # choose from horizontal angle
                                #                     j = 0
                                #                     while j < cols:
                                #                         if len(curr_buffer) < buffer_size:
                                #                             print("masuk ke horizontal sec\n")
                                                            
                                #                             print("Nilai i: ", i)
                                #                             print("Nilai j: ", j)
                                #                             print("Curr buffer 2: ",curr_buffer)
                                #                             print("Curr coord 2: ",curr_coords)
                                #                             print("TESSSS",matrix[i][j])
                                #                             id_seq = len(curr_buffer)
                                #                             # print("Next token: ",list_of_sequences[seq][id_seq]) #ini token yang mau kita check di next
                                #                             print(mused[i][j])
                                #                             sec_copy_mused = mused
                                #                             # if id_seq >= len(list_of_sequences[seq]):
                                #                             #     break

                                #                             if check_next_vertical(i, j, list_of_sequences[seq][id_seq], matrix, rows) and mused[j][i] != False and matrix[i][j] == list_of_sequences[seq][id_seq-1]:
                                #                                 curr_buffer.append(matrix[i][j])
                                #                                 curr_coords.append((i,j))
                                #                                 mused[i][j] = False
                                #                                 final_points,final_buffer = max_point(curr_buffer, list_of_sequences, points, final_points,final_buffer)
                                #                                 print("Final points horizontal",final_points)
                                #                                 print("")
                                #                                 i = -1  # Reset i to 0 in the next iteration
                                #                                 first = False
                                #                                 break
                                #                             mused = sec_copy_mused
                                #                         else:
                                #                             break
                                #                         j += 1
                                #                     mused = copy_mused
                                #                 i += 1
                            # TESTING LIMIT 
                            cekhori = check_next_horizontal(i,idcol,list_of_sequences[seq][id_seq],matrix,cols)
                            if cekhori==False or matrix[i][idcol] != list_of_sequences[seq][id_seq-1]:
                                countstop+=1
                            if countstop==rows:
                                maincounterstop+=1
                                break

                            if cekhori and mused[i][idcol] != False and matrix[i][idcol] == list_of_sequences[seq][id_seq-1]:
                                curr_buffer.append(matrix[i][idcol])
                                curr_coords.append((i,idcol))
                                mused[i][idcol] = False
                                final_points, final_buffer = max_point(curr_buffer,list_of_sequences,points,final_points,final_buffer)
                                # choose from horizontal angle
                                j = 0
                                countstop=0
                                while j < cols:
                                    if len(curr_buffer) < buffer_size:
                                        print("Final point", final_points)
                                        print("---------------------masuk ke horizontal sec (FIRST)\n")
                                        
                                        print("Nilai i: ", i)
                                        print("Nilai j: ", j)
                                        print("Curr buffer 2: ",curr_buffer)
                                        print("Curr coord 2: ",curr_coords)
                                        print("TESSSS",matrix[i][j])
                                        id_seq = len(curr_buffer)
                                        # print("Next token: ",list_of_sequences[seq][id_seq]) #ini token yang mau kita check di next
                                        sec_copy_mused = mused
                                        # if id_seq >= len(list_of_sequences[seq]):
                                        #     break
                                        cekveri = check_next_vertical(i, j, list_of_sequences[seq][id_seq], matrix, rows)
                                        if cekveri==False or matrix[i][j] != list_of_sequences[seq][id_seq-1]:
                                            countstop+=1
                                        if countstop==cols:
                                            stop = True
                                            break
                                        if cekveri and mused[j][i] != False and matrix[i][j] == list_of_sequences[seq][id_seq-1]:
                                            curr_buffer.append(matrix[i][j])
                                            curr_coords.append((i,j))
                                            mused[i][j] = False
                                            final_points,final_buffer = max_point(curr_buffer, list_of_sequences, points, final_points,final_buffer)
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
                            
                            countstop=0
                            while i < rows:
                                print("CURR BUFFER:", curr_buffer)
                                print("Final point", final_points)
                                print("--------------------------Masuk ke vertical sec (NOT FIRST)\n")
                                copy_mused = mused
                                print("Curr coord: ",curr_coords)
                                print("Curr buffer ",curr_buffer)
                                print("TESSSS",matrix[i][j])
                                id_seq = len(curr_buffer)
                                # print("Next token: ",list_of_sequences[seq][id_seq])
                                print("Nilai i:",i)
                                print("Nilai j:",j)
                                # if id_seq >= len(list_of_sequences[seq]):
                                #     break
                                cekhori = check_next_horizontal(i,idcol,list_of_sequences[seq][id_seq],matrix,cols)
                                if cekhori==False or matrix[i][idcol] != list_of_sequences[seq][id_seq-1]:
                                    countstop+=1
                                if countstop==rows:
                                    maincounterstop+=1
                                    break

                                if cekhori and mused[i][j] != False and matrix[i][j] == list_of_sequences[seq][id_seq-1]:
                                    curr_buffer.append(matrix[i][j])
                                    curr_coords.append((i,j))
                                    
                                    mused[i][j] = False
                                    final_points, final_buffer = max_point(curr_buffer,list_of_sequences,points,final_points,final_buffer)
                                    # choose from horizontal angle
                                    j = 0
                                    countstop=0
                                    while j < cols:
                                        if len(curr_buffer) < buffer_size:
                                            print("Final point", final_points)
                                            print("-------------------------Masuk ke horizontal sec (NOT FIRST)\n")
                                            
                                            print("Nilai i: ", i)
                                            print("Nilai j: ", j)
                                            print("Curr buffer 2: ",curr_buffer)
                                            print("Curr coord 2: ",curr_coords)
                                            print("TESSSS",matrix[i][j])
                                            id_seq = len(curr_buffer)
                                            # print("Next token: ",list_of_sequences[seq][id_seq]) #ini token yang mau kita check di next
                                            sec_copy_mused = mused
                                            # if id_seq >= len(list_of_sequences[seq]):
                                            #     break
                                            cekveri = check_next_vertical(i, j, list_of_sequences[seq][id_seq], matrix, rows)
                                            if cekveri==False or matrix[i][j] != list_of_sequences[seq][id_seq-1]:
                                                countstop+=1
                                            if countstop==cols:
                                                stop = True
                                                break
                                            if cekveri and mused[j][i] != False and matrix[i][j] == list_of_sequences[seq][id_seq-1]:
                                                curr_buffer.append(matrix[i][j])
                                                curr_coords.append((i,j))
                                                mused[i][j] = False
                                                final_points,final_buffer = max_point(curr_buffer, list_of_sequences, points, final_points,final_buffer)
                                                i = -1  # Reset i to 0 in the next iteration
                                                first = False
                                                break
                                            mused = sec_copy_mused
                                        else:
                                            break
                                        j += 1
                                    mused = copy_mused
                                i += 1
                    
              
end_time = time.time()
elapsed_time = end_time - start_time


# Output on terminal
print("---------------- Results:\n")
print("Points obtained: " + str(final_points))
if final_points==0:
    print("It aint worth/no possible solution")
else:
    print(' '.join(final_buffer))
    print(final_coords)
print(str(elapsed_time) + " ms\n")
while(True):
    # prompt = input("Do you want to save the result? (y/n) => ")
    if (prompt == "y"):
        output_name = input("Output file name? (ex: output.txt) => ")
        with open(output_name, "w") as output:
            output.write(str(final_points) + "\n")
            output.write(str(' '.join(final_buffer)) + "\n") 
            # TESTING - Save coords not yet implemented
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


