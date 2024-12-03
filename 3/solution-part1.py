def check_mul():
    score = 0
    with open('input.txt') as file:
        for line in file:
            for i in range(0, len(line)):
                is_valid_mul_expression, first, sec = check_valid_mul_expression(line, i)
                if is_valid_mul_expression:
                    score += int(first) * int(sec)
    return score


def check_valid_mul_expression(line: str, i: int) -> tuple:
    first, sec = 0, 0
    if check_starts_with_mul(line, i):
        is_valid_first_number, first_number = check_is_valid_number(line, i + 4)
        
        if is_valid_first_number:          
            first_digits_count = len(first_number)
            is_valid_sec_number, sec_number = check_is_valid_number(line, i + first_digits_count + 5)
           
            if is_valid_sec_number:
                sec_digits_count = len(sec_number)
                return check_ends_with_parenthesis(line, i + first_digits_count + sec_digits_count + 5), first_number, sec_number
    return False, first, sec


def check_ends_with_parenthesis(line: str, i: int) -> bool:
    return line[i] == ')'


def check_starts_with_mul(line: str, i: int) -> bool:
    return line[i:i+4] == 'mul('


def check_is_valid_number(line: str, i: int) -> tuple:
    number_str = ''
    nr_digits = 0
    for j in range(i, len(line)):

        if line[j].isdigit():
            if nr_digits == 3:
                return False, ''
            number_str += line[j]
            nr_digits += 1
            continue

        elif line[j] == ',' or line[j] == ')':
            if nr_digits > 0 and nr_digits <= 3:
                return True, number_str
            else:
                return False, ''
            
        else:
            return False, ''     
    return False, ''

print(check_mul())