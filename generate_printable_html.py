import re

def parse_lo_to_cards(txt_file):
    """Parse lo to cards from txt file"""
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all card blocks between the header and footer
    card_pattern = r'┌─+┐\n│\s+LO TO ✦ VSA TET 2026\s+│\n├─+┤\n(.*?)└─+┘'
    
    cards = []
    for match in re.finditer(card_pattern, content, re.DOTALL):
        grid_text = match.group(1)
        lines = grid_text.split('\n')
        
        # Parse only the lines with data (not the separator lines with ├┼┤)
        data_lines = []
        for line in lines:
            if '│' in line and '─' not in line and '┼' not in line and '├' not in line:
                data_lines.append(line)
        
        # Each row has 2 lines: line with filled markers, line with numbers
        # We need to take lines at indices 0,1 (row 1), 2,3 (row 2), 4,5 (row 3)
        card_data = []
        for row_idx in range(0, 6, 2):  # 0, 2, 4
            if row_idx + 1 < len(data_lines):
                marker_line = data_lines[row_idx]  # Line with ▓▓▓▓▓▓ markers
                number_line = data_lines[row_idx + 1]  # Line with actual numbers
                
                marker_cells = marker_line.split('│')[1:-1]  # Remove first and last empty elements
                number_cells = number_line.split('│')[1:-1]
                
                row_data = []
                for marker_cell, number_cell in zip(marker_cells, number_cells):
                    marker_text = marker_cell.strip()
                    number_text = number_cell.strip()
                    
                    if '▓' in marker_text:
                        row_data.append('')  # Filled cell
                    else:
                        # Extract number from number line
                        row_data.append(number_text)
                
                if len(row_data) == 9:
                    card_data.append(row_data)
        
        if len(card_data) == 3:
            cards.append(card_data)
    
    return cards

def generate_html_card(card_num, card_data):
    """Generate HTML for a single card"""
    html = '        <div class="card">\n'
    html += '            <div class="card-header">LO TO ✦ VSA TET 2026</div>\n'
    html += '            <div class="bingo-grid">\n'
    
    for row in card_data:
        for cell in row:
            if cell:
                html += f'                <div class="bingo-cell empty">{cell}</div>\n'
            else:
                html += '                <div class="bingo-cell filled"></div>\n'
    
    html += '            </div>\n'
    html += '        </div>\n'
    return html

def generate_complete_html(cards):
    """Generate complete HTML with all cards"""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LO TO BINGO - VSA TET 2026</title>
    <style>
        :root {
            --vsa-red: #C41E3A;
            --vsa-gold: #FFD700;
            --vsa-yellow: #FFC72C;
            --vsa-dark-red: #8B0000;
            --border-color: #2C1810;
            --text-color: #1a1a1a;
        }
        
        @media print {
            body {
                margin: 0;
                padding: 0;
            }
            .page-break {
                page-break-after: always;
            }
            .no-print {
                display: none;
            }
            @page {
                size: letter portrait;
                margin: 0.3in 0.4in;
            }
            .cards-container {
                display: flex;
                flex-direction: column;
                gap: 8px;
            }
            .card {
                border: 2px solid var(--vsa-red);
                margin-bottom: 0;
                padding: 10px;
            }
            .card-header {
                padding: 8px;
                font-size: 13px;
                margin-bottom: 8px;
            }
            .bingo-cell {
                font-size: 13px;
            }
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: #FFF8E7;
            padding: 10px;
        }
        
        .print-button {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 30px;
            background: var(--vsa-red);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            z-index: 1000;
        }
        
        .print-button:hover {
            background: var(--vsa-dark-red);
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.3);
        }
        
        .cards-page {
            break-inside: avoid;
            page-break-after: always;
        }
        
        .cards-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 15px;
        }
        
        .card {
            background: #FFF8E7;
            border: 3px solid var(--vsa-red);
            border-radius: 6px;
            padding: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            break-inside: avoid;
        }
        
        .card-header {
            text-align: center;
            padding: 10px;
            background: linear-gradient(135deg, var(--vsa-red) 0%, var(--vsa-dark-red) 100%);
            color: white;
            border-radius: 4px;
            margin-bottom: 10px;
            font-weight: bold;
            font-size: 15px;
            letter-spacing: 1px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        .bingo-grid {
            display: grid;
            grid-template-columns: repeat(9, 1fr);
            gap: 2px;
            border: 2px solid var(--border-color);
            border-radius: 6px;
            overflow: hidden;
            background: var(--border-color);
        }
        
        .bingo-cell {
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 15px;
            background: #FFF8E7;
            border: 1px solid #ddd;
        }
        
        .bingo-cell.filled {
            background: repeating-linear-gradient(
                45deg,
                var(--vsa-gold),
                var(--vsa-gold) 5px,
                var(--vsa-yellow) 5px,
                var(--vsa-yellow) 10px
            );
            color: var(--vsa-dark-red);
            font-weight: bold;
        }
        
        .bingo-cell.empty {
            background: #FFF8E7;
            color: var(--text-color);
        }
    </style>
</head>
<body>
    <button class="print-button no-print" onclick="window.print()">🖨️ Print Cards</button>
    
'''
    
    # Generate cards in groups of 3 per page
    for i in range(0, len(cards), 3):
        html += '    <div class="cards-page">\n'
        html += '    <div class="cards-container">\n'
        
        # Add up to 3 cards
        for j in range(3):
            if i + j < len(cards):
                html += generate_html_card(i + j + 1, cards[i + j])
        
        html += '    </div>\n'
        html += '    </div>\n\n'
    
    html += '''    <script>
        // Add print functionality
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
                e.preventDefault();
                window.print();
            }
        });
    </script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    # Parse cards from txt file
    print("Parsing cards from lo_to_cards.txt...")
    cards = parse_lo_to_cards('/Users/khaita/Documents/PSU/VSA/Lo To/lo_to_cards.txt')
    print(f"Found {len(cards)} cards")
    
    # Generate HTML
    print("Generating HTML...")
    html = generate_complete_html(cards)
    
    # Save to file
    output_file = '/Users/khaita/Documents/PSU/VSA/Lo To/lo_to_cards_printable.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Generated {output_file}")
    print(f"   Total cards: {len(cards)}")
    print(f"   Total pages: {(len(cards) + 2) // 3}")
