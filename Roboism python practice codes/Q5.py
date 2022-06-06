#taking input of any array    

input_string = input ("Enter the elements of array with spaces between them :")
arr = input_string.split();
len(arr) == 100
range(len(arr)) == (0,99)
print("Duplicate elements in given array: ");    
#Searches for duplicate element    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);   
