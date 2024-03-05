races = [
    {"time": 54, "record": 302},
    {"time": 94, "record": 1476},
    {"time": 65, "record": 1029},
    {"time": 92, "record": 1404},
]


def calculate_charge_time(race):
    # print(race["time"])
    record_breakers = []
    time = race["time"]
    for duration in range(0, time):
        time_left = time - duration
        distance_travelled = time_left * duration
        # print(distance_travelled)
        if distance_travelled > race["record"]:
            record_breakers.append(distance_travelled)

    return record_breakers


if __name__ == "__main__":
    total = 1
    for race in races:
        record_breakers = calculate_charge_time(race)
        # print(len(record_breakers))
        total *= len(record_breakers)
    print(total)
