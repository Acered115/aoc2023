def calibration_value_extractor(line):
    digits_list = []

    for x in line:
        try:
            # print(int(x))r
            digits_list.append(int(x))
        except:
            pass
    first_digit = digits_list[0]
    last_digit = digits_list[-1]

    return int(str(first_digit) + str(last_digit))


with open("puzzle_inputs/day1.txt", "r") as file:
    sum_of_cal_val = 0
    for line in file:
        sum_of_cal_val += calibration_value_extractor(line)

    print(sum_of_cal_val)
