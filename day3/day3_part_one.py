line_list = []
digit_str_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def line_parser(line):
    line_list.append(line)
    symbol_index = []
    number_buffer = ""
    number_list = []
    digit_ends = []
    # print(line)
    for index, x in enumerate(line):
        # print(index)
        if x not in digit_str_list and x != "." and x != "\n":
            # print(x, index)
            symbol_index.append((x, index))

        if x.isdigit():
            digit_ends.append(index)
            number_buffer += x
        else:
            if len(number_buffer) != 0:
                number_list.append({"number": int(number_buffer), "ends": digit_ends})
                digit_ends = []
            number_buffer = ""
    # print(number_list)

    return {"number_list": number_list, "symbols_index": symbol_index}


# Need to create symbol index checker between adjascent lines
#

if __name__ == "__main__":
    sum_of_all = 0
    print(
        line_parser(
            "........................#....374...382....250...*..........737*....*896.395...........*....................$.........................#......\n"
        )
    )
    # with open("puzzle_inputs/test3.txt", "r") as file:
    #     for line in file:
    #         line_parser(line)
    # print((sum_of_all - 114) - 58)
    # print(line_list)
