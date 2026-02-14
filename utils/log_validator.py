def check_log_for_error(log_file):
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                return True
    return False


def count_log_keyword(log_file, keyword):
    count = 0
    with open(log_file, "r") as file:
        for line in file:
            if keyword in line:
                count += 1
    return count
