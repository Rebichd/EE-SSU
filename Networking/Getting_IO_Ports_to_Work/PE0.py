#!/usr/bin/python
#Takes a positive number from the user and outputs the sum of the numbers from 1 to
#the number entered by user. If the sum from 1 to the number enter by user is Odd
#it prints the the sum is Odd. Same if performed for Even sum

promptText = "Enter a number: ";
userNum = int(input(promptText));

print("Number entered: " + str(userNum));

answerNum = 0;
origNum = userNum;

while userNum > 0:
	answerNum += userNum;
	userNum -= 1;

print("The sum of the numbers from 1-" + str(origNum) + " is: " + str(answerNum));

if (answerNum % 2) == 0:
	print("The sum " + str(answerNum) + " is an Even number");
else:
	print("The sum " + str(answerNum) + " is an Odd number");
