from numbers import Real

def check_divisibility(num, divisor):
    # Ensure both inputs are numeric
    if not isinstance(num, Real) or not isinstance(divisor, Real) or isinstance(num, bool) or isinstance(divisor, bool):
        return False 

    if divisor == 0:
        return False  # division by zero not allowed

    return num % divisor == 0 # num % divisor == 0 checks remainder = 0, which means divisible

if __name__ == "__main__":
    # Scenario 1
    result1 = check_divisibility(10, 2)
    print(result1) #10 can be divided by 2, result is True 

    # Scenario 2
    result2 = check_divisibility(7, 3)
    print(result2) # 7 cannot be divided by 3, result is false 