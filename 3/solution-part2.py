def check_mul():
    score = 0
    is_mul_active = True
    with open('input-part2.txt') as file:
        for line in file:
            for i in range(0, len(line)):
                is_do_or_dont_expression, value = check_valid_do_or_dont_expression(line, i)
                if is_do_or_dont_expression:
                    is_mul_active = value
                else:
                    if is_mul_active:
                        is_valid_mul_expression, first, sec = check_valid_mul_expression(line, i)
                        if is_valid_mul_expression:
                            score += int(first) * int(sec)
    return score

def check_valid_do_or_dont_expression(line: str, i: int) -> tuple:
    if check_is_do_expr(line, i):
        return True, True
    elif check_is_dont_expr(line, i):
        return True, False
    return False, False

def check_is_do_expr(line: str, i: int) -> bool:
    return line[i:i+4] == 'do()'

def check_is_dont_expr(line: str, i: int) -> bool:
    return line[i:i+7] == 'don\'t()'

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