def string_reverse(s):
    if not isinstance(s, str):
        return None 

    return s[::-1]

if __name__ == "__main__":
    #1
    scenario1 = string_reverse("Hello World")
    print(scenario1)  

    #2
    scenario2 = string_reverse("Python")
    print(scenario2) 