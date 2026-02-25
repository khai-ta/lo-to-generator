import random
import json
import csv
from datetime import datetime

def generate_lo_to_card():
    """
    Generate a Vietnamese lo to (bingo) card.
    - 3 rows, 9 columns
    - 5 numbers per row (15 numbers total per card)
    - Column 0: numbers 1-9
    - Column 1: numbers 10-19
    - Column 2: numbers 20-29
    - ... and so on
    - Column 8: numbers 80-90
    - No duplicate numbers on the same card
    """
    card = []
    used_numbers = set()
    
    for row in range(3):
        row_data = [None] * 9
        # Get 5 random positions for this row
        positions = random.sample(range(9), 5)
        
        for col in positions:
            # Determine number range for this column
            if col == 0:
                available = [n for n in range(1, 10) if n not in used_numbers]
            elif col == 8:
                available = [n for n in range(80, 91) if n not in used_numbers]
            else:
                available = [n for n in range(col * 10, col * 10 + 10) if n not in used_numbers]
            
            if available:
                number = random.choice(available)
                row_data[col] = number
                used_numbers.add(number)
        
        card.append(row_data)
    
    # Sort numbers in each column for traditional Lo To appearance
    for col in range(9):
        column_numbers = [card[row][col] for row in range(3) if card[row][col] is not None]
        column_numbers.sort()
        
        col_idx = 0
        for row in range(3):
            if card[row][col] is not None:
                card[row][col] = column_numbers[col_idx]
                col_idx += 1
    
    return card

def card_to_string(card, card_number):
    """Convert card to a formatted string matching traditional Vietnamese lo to cards"""
    lines = []
    
    # Top border with traditional header
    lines.append("\n┌──────────────────────────────────────────────────────────────┐")
    lines.append("│                   LO TO ✦ VSA TET 2026                       │")
    lines.append("├──────────────────────────────────────────────────────────────┤")
    
    # Card rows with checkered pattern (alternating cells)
    for row_idx, row in enumerate(card):
        # Top line of cells
        line1 = "│"
        line2 = "│"
        
        for col_idx, val in enumerate(row):
            if val is None:
                # Empty cell (red in original) - use shading
                line1 += "▓▓▓▓▓▓"
                line2 += "▓▓▓▓▓▓"
            else:
                # Number cell (white in original)
                line1 += "      "
                line2 += f"  {val:2d}  "
            
            if col_idx < 8:
                line1 += "│"
                line2 += "│"
        
        line1 += "│"
        line2 += "│"
        
        lines.append(line1)
        lines.append(line2)
        
        # Bottom border of row
        if row_idx < 2:
            lines.append("├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤")
    
    # Bottom border with card number
    lines.append("└──────────────────────────────────────────────────────────────┘")
    lines.append(f"                                                  CARD #{card_number:03d}")
    
    return '\n'.join(lines)

def generate_cards(num_cards=200):
    """Generate specified number of unique lo to cards"""
    cards = []
    cards_set = set()  # To track unique cards
    
    attempts = 0
    max_attempts = num_cards * 10  # Prevent infinite loop
    
    while len(cards) < num_cards and attempts < max_attempts:
        card = generate_lo_to_card()
        card_tuple = tuple(tuple(row) for row in card)
        
        if card_tuple not in cards_set:
            cards_set.add(card_tuple)
            cards.append(card)
        
        attempts += 1
    
    return cards

def save_cards_to_json(cards, filename='lo_to_cards.json'):
    """Save cards to JSON file"""
    data = {
        'generated_at': datetime.now().isoformat(),
        'total_cards': len(cards),
        'cards': cards
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(cards)} cards to {filename}")

def save_cards_to_csv(cards, filename='lo_to_cards.csv'):
    """Save cards to CSV file (one row per card)"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        header = ['Card #']
        for row in range(3):
            for col in range(9):
                header.append(f'R{row+1}C{col+1}')
        writer.writerow(header)
        
        # Cards
        for idx, card in enumerate(cards, 1):
            row_data = [idx]
            for row in card:
                for val in row:
                    row_data.append(val if val is not None else '')
            writer.writerow(row_data)
    
    print(f"Saved {len(cards)} cards to {filename}")

def save_cards_to_text(cards, filename='lo_to_cards.txt'):
    """Save cards to formatted text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        # Festive title page for Tet
        f.write("\n" + "═"*80 + "\n")
        f.write("\n")
        f.write("    ██╗      ██████╗     ████████╗ ██████╗     ██████╗ ██╗███╗   ██╗ ██████╗  ██████╗ \n")
        f.write("    ██║     ██╔═══██╗    ╚══██╔══╝██╔═══██╗    ██╔══██╗██║████╗  ██║██╔════╝ ██╔═══██╗\n")
        f.write("    ██║     ██║   ██║       ██║   ██║   ██║    ██████╔╝██║██╔██╗ ██║██║  ███╗██║   ██║\n")
        f.write("    ██║     ██║   ██║       ██║   ██║   ██║    ██╔══██╗██║██║╚██╗██║██║   ██║██║   ██║\n")
        f.write("    ███████╗╚██████╔╝       ██║   ╚██████╔╝    ██████╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝\n")
        f.write("    ╚══════╝ ╚═════╝        ╚═╝    ╚═════╝     ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ \n")
        f.write("\n")
        f.write("═"*80 + "\n\n")
        f.write(f"    Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n")
        f.write(f"    Total Cards: {len(cards)}\n")
        f.write("\n" + "═"*80 + "\n")
        f.write("\n" + "─"*80 + "\n")
        
        for idx, card in enumerate(cards, 1):
            f.write(card_to_string(card, idx))
            
            # Page break every 3 cards for better printing
            if idx % 3 == 0 and idx < len(cards):
                f.write('\n\n')
                f.write('═'*65 + '\n')
                f.write(' '*25 + '✂ CUT HERE ✂\n')
                f.write('═'*65 + '\n')
            else:
                f.write('\n')
    
    print(f"Saved {len(cards)} cards to {filename}")

def main():
    print("Generating 200 Vietnamese Lo To Bingo Cards...")
    print("-" * 60)
    
    # Generate cards
    cards = generate_cards(200)
    
    print(f"\nSuccessfully generated {len(cards)} unique cards!")
    print("\nSaving to files...")
    
    # Save in multiple formats
    save_cards_to_json(cards)
    save_cards_to_csv(cards)
    save_cards_to_text(cards)
    
    print("\n" + "="*60)
    print("COMPLETE!")
    print("="*60)
    print("\nFiles created:")
    print("  - lo_to_cards.json (JSON format)")
    print("  - lo_to_cards.csv (CSV format)")
    print("  - lo_to_cards.txt (Human-readable format)")
    print("\nPreview of first card:")
    print(card_to_string(cards[0], 1))

if __name__ == "__main__":
    main()
