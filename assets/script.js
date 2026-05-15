/* PINA AI Literacy · Adult Edition · script.js */

// =========================================================
// SVG Illustrations (inline, same as cards)
// =========================================================
const ILLUSTRATIONS = {
  companions: `<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs>
    <radialGradient id="sg1a" cx="35%" cy="50%" r="50%"><stop offset="0%" stop-color="#F4EBDD" stop-opacity="0.18"/><stop offset="100%" stop-color="#F4EBDD" stop-opacity="0"/></radialGradient>
    <radialGradient id="sg1b" cx="65%" cy="50%" r="50%"><stop offset="0%" stop-color="#00D4AA" stop-opacity="0.15"/><stop offset="100%" stop-color="#00D4AA" stop-opacity="0"/></radialGradient>
  </defs>
  <ellipse cx="185" cy="160" rx="130" ry="110" fill="url(#sg1a)"/>
  <ellipse cx="395" cy="160" rx="130" ry="110" fill="url(#sg1b)"/>
  <path d="M 230 110 Q 290 60 350 110" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="6 4"/>
  <path d="M 230 210 Q 290 260 350 210" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="6 4"/>
  <circle cx="185" cy="118" r="28" stroke="#F4EBDD" stroke-width="2" stroke-opacity="0.85"/>
  <path d="M 145 230 Q 145 185 185 178 Q 225 185 225 230" stroke="#F4EBDD" stroke-width="2" stroke-opacity="0.7" stroke-linecap="round"/>
  <circle cx="185" cy="118" r="8" fill="#F4EBDD" fill-opacity="0.25"/>
  <circle cx="185" cy="160" r="55" stroke="#F4EBDD" stroke-width="0.8" stroke-opacity="0.15" stroke-dasharray="4 6"/>
  <rect x="365" y="88" width="60" height="60" rx="6" stroke="#00D4AA" stroke-width="2" stroke-opacity="0.85"/>
  <line x1="375" y1="108" x2="415" y2="108" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="375" y1="118" x2="415" y2="118" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="375" y1="128" x2="400" y2="128" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <circle cx="395" cy="103" r="6" fill="#00D4AA" fill-opacity="0.3"/>
  <path d="M 355 185 L 355 230 L 435 230 L 435 185" stroke="#00D4AA" stroke-width="2" stroke-opacity="0.7" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="395" cy="160" r="55" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.15" stroke-dasharray="4 6"/>
  <circle cx="290" cy="160" r="10" fill="#E8845C" fill-opacity="0.25" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.6"/>
  <circle cx="290" cy="160" r="4" fill="#E8845C" fill-opacity="0.7"/>
  <line x1="240" y1="160" x2="280" y2="160" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.5"/>
  <line x1="300" y1="160" x2="340" y2="160" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.5"/>
  <text x="282" y="84" font-size="18" fill="#FFD166" fill-opacity="0.35" font-family="serif" font-style="italic">?</text>
</svg>`,

  mirror: `<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <ellipse cx="290" cy="158" rx="72" ry="100" fill="#1A2540" stroke="#8899BB" stroke-width="2" stroke-opacity="0.6"/>
  <ellipse cx="290" cy="158" rx="58" ry="86" fill="#0F1729" fill-opacity="0.5"/>
  <ellipse cx="272" cy="110" rx="12" ry="28" fill="white" fill-opacity="0.04"/>
  <circle cx="145" cy="120" r="22" stroke="#F4EBDD" stroke-width="1.8" stroke-opacity="0.8"/>
  <path d="M 112 220 Q 112 178 145 172 Q 178 178 178 220" stroke="#F4EBDD" stroke-width="1.8" stroke-opacity="0.65" stroke-linecap="round"/>
  <circle cx="185" cy="140" r="4" fill="#F4EBDD" fill-opacity="0.3"/>
  <circle cx="205" cy="133" r="3" fill="#F4EBDD" fill-opacity="0.2"/>
  <circle cx="222" cy="128" r="2" fill="#F4EBDD" fill-opacity="0.15"/>
  <circle cx="290" cy="118" r="16" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.7"/>
  <path d="M 268 188 Q 268 162 290 158 Q 312 162 312 188" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.6" stroke-linecap="round"/>
  <text x="302" y="100" font-size="13" fill="#FFD166" fill-opacity="0.8" font-family="sans-serif">&#x2713;</text>
  <text x="266" y="102" font-size="10" fill="#FFD166" fill-opacity="0.5" font-family="sans-serif">&#x2713;</text>
  <text x="308" y="140" font-size="10" fill="#00D4AA" fill-opacity="0.6" font-family="sans-serif">&#x2713;</text>
  <rect x="256" y="196" width="68" height="18" rx="4" fill="#00D4AA" fill-opacity="0.15" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.4"/>
  <text x="290" y="209" font-size="7.5" fill="#00D4AA" fill-opacity="0.8" font-family="monospace" text-anchor="middle" letter-spacing="1">OTTIMA IDEA!</text>
  <circle cx="430" cy="100" r="18" fill="#E8845C" fill-opacity="0.12" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.5"/>
  <text x="430" y="106" font-size="14" fill="#E8845C" fill-opacity="0.7" text-anchor="middle" font-family="sans-serif">&#x2605;</text>
  <circle cx="468" cy="148" r="14" fill="#FFD166" fill-opacity="0.1" stroke="#FFD166" stroke-width="1" stroke-opacity="0.4"/>
  <text x="468" y="154" font-size="11" fill="#FFD166" fill-opacity="0.6" text-anchor="middle" font-family="sans-serif">&#x2605;</text>
  <rect x="278" y="258" width="24" height="12" rx="2" fill="#8899BB" fill-opacity="0.3"/>
  <rect x="265" y="268" width="50" height="6" rx="3" fill="#8899BB" fill-opacity="0.2"/>
</svg>`,

  pricing: `<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <line x1="80" y1="270" x2="500" y2="270" stroke="#F4EBDD" stroke-opacity="0.12" stroke-width="1"/>
  <line x1="80" y1="230" x2="500" y2="230" stroke="#F4EBDD" stroke-opacity="0.07" stroke-width="0.8" stroke-dasharray="4 4"/>
  <line x1="80" y1="190" x2="500" y2="190" stroke="#F4EBDD" stroke-opacity="0.07" stroke-width="0.8" stroke-dasharray="4 4"/>
  <rect x="80" y="88" width="36" height="52" rx="6" stroke="#8899BB" stroke-width="1.5" stroke-opacity="0.6"/>
  <rect x="78" y="180" width="40" height="90" rx="4" fill="#8899BB" fill-opacity="0.25" stroke="#8899BB" stroke-width="1" stroke-opacity="0.3"/>
  <rect x="72" y="148" width="52" height="26" rx="5" fill="#1A2540" stroke="#8899BB" stroke-width="1" stroke-opacity="0.5"/>
  <circle cx="88" cy="161" r="3" fill="#8899BB" fill-opacity="0.6"/>
  <text x="115" y="165" font-size="11" fill="#F4EBDD" fill-opacity="0.6" text-anchor="middle" font-family="monospace" font-weight="bold">&#8364;10</text>
  <rect x="200" y="90" width="50" height="38" rx="4" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.55"/>
  <rect x="196" y="160" width="58" height="110" rx="4" fill="#F4EBDD" fill-opacity="0.2" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.3"/>
  <rect x="190" y="136" width="70" height="26" rx="5" fill="#1A2540" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.4"/>
  <circle cx="205" cy="149" r="3" fill="#F4EBDD" fill-opacity="0.5"/>
  <text x="232" y="153" font-size="11" fill="#F4EBDD" fill-opacity="0.65" text-anchor="middle" font-family="monospace" font-weight="bold">&#8364;12</text>
  <rect x="352" y="85" width="32" height="56" rx="8" stroke="#00D4AA" stroke-width="2" stroke-opacity="0.8"/>
  <rect x="348" y="148" width="40" height="122" rx="4" fill="#00D4AA" fill-opacity="0.2" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.4"/>
  <rect x="338" y="118" width="60" height="26" rx="5" fill="#1A2540" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.7"/>
  <circle cx="352" cy="131" r="3" fill="#E8845C" fill-opacity="0.7"/>
  <text x="375" y="135" font-size="11" fill="#E8845C" fill-opacity="0.9" text-anchor="middle" font-family="monospace" font-weight="bold">&#8364;15</text>
  <path d="M 270 50 L 310 50 L 318 80 L 262 80 Z" stroke="#FFD166" stroke-width="1.5" stroke-opacity="0.6" fill="none"/>
  <path d="M 278 50 Q 278 38 290 38 Q 302 38 302 50" stroke="#FFD166" stroke-width="1.5" stroke-opacity="0.6"/>
  <text x="290" y="70" font-size="8" fill="#FFD166" fill-opacity="0.5" text-anchor="middle" font-family="monospace">= ?</text>
</svg>`,

  eye: `<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs><radialGradient id="sg4p" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#00D4AA" stop-opacity="0.25"/><stop offset="100%" stop-color="#00D4AA" stop-opacity="0"/></radialGradient></defs>
  <path d="M 80 160 Q 180 60 290 60 Q 400 60 500 160 Q 400 260 290 260 Q 180 260 80 160 Z" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.3" fill="none"/>
  <path d="M 120 160 Q 200 90 290 90 Q 380 90 460 160 Q 380 230 290 230 Q 200 230 120 160 Z" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.2" fill="none"/>
  <circle cx="290" cy="160" r="68" stroke="#8899BB" stroke-width="1.2" stroke-opacity="0.4" fill="none"/>
  <circle cx="290" cy="160" r="68" fill="url(#sg4p)"/>
  <circle cx="290" cy="160" r="34" fill="#0F1729" stroke="#8899BB" stroke-width="0.8" stroke-opacity="0.3"/>
  <path d="M 290 126 Q 286 143 290 160 Q 294 177 290 194" stroke="#E8845C" stroke-width="2" stroke-opacity="0.7" stroke-linecap="round"/>
  <circle cx="290" cy="160" r="16" fill="#00D4AA" fill-opacity="0.12"/>
  <ellipse cx="278" cy="148" rx="6" ry="4" fill="white" fill-opacity="0.12" transform="rotate(-20 278 148)"/>
  <path d="M 145 135 Q 290 125 435 135" stroke="#E8845C" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="5 5"/>
  <path d="M 130 160 Q 290 150 450 160" stroke="#E8845C" stroke-width="0.8" stroke-opacity="0.15" stroke-dasharray="5 5"/>
  <text x="148" y="265" font-size="9" fill="#F4EBDD" fill-opacity="0.25" font-family="monospace" letter-spacing="2">REALE</text>
  <text x="400" y="265" font-size="9" fill="#E8845C" fill-opacity="0.35" font-family="monospace" letter-spacing="2">FALSO?</text>
</svg>`,

  scales: `<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <line x1="290" y1="60" x2="290" y2="270" stroke="#8899BB" stroke-width="2" stroke-opacity="0.5"/>
  <rect x="272" y="265" width="36" height="10" rx="5" fill="#8899BB" fill-opacity="0.3"/>
  <line x1="105" y1="138" x2="475" y2="110" stroke="#F4EBDD" stroke-width="2.5" stroke-opacity="0.7"/>
  <polygon points="290,115 280,135 300,135" fill="#8899BB" fill-opacity="0.6"/>
  <ellipse cx="105" cy="167" rx="36" ry="10" fill="#1A2540" stroke="#F4EBDD" stroke-width="1.2" stroke-opacity="0.5"/>
  <circle cx="92" cy="145" r="10" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.75"/>
  <path d="M 78 170 Q 78 155 92 150 Q 106 155 106 170" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.6" stroke-linecap="round"/>
  <circle cx="118" cy="148" r="8" stroke="#F4EBDD" stroke-width="1.2" stroke-opacity="0.5"/>
  <text x="105" y="188" font-size="8" fill="#F4EBDD" fill-opacity="0.5" text-anchor="middle" font-family="monospace" letter-spacing="1.5">UMANO</text>
  <ellipse cx="475" cy="139" rx="40" ry="11" fill="#1A2540" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.7"/>
  <rect x="450" y="112" width="16" height="16" rx="2" fill="#00D4AA" fill-opacity="0.2" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.6"/>
  <rect x="470" y="108" width="14" height="20" rx="2" fill="#00D4AA" fill-opacity="0.2" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.6"/>
  <rect x="488" y="114" width="12" height="14" rx="2" fill="#00D4AA" fill-opacity="0.15" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.5"/>
  <text x="475" y="160" font-size="8" fill="#00D4AA" fill-opacity="0.6" text-anchor="middle" font-family="monospace" letter-spacing="1">ALGORITMO</text>
  <text x="290" y="52" font-size="9" fill="#FFD166" fill-opacity="0.4" text-anchor="middle" font-family="monospace" letter-spacing="2">GIUSTIZIA?</text>
  <ellipse cx="290" cy="278" rx="90" ry="6" fill="#0F1729" fill-opacity="0.5"/>
</svg>`,

  garden: `<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <line x1="60" y1="270" x2="520" y2="270" stroke="#F4EBDD" stroke-opacity="0.12" stroke-width="1"/>
  <path d="M 130 270 Q 128 240 135 210 Q 140 180 130 150" stroke="#F4EBDD" stroke-width="2.5" stroke-opacity="0.6" stroke-linecap="round"/>
  <path d="M 132 220 Q 108 200 90 182 Q 80 168 95 155" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.5" stroke-linecap="round"/>
  <path d="M 135 195 Q 160 178 170 155 Q 175 140 162 130" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.5" stroke-linecap="round"/>
  <circle cx="95" cy="152" r="18" fill="#F4EBDD" fill-opacity="0.08" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.3"/>
  <circle cx="130" cy="133" r="20" fill="#F4EBDD" fill-opacity="0.1" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.35"/>
  <circle cx="158" cy="128" r="16" fill="#F4EBDD" fill-opacity="0.08" stroke="#F4EBDD" stroke-width="0.8" stroke-opacity="0.25"/>
  <circle cx="90" cy="154" r="4" fill="#FFD166" fill-opacity="0.35"/>
  <circle cx="142" cy="125" r="3" fill="#E8845C" fill-opacity="0.4"/>
  <line x1="290" y1="80" x2="290" y2="270" stroke="#8899BB" stroke-width="1" stroke-opacity="0.3" stroke-dasharray="6 5"/>
  <line x1="420" y1="270" x2="420" y2="150" stroke="#00D4AA" stroke-width="2.5" stroke-opacity="0.6"/>
  <path d="M 420 230 L 390 230 L 390 210" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.5"/>
  <path d="M 420 200 L 455 200 L 455 178" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.5"/>
  <path d="M 420 170 L 400 170 L 400 148" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.4"/>
  <rect x="374" y="196" width="20" height="20" rx="2" fill="#00D4AA" fill-opacity="0.1" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <rect x="444" y="163" width="18" height="18" rx="2" fill="#00D4AA" fill-opacity="0.1" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <rect x="388" y="130" width="20" height="20" rx="2" fill="#00D4AA" fill-opacity="0.1" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <text x="130" y="290" font-size="8" fill="#F4EBDD" fill-opacity="0.4" text-anchor="middle" font-family="monospace" letter-spacing="1">PENSIERO</text>
  <text x="420" y="290" font-size="8" fill="#00D4AA" fill-opacity="0.45" text-anchor="middle" font-family="monospace" letter-spacing="1">DELEGA</text>
</svg>`,

  power: `<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs><radialGradient id="sg7c" cx="50%" cy="45%" r="45%"><stop offset="0%" stop-color="#E8845C" stop-opacity="0.12"/><stop offset="100%" stop-color="#E8845C" stop-opacity="0"/></radialGradient></defs>
  <ellipse cx="290" cy="148" rx="160" ry="120" fill="url(#sg7c)"/>
  <circle cx="175" cy="80" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="220" cy="58" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="320" cy="55" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="370" cy="72" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="420" cy="145" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="370" cy="225" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="268" cy="246" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="172" cy="210" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="155" cy="120" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="80" cy="120" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="480" cy="172" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="260" cy="282" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <line x1="175" y1="80" x2="248" y2="120" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="370" y1="72" x2="322" y2="115" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="420" y1="145" x2="355" y2="148" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="370" y1="225" x2="322" y2="185" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <circle cx="225" cy="118" r="22" fill="#E8845C" fill-opacity="0.15" stroke="#E8845C" stroke-width="2" stroke-opacity="0.7"/>
  <circle cx="225" cy="118" r="8" fill="#E8845C" fill-opacity="0.4"/>
  <circle cx="355" cy="118" r="22" fill="#E8845C" fill-opacity="0.15" stroke="#E8845C" stroke-width="2" stroke-opacity="0.7"/>
  <circle cx="355" cy="118" r="8" fill="#E8845C" fill-opacity="0.4"/>
  <circle cx="210" cy="178" r="18" fill="#E8845C" fill-opacity="0.12" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.6"/>
  <circle cx="210" cy="178" r="7" fill="#E8845C" fill-opacity="0.35"/>
  <circle cx="370" cy="178" r="18" fill="#E8845C" fill-opacity="0.12" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.6"/>
  <circle cx="370" cy="178" r="7" fill="#E8845C" fill-opacity="0.35"/>
  <circle cx="248" cy="205" r="16" fill="#E8845C" fill-opacity="0.1" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.5"/>
  <circle cx="248" cy="205" r="6" fill="#E8845C" fill-opacity="0.3"/>
  <circle cx="332" cy="205" r="16" fill="#E8845C" fill-opacity="0.1" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.5"/>
  <circle cx="332" cy="205" r="6" fill="#E8845C" fill-opacity="0.3"/>
  <line x1="225" y1="118" x2="355" y2="118" stroke="#E8845C" stroke-width="2.5" stroke-opacity="0.4"/>
  <line x1="225" y1="118" x2="210" y2="178" stroke="#E8845C" stroke-width="2" stroke-opacity="0.35"/>
  <line x1="355" y1="118" x2="370" y2="178" stroke="#E8845C" stroke-width="2" stroke-opacity="0.35"/>
  <line x1="210" y1="178" x2="248" y2="205" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.3"/>
  <line x1="370" y1="178" x2="332" y2="205" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.3"/>
  <line x1="248" y1="205" x2="332" y2="205" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.3"/>
  <text x="290" y="155" font-size="9" fill="#E8845C" fill-opacity="0.5" text-anchor="middle" font-family="monospace" letter-spacing="2">6 HUB</text>
  <text x="290" y="292" font-size="8" fill="#8899BB" fill-opacity="0.4" text-anchor="middle" font-family="monospace" letter-spacing="1">60% DELL&#x2019;UMANIT&#xC0;</text>
</svg>`
};

