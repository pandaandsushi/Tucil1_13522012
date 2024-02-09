# from collections import Counter
def count_points(buffer,arr_of_seq,arr_of_points):
    res = 0
    for i in range (len(arr_of_seq)):
        for j in range (len(buffer)):
            if (buffer[j]==arr_of_seq[i][0]):
                count = 1
                print("tes")
                if len(buffer)>=len(arr_of_seq[i]):
                    for k in range(len(arr_of_seq[i])-1):
                        if (buffer[k+j] == arr_of_seq[i][k]):
                            count += 1
                    print("Count",count)
                    if count == len(arr_of_seq[i]):
                        res = arr_of_points[i] + res
                        break
                else:
                    return 0
    return res
def max_point(curr_buffer,list_of_sequences,points,final_points,final_buffer):
    curr_points = count_points(curr_buffer,list_of_sequences,points) 
    if final_points == None:
        final_points = curr_points
        final_buffer = curr_buffer
    elif final_points < curr_points:
        final_points = curr_points
        final_buffer = curr_buffer
    return final_points,final_buffer

curr_buffer = ["BD", "E9", "55","7A"]
list_of_sequences = ["BD", "E9", "55","7A"]
points = [15]
final_points=0
final_buffer=[]
final_points, final_buffer = max_point(curr_buffer,list_of_sequences,points,final_points,final_buffer)
print(final_points)
# def calc_intersect(nums1, nums2):
#     num_to_count_1 = Counter(nums1)
#     intersect = []
#     for num in nums2:
#         if num_to_count_1[num] > 0:
#             intersect.append(num)
#             num_to_count_1[num] -= 1
#     return intersect

# buffer = ["X","A","B","C","D","A"]
# seqs = ["X","A","C"]
# print(calc_intersect(buffer,seqs))

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