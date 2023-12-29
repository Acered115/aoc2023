import time


class Line:
    def __init__(self, line):
        self.line = line
        self.this = ""
        self.left = ""
        self.right = ""
        self._parse_line()

    def _parse_line(self):
        # print(self.line)
        self.this = self.line[:3]
        self.left = self.line[7:10]
        self.right = self.line[12:15]


def parse_file(file):
    directions = ""
    line_list = []
    for line in list(file):
        line = line.replace("\n", "")
        if len(line) != 16 and len(line) != 0:
            directions = line
            continue
        elif len(line) == 0:
            continue
        else:
            line_list.append(Line(line))

    return directions, line_list


def traverse_directions(directions, line_list):
    index = 0
    loop = True
    this = "AAA"
    # line = line_list[index]

    while loop == True:
        for direct in directions:
            print(direct)
            print(this)
            if this != "ZZZ":
                this = find_in_list(this, direct, line_list)
                index += 1

            else:
                # print(this)
                print(f"Found 'ZZZ' after {index} directions")
                loop = False
                break
    return index


def find_in_list(this, direction, line_list):
    # print(direction)
    # print(line.this, line.left, line.right)
    new_this = ""
    if direction == "R":
        for line in line_list:
            if line.this == this:
                # print(line.this)
                new_this = line.right
    else:
        for line in line_list:
            if line.this == this:
                # print(line.this)
                new_this = line.left
    # time.sleep(1)
    return new_this


if __name__ == "__main__":
    with open("puzzle_inputs/day8.txt", "r") as file:
        parsed_file = parse_file(file)
        # print(parsed_file)
    steps = traverse_directions(directions=parsed_file[0], line_list=parsed_file[1])
    print(steps)
