def compute_distance() -> int:
    leftList, rightList = read_file()
    return compare_lists(leftList, rightList)


def read_file() -> tuple:
    with open('input-part1.txt', 'r') as file:
        leftList = []
        rightList = []
        for line in file:
            left, right = line.strip().split('   ')
            leftList.append(int(left))
            rightList.append(int(right))
    return leftList, rightList


def distance_between_pairs(left, right) -> int:
    return abs(left - right)


def compare_lists(leftList, rightList) -> list:
    distance = 0
    leftList = sorted(leftList)
    rightList = sorted(rightList)

    for left, right in zip(leftList, rightList):
        distance += distance_between_pairs(left, right)
    
    return distance


print(compute_distance())