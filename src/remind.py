def can_connect(curr_buffer,seqarr):
    for i in range (len(curr_buffer)):
        if (curr_buffer[i] == seqarr[0]):
            count=0
            for j in range (len(seqarr)-1):
                if(curr_buffer[j+i] == seqarr[j]):
                    print("succeed\n")
                    print(f"{curr_buffer[j+i]}\n")
                    print(f"{seqarr[j]}\n")
                    count+=1
                print("Count",count)
                if len(curr_buffer)-count==0:
                    return True
    return False

# Example usage:
# arr1 = ["AD"]
# arr2 = ["AD", "FF", "SS", "AA"]
# result = can_connect(arr1, arr2)
# print(result)  # Output: True

def count_points(buffer,arr_of_seq,arr_of_points):
    res = 0
    for i in range (len(arr_of_seq)):
        for j in range (len(buffer)):
            if (buffer[j]==arr_of_seq[i][0]):
                count = 1
                if len(buffer)>=len(arr_of_seq[i]):
                    print("--Nilai j:",j)
                    for k in range(len(arr_of_seq[i])-1):
                        print("XX")
                        print(k+j+1)
                        if (buffer[k+j] == arr_of_seq[i][k]):
                            count += 1
                    if count == len(arr_of_seq[i]):
                        print(arr_of_points[i])
                        res = arr_of_points[i] + res
                        break
                else:
                    return 0
    return res
# def count_points(buffer,arr_of_seq,arr_of_points):
#     res = 0
#     for i in range (len(arr_of_seq)):
#         for j in range (len(buffer)):
#             print(buffer[j])
#             print(arr_of_seq[i][0])
#             print("....")
#             if (buffer[j]==arr_of_seq[i][0]):
#                 count = 1
#                 print("in")
#                 for k in range(len(arr_of_seq[i])-1):
#                     print(buffer[k+j+1])
#                     print(arr_of_seq[i][k+1])
#                     print("out")
#                     if (buffer[k+j+1] == arr_of_seq[i][k+1]):
#                         count += 1
#                 print("Count" + str(count))
#                 if count == len(arr_of_seq[i]):
#                     res += arr_of_points[i]
#                     break
#     return res
buffer = ["50", "BD", "E9","1C"]
seqs = [["BD","E9","1C"],["B","C","D"],["X","A","A"]]
# buffer = ["X","A","B","C","D","A"]
# seqs = [["A","B","C"],["B","C","D"],["X","A","A"]]
point = [10,80,3]
cc = count_points(buffer,seqs,point)
print(cc)