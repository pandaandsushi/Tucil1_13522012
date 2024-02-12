list1 = [1,2,3]
list2 = [4,5]
print(list1+list2)
list_seq = [[2,3,4],[1,2,],[4,6,3]]
num_seq = 3
for i in range (num_seq):
    print(i)
    lst = list_seq[0]+list_seq[i]
    if i!=0:
        list_seq.append(lst)
        num_seq+=1
print(num_seq)