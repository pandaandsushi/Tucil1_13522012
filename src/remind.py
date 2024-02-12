# Buffer continues
# buat cp per sequence
# 2
# 7A BD 1C 7A E9 1C
# 20
# BD E9 1C E9 1C
# 30
def can_connect(curr_buffer, seqarr):
    if len(curr_buffer)==1 and seqarr[0]!=curr_buffer[0]:
        return False,0
    overlap_lens = (i + 1 for i, e in enumerate(seqarr) if e == curr_buffer[-1])
    for overlap_len in overlap_lens:
        print(overlap_len)
        for i in range(overlap_len):
            if curr_buffer[-overlap_len + i] != seqarr[i]:
                break
        else:
            return True,overlap_len
    return False,0

# Example usage:
arr1=["7A"]
arr2 = ["7SA","1C","5X","BD","7A","1C","55"]
# arr2 = ["SS","S"]
# arr1 = ["SS","S","SS"]
result,x = can_connect(arr1, arr2)
print(result)  # Output: True
print(x)


def count_points(buffer,arr_of_seq,arr_of_points):
    res = 0
    for i in range (len(arr_of_seq)):
        remaindertocheck = len(buffer)
        print("tes")
        for j in range (len(buffer)):
            remaindertocheck-=1
            print(buffer[j])
            print(arr_of_seq[i][0])
            if (buffer[j]==arr_of_seq[i][0]):
                count = 0
                if len(buffer)>=len(arr_of_seq[i]):
                    print("--Nilai remainder:",remaindertocheck)
                    for k in range(len(arr_of_seq[i])):
                        if remaindertocheck+1<len(arr_of_seq[i]):
                            break
                        print("Buff to check ",buffer[k+j])
                        if (buffer[k+j] == arr_of_seq[i][k]):
                            count += 1
                    if count == len(arr_of_seq[i]):
                        print("POINTT COUNT",count)
                        res = arr_of_points[i] + res
                        print("RES",res)
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
buffer = ['50', 'BD', 'E9', '1C', 'E9', '7A']
seqs = [['BD', 'E9', '1C', 'E9', '7A'], ['7A', 'BD', '1C', '7A', 'E9', 'E9']]
# buffer = ["50", "BD", "E9","1C"]
# seqs = [["BD","E9","1C"],["50","BD"],["B","C","D"],["X","A","A"]]
# buffer = ["X","A","B","C","D","A"]
# seqs = [["A","B","C"],["B","C","D"],["X","A","A"]]
point = [10,80,3]
# cc = count_points(buffer,seqs,point)
# print(cc)

# 7A BD 1C 7A E9 1C
# 20
# BD E9 1C E9 7A
# 15