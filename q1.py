from numbers import Real

def swap(x, y):
    if not (isinstance(x, Real) and isinstance(y, Real)) or isinstance(x, bool) or isinstance(y, bool):
        return -1

    x, y = y, x

    print("After swap: x =", x, ", y =", y)

if __name__ == "__main__":
	# 1) Non-numeric case
    result1 = swap("Apple", 10)
    print(result1)
    
    # 2) Numeric case
    swap(9, 17) 