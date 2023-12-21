from pprint import pprint
import concurrent.futures


class ParseMaps:
    def __init__(self, file):
        self.file = file
        self.maps_obj = {}
        self.parse_into_maps()

    def parse_into_maps(self):
        line_buffer = ""
        current_map = ""
        for line in self.file:
            line_buffer += line
            if "seeds:" in line:
                current_map = line.replace("\n", "")
                seeds = current_map[6:].split(" ")
                seeds.remove("")
                seeds = list(map(int, seeds))

                self.maps_obj[current_map[:5]] = seeds
                line_buffer = ""
                continue

            if ":" in line:
                current_map = line.replace(" map:\n", "")
                self.maps_obj[current_map] = []
                line_buffer = ""
                continue

            if len(line) != 1:
                current_line = line.replace("\n", "")
                line_maps = current_line.split(" ")
                line_maps = list(map(int, line_maps))

                self.maps_obj[current_map].append(line_maps)

            if line == "\n":
                line_buffer = ""
                continue


def parse_map(maps_obj, seed: int):
    locations = []
    for map_ in maps_obj:
        print(map_)
        if map_ == "seeds":
            continue

        source_dest = {}
        for row in maps_obj[map_]:
            range_incr = row[2] - 1
            source_dest[row[1]] = row[0]
            while range_incr != 0:
                source_dest[row[1] + range_incr] = row[0] + range_incr
                range_incr -= 1

        # filling_incr = max(source_dest)

        # while filling_incr != 0:
        #     if filling_incr not in source_dest:
        #         source_dest[filling_incr] = filling_incr
        #         ...
        #     filling_incr -= 1

        # pprint(source_dest)
        if seed not in source_dest:
            source_dest[seed] = seed
            seed = source_dest[seed]
        else:
            seed = source_dest[seed]
        locations.append(seed)
        # print(f"location of seed: {seed}")
        # break
    return seed


def main():
    with open("puzzle_inputs/test5.txt", "r") as file:
        obj = ParseMaps(file)

    seeds = obj.maps_obj["seeds"]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(parse_map, [obj.maps_obj] * len(seeds), seeds))

    pprint(results)


if __name__ == "__main__":
    ### This solution works on small tests...
    ### However with the big data set it just breaks my laptop lol
    ### Need to rework and figure this out lol
    main()
