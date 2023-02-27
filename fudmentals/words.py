largest = None
smallest = None


while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fNum = int(num)
        if largest is None or fNum > largest:
             largest = fNum
        if smallest is None or fNum < smallest:
            smallest = fNum

      """   print(fNum)
        print("Maximum is ", largest)
        print("Minimum is ", smallest) """
    except: 
        print("Invalid input")

print(fNum)       
print("Maximum is ", largest)
print("Minimum is ", smallest)