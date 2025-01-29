import math

def convert_continuous_string_to_numbers(input_string, key_value):
    """
    Converts a continuous string into merged numerical values based on A-Z mapping (0-25).
    Adds a key value to each part of the converted string.

    Args:
        input_string (str): The continuous input string.
        key_value (int): The key value to be added.

    Returns:
        list: A list of merged numerical values corresponding to the segments in the input string.
    """
    # Create a dictionary to map letters to their numerical values (A=0, B=1, ..., Z=25)
    letter_values = {chr(ord('A') + i): i for i in range(26)}

    # Split the input string into two-letter segments
    segments = [input_string[i:i + 2] for i in range(0, len(input_string), 2)]

    # Convert each segment to its numerical value and store them separately
    merged_values = []
    for segment in segments:
        if len(segment) == 2:
            value1 = letter_values.get(segment[0].upper(), None)
            value1 = value1 + key_value
            value2 = letter_values.get(segment[1].upper(), None)
            value2 = value2 + key_value
            if value1 is not None and value2 is not None:
                # Add a leading zero to the numerical value if it's less than 10
                value1_str = str(value1).zfill(2)
                value2_str = str(value2).zfill(2)
                # Add the key value to each part of the converted string
                merged_values.append(f"{(value1_str)}{value2_str}")
        else:
            print(f"Skipping invalid segment: {segment}")

    return merged_values

def convert_numbers_to_characters(input_string):
    """
    Converts a string of numbers into characters where each character is mapped to a letter from 'a' to 'z'.

    Args:
        input_string (str): The input string of numbers.

    Returns:
        str: The resulting string of characters.
    """
    # Create a dictionary to map numbers to characters (00-25 => a-z)
    number_to_char = {str(i).zfill(2): chr(i + 97) for i in range(26)}

    # Split the input string into two-digit segments
    segments = [input_string[i:i + 2] for i in range(0, len(input_string), 2)]

    # Convert each segment to its corresponding character
    characters = [number_to_char.get(segment, '?') for segment in segments]

    # Join the characters to form the resulting string
    result_string = ''.join(characters)

    return result_string


def degrees_to_tan(degrees):
    """
    Converts an angle from degrees to its tangent value.

    Args:
        degrees (float): Angle in degrees.

    Returns:
        float: Tangent value of the angle.
    """
    radians = math.radians(degrees)  # Convert degrees to radians
    return math.tan(radians)

# # Example usage:
# degree_angle = 45  # Example angle in degrees
# tan_value = degrees_to_tan(degree_angle)
# print(f"Tangent of {degree_angle} degrees is approximately {tan_value:.4f}.")


def radians_to_degrees(radians):
    """
    Converts an angle from radians to degrees.
    
    Args:
        radians (float): Angle in radians.
    
    Returns:
        float: Angle in degrees.
    """
    return radians * (180 / 3.141592653589793)  # Using pi as an approximation

def convert_to_float(arr):
    return [float('0.' + str(i)) for i in arr]

# def get_binary(floats):
#     """
#     Checks the decimal length of each float and assigns a binary value based on it.

#     Args:
#         floats (list): The list of floats.

#     Returns:
#         str: The binary number.
#     """
#     binary = ""
#     for f in floats:
#         # Get the decimal part of the float
#         decimal_part = str(f).split('.')[1]
#         # Assign a binary value based on the decimal length
#         binary += '0' if len(decimal_part) == 3 else '1'
#     return binary



def calculate_arctan(tan_values):
    """
    Calculate the arctangent (tan inverse) for each element in the given array of tangent values.

    Args:
        tan_values (list): List of tangent values.

    Returns:
        list: List of arctangent values.
    """
    arctan_values = [round(math.atan(value), 4) for value in tan_values]
    return arctan_values


def convert_to_numbers(arr):
    return [str(i)[2:] for i in arr] 

def convert_numbers_to_string(numbers, key_value):
    """
    Converts a list of numerical values back into a continuous string based on A-Z mapping (0-25).
    Subtracts a key value from each part of the number.

    Args:
        numbers (list): The list of numerical values.
        key_value (int): The key value to be subtracted.

    Returns:
        str: The continuous string.
    """
    # Create a dictionary to map numerical values to their letters (0=A, 1=B, ..., 25=Z)
    number_values = {i: chr(ord('A') + i) for i in range(26)}

    # Convert each number to its string value and concatenate them
    input_string = ""
    for number in numbers:
        number_str = str(number)
        # Check if the number has an odd length
        if len(number_str) % 2 != 0:
            # Take the first digit, subtract the key value, and convert it to its letter value
            part = int(number_str[0]) - key_value
            letter = number_values.get(part, None)
            if letter is not None:
                input_string += letter
            # Split the rest of the number into two parts
            rest_str = number_str[1:]
            for i in range(0, len(rest_str), 2):
                part_str = rest_str[i:i+2]
                part = int(part_str) - key_value
                letter = number_values.get(part, None)
                if letter is not None:
                    input_string += letter
        # Check if the number has an even length
        elif len(number_str) % 2 == 0:
            # Take the first two digits and last two digits, subtract the key value, and convert them to their letter values
            part1 = int(number_str[:2]) - key_value
            letter1 = number_values.get(part1, None)
            if letter1 is not None:
                input_string += letter1
            part2 = int(number_str[-2:]) - key_value
            letter2 = number_values.get(part2, None)
            if letter2 is not None:
                input_string += letter2

    return input_string



