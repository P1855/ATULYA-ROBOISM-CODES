x = list(input("list of numbers without any commas or spaces: "))
y = input("asc, desc, none: ")
result = [list(x) for x in list(x)]
if y == "asc":
    result.sort()
    print(list(result))
if y == "desc":
    result.sort(reverse=True)
    print(list(result))
if y == "none":
   print(list(result))
