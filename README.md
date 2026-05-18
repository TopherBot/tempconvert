# TempConvert

**TempConvert** is a minimal Python script that converts a temperature from one unit to another directly from the terminal.

## Features
- No external dependencies – pure Python 3.
- Supports Celsius (C), Fahrenheit (F) and Kelvin (K).
- Simple, one‑file implementation.

## Usage
```bash
# Convert 100 Celsius to Fahrenheit
python tempconvert.py 100 C F

# Convert 212 Fahrenheit to Kelvin
python tempconvert.py 212 F K
```
If you omit the target unit, the script will display all three conversions for the given input.

## Installation
1. Ensure you have Python 3.6+ installed.
2. Save `tempconvert.py` to a directory in your `$PATH` or run it directly.
3. Make it executable (optional):
   ```bash
   chmod +x tempconvert.py
   ```

## License
MIT – see the `LICENSE` file.