# # Example usage:
# radian_angle = 0.7853981633974483  # π/4 radians
# degree_angle = radians_to_degrees(radian_angle)
# print(f"{radian_angle:.4f} radians is approximately {degree_angle:.2f} degrees.")
# # Example usage:
# continuous_str = "DEVESH"
# results = convert_continuous_string_to_numbers(continuous_str)
# print(f"Continuous string: {continuous_str}")
# print(f"Merged numerical values: {results}")
def convert_tan_values(tan_values):
    results = []
    remainders = []
    quotients_set = []

    for val in tan_values:
        # Remove decimal and convert to integer
        integer_value = int(val * 10000)

        # Pair 2 digits from the back
        pair = divmod(integer_value, 100)

        # Divide each pair by 25 and store quotient and remainder
        quotient, remainder = divmod(pair[0], 23)
        results.append(str(quotient))
        remainders.append(f"{remainder:02d}")  # Pad remainder to 2 digits
        quotients_set.append([quotient])

        quotient, remainder = divmod(pair[1], 23)
        results.append(str(quotient))
        remainders.append(f"{remainder:02d}")  # Pad remainder to 2 digits
        quotients_set[-1].append(quotient)

    # Concatenate the results and remainders
    concatenated_result = ''.join(results)
    concatenated_remainders = ''.join(remainders)

    return concatenated_result, concatenated_remainders, quotients_set

def convert_quotient_pairs_to_tan_values(quotient_pairs, ciphertext_numbers):
    """
    Converts quotient pairs and ciphertext numbers into tangent values.

    Args:
        quotient_pairs (list): List of pairs of quotient values.
        ciphertext_numbers (list): List of ciphertext numbers.

    Returns:
        list: List of tangent values.
    """
    tan_values = []
    degree_values = []
    for pair, number in zip(quotient_pairs, ciphertext_numbers):
        if len(pair) != 2:
            print("Invalid pair:", pair)
            continue

        # Extract values from the pair
        quotient1, quotient2 = pair
        
        # Multiply the first quotient by 25 and add it to the first two digits of the first number
        number1 = int(str(number)[:2]) + quotient1 * 25
        # print(number1)
        # Multiply the second quotient by 25 and add it to the last two digits of the second number
        number2 = int(str(number)[2:]) + quotient2 * 25
        # print(number2)
        # Concatenate the modified numbers
        concatenated_result = str(number1).zfill(2) + str(number2).zfill(2)

        # print(concatenated_result)
        
        # Convert the concatenated number to radians (dividing by 10000 as we multiplied by it during encryption)
        
        degree = int(concatenated_result) / 10000.0
        # print(radians)
        # # Calculate tangent value and round off to 4 decimal places
        tan_value = round(degree, 4)
        tan_values.append(tan_value)

    return tan_values



def process_float(num):
    # Convert the float to string
    str_num = str(num)
    
    # Remove leading zeros
    str_num = str_num.lstrip('0')
    
    # Remove the dot from the string
    str_num = str_num.replace('.', '')
    
    int_num = int(str_num)
    
    # If the number is not 4 digits, multiply it by 10
    if len(str(str_num)) != 4:
        int_num *= 10
    
    return int_num

def process_array(array):
    # Process each float number in the array
    processed_array = [process_float(num) for num in array]
    
    # Return the processed array
    return processed_array





# Take string input from the user
print(f"\n\n----Encryption----")
input_string = input("Enter a string: ")

# Replace spaces with 'x'
input_string = input_string.replace(' ', 'x')

# Check if the length of the input string is even
if len(input_string) % 2 != 0:
    # If it's not, append an "x" to the end of the string
    input_string += "x"

def convert_decimal_to_int(decimal_value):
    # Remove the leading dot (if any)
    decimal_value = decimal_value.lstrip('.')
    
    # Convert to an integer with 4 decimal places
    int_value = int(float(decimal_value) * 10000)
    
    return int_value



key = input("Enter a key value: ")
# Convert the string into numbers
numbers = convert_continuous_string_to_numbers(input_string, int(key))

print(f"Converted string: {numbers}")

# Convert the numbers into floats
floats = convert_to_float(numbers)

print(f"Converted numbers: {floats}")

# Convert the floats (considered as radians) into degrees
degrees = [radians_to_degrees(radian) for radian in floats]

# Get the tangent values of the degrees
tan_values = [round(degrees_to_tan(degree), 4) for degree in degrees]

print(f"Tan values: {tan_values}")

result, remainders, quotients_set = convert_tan_values(tan_values)
#print(f"Concatenated result: {result}")
print(f"Encrypted value after key2: {remainders}")
print("Key2 values  for each pair:")
for i, quotients in enumerate(quotients_set, 1):
    print(f"Pair {i}: {quotients}")

ciphertext = convert_numbers_to_characters(remainders)
print("CipherText:", ciphertext)
print(f"\n----Decryption----")
key_dec = input("Input the key value to decrypt:- ")

xy= convert_continuous_string_to_numbers(ciphertext, 0)
print(f"Converted ciphertext: {xy}")
tan_values1 = convert_quotient_pairs_to_tan_values(quotients_set, xy)
print("Tangent values:", tan_values1)

arctan_values = calculate_arctan(tan_values)
print("Arctangent values:", arctan_values)

plain_t = process_array(arctan_values)

print(plain_t)

plaint_text = convert_numbers_to_string(plain_t,int(key_dec))
if(len(plaint_text)%2!=0):
    plaint_text  = plaint_text - plaint_text[-1]
print(plaint_text)