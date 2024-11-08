# Problem 1
score = 0
excellent = 0
good = 0
pass_count=0
fail = 0

while score >= 0:
    score = int(input("please enter a score:")) # user enters a score
    if score >=90: # if score is greater than or equal to 90
        print("Excellent") # print excellent if so
        excellent = excellent + 1
    elif 70<= score <=79: # if score is greater than or equal to 79 and 70
        print("good") # print good if so
        good = good + 1
    elif 50<= score <=69: # if score is greater than or equal to 50 and 69
        print("pass") # if so print pass
        pass_count = pass_count + 1
    elif 0 <= score < 50: # if score is greater than or equal to 0 and 50
        print("fail") # if so print fail
        fail = fail + 1
    else:
        print("error cannot be a negative number!") # incase the user inputs a negative number
        break
# print when user inputs a score
print(f"The amount of excellent scores are {excellent}")
print(f"The amount of good scores are {good}")
print(f"The amount of pass scores are {pass_count}")
print(f"The amount of Fail scores are {fail}")



# Problem 2

start = input("Enter a number 1-30")
for item in range (1, 31):
    if item %2==0 and item >= 10:
# #this is checking each num to see if its even or odd
        print("Special even")
    else: print("Special Odd")
#this will print whether its even or odd