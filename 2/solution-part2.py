def safe_reports() -> int:
    count_safe_reports = 0
    reportList = read_file()
    for report in reportList:
        if (is_report_safe(report)):
            count_safe_reports += 1
        else:
            for i, level in enumerate(report):
                reportCopy = report.copy()
                reportCopy.pop(i)
                if is_report_safe(reportCopy) == True:
                    count_safe_reports += 1
                    break
    return count_safe_reports

def read_file() -> tuple:
    with open('input-part1.txt', 'r') as file:
        reportList = []
        for line in file:
            report = line.strip().split(' ')
            reportList.append(report)
    return reportList

def is_report_safe(report: list) -> bool:
    is_asc_order = False
    for i in range(1, len(report)):
        prev = int(report[i - 1])
        curr = int(report[i])
        diff = abs(curr - prev)
   
        if (i == 1):
           is_asc_order = curr > prev
        if (diff < 1 or diff > 3):
            return False
        if (curr > prev and is_asc_order or curr < prev and not is_asc_order):
            continue
        else:
            return False
        
    return True

print(safe_reports())