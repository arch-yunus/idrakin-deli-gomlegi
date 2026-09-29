#!/usr/bin/env python3
"""
İdrakin Deli Gömleği — Çevrimdışı E-Kitap Derleyici
--------------------------------------------------
Tüm dokümanları (README, MANIFESTO, LITERATURE, ACTION_PLAN)
bağımsız, sıfır bağımlılıklı tek bir çevrimdışı HTML e-kitap dosyasına derler.
"""

import os
import re

def markdown_to_simple_html(md_text):
    # Escape HTML special chars
    # Headings
    md_text = re.sub(r'^### (.*)$', r'<h3>\1</h3>', md_text, flags=re.M)
    md_text = re.sub(r'^## (.*)$', r'<h2>\1</h2>', md_text, flags=re.M)
    md_text = re.sub(r'^# (.*)$', r'<h1>\1</h1>', md_text, flags=re.M)
    # Bold & Italic
    md_text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', md_text)
    md_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md_text)
    md_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', md_text)
    # Blockquotes
    md_text = re.sub(r'^> (.*)$', r'<blockquote>\1</blockquote>', md_text, flags=re.M)
    # Lists
    md_text = re.sub(r'^\* (.*)$', r'<li>\1</li>', md_text, flags=re.M)
    md_text = re.sub(r'^- (.*)$', r'<li>\1</li>', md_text, flags=re.M)
    # Paragraphs (simple)
    paragraphs = md_text.split('\n\n')
    formatted = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith('<h') or p.startswith('<blockquote') or p.startswith('<li>') or p.startswith('<table') or p.startswith('```') or p.startswith('<p'):
            formatted.append(p)
        else:
            formatted.append(f'<p>{p}</p>')
    return '\n'.join(formatted)

def build_offline_book():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(base_dir, 'README.md')
    action_path = os.path.join(base_dir, 'ACTION_PLAN.md')
    lit_path = os.path.join(base_dir, 'LITERATURE.md')
    manifesto_path = os.path.join(base_dir, 'MANIFESTO.md')

    content = ""
    for path, title in [(readme_path, "Ana Metin"), (manifesto_path, "Manifesto Bildirgesi"), (action_path, "Eylem Planı"), (lit_path, "Literatür Atlası")]:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content += f"\n\n<!-- SECTION: {title} -->\n\n" + f.read()

    html_body = markdown_to_simple_html(content)

    html_template = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>İdrakin Deli Gömleği — Tam Çevrimdışı E-Kitap</title>
  <style>
    body {{
      font-family: Georgia, serif;
      line-height: 1.8;
      max-width: 800px;
      margin: 40px auto;
      padding: 0 20px;
      color: #1a1a1a;
      background: #fdfdfd;
    }}
    h1, h2, h3 {{ font-family: 'Cinzel', serif, Arial; color: #990000; margin-top: 1.8em; }}
    h1 {{ font-size: 2.2em; border-bottom: 2px solid #990000; padding-bottom: 10px; text-align: center; }}
    h2 {{ font-size: 1.5em; border-bottom: 1px solid #ccc; padding-bottom: 6px; }}
    blockquote {{
      border-left: 4px solid #990000;
      margin: 20px 0;
      padding: 10px 20px;
      background: #f9f2f2;
      font-style: italic;
    }}
    li {{ margin-bottom: 6px; }}
    img {{ max-width: 100%; height: auto; border-radius: 8px; margin: 15px 0; }}
    @media print {{
      body {{ font-size: 11pt; margin: 0; padding: 0; }}
      h1, h2, h3 {{ page-break-after: avoid; }}
    }}
  </style>
</head>
<body>
  {html_body}
</body>
</html>"""

    out_file = os.path.join(base_dir, 'dist', 'idrakin-deli-gomlegi-kitap.html')
    os.makedirs(os.path.join(base_dir, 'dist'), exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"[OK] Cevrimdisi e-kitap olusturuldu: {out_file}")

if __name__ == '__main__':
    build_offline_book()
