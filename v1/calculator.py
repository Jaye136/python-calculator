# Perform up to 5 numerical operations on the starting value
dsf = 0
err = "f"
print("Enter your starting value.")
ssf = int(input())

for dsf in range(5):
 print("Enter the operation being used, or 'finish' to see the result.")
 print("Value so far: " + str(ssf))
 print("Number of operations used so far: " + str(dsf))
 opp = str(input())

 if opp == "+":
  print("What value are you adding?")
  num = input()
  if num.isdigit():
   ssf = ssf + int(num)
   dsf = dsf + 1
  else:
   err = "t"
   break

 elif opp == "-":
  print("What value are you subtracting?")
  num = input()
  if num.isdigit():
   ssf = ssf - int(num)
   dsf = dsf + 1
  else:
   err = "t"
   break

 elif opp == "*":
  print("What value are you multiplying?")
  num = input()
  if num.isdigit():
   ssf = ssf * int(num)
   dsf = dsf + 1
  else:
   err = "t"
   break

 elif opp == "/":
  print("What value are you dividing?")
  num = input()
  if num.isdigit():
   ssf = ssf / int(num)
   dsf = dsf + 1
  else:
   err = "t"
   break

 elif opp == "finish":
  break

 else:
  err = "t"
  break

if err == "t":
  print("This is an invalid operation.")
  print("Please restart the program.")

if (dsf == 5 or opp == "finish"):
  print("Your resulting value is " + str(ssf) + ". You performed " + str(dsf) + " operations.")
