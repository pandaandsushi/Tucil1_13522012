# from collections import Counter

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