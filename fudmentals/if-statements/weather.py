# if, else if and else statements 
    # different from JS sytnax and elif(else if in JS )
temp = 95 

if temp > 80:
    print("It's to hot ")
    print("Stay inside!")
    # white space is improtant will get a indetational error 
elif temp < 60:
    print("its to cold")
    print ("Stay inside")
else:
    print("Enjoy the outdoors!")

print("Have a nice Day")
    # will run after the if statement even if false 

# logical Operator Or 
temperature = 75 
if temperature > 80 or temperature < 60:
    # one the comparisons must be ture to run the if statement 
    print("Stay inside!")
else:
    print("enjoy the outdoors!")

# logical Operator And 
forcast = "rain"

if temperature <80 and forcast != "rain":
      # both of the comparisons must be ture to run the if statement 
    print("Go Outside!")
else:
    print("Stay inside!")

# logical Operator Not 
if not forcast == "rain":
    # makes the statment more readable
    print("Go Outside!")
else:
    print("Stay inside!") 

# Boolean 

raining= True 
if raining:
    print("Stay inside!")