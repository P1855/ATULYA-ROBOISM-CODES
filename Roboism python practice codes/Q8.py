def sum_of_digits_in_string(sumation):
    sum_digit = 0
    for x in sumation:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit

  
print(sum_of_digits_in_string(input("Enter the elements of the string:")))

