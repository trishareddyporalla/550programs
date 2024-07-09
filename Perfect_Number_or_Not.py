def is_perfect_number(number):
    if number <= 0:
        return False  # Negative numbers and zero are not perfect numbers
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number

def main():
    try:
        num = int(input("Enter a number to check if it's perfect: "))
        if is_perfect_number(num):
            print(num, "is a perfect number.")
        else:
            print(num, "is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
