#!/usr/bin/env python3
import sys
import json

info_city = {}

for line in sys.stdin:
    try:
        city, check_prof = line.strip().split("\t")
        check_prof = int(check_prof)

        if city not in info_city:
            info_city[city] = {"profit_stores": 0, "loss_stores": 0}

        if check_prof == 1:
            info_city[city]["profit_stores"] += 1
        else:
            info_city[city]["loss_stores"] += 1

    except Exception as e:
        print(f"Error processing line: {line}, Error: {e}", file=sys.stderr)

output_lines = []

for city, countt in info_city.items():
    output = {
        "city": city,
        "profit_stores": countt["profit_stores"],
        "loss_stores": countt["loss_stores"]
    }

    print(json.dumps(output))
    output_lines.append(json.dumps(output))

with open('output.txt', 'w') as f:
    f.write("\n".join(output_lines))

