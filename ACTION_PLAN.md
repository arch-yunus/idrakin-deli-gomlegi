# Otonom İnşa ve Milli Eylem Planı (Uygulama Kılavuzu)

Bu kılavuz, **"İdrakin Deli Gömleği"** manifestosunu teoriden eyleme geçirmek isteyen bağımsız araştırmacılar, mühendisler ve öğrenciler için adım adım pratik yol haritasıdır.

---

## 🛠️ 1. Otonom Araştırmacı Yığını (Tech Stack)

Amfilerin sararmış notlarına ve kilitli veritabanlarına mahkûm olmadan 1 kişilik enstitü kapasitesine ulaşmak için önerilen açık kaynak araç seti:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OTONOM POLİMATIN ÇALIŞMA İSTASYONU                       │
├──────────────────────┬──────────────────────────────────────────────────────┤
│ Katman               │ Önerilen Açık Kaynak Araçlar                         │
├──────────────────────┼──────────────────────────────────────────────────────┤
│ Literatür & Keşif    │ arXiv, Hugging Face Papers, Semantic Scholar, OSF    │
│ Sentez & Notasyon    │ Obsidian (Markdown & Zettelkasten), Logseq, LaTeX    │
│ Yerel Yapay Zekâ     │ Ollama (Llama 3, DeepSeek, Qwen), LM Studio, ComfyUI │
│ Kodlama & Sürüm      │ Git, GitHub, VS Code / Cursor, NeoVim, Docker        │
│ Donanım & Elektronik │ KiCad, FreeCAD, ESP32, STM32, RISC-V, Arduino, QEMU  │
│ Masaüstü Fabrikasyon │ Cura / PrusaSlicer, 3D Yazıcı, USB Osiloskop, Havya  │
└──────────────────────┴──────────────────────────────────────────────────────┘
```

---

## ⚡ 2. Günlük 7 Otonom İnşa Rutini

1. **Günde 1 Saat Orijinal Mimari Oku:** Hocanın hazırladığı özensiz slaytları değil; Linux çekirdeği kaynak kodunu, RFC standartlarını ve doğrudan orijinal arXiv makalelerini incele.
2. **Her Gün 'Proof of Work' Üret:** En az 1 anlamlı Git commit'i at, lehimlenmiş bir devre test et veya çalıştırılabilir bir Jupyter Notebook paylaş. Günü boş geçirme.
3. **İlk İlkelere (First Principles) İn:** Formülleri ezberleme. "Bu denklem nereden türetildi, fiziksel veya mantıksal sebebi ne?" sorusunu sor ve atomik gerçeğine kadar sök.
4. **Otoriteyi Değil Delili Tart:** Karşıdaki kişinin unvanına değil; çalışan sistemine, matematiksel tutarlılığına ve tekrarlanabilirliğine bak.
5. **Kişisel Bilgi Ağını (PKM) Büyüt:** Okuduğun her makale ve yazdığın her kod için Markdown formatında atomik notlar al; bağlantılı bir zihin haritası oluştur.
6. **Milli Kökler & Küresel Standart:** Çözdüğün problem bu toprakların bir derdine derman olsun, ancak inşa ettiğin çözüm küresel en üst açık kaynak standartlarında olsun.
7. **Bedel Ödemekten Korkma (Skin in the Game):** Hata keşfin başlangıcıdır. Çalışmayan prototip, çöken kod veya patlayan transistör; sahte vize notundan bin kat daha öğreticidir.

---

## 📋 3. 30 Günlük "Amfisiz Üretim" Meydan Okuması (Challenge)

| Gün | Görev | Çıktı |
| :--- | :--- | :--- |
| **1–5** | Kendi yerel LLM ve Markdown bilgi grafını kur. | Çalışan Ollama + Obsidian Zettelkasten ağı. |
| **6–12** | İlgilendiğin alanda çığır açmış 3 orijinal makaleyi oku ve analiz et. | GitHub'da yayınlanmış 3 detaylı teknik özet. |
| **13–20** | Seçtiğin bir donanım veya yazılım sistemini tersine mühendislikle sök. | Mimari şeması ve blok diyagramı. |
| **21–27** | Kendi çalışan açık kaynak prototipini (kod veya PCB) inşa et. | Canlı demo reposu ve README belgesi. |
| **28–30** | Projeni açık lisansla (MIT / Apache / CC) dünyaya sun ve akran denetimi iste. | Proof of Work portfolyo girdisi. |

---

## 🎯 4. Ahilik ve Usta-Çırak İletişim Protokolü

- **Doğrudan Eserle Git:** Bir ustaya veya kıdemli bir mühendise soru sorarken "Bana yol gösterin" demek yerine; *"Şu projeyi geliştirdim, şurada tıkandım, osiloskop çıktım ve repo linkim buradadır"* diyerek derini masaya koyduğunu ispatla.
- **Pabucun Dama Atılmasından Korkma:** Kod incelemesinde (PR Review) gelen sert eleştirileri şahsına değil, eserin mükemmelleşmesine yapılmış bir hediye kabul et.

---

> *"İstikbal göklerdedir. Amfiler yerinde sayanların, gökler ise sınır tanımayan hür idraklerindir."*
