# 1. Ask a person's age
# 2. Record response
age = float(input("How old is the person?\n>"))

# 3. Test to see if the person is an infant (age <= 1)
if age <= 1:
	# 3a1. If true, communicate "infant"
	print("The person is an infant")
	# 3a2. goto step 7
# 4. Test to see if the person is a child (afe greater than 1 but less than 13)
elif (age > 1 and age < 13):
	# 4a1. If true, communicate "child"
	print("The person is a child")
	# 4a2. goto step 7
	
# 5. Test to see if the person is a teenager (age greater or equal to 13 but less than 20)
elif (age >= 13 and age < 20):
	# 5a1. If true communicate "teenager"
	print("The person is a teenager")
	# 5a2. goto step 7
# 6. Because none of steps 3,4,5 are true, commmunicate "adult"
else :
	print("The person is an adult")
# 7. Terminate