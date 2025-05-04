#!/usr/bin/env python3
import sys
import json

def store_check(data):
    city = data.get("city")
    categories = data.get("categories", [])
    sales_data = data.get("sales_data", {})

    if not categories or not sales_data:
        return

    # Filter sales_data to only include categories present in the 'categories' array
    filtered_sales_data = {cat: sales_data[cat] for cat in categories if cat in sales_data}

    if not filtered_sales_data:
        return

    net_returns = 0
    chck_valid = False

    for category, sales in filtered_sales_data.items():
        revenue = sales.get("revenue", 0)
        cogs = sales.get("cogs", 0)

        if revenue or cogs:
            chck_valid = True
            net_returns += revenue - cogs

    if chck_valid:
        check_prof = 1 if net_returns > 0 else 0
        print(f"{city}\t{check_prof}")

# Mapper function for Pre-processing Array of JSON objects
def mapper():
    buffer = ""
    inside_array = False
    try:
        for line in sys.stdin:
            line = line.strip()

            # removing [] to make it separate json obj
            if line.startswith("["):
                inside_array = True
                continue
            
            if line.endswith("]"):
                inside_array = False
                continue
            
            line = line.rstrip(",")
            buffer += line

            try:
                data = json.loads(buffer)
                store_check(data)
                buffer = "" 
            except json.JSONDecodeError:
                continue

    except Exception as e:
        print(f"Error processing input: {e}", file=sys.stderr)

if __name__ == "__main__":
    mapper()

