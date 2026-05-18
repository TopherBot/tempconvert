#!/usr/bin/env python3
"""TempConvert – tiny temperature conversion CLI.

Usage:
    python tempconvert.py <value> <source_unit> [<target_unit>]

Units are case‑insensitive and can be:
    C  – Celsius
    F  – Fahrenheit
    K  – Kelvin

If <target_unit> is omitted, the script prints the value in all three units.
"""
import sys

UNITS = {"c": "C", "f": "F", "k": "K"}

def to_celsius(value: float, src: str) -> float:
    if src == "C":
        return value
    if src == "F":
        return (value - 32) * 5 / 9
    if src == "K":
        return value - 273.15
    raise ValueError(f"Unsupported source unit: {src}")

def from_celsius(value: float, tgt: str) -> float:
    if tgt == "C":
        return value
    if tgt == "F":
        return value * 9 / 5 + 32
    if tgt == "K":
        return value + 273.15
    raise ValueError(f"Unsupported target unit: {tgt}")

def convert(value: float, src: str, tgt: str) -> float:
    c = to_celsius(value, src)
    return from_celsius(c, tgt)

def pretty(value: float, unit: str) -> str:
    return f"{value:.2f} °{unit}"

def main(argv):
    if len(argv) not in (3, 4):
        print("Usage: tempconvert.py <value> <source_unit> [<target_unit>]")
        sys.exit(1)
    try:
        val = float(argv[1])
    except ValueError:
        print(f"Error: '{argv[1]}' is not a numeric value.")
        sys.exit(1)
    src = UNITS.get(argv[2].lower())
    if not src:
        print(f"Error: unknown source unit '{argv[2]}'. Use C, F, or K.")
        sys.exit(1)
    if len(argv) == 4:
        tgt = UNITS.get(argv[3].lower())
        if not tgt:
            print(f"Error: unknown target unit '{argv[3]}'. Use C, F, or K.")
            sys.exit(1)
        result = convert(val, src, tgt)
        print(pretty(result, tgt))
    else:
        # Show all three conversions
        for unit in ("C", "F", "K"):
            out = convert(val, src, unit)
            print(pretty(out, unit))

if __name__ == "__main__":
    main(sys.argv)
