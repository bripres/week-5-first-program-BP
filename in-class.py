# Example 1: Create a variable
name="Briana"

# Example 2: Create another variable with a number
num=36

# Example 3: Print text on the screen 
print("Hello there, I'm printing text")

# Example 3: Print what the varibale "name" has inside 
print(name)

#Example 5: Print a sentence using a variable "name"
print("My name is", name)

#Example 6: Change the value of the variable and print it again
name="Bri"
print("My nickname is", name)

# Example 7: Ask user what their favorite anime is
print("What is your favorite animal?")
animal=input()
print("I didn't know that", animal, "was your favorite animal!")

#Example 8: Use the variable created in example 2
#If the variable is greater than 10 to print a message
#Otherwise, print another message
if num>10:
    print("Congrats. your number is greater than 10!")
else:
    print("Sorry your number is not greater than 10")