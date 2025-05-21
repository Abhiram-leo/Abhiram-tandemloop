def generate_odd_series(a: int) -> str:
    if a < 1:
        return "Input must be a positive integer"
    
    result = []
    current = 1
    for _ in range(a):
        result.append(str(current))
        current += 2
    return ", ".join(result)
    if not a.isdigit():
      print("output:1,3,5,7,.......")  
a= int(input("enter a positive number"))
print(generate_odd_series(a))
