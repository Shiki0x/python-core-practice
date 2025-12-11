name = input("What is your name? ")
age = input("How old are you? ")

print("\nNice to meet you, " + name + "!")
print("You are " + age + " years old.")

try:
    age_num = int(age)
    print("Next year, you will be", age_num + 1)
except ValueError:
    print("I couldn't understand your age, but it's all good.")