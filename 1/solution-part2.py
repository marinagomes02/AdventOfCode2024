def similarity_score() -> int:
    leftList, rightList = read_file()
    similarities = similarities_map(leftList, rightList)
    return calculate_similarity_score(leftList, similarities)

def read_file() -> tuple:
    with open('input-part2.txt', 'r') as file:
        leftList = []
        rightList = []
        for line in file:
            left, right = line.strip().split('   ')
            leftList.append(int(left))
            rightList.append(int(right))
    return leftList, rightList

def similarities_map(left_list: list, rigth_list) -> dict:
    similarities = {}
    for num in left_list:
        similarities[num] = count_times_in_list(rigth_list, num)
    return similarities


def count_times_in_list(lst: list, num: int) -> int:
    return lst.count(num)

def calculate_similarity_score(leftList: list, similarities: dict) -> int:
    score = 0
    for num in leftList:
        score += num * similarities[num]
    return score

print(similarity_score())