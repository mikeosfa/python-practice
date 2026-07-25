

def number_check (starting_number):
    if not starting_number.isdigit():
        print("Numbers only please, e.g. 1234")
        return False
    if int(starting_number) < 1000:
        print("Needs to be a 4 digit number, e.g. 1234")
        return False
    if len(set(starting_number)) == 1:
        print ("No repeating numbers, please make sure there are at least 2 different numbers")
        return False
    return True

def convert_to_number (list_input):
    temp_number = ""
    for x in list_input:
        temp_number = temp_number + x
    return int(temp_number)

def kaprekar_step(current_number):
    number_array = list(str(current_number))
    high_list = sorted(number_array,reverse=True)
    low_list = sorted(number_array,reverse=False)
    high_number = convert_to_number(high_list)
    low_number = convert_to_number(low_list)
    new_total = high_number-low_number
    print(f"{high_number:04d} - {low_number:04d} = {new_total:04d}")
    return f"{new_total:04d}"               
starting_number = input ("Please enter a 4 digit number: ")

while not number_check(starting_number):
    starting_number = input ("Please enter a 4 digit number: ")

current_number = starting_number
step_counter=0

while current_number !="6174":
    current_number = kaprekar_step(current_number)
    step_counter = step_counter + 1

print (f"Total steps = {step_counter}")