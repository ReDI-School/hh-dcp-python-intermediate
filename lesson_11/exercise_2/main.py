def increase(my_list: str) -> str:
    if len(my_list) == 0:
        return ""

    # Split the string into a list of numbers
    number_list = my_list.split(',')

    # Increase each number by 2
    new_number_list = [str(int(num) + 2) for num in number_list]

    # Join the list back into a comma-separated string
    new_numbers = ','.join(new_number_list)
    return new_numbers


