line01 = "************************"
line02 = "*WELCOME TO ABIB QUIZ BR*"
line03 = "************************"

print(line01)
print(line02)
print(line03)
score = 0
print("")
print("In todays quiz there will be questions")
print("The questions are geography, science and literature")
response1 = input("Are you ready? ")

question1 = input("Which planet in our solar system spins the fastest? ")
if question1 == "Jupiter":
    print("You are correct! ")
    score += 1
else:
    print("You are wrong! ")
question2 = input("What is the capital city of Peru? ")
if question2 == "Lima":
    print("You are correct! ")
    score += 1
else:
    print("You are wrong! ")
question3 = input("Who wrote the play Romeo and Juliet? ")
if question3 == "William Shakespeare":
    print("You are correct! ")
    score += 1
else:
    print("You are wrong! ")
print("")
if score == 3:
    print("You got 3/3, Perfect Score! ")
elif score == 2:
    print("You got 2/3, Great job! ")
elif score == 1:
    print("You got 1/3, You tried! ")
print("")
line04 = "************************"
line05 = "*THANKS FOR PLAYINGG BR*"
line06 = "************************"

print(line04)
print(line05)
print(line06)