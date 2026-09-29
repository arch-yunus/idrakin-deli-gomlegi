#!/usr/bin/env python3
"""
İdrakin Deli Gömleği — Otonom Polimat arXiv Özümseyici ve PKM Entegratörü
-------------------------------------------------------------------------
Bu betik; amfilerin kilitli veritabanlarına ihtiyaç duymadan, açık bilim
kaynaklarından (arXiv) en güncel araştırmaları çeker ve Zettelkasten
formatında Markdown araştırma notlarına dönüştürür.

Kullanım:
    python scripts/arxiv_polymat_digest.py --query "quantum computing" --max-results 5
    python scripts/arxiv_polymat_digest.py --category "cs.AI" --max-results 10
"""

import argparse
import datetime
import os
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


def fetch_arxiv_papers(query: str, max_results: int = 5):
    base_url = "https://export.arxiv.org/api/query?"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = base_url + urllib.parse.urlencode(params)
    print(f"[*] arXiv sorgulanıyor: {url}")

    req = urllib.request.Request(url, headers={"User-Agent": "IdrakinDeliGomlegi/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read()
    except Exception as e:
        print(f"[!] arXiv bağlantı hatası: {e}")
        return []

    root = ET.fromstring(xml_data)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

    papers = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
        published = entry.find("atom:published", ns).text[:10]
        link = entry.find("atom:id", ns).text.strip()
        
        pdf_link = link.replace("abs", "pdf")
        
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]

        papers.append({
            "title": title,
            "summary": summary,
            "published": published,
            "link": link,
            "pdf_link": pdf_link,
            "authors": authors
        })
    return papers


def export_to_markdown(papers, output_dir="notes"):
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.date.today().isoformat()
    filename = os.path.join(output_dir, f"arxiv_digest_{today}.md")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# ⚡ Otonom Polimat Araştırma Notları — {today}\n\n")
        f.write("> *\"Bilgiye erişim bir ayrıcalık değil, evrensel bir insan hakkıdır.\"* — **Aaron Swartz**\n\n")
        f.write("---\n\n")

        for idx, p in enumerate(papers, 1):
            f.write(f"## {idx}. {p['title']}\n\n")
            f.write(f"- **Yazarlar:** {', '.join(p['authors'])}\n")
            f.write(f"- **Yayın Tarihi:** {p['published']}\n")
            f.write(f"- **arXiv Linki:** [{p['link']}]({p['link']})\n")
            f.write(f"- **Doğrudan Açık PDF:** [PDF İndir]({p['pdf_link']})\n\n")
            f.write("### 📜 Öz (Abstract)\n")
            f.write(f"{p['summary']}\n\n")
            f.write("### 🛠️ İlk İlkeler (First Principles) ve Eylem Değerlendirmesi\n")
            f.write("- [ ] Bu çalışmanın matematiksel / fiziksel temeli doğrulanabilir mi?\n")
            f.write("- [ ] Açık kaynak kod / veri seti mevcut mu?\n")
            f.write("- [ ] Kendi yerel garaj / yazılım tezgâhımda nasıl test edebilirim?\n\n")
            f.write("---\n\n")

    print(f"[OK] Notlar basariyla olusturuldu: {filename}")
    return filename


def main():
    parser = argparse.ArgumentParser(description="Otonom Polimat arXiv Özümseyici")
    parser.add_argument("--query", "-q", default="all:electron OR all:transformer OR all:robotics", help="Arama sorgusu")
    parser.add_argument("--max-results", "-n", type=int, default=5, help="Çekilecek makale sayısı")
    parser.add_argument("--output-dir", "-o", default="notes", help="Çıktı klasörü")

    args = parser.parse_args()
    papers = fetch_arxiv_papers(args.query, args.max_results)

    if not papers:
        print("[!] Hiçbir makale bulunamadı.")
        return

    print(f"[+] {len(papers)} adet açık bilim makalesi çekildi.")
    export_to_markdown(papers, args.output_dir)


if __name__ == "__main__":
    main()
