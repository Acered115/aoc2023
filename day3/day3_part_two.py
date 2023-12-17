from pprint import pprint


def line_parser(line: str):
    """This function just parses each line into its important parts,
    numbers and symbols, it takes not of their indexes as this will be useful later

    :param line: incoming line string
    :type line: str
    :return: Object storing the indexes and symbols found in this line
    :rtype: Dictionary
    """
    number_list = []
    symbols_list = []
    number_buffer = ""
    number_index_buffer = []
    for index, x in enumerate(line):
        if x.isdigit():
            number_buffer += x
            number_index_buffer.append(index)
        else:
            if len(number_buffer) != 0:
                number = int(number_buffer)
                number_list.append({"index": number_index_buffer, "number": number})
                number_buffer = ""
                number_index_buffer = []

            if x == "*":
                symbols_list.append({"index": [index], "symbol": x})
    # print(symbols_list)
    # print(number_list)
    return_object = {"numbers": number_list, "symbols": symbols_list}
    return return_object


def symbol_appender():
    """Function responsible for broadening the index footprint so that
    in the following function i can just do an intersection with the numbers
    which share an index with the symbols
    """
    for row in lines_list:
        # symbol_appender(index, row)
        for symbol in row["symbols"]:
            symbol["index"].insert(0, symbol["index"][0] - 1)
            symbol["index"].append(symbol["index"][-1] + 1)
    # print(row)


def find_adj_numbers(index, symbol_in_line):
    # print(symbol_in_line)
    adjacent_numbers = []
    symbols_index = symbol_in_line["index"]
    for number in lines_list[index]["numbers"]:
        # print("current", number["index"])
        inter_index = list(set(number["index"]) & set(symbols_index))
        if inter_index:
            # print("currents", inter_index)
            adjacent_numbers.append(number["number"])
    if index == 0:
        for number in lines_list[index + 1]["numbers"]:
            # print("current", number["index"])
            inter_index = list(set(number["index"]) & set(symbols_index))
            if inter_index:
                # print("currents", inter_index)
                adjacent_numbers.append(number["number"])
    elif index == len(lines_list) - 1:
        for number in lines_list[index - 1]["numbers"]:
            # print("prev", number)
            inter_index = list(set(number["index"]) & set(symbols_index))
            if inter_index:
                # print("prevs", inter_index)
                adjacent_numbers.append(number["number"])
    else:
        for number in lines_list[index - 1]["numbers"]:
            # print("prev", number)
            inter_index = list(set(number["index"]) & set(symbols_index))
            if inter_index:
                # print("prevs", inter_index)
                adjacent_numbers.append(number["number"])
        for number in lines_list[index + 1]["numbers"]:
            # print("current", number["index"])
            inter_index = list(set(number["index"]) & set(symbols_index))
            if inter_index:
                # print("currents", inter_index)
                adjacent_numbers.append(number["number"])
    # print(f"Symbol in line:{symbol_in_line}, adjacent_numbers:{adjacent_numbers}")
    return symbol_in_line, adjacent_numbers


def gear_ratio_finder():
    """Main function used to check the above and below members of each
    line. Figures out which numbers are in the footprint of the symbols
    of the above and below line and just summs them up
    """
    # pprint(lines_list)
    total_sum = 0
    for index, row in enumerate(lines_list):
        print("index:", index)
        all_symbols_in_line = []
        for symbol in row["symbols"]:
            all_symbols_in_line.append(symbol["symbol"])
        if "*" in all_symbols_in_line:
            for symbol_in_line in lines_list[index]["symbols"]:
                adj_num = find_adj_numbers(index, symbol_in_line)
                if len(adj_num[1]) == 2:
                    summ = 1
                    for number in adj_num[1]:
                        summ *= number
                    print(summ)
                    total_sum += summ
    print(total_sum)

    return


if __name__ == "__main__":
    # test_row = line_parser(
    #     "........................#....374...382....250...*..........737*....*896.395...........*....................$.........................#......\n"
    # )
    lines_list = []

    with open("puzzle_inputs/day3.txt", "r") as file:
        for line in file:
            current_line = line_parser(line)
            lines_list.append(current_line)
    symbol_appender()
    gear_ratio_finder()
