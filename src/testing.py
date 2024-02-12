def sublist(main_list, sublist):
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False
def check_seq(curr_buffer,list_of_sequences):
    count=0
    for i in range (len(list_of_sequences)):
        if sublist(curr_buffer,list_of_sequences[i]):
            count+=1
    if count==len(list_of_sequences):
        return True
    return False 
# Example usage:
a = [1, 2, 3, 4, 5]
b1 = [2, 3]
b2 = [2, 3, 4]
b3 = [1, 2, 3, 4, 5]
curr_buffer = ["7A","BD","SS"]
list_of_sequences = ["7A","BD"]
print(sublist(a, b1))  # True
print(sublist(a, b2))  # True
print(sublist(a, b3))  # False
print(sublist(curr_buffer,list_of_sequences))


def count_points(buffer,arr_of_seq,arr_of_points):
    res = 0
    for i in range (len(arr_of_seq)):
        if sublist(buffer,arr_of_seq[i]):
            res+=arr_of_points[i]
    return res

# def count_points(buffer,arr_of_seq,arr_of_points):
#     res = 0
#     for i in range (len(arr_of_seq)):
#         remaindertocheck = len(buffer)
#         for j in range (len(buffer)):
#             remaindertocheck-=1
#             print(buffer[j])
#             print(arr_of_seq[i][0])
#             print("tes")
#             if (buffer[j]==arr_of_seq[i][0]):
#                 count = 0
#                 if len(buffer)>=len(arr_of_seq[i]):
#                     for k in range(len(arr_of_seq[i])):
#                         if remaindertocheck+1<len(arr_of_seq[i]):
#                             break
#                         if (buffer[k+j] == arr_of_seq[i][k]):
#                             count += 1
#                     print(count)
#                     if count == len(arr_of_seq[i]):
#                         res = arr_of_points[i] + res
#                         break
#                 else:
#                     return 0
#     return res
def max_point(curr_buffer,list_of_sequences,points,final_points,final_buffer):
    curr_points = count_points(curr_buffer,list_of_sequences,points) 
    if final_points == None:
        final_points = curr_points
        final_buffer = curr_buffer
    elif final_points < curr_points:
        final_points = curr_points
        final_buffer = curr_buffer
    return final_points,final_buffer

curr_buffer = ["7A","BD","SS"]
list_of_sequences = [["7A","BD"]]
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