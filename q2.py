def find_and_replace(lst, find_val, replace_val):
    if not isinstance(lst, list):
        return None
        
    lst = [replace_val if item == find_val else item for item in lst]
    return lst
        
if __name__ == "__main__":
    # scenario1
    result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
    print(result1)  
    
    # scenario 2
    result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
    print(result2)