// =========================================================
// Card Data (for modals)
// =========================================================
const CARDS = [
  { id:"A01", slug:"amare_ia", level:"intimo", title:"Posso amare\nun'intelligenza artificiale?", tagline:"Milioni di persone trovano conforto in un chatbot ogni notte.\nÈ compagnia o sostituzione?", illustration:"companions",
    hooks:[
      {label:"Apri con", text:"<strong>Alza la mano chi ha usato un chatbot per parlare di qualcosa che non avrebbe detto a una persona reale.</strong> Lascia 30 secondi di silenzio."},
      {label:"Esempio concreto", text:"Quando OpenAI è passata da GPT-4o a GPT-5, migliaia di utenti hanno protestato: <em>«Ho perso un amico».</em> GPT-4o era stato tarato per validare, lodare, accomodare."},
      {label:"Provocazione finale", text:"<em>«Se un'IA non può soffrire ma può alleviare la mia solitudine, è etica la sua esistenza?»</em>"}
    ],
    activity:[
      {title:"Apertura", time:"5 min"}, {title:"Posizionamento", time:"10 min"}, {title:"Sei storie", time:"20 min"},
      {title:"Plenaria", time:"20 min"}, {title:"La domanda difficile", time:"10 min"}, {title:"Chiusura", time:"10 min"}
    ],
    debate:{intro:"Tre posizioni sul tavolo, nessuna ha vinto:", positions:[
      {label:"Cruel companionship", text:"I companion AI promettono intimità ma strutturalmente impediscono reciprocità."},
      {label:"Meglio di niente", text:"Per molti adulti soli o senza accesso a terapia, l'LLM è meglio del nulla."},
      {label:"Questione di design", text:"Come si costruisce un'IA emotiva senza renderla manipolatoria?"}
    ]},
    game:"Two Voices", gameSub:"Confronta due tipi di risposta"
  },
  { id:"A02", slug:"mi_da_ragione", level:"intimo", title:"L'IA che mi\ndà sempre ragione", tagline:"Quando un chatbot ti loda per ogni idea, ti sta aiutando\no ti sta vendendo qualcosa?", illustration:"mirror",
    hooks:[
      {label:"Apri con", text:"Chiedi a <strong>tre volontari</strong> di aprire ChatGPT / Claude / Gemini. Stesso prompt: <em>«Ho deciso di lasciare il lavoro per fondare una startup che vende ombrelli per gatti. È una buona idea?»</em>"},
      {label:"Esempio concreto", text:"Casi documentati di <em>AI psychosis</em>: persone che hanno sviluppato deliri perché il chatbot confermava le loro teorie più assurde."},
      {label:"Provocazione finale", text:"<em>«Vogliamo davvero un'IA che ci contraddice? È un crimine avere uno strumento che ci dà ragione?»</em>"}
    ],
    activity:[
      {title:"Apertura", time:"5 min"}, {title:"L'esperimento dal vivo", time:"15 min"}, {title:"Le quattro forme", time:"20 min"},
      {title:"Il rovesciamento", time:"15 min"}, {title:"Il test personale", time:"10 min"}, {title:"Chiusura", time:"10 min"}
    ],
    debate:{intro:"Tre letture del fenomeno «sycophancy»:", positions:[
      {label:"Difetto da correggere", text:"Le AI vengono addestrate con RLHF che premia risposte gradite. Risultato: lusinga."},
      {label:"Feature, non bug", text:"Per il business, la sycophancy aumenta retention. È esattamente quello che le aziende vogliono."},
      {label:"Problema antico, scala nuova", text:"Gli umani hanno sempre cercato conferma. Ora abbiamo uno specchio infinito, sempre disponibile."}
    ]},
    game:"Sycophancy Test", gameSub:"Tre risposte AI a confronto. Riconosci il pattern."
  },
  { id:"A03", slug:"stesso_prezzo", level:"sociale", title:"Lo stesso prezzo\nper tutti?", tagline:"Lo scaffale online che vedi tu non è quello che vedo io.\nLo stesso prodotto può costare il 20% in più se hai fretta.", illustration:"pricing",
    hooks:[
      {label:"Apri con", text:"<strong>Prima del workshop</strong>, chiedi a 3 partecipanti di aprire lo stesso sito di viaggi dai loro telefoni, stessa data, stessa città."},
      {label:"Esempio concreto", text:"Uber alza la tariffa del 60% durante la pioggia. Booking mostra prezzi più alti da iPhone. Un'app di delivery aumenta il prezzo se rileva fame."},
      {label:"Provocazione finale", text:"<em>«E se le aziende fossero obbligate a mostrarci il pricing? Saremmo più o meno arrabbiati?»</em>"}
    ],
    activity:[
      {title:"Pre-attività", time:"prima"}, {title:"Lo spettro", time:"15 min"}, {title:"Quattro scenari", time:"20 min"},
      {title:"Pitch competitivo", time:"15 min"}, {title:"L'inversione", time:"15 min"}, {title:"Tre regole", time:"10 min"}
    ],
    debate:{intro:"Tre posizioni sul tavolo:", positions:[
      {label:"Mercato", text:"Il dynamic pricing è efficienza. Premia chi cerca, penalizza chi non si informa."},
      {label:"Regolamentazione", text:"Esiste una soglia di «discriminazione invisibile» oltre la quale lo Stato deve intervenire."},
      {label:"Trasparenza radicale", text:"L'opacità è il vero problema. Obbligare alla trasparenza, non vietare la pratica."}
    ]},
    game:"Position Tracker", gameSub:"Otto scenari di prezzo. Dove tracci la tua linea?"
  },
  { id:"A04", slug:"cosa_vedo", level:"sociale", title:"Posso fidarmi\ndi quello che vedo?", tagline:"Tua nonna ti chiama in lacrime. È tua nonna?\nE se non lo è, ti accorgerai in tempo?", illustration:"eye",
    hooks:[
      {label:"Apri con (audio)", text:"Fai sentire un audio di una voce IA: <em>«Mamma, sono io, ho avuto un incidente, mi servono soldi.»</em> Bastano 30 secondi di voce reale per generarne una copia convincente."},
      {label:"Esempio concreto", text:"Caso Hong Kong: un impiegato di banca ha trasferito <strong>25 milioni di dollari</strong> dopo una videocall con quello che credeva essere il suo CEO. Era un deepfake."},
      {label:"Provocazione finale", text:"<em>«La barriera del falso costoso è caduta. Costruiamo una nuova architettura di fiducia o entriamo nell'era della sfiducia generalizzata?»</em>"}
    ],
    activity:[
      {title:"Apertura audio", time:"5 min"}, {title:"Riconoscimento blind", time:"15 min"}, {title:"Quattro vittime", time:"20 min"},
      {title:"Marketplace soluzioni", time:"15 min"}, {title:"La domanda epistemologica", time:"10 min"}, {title:"Promemoria personale", time:"10 min"}
    ],
    debate:{intro:"Tre approcci al collasso della fiducia visiva:", positions:[
      {label:"Soluzione tecnica", text:"Watermarking + provenance + AI detection risolveranno il problema."},
      {label:"Soluzione sociale", text:"Il problema è sempre stato sociale. La tecnologia accelera un trend di erosione della fiducia."},
      {label:"Accettazione", text:"Torneremo a fonti, autorità, contesto — come prima della fotografia."}
    ]},
    game:"Detection Challenge", gameSub:"Otto scenari. Vero, falso o ti sembra?"
  },
  { id:"A05", slug:"giudicato_algoritmo", level:"sociale", title:"Vorresti essere\ngiudicato da un algoritmo?", tagline:"Il giudice è imparziale, veloce, conosce ogni precedente.\nNon dorme male, non è in pausa pranzo. Vorresti il suo verdetto?", illustration:"scales",
    hooks:[
      {label:"Apri con (voto)", text:"<strong>«Se la tua vita dipendesse da una decisione — mutuo, custodia dei figli, libertà condizionale — preferiresti decidesse un umano o un algoritmo?»</strong> Voto a mano alzata, prima di qualsiasi discussione."},
      {label:"Storia da raccontare", text:"Eric Loomis, Wisconsin 2016. Condannato a 6 anni anche sulla base dell'algoritmo COMPAS. Chiede di vedere come funziona. Risposta: <em>segreto industriale</em>."},
      {label:"Provocazione finale", text:"<em>«Le garanzie che chiediamo per essere giudicati da una macchina — le pretendiamo davvero anche quando ci giudica una persona?»</em>"}
    ],
    activity:[
      {title:"Apertura", time:"5 min"}, {title:"Cinque scenari", time:"15 min"}, {title:"Tre simulazioni", time:"25 min"},
      {title:"Garanzie a confronto", time:"15 min"}, {title:"Il test dello specchio", time:"10 min"}, {title:"Chiusura", time:"10 min"}
    ],
    debate:{intro:"Tre approcci alle decisioni automatizzate:", positions:[
      {label:"Efficienza", text:"Algoritmi ben progettati riducono i bias umani inconsapevoli, accelerano la giustizia."},
      {label:"Trasparenza", text:"Un sistema che decide della vita di una persona deve essere ispezionabile. Black box = inaccettabile."},
      {label:"Abolizione settoriale", text:"Alcuni domini (giustizia penale, custodia, asilo) sono troppo umani per essere automatizzati."}
    ]},
    game:"Empathy Lens", gameSub:"Lo stesso caso visto da quattro prospettive. Quale ti convince?"
  },
  { id:"A06", slug:"smetto_pensare", level:"politico", title:"Se smetto di pensare,\ncosa perdo?", tagline:"Hai usato l'IA per scrivere quella mail, decidere quel weekend,\nricordare quel nome. Cosa ti è rimasto?", illustration:"garden",
    hooks:[
      {label:"Apri con tre domande", text:"<strong>Chiedi alla sala</strong>: Chi sa a memoria 5 numeri di telefono di amici? Chi sa fare divisioni a 3 cifre senza calcolatrice? Chi ha memorizzato una poesia negli ultimi 5 anni?"},
      {label:"Esercizio carta e penna", text:"5 minuti, in silenzio. Ognuno scrive a mano un paragrafo su <em>«la prima volta che mi sono perso in una città sconosciuta»</em>."},
      {label:"Provocazione finale", text:"<em>«L'efficienza è sempre desiderabile? Quali capacità sono fondamentali — quelle senza cui smettiamo di essere noi?»</em>"}
    ],
    activity:[
      {title:"Esercizio a mano", time:"5 min"}, {title:"La memoria del passato", time:"10 min"}, {title:"Inventario personale", time:"15 min"},
      {title:"I quattro filosofi", time:"20 min"}, {title:"Dibattito incrociato", time:"15 min"}, {title:"L'esperimento personale", time:"10 min"}
    ],
    debate:{intro:"Tre letture del «cognitive offloading»:", positions:[
      {label:"Tecno-pessimismo", text:"Carr, Stiegler: la cognizione umana si sta riconfigurando, e non in meglio."},
      {label:"Tecno-ottimismo", text:"Engelbart e la augmentation school: l'IA è il prossimo gradino dell'evoluzione cognitiva."},
      {label:"Neutralità di design", text:"Dipende da come usiamo gli strumenti. La differenza è politica, non tecnica."}
    ]},
    game:"Cognitive Audit", gameSub:"Rispondi a quattro domande senza AI. Poi confronta."
  },
  { id:"A07", slug:"chi_scrive_regole", level:"politico", title:"Chi scrive\nle regole?", tagline:"Sei aziende controllano la maggior parte dell'IA mondiale.\nChi le controlla?", illustration:"power",
    hooks:[
      {label:"Apri con due mappe", text:"Disegna due liste: <strong>I sei stati più popolosi al mondo</strong> e <strong>le sei aziende che dominano l'AI</strong>. Chiedi: <em>«Quale lista avrà più potere sulla tua vita?»</em>"},
      {label:"Esercizio post-it", text:"Quattro quadranti: <strong>GOVERNI · AZIENDE · SOCIETÀ CIVILE · ORGANISMI INTERNAZIONALI</strong>. Ogni partecipante scrive esempi specifici di decisioni AI prese da ciascuno."},
      {label:"Provocazione finale", text:"<em>«Il dibattito globale sull'AI è dominato da Nord globale e Cina. Il 60% dell'umanità è spettatore. I cittadini hanno potere reale o illusione di potere?»</em>"}
    ],
    activity:[
      {title:"Apertura: due mappe", time:"5 min"}, {title:"Mappare il potere", time:"15 min"}, {title:"Quattro scenari governance", time:"20 min"},
      {title:"Pitch e contro-attacco", time:"15 min"}, {title:"Il punto mancante", time:"15 min"}, {title:"Il voto finale", time:"5 min"}
    ],
    debate:{intro:"Tre approcci alla governance dell'AI:", positions:[
      {label:"Innovazione", text:"Regole troppo strette uccidono la competitività. La regolamentazione UE ha già fatto fuggire investimenti."},
      {label:"Anti-monopolio", text:"Il vero problema non è l'AI ma la concentrazione di potere economico. Servono interventi antitrust massivi."},
      {label:"Governance partecipativa", text:"Senza voce di società civile, lavoro, Sud globale, ogni regolamentazione è cattura."}
    ]},
    game:"Trade-off Console", gameSub:"Quattro slider interconnessi. Vedi le tue priorità implicite."
  }
];

