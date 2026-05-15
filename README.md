# PINA AI Literacy · Adult Edition

> Sette conversazioni difficili che vale la pena avere.

Un kit di 7 carte etiche A4 per workshop facilitati di 75 minuti
sull'intelligenza artificiale, rivolti a un pubblico adulto. Pensato per
biblioteche pubbliche, centri civici, formazione aziendale, gruppi di
discussione.

🌐 **Sito**: https://pablosandri05-a11y.github.io/adult-cart

## Cosa c'è

- 7 carte A4 fronte-retro (PDF print-ready)
- 7 giochi digitali standalone (mobile-first)
- Note per il facilitatore
- Sorgenti per rigenerare tutto

## Tre fasce

- **Intimo** — A01 amare un'IA, A02 mi dà ragione
- **Sociale** — A03 prezzi, A04 deepfake, A05 algoritmi giudicanti
- **Politico** — A06 smetto di pensare, A07 chi scrive le regole

## Struttura

```
adult-cart/
├── index.html          ← sito editoriale
├── cards/pdf/          ← 7 PDF stampabili
├── cards/html/         ← 7 HTML sorgenti (rigenerabili)
├── games/              ← 7 giochi interattivi
├── qr/                 ← 7 QR code (URL adult-cart/games)
├── src/                ← pipeline di generazione
│   ├── cards_data.py
│   ├── cards_generator.py
│   ├── generate_qr.py
│   └── html_to_pdf.js
├── assets/             ← CSS, JS, OG image del sito
└── docs/               ← note per il facilitatore
```

## Pipeline di rigenerazione

```bash
pip install qrcode Pillow
npm install puppeteer
python src/generate_qr.py
python src/cards_generator.py
node src/html_to_pdf.js
```

## GitHub Pages

Dopo il push, abilitare GitHub Pages:
- Settings → Pages → Source: Deploy from branch → `main` / `/ (root)`
- Entro 1-2 minuti: https://pablosandri05-a11y.github.io/adult-cart/

## Licenza

CC BY-NC-SA 4.0 — usabile, condivisibile, adattabile. Non vendibile.

## Crediti

PINA AI Literacy — sviluppato da Pablo Sandri in collaborazione con NGO
italiane attive nell'educazione digitale.
