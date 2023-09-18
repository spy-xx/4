def roman2decimal(roman_str):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    prev_value = 0
    
    for numeral in reversed(roman_str):
        current_value = roman_dict[numeral]
        
        if current_value < prev_value:
            value -= current_value
        else:
            value += current_value
        
        prev_value = current_value
    
    return value

roman_str = input("Enter a Roman Numeral: ")
print(roman2decimal(roman_str))