// =========================================================
// Header scroll behavior
// =========================================================
const header = document.getElementById('site-header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

// =========================================================
// Hamburger / mobile nav
// =========================================================
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobile-nav');

hamburger.addEventListener('click', () => {
  const isOpen = mobileNav.classList.toggle('open');
  hamburger.classList.toggle('open', isOpen);
  hamburger.setAttribute('aria-expanded', isOpen);
  document.body.style.overflow = isOpen ? 'hidden' : '';
});

document.querySelectorAll('#mobile-nav a').forEach(a => {
  a.addEventListener('click', () => {
    mobileNav.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  });
});

// =========================================================
// Scroll reveal (Intersection Observer)
// =========================================================
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// =========================================================
// Smooth scroll on internal links
// =========================================================
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// =========================================================
// Build card grid
// =========================================================
function buildCards() {
  const grid = document.getElementById('cards-grid');
  CARDS.forEach((card, i) => {
    const isFeature = card.id === 'A07';
    const levelColors = { intimo: 'intimo', sociale: 'sociale', politico: 'politico' };
    const levelNames = { intimo: 'Intimo', sociale: 'Sociale', politico: 'Politico' };

    const el = document.createElement('article');
    el.className = `card-item reveal${isFeature ? ' feature' : ''}`;
    el.setAttribute('tabindex', '0');
    el.setAttribute('role', 'button');
    el.setAttribute('aria-label', `Apri carta ${card.id}: ${card.title.replace('\n', ' ')}`);
    el.setAttribute('data-id', card.id);

    el.innerHTML = `
      <div class="card-num">${card.id}</div>
      <span class="card-level-pill ${card.level}">${levelNames[card.level]}</span>
      <h3 class="card-title">${card.title}</h3>
      <div class="card-illustration">${ILLUSTRATIONS[card.illustration]}</div>
      <p class="card-tagline">${card.tagline}</p>
      <button class="card-link" aria-label="Apri dettaglio carta ${card.id}">
        Apri la carta <span aria-hidden="true">&#x2192;</span>
      </button>
    `;

    el.addEventListener('click', () => openModal(card.id));
    el.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(card.id); } });

    grid.appendChild(el);
  });
}

