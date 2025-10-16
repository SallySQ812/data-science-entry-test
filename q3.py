def update_dictionary(dct, key, value):
    if not isinstance(dct, dict):
        return None

    if key in dct:
        print(f"Original value for '{key}':", dct[key])

    dct[key] = value
    return dct
    
if __name__ == "__main__":
    # 1) 
    scenario1 = update_dictionary({}, "name", "Alice")
    print(scenario1)  

    # 2) 
    scenario2 = update_dictionary({"age": 25}, "age", 26)
    print(scenario2)  