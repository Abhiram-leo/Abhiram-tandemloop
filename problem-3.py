print("Welcome to the Odd Number Generator!")
print("I'll show you odd numbers up to your number")

while True:
    try:
        a = int(input("Please enter a positive whole number: "))
        if a < 1:
            print("That's not positive. Try again!")
            continue
        break
    except:
        print("That's not valid. Try again!")

if a % 2 == 1:
    stop_at = a
else:
    stop_at = a - 1

numbers = []
num = 1

while num <= stop_at:
    numbers.append(str(num))
    num += 2

if len(numbers) == 0:
    print("No odd numbers!")
else:
    print("Odd numbers:")
    print(", ".join(numbers))

print("\nThanks for using the program!")
