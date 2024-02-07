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
arr1 = ["AD"]
arr2 = ["AD", "FF", "SS", "AA"]
result = can_connect(arr1, arr2)
print(result)  # Output: True