def count_words():
    count = 0
    lines = get_input_lines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'X':
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[x]):
                            continue
                        elif lines[x][y] == 'M':
                            direction = (x - i, y - j)
                            if check_letter_in_direction('A', x + direction[0], y + direction[1], lines) and \
                                check_letter_in_direction('S', x + direction[0]*2, y + direction[1]*2, lines):
                                count += 1
    return count


def check_letter_in_direction(letter, x, y, lines) -> bool:
    if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[x]):
        return False
    elif lines[x][y] == letter:
        return True
    else:
        return False


def get_input_lines() -> list:
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line)
    return lines

print(count_words())      