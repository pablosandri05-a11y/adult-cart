# PINA AI Literacy · Adult Edition · MVP

Kit completo per workshop in biblioteche pubbliche (Zara, Bovisa). Sette carte etiche A4 fronte-retro + sette giochi digitali standalone. Target adulti 18+, sessioni facilitate da 75 minuti.

---

## Cosa c'è dentro

```
pina-adult-mvp/
├── README.md                  ← questo file
├── carte/                     ← 7 HTML self-contained delle carte (sorgente)
├── pdf/                       ← 7 PDF A4 print-ready (le carte da stampare)
├── giochi/                    ← 7 HTML standalone (i giochi digitali)
└── qr/                        ← 7 PNG dei QR code (già embedded nelle carte)
```

Le sette carte: **A01 Posso amare un'IA**, **A02 L'IA che mi dà sempre ragione**, **A03 Lo stesso prezzo per tutti**, **A04 Posso fidarmi di quello che vedo**, **A05 Vorresti essere giudicato da un algoritmo**, **A06 Se smetto di pensare cosa perdo**, **A07 Chi scrive le regole**.

---

## Come deployare i giochi su GitHub Pages

I QR code embedded nelle carte puntano tutti a:

```
https://pablosandri05-a11y.github.io/pina-games/game_AXX_slug.html
```

Per fare funzionare i QR devi:

1. Aprire la repo `pina-games` su GitHub (quella che usi già per i giochi delle carte kids).
2. Copiare i 7 file della cartella `giochi/` nella root della repo (oppure dentro una sottocartella, ma allora i QR devono essere ricalcolati).
3. Commit + push. GitHub Pages aggiorna entro 1-2 minuti.
4. Verifica aprendo da telefono uno dei link: `https://pablosandri05-a11y.github.io/pina-games/game_A01_amare_ia.html`.

Se vuoi controllare prima localmente: apri direttamente `giochi/game_A01_amare_ia.html` con doppio click. Sono tutti standalone, nessuna dipendenza esterna oltre Google Fonts (caricato via CDN).

---

## Come stampare le carte

I PDF in `pdf/` sono già pronti per la stampa professionale:

- **Formato:** A4 (210x297mm), margini a filo, due pagine per file (fronte + retro)
- **Colore:** CMYK funziona, ma il navy `#0F1729` rende meglio in stampa offset. Per stampa digitale standard va bene anche RGB.
- **Carta consigliata:** 250-300g satinata o opaca. Il satinato fa risaltare la palette navy/teal/copper.
- **Stampa fronte-retro:** lato lungo (giro come un libro). I PDF sono già impaginati per questa modalità.

Per stampe rapide (test casa o ufficio): la carta normale 80g funziona, ma i colori risulteranno più piatti.

---

## Se vuoi modificare il contenuto delle carte

I sorgenti sono in `/home/claude/pina-adult/` (nel container Claude), ma per facilità qui hai i file HTML completi delle carte in `carte/`. Sono self-contained: tutto il CSS è inline, tutte le illustrazioni SVG sono inline, i QR sono in base64.

Per rigenerare un PDF da un HTML modificato, sul tuo Windows usa la stessa pipeline Puppeteer che già hai per le carte kids: punta il convertitore HTML→PDF al file modificato, formato A4, `printBackground: true`, margini a zero.

Se vuoi rifare l'intero kit da capo cambiando contenuti, i sorgenti Python (`cards_data.py`, `cards_generator.py`, `generate_qr.py`, `html-to-pdf.js`) sono modulari:

```
cards_data.py        ← contenuto strutturato (modifica qui)
cards_generator.py   ← template HTML + illustrazioni SVG
generate_qr.py       ← genera i QR PNG
html-to-pdf.js       ← Playwright HTML→PDF
```

Pipeline completa:
```bash
python3 generate_qr.py        # genera i QR locali
python3 cards_generator.py    # genera gli HTML
node html-to-pdf.js           # converte in PDF
```

---

## I sette giochi: cosa fanno

Ogni gioco è pensato per essere fatto da soli (a casa, dopo il workshop) o nei minuti finali del workshop, prima della plenaria.

| Carta | Gioco | Cosa fa |
|---|---|---|
| **A01** | Two Voices | 6 situazioni emotive, l'utente sceglie tra «voce calda» e «voce onesta» per ognuna. A fine: profilo dell'utente. |
| **A02** | Sycophancy Test | L'utente sceglie un'affermazione tra 5 (anche assurde). Vede tre risposte AI tarate: accomodante / cauta / diretta. |
| **A03** | Position Tracker | 8 scenari di pricing algoritmico con slider continuo. A fine: mappa visiva delle posizioni + interpretazione. |
| **A04** | Detection Challenge | 8 scenari testuali (WhatsApp, mail, voce, foto). L'utente classifica: autentico/falso/dubbio. Reveal con tips concreti. |
| **A05** | Empathy Lens | Un caso (mutuo negato) visto da 4 prospettive cliccabili (Anna / ingegnere / banca / regolatore). Voto + riflessione. |
| **A06** | Cognitive Audit | 4 domande con timer 90s ciascuna. L'utente scrive a mano, poi vede la risposta AI a confronto. |
| **A07** | Trade-off Console | 4 slider interconnessi (innovazione, equità, sicurezza, sovranità). Budget di 200 punti totali. A fine: profilo politico AI implicito. |

Tutti sono mobile-first (testati a 390px di larghezza), funzionano offline una volta caricati, nessun login, nessun tracking. I dati non vengono salvati né inviati da nessuna parte — è una scelta deliberata per il contesto biblioteca pubblica.

---

## Per i workshop in biblioteca

Ogni carta è progettata per una sessione di 75 minuti con 12-20 partecipanti. La struttura è sempre la stessa:

1. **Apertura** (5 min) — una storia o domanda d'innesco
2. **Posizionamento** (10-15 min) — esercizio collettivo di mappatura delle opinioni
3. **Casi/scenari** (15-25 min) — lavoro in piccoli gruppi
4. **Plenaria** (15 min) — condivisione e dibattito
5. **Provocazione** (10 min) — la domanda «scomoda» che ribalta la prospettiva
6. **Chiusura** (10 min) — qualcosa da portarsi a casa

Il retro di ogni carta è il «Facilitator Zone»: lo trovi stampato, ma se preferisci puoi farne una copia su carta separata per consultarla durante la sessione senza girare la carta principale.

---

## Cosa manca / cosa potresti aggiungere dopo

- **Italian National Curriculum mapping** — per quando vorrai proporle al MIUR
- **Teacher kit** in formato A4 separato (più lungo, più discorsivo, con bibliografia)
- **Licenza CC BY-NC-SA 4.0** — da aggiungere come pagina iniziale o footer del sito
- **Post LinkedIn** di lancio (lingua italiana, tono diretto come ti piace)
- **Pagina di presentazione** del set Adult sul sito `pina-games` (parallela a quella delle card kids)

Quando vuoi, parlami di una delle voci sopra e procediamo.

---

PINA AI Literacy · Adult Edition · MVP v1.0 · maggio 2026