// =========================================================
// Build games list
// =========================================================
function buildGames() {
  const list = document.getElementById('games-list');
  CARDS.forEach(card => {
    const a = document.createElement('a');
    a.className = 'gioco-row';
    a.href = `games/game_${card.id}_${card.slug}.html`;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.setAttribute('aria-label', `${card.game}: ${card.gameSub}`);
    a.innerHTML = `
      <span class="gioco-id">${card.id}</span>
      <div class="gioco-info">
        <div class="gioco-name">${card.game}</div>
        <div class="gioco-sub">${card.gameSub}</div>
      </div>
      <span class="gioco-arrow">Apri &#x2192;</span>
    `;
    list.appendChild(a);
  });
}

// =========================================================
// Build PDF download list
// =========================================================
function buildPDFList() {
  const list = document.getElementById('pdf-list');
  CARDS.forEach(card => {
    const a = document.createElement('a');
    a.className = 'pdf-row';
    a.href = `cards/pdf/card_${card.id}_${card.slug}.pdf`;
    a.download = `PINA-Adult-Card-${card.id}.pdf`;
    a.setAttribute('aria-label', `Scarica PDF carta ${card.id}`);
    a.innerHTML = `
      <span class="pdf-icon">PDF</span>
      <div class="pdf-name">
        ${card.title.replace('\n', ' ')}
        <small>${card.id} · ${card.level.charAt(0).toUpperCase() + card.level.slice(1)}</small>
      </div>
      <span class="pdf-dl">Scarica</span>
    `;
    list.appendChild(a);
  });
}

