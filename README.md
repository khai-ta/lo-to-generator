# Vietnamese Lo To (Bingo) Card Generator

A Python-based tool to generate custom Vietnamese lo to (bingo) cards for events like TET celebrations.

## Features

- **Generates 200 unique Vietnamese lo to cards**
- **Traditional checkered pattern design** with alternating filled/empty cells
- **Multiple output formats**:
  - **JSON**: Structured data format
  - **CSV**: Spreadsheet compatible
  - **TXT**: Human-readable text format
  - **HTML**: Print-ready web page with VSA TET 2026 branding
- **Print-optimized HTML**: 3 cards per page, custom styling

## Card Format

Each card follows the traditional Vietnamese lo to format:
- 3 rows × 9 columns (27 cells total)
- 5 numbers per row (15 numbers total)
- 12 filled/checkered cells per card
- Numbers organized by column ranges:
  - Column 1: 1-9
  - Column 2: 10-19
  - Column 3: 20-29
  - ...
  - Column 9: 80-90
- Numbers sorted within each column

## Usage

### Step 1: Generate Cards

```bash
python generate_lo_to_cards.py
```

This creates three files:
- `lo_to_cards.json` - JSON format
- `lo_to_cards.csv` - CSV format for Excel/Sheets
- `lo_to_cards.txt` - Formatted text with Unicode box drawing

### Step 2: Generate Printable HTML

```bash
python generate_printable_html.py
```

This creates:
- `lo_to_cards_printable.html` - Print-ready HTML with all 200 cards (3 per page)

### Printing

1. Open `lo_to_cards_printable.html` in your browser
2. Click the **🖨️ Print Cards** button (or press Ctrl/Cmd+P)
3. Print settings:
   - Paper: Letter (8.5" × 11")
   - Orientation: Portrait
   - Margins: Auto
   - Background graphics: Enabled

## Project Files

- `generate_lo_to_cards.py` - Main card generator
- `generate_printable_html.py` - HTML generator for printing
- `lo_to_cards.json` - Generated card data (JSON)
- `lo_to_cards.csv` - Generated card data (CSV)
- `lo_to_cards.txt` - Generated card data (TXT)
- `lo_to_cards_printable.html` - Print-ready HTML output

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## License

Free to use for personal and community events

---

**Chúc Mừng Năm Mới!** 🧧
