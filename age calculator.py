## lets see if i can get this test program to run

userAge = int(input(print("enter your age")))
currYear = int(input(print("what year is it?")))
userAge2 = 0
while userAge2 < 100:
	userAge2 = userAge + 10
	print("if you are ", userAge)
	print(" in ", currYear)
	print(" you will be ", userAge2)
	print(" in ", currYear + 10)
	print()

	currYear = currYear + 10
	userAge = userAge + 10

input(print("Press enter to exit"))