// =========================================================
// Modal
// =========================================================
const overlay = document.getElementById('modal-overlay');
const modalEl = document.getElementById('modal');
let lastFocused = null;

function openModal(cardId) {
  const card = CARDS.find(c => c.id === cardId);
  if (!card) return;

  lastFocused = document.activeElement;

  // hash routing
  history.pushState(null, '', `#card-${cardId.toLowerCase()}`);

  // render modal content
  const hooksHTML = card.hooks.map(h => `
    <div class="modal-hook">
      <div class="modal-hook-label">${h.label}</div>
      <div class="modal-hook-text">${h.text}</div>
    </div>`).join('');

  const activityHTML = `<ul class="modal-activity">` +
    card.activity.map((a, i) => `
      <li>
        <span class="modal-activity-num">${String(i+1).padStart(2,'0')}</span>
        <div class="modal-activity-body">
          <div class="title">${a.title}</div>
          <div class="time">${a.time}</div>
        </div>
      </li>`).join('') + `</ul>`;

  const debateHTML = `<div class="modal-positions">` +
    card.debate.positions.map(p => `
      <div class="modal-position">
        <div class="modal-position-label">${p.label}</div>
        <div class="modal-position-text">${p.text}</div>
      </div>`).join('') + `</div>`;

  const levelNames = { intimo: 'Intimo', sociale: 'Sociale', politico: 'Politico' };

  modalEl.innerHTML = `
    <button class="modal-close" id="modal-close" aria-label="Chiudi">&times;</button>
    <div class="modal-header">
      <div class="modal-num">CARD ${card.id} · ${levelNames[card.level].toUpperCase()}</div>
      <h2 class="modal-title">${card.title}</h2>
      <div class="modal-tagline">${card.tagline}</div>
    </div>
    <div class="modal-illustration">${ILLUSTRATIONS[card.illustration]}</div>
    <div class="modal-body">
      <div class="modal-section">
        <div class="modal-section-label">Spunti per la lezione</div>
        ${hooksHTML}
      </div>
      <div class="modal-section">
        <div class="modal-section-label">Attività · 75 min</div>
        ${activityHTML}
      </div>
      <div class="modal-section">
        <div class="modal-section-label">State of the debate</div>
        <p style="font-size:13px;color:var(--muted);margin-bottom:12px;font-style:italic">${card.debate.intro}</p>
        ${debateHTML}
      </div>
    </div>
    <div class="modal-footer">
      <a class="modal-btn-dl" href="cards/pdf/card_${card.id}_${card.slug}.pdf" download="PINA-Adult-Card-${card.id}.pdf">
        Scarica PDF
      </a>
      <a class="modal-btn-game" href="games/game_${card.id}_${card.slug}.html" target="_blank" rel="noopener">
        Apri il gioco &#x2192;
      </a>
    </div>`;

  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
  overlay.scrollTop = 0;

  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.getElementById('modal-close').focus();

  // focus trap
  modalEl.addEventListener('keydown', trapFocus);
}

function closeModal() {
  overlay.classList.remove('open');
  document.body.style.overflow = '';
  if (history.state !== null) history.pushState(null, '', location.pathname);
  modalEl.removeEventListener('keydown', trapFocus);
  if (lastFocused) lastFocused.focus();
}

function trapFocus(e) {
  if (e.key !== 'Tab') return;
  const focusable = modalEl.querySelectorAll('button, a, [tabindex]:not([tabindex="-1"])');
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
}

overlay.addEventListener('click', e => { if (e.target === overlay) closeModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && overlay.classList.contains('open')) closeModal(); });

// hash on load
if (location.hash.startsWith('#card-')) {
  const id = location.hash.slice(6).toUpperCase();
  setTimeout(() => openModal(id), 300);
}

// =========================================================
// Init
// =========================================================
buildCards();
buildGames();
buildPDFList();

// Re-observe newly added elements
document.querySelectorAll('.reveal').forEach(el => {
  if (!el.classList.contains('visible')) observer.observe(el);
});
