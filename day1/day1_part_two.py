str_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def calibration_value_extractor(line):
    first_digit = scan_string(line)
    last_digit = scan_string(line, reverse=True)

    return int(str(first_digit) + str(last_digit))


def scan_string(line, reverse=False):
    if reverse == True:
        line = line[::-1]
    word_buffer = ""
    digit = 0
    for x in line:
        try:
            digit = int(x)
            break
        except:
            word_buffer += x
            if reverse == True:
                word_buffer = x + word_buffer
            for word in word_digits:
                if word in word_buffer:
                    digit = str_dict[word]
                    return digit
    return digit


if __name__ == "__main__":
    sum_of_cal_val = 0

    with open("puzzle_inputs/day1.txt", "r") as file:
        for line in file:
            sum_of_cal_val += calibration_value_extractor(line)
            print(sum_of_cal_val)
    print(f"Final Val: {sum_of_cal_val}")
