# Vietnamese Lo To (Bingo) Card Generator

A Python script to generate custom Vietnamese lo to (bingo) cards for events like TET

## Features

- Generates 200 unique Vietnamese lo to cards
- Traditional checkered pattern design
- Outputs in multiple formats:
  - **JSON**: Structured data format
  - **CSV**: Spreadsheet compatible
  - **TXT**: Human-readable, print-ready format

## Card Format

Each card follows the traditional Vietnamese lo to format:
- 3 rows × 9 columns
- 5 numbers per row (15 numbers total)
- Numbers organized by column ranges:
  - Column 1: 1-9
  - Column 2: 10-19
  - Column 3: 20-29
  - ...
  - Column 9: 80-90

## Usage

```bash
python generate_lo_to_cards.py
```

This will generate three files:
- `lo_to_cards.json` - JSON format
- `lo_to_cards.csv` - CSV format for Excel/Sheets
- `lo_to_cards.txt` - Formatted text ready for printing

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## License

Free to use for personal and community events

---

**Chúc Mừng Năm Mới!** 🧧
