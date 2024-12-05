import math

def valid_order_pages() -> int:
    rules, pages = read_input()
    parsed_rules = parse_rules(rules)
    parsed_pages = parse_pages(pages)
    score = 0
    for page in parsed_pages:
        if not is_valid_order(page, parsed_rules):
            valid_ordered = get_valid_order(page, parsed_rules)
            score += int(valid_ordered[math.floor(len(valid_ordered)/2)])    
    return score


def is_valid_order(page: list, rules: dict) -> bool:
    for i in range(len(page)):
        if page[i] in rules:
            after = page[i+1:]
            if [x for x in after if x in rules.get(page[i])] != []:
                return False
    return True


def get_valid_order(page: list, rules: dict) -> list:
    dict_page = {}
    for i in range(len(page)):
        num = page[i]
        if num not in rules:
            dict_page[0] = num
            continue
        else:
            after_in_before_list = [x for x in page if x in rules[num]]
            if after_in_before_list != []:
                dict_page[len(after_in_before_list)] = num
            else:
                dict_page[0] = num
    return [dict_page[key] for key in sorted(dict_page.keys())]
           

def parse_rules(rules: list) -> dict:
    orders = {}
    for rule in rules:
        before, num = rule.split('|')
        if num not in orders:
            orders[num] = []
        if before not in orders.get(num):
            orders[num] += [before]
    return orders

def parse_pages(pages_str: list) -> list:
    pages = []
    for page_str in pages_str:
        page = page_str.split(',')
        pages.append(page)
    return pages


def read_input() -> tuple:
    rules = []
    pages = []
    in_pages = False
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                in_pages = True
                continue
            if in_pages:
                pages.append(line.strip())
            else:
                rules.append(line.strip())
    return rules, pages

print(valid_order_pages())