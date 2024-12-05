def count_words():
    count = 0
    lines = get_input_lines()
    for i, line in enumerate(lines):
        if i > 0 and i < len(lines)-1:
            for j, char in enumerate(line):
                if j > 0 and j < len(line)-1 :
                  if char == 'A':
                    print(i, j, char)
                    if check_xmas_left_diagonal(i, j, lines) and \
                        check_xmas_right_diagonal(i, j, lines):
                        count += 1
    return count

def check_xmas_left_diagonal(x, y, lines):
    return lines[x-1][y-1] == 'M' and lines[x+1][y+1] == 'S' or \
        lines[x-1][y-1] == 'S' and lines[x+1][y+1] == 'M'


def check_xmas_right_diagonal(x, y, lines):
    return lines[x+1][y-1] == 'M' and lines[x-1][y+1] == 'S' or \
        lines[x+1][y-1] == 'S' and lines[x-1][y+1] == 'M'


def get_input_lines() -> list:
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line)
    return lines

print(count_words())      