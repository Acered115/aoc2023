import time
import math

dict_list = {}


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
            dict_list[line[:3]] = Line(line)

    return directions, line_list


def find_start_nodes(line_list):
    nodes = []
    for line in line_list:
        if line.this.endswith("A"):
            nodes.append(line.this)
    nodes = sorted(nodes)
    return nodes


def traverse_directions(this):
    index = 0
    loop = True
    # line = line_list[index]

    while loop == True:
        for direct in directions:
            # print(direct)
            # print(this)
            if not this.endswith("Z"):
                this = find_in_list(this, direct)
                index += 1

            else:
                # print(this)
                print(f"Found the end after {index} directions")
                loop = False
                break
    return index


def find_in_list(this, direction):
    new_this = ""
    line = dict_list[this]
    if direction == "R":
        new_this = line.right
    else:
        new_this = line.left
    return new_this


if __name__ == "__main__":
    with open("puzzle_inputs/day8.txt", "r") as file:
        parsed_file = parse_file(file)
        # print(parsed_file)
    directions = parsed_file[0]
    start_nodes = find_start_nodes(line_list=parsed_file[1])
    print(start_nodes)
    ret = 1
    for node in start_nodes:
        ret = math.lcm(ret, traverse_directions(this=node))

    # print(steps_counts)
    print(f"The lowest commond multiple of this list is {ret}")
