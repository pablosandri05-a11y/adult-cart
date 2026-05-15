# -*- coding: utf-8 -*-
"""Generatore HTML delle 7 carte PINA Adult Edition con SVG illustrazioni inline."""

import os, sys, base64, urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from cards_data import CARDS, GAMES_BASE_URL

ROOT = Path(__file__).parent.parent
OUTPUT_DIR = ROOT / "cards" / "html"
QR_DIR = ROOT / "qr"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# SVG Illustrations (built-in, one per illustration_type)
# -----------------------------------------------------------------------------
ILLUSTRATIONS = {

    "companions": """<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs>
    <radialGradient id="g1a" cx="35%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F4EBDD" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#F4EBDD" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g1b" cx="65%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00D4AA" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#00D4AA" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- ambient glows -->
  <ellipse cx="185" cy="160" rx="130" ry="110" fill="url(#g1a)"/>
  <ellipse cx="395" cy="160" rx="130" ry="110" fill="url(#g1b)"/>
  <!-- connecting arc -->
  <path d="M 230 110 Q 290 60 350 110" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="6 4"/>
  <path d="M 230 210 Q 290 260 350 210" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="6 4"/>
  <path d="M 240 160 L 340 160" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.2"/>
  <!-- human figure — left -->
  <circle cx="185" cy="118" r="28" stroke="#F4EBDD" stroke-width="2" stroke-opacity="0.85"/>
  <path d="M 145 230 Q 145 185 185 178 Q 225 185 225 230" stroke="#F4EBDD" stroke-width="2" stroke-opacity="0.7" stroke-linecap="round"/>
  <circle cx="185" cy="118" r="8" fill="#F4EBDD" fill-opacity="0.25"/>
  <!-- pulse rings around human -->
  <circle cx="185" cy="160" r="55" stroke="#F4EBDD" stroke-width="0.8" stroke-opacity="0.15" stroke-dasharray="4 6"/>
  <circle cx="185" cy="160" r="80" stroke="#F4EBDD" stroke-width="0.6" stroke-opacity="0.08" stroke-dasharray="3 8"/>
  <!-- digital figure — right (geometric) -->
  <rect x="365" y="88" width="60" height="60" rx="6" stroke="#00D4AA" stroke-width="2" stroke-opacity="0.85"/>
  <line x1="375" y1="108" x2="415" y2="108" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.6"/>
  <line x1="375" y1="118" x2="415" y2="118" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="375" y1="128" x2="400" y2="128" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <circle cx="395" cy="103" r="6" fill="#00D4AA" fill-opacity="0.3"/>
  <path d="M 355 185 L 355 230 L 435 230 L 435 185" stroke="#00D4AA" stroke-width="2" stroke-opacity="0.7" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- pulse rings around digital -->
  <circle cx="395" cy="160" r="55" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.15" stroke-dasharray="4 6"/>
  <circle cx="395" cy="160" r="80" stroke="#00D4AA" stroke-width="0.6" stroke-opacity="0.08" stroke-dasharray="3 8"/>
  <!-- central connection node -->
  <circle cx="290" cy="160" r="10" fill="#E8845C" fill-opacity="0.25" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.6"/>
  <circle cx="290" cy="160" r="4" fill="#E8845C" fill-opacity="0.7"/>
  <line x1="240" y1="160" x2="280" y2="160" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.5"/>
  <line x1="300" y1="160" x2="340" y2="160" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.5"/>
  <!-- question marks floating -->
  <text x="282" y="84" font-size="18" fill="#FFD166" fill-opacity="0.35" font-family="serif" font-style="italic">?</text>
  <text x="295" y="252" font-size="14" fill="#FFD166" fill-opacity="0.25" font-family="serif" font-style="italic">?</text>
</svg>""",

    "mirror": """<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs>
    <linearGradient id="g2m" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1A2540"/>
      <stop offset="50%" stop-color="#243154"/>
      <stop offset="100%" stop-color="#1A2540"/>
    </linearGradient>
  </defs>
  <!-- mirror frame -->
  <ellipse cx="290" cy="158" rx="72" ry="100" fill="#1A2540" stroke="#8899BB" stroke-width="2" stroke-opacity="0.6"/>
  <ellipse cx="290" cy="158" rx="64" ry="92" fill="#243154" stroke="#8899BB" stroke-width="0.8" stroke-opacity="0.3"/>
  <!-- mirror reflection plane -->
  <ellipse cx="290" cy="158" rx="58" ry="86" fill="#0F1729" fill-opacity="0.5"/>
  <!-- reflection highlight -->
  <ellipse cx="272" cy="110" rx="12" ry="28" fill="white" fill-opacity="0.04"/>
  <!-- person left side (original) -->
  <circle cx="145" cy="120" r="22" stroke="#F4EBDD" stroke-width="1.8" stroke-opacity="0.8"/>
  <circle cx="145" cy="120" r="7" fill="#F4EBDD" fill-opacity="0.2"/>
  <path d="M 112 220 Q 112 178 145 172 Q 178 178 178 220" stroke="#F4EBDD" stroke-width="1.8" stroke-opacity="0.65" stroke-linecap="round"/>
  <!-- thought bubble from person to mirror -->
  <circle cx="185" cy="140" r="4" fill="#F4EBDD" fill-opacity="0.3"/>
  <circle cx="205" cy="133" r="3" fill="#F4EBDD" fill-opacity="0.2"/>
  <circle cx="222" cy="128" r="2" fill="#F4EBDD" fill-opacity="0.15"/>
  <!-- inside mirror: reflected self with check marks -->
  <circle cx="290" cy="118" r="16" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.7"/>
  <path d="M 268 188 Q 268 162 290 158 Q 312 162 312 188" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.6" stroke-linecap="round"/>
  <!-- checkmarks floating around reflection -->
  <text x="302" y="100" font-size="13" fill="#FFD166" fill-opacity="0.8" font-family="sans-serif">✓</text>
  <text x="266" y="102" font-size="10" fill="#FFD166" fill-opacity="0.5" font-family="sans-serif">✓</text>
  <text x="308" y="140" font-size="10" fill="#00D4AA" fill-opacity="0.6" font-family="sans-serif">✓</text>
  <text x="264" y="140" font-size="8" fill="#00D4AA" fill-opacity="0.4" font-family="sans-serif">✓</text>
  <!-- "great idea!" label in mirror -->
  <rect x="256" y="196" width="68" height="18" rx="4" fill="#00D4AA" fill-opacity="0.15" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.4"/>
  <text x="290" y="209" font-size="7.5" fill="#00D4AA" fill-opacity="0.8" font-family="monospace" text-anchor="middle" letter-spacing="1">OTTIMA IDEA!</text>
  <!-- right side: sycophancy signals -->
  <circle cx="430" cy="100" r="18" fill="#E8845C" fill-opacity="0.12" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.5"/>
  <text x="430" y="106" font-size="14" fill="#E8845C" fill-opacity="0.7" text-anchor="middle" font-family="sans-serif">★</text>
  <circle cx="468" cy="148" r="14" fill="#FFD166" fill-opacity="0.1" stroke="#FFD166" stroke-width="1" stroke-opacity="0.4"/>
  <text x="468" y="154" font-size="11" fill="#FFD166" fill-opacity="0.6" text-anchor="middle" font-family="sans-serif">★</text>
  <circle cx="435" cy="190" r="12" fill="#E8845C" fill-opacity="0.1" stroke="#E8845C" stroke-width="1" stroke-opacity="0.3"/>
  <text x="435" y="196" font-size="10" fill="#E8845C" fill-opacity="0.5" text-anchor="middle" font-family="sans-serif">★</text>
  <!-- mirror stand -->
  <rect x="278" y="258" width="24" height="12" rx="2" fill="#8899BB" fill-opacity="0.3"/>
  <rect x="265" y="268" width="50" height="6" rx="3" fill="#8899BB" fill-opacity="0.2"/>
</svg>""",

    "pricing": """<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <!-- grid backdrop -->
  <line x1="80" y1="270" x2="500" y2="270" stroke="#F4EBDD" stroke-opacity="0.12" stroke-width="1"/>
  <line x1="80" y1="230" x2="500" y2="230" stroke="#F4EBDD" stroke-opacity="0.07" stroke-width="0.8" stroke-dasharray="4 4"/>
  <line x1="80" y1="190" x2="500" y2="190" stroke="#F4EBDD" stroke-opacity="0.07" stroke-width="0.8" stroke-dasharray="4 4"/>
  <line x1="80" y1="150" x2="500" y2="150" stroke="#F4EBDD" stroke-opacity="0.07" stroke-width="0.8" stroke-dasharray="4 4"/>
  <!-- Person A — smartphone icon + bar -->
  <rect x="80" y="88" width="36" height="52" rx="6" stroke="#8899BB" stroke-width="1.5" stroke-opacity="0.6"/>
  <rect x="86" y="95" width="24" height="32" rx="2" fill="#8899BB" fill-opacity="0.12"/>
  <circle cx="98" cy="132" r="2.5" fill="#8899BB" fill-opacity="0.5"/>
  <rect x="78" y="180" width="40" height="90" rx="4" fill="#8899BB" fill-opacity="0.25" stroke="#8899BB" stroke-width="1" stroke-opacity="0.3"/>
  <!-- price tag A -->
  <rect x="72" y="148" width="52" height="26" rx="5" fill="#1A2540" stroke="#8899BB" stroke-width="1" stroke-opacity="0.5"/>
  <circle cx="88" cy="161" r="3" fill="#8899BB" fill-opacity="0.6"/>
  <text x="115" y="165" font-size="11" fill="#F4EBDD" fill-opacity="0.6" text-anchor="middle" font-family="monospace" font-weight="bold">€10</text>
  <!-- Person B — laptop icon + bar -->
  <rect x="200" y="90" width="50" height="38" rx="4" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.55"/>
  <rect x="207" y="97" width="36" height="24" rx="2" fill="#F4EBDD" fill-opacity="0.08"/>
  <path d="M 188 128 L 262 128 L 262 132 L 188 132 Z" fill="#F4EBDD" fill-opacity="0.15"/>
  <rect x="196" y="160" width="58" height="110" rx="4" fill="#F4EBDD" fill-opacity="0.2" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.3"/>
  <!-- price tag B -->
  <rect x="190" y="136" width="70" height="26" rx="5" fill="#1A2540" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.4"/>
  <circle cx="205" cy="149" r="3" fill="#F4EBDD" fill-opacity="0.5"/>
  <text x="232" y="153" font-size="11" fill="#F4EBDD" fill-opacity="0.65" text-anchor="middle" font-family="monospace" font-weight="bold">€12</text>
  <!-- Person C — iPhone icon + bar (taller = premium) -->
  <rect x="352" y="85" width="32" height="56" rx="8" stroke="#00D4AA" stroke-width="2" stroke-opacity="0.8"/>
  <rect x="358" y="92" width="20" height="34" rx="2" fill="#00D4AA" fill-opacity="0.1"/>
  <rect x="362" y="88" width="12" height="2.5" rx="1" fill="#00D4AA" fill-opacity="0.5"/>
  <circle cx="368" cy="133" r="3" fill="#00D4AA" fill-opacity="0.6"/>
  <rect x="348" y="148" width="40" height="122" rx="4" fill="#00D4AA" fill-opacity="0.2" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.4"/>
  <!-- price tag C — higher price, copper color -->
  <rect x="338" y="118" width="60" height="26" rx="5" fill="#1A2540" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.7"/>
  <circle cx="352" cy="131" r="3" fill="#E8845C" fill-opacity="0.7"/>
  <text x="375" y="135" font-size="11" fill="#E8845C" fill-opacity="0.9" text-anchor="middle" font-family="monospace" font-weight="bold">€15</text>
  <!-- algorithm signal waves -->
  <path d="M 460 130 Q 470 110 480 130 Q 490 150 500 130" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.4" stroke-linecap="round"/>
  <path d="M 455 130 Q 468 100 480 130 Q 492 160 505 130" stroke="#E8845C" stroke-width="1" stroke-opacity="0.25" stroke-linecap="round"/>
  <text x="480" y="175" font-size="8" fill="#E8845C" fill-opacity="0.5" text-anchor="middle" font-family="monospace" letter-spacing="1">ALGO</text>
  <!-- same product icon (shopping bag) at top center -->
  <path d="M 270 50 L 310 50 L 318 80 L 262 80 Z" stroke="#FFD166" stroke-width="1.5" stroke-opacity="0.6" fill="none"/>
  <path d="M 278 50 Q 278 38 290 38 Q 302 38 302 50" stroke="#FFD166" stroke-width="1.5" stroke-opacity="0.6"/>
  <text x="290" y="70" font-size="8" fill="#FFD166" fill-opacity="0.5" text-anchor="middle" font-family="monospace">= ?</text>
  <!-- connecting dotted lines from product to bars -->
  <line x1="270" y1="78" x2="118" y2="155" stroke="#FFD166" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="3 4"/>
  <line x1="290" y1="80" x2="225" y2="142" stroke="#FFD166" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="3 4"/>
  <line x1="310" y1="78" x2="366" y2="122" stroke="#FFD166" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="3 4"/>
</svg>""",

    "eye": """<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs>
    <radialGradient id="g4p" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00D4AA" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="#00D4AA" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#00D4AA" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- outer eye shape (very large) -->
  <path d="M 80 160 Q 180 60 290 60 Q 400 60 500 160 Q 400 260 290 260 Q 180 260 80 160 Z"
        stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.3" fill="none"/>
  <!-- second layer -->
  <path d="M 120 160 Q 200 90 290 90 Q 380 90 460 160 Q 380 230 290 230 Q 200 230 120 160 Z"
        stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.2" fill="none"/>
  <!-- iris -->
  <circle cx="290" cy="160" r="68" stroke="#8899BB" stroke-width="1.2" stroke-opacity="0.4" fill="none"/>
  <circle cx="290" cy="160" r="68" fill="url(#g4p)"/>
  <!-- iris detail lines (radial) -->
  <line x1="290" y1="92" x2="290" y2="107" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="290" y1="213" x2="290" y2="228" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="222" y1="160" x2="237" y2="160" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="343" y1="160" x2="358" y2="160" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <line x1="241" y1="111" x2="251" y2="121" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.3"/>
  <line x1="329" y1="199" x2="339" y2="209" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.3"/>
  <line x1="339" y1="111" x2="329" y2="121" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.3"/>
  <line x1="241" y1="199" x2="251" y2="209" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.3"/>
  <!-- pupil — fragmented (split vertically to suggest doubt) -->
  <circle cx="290" cy="160" r="34" fill="#0F1729" stroke="#8899BB" stroke-width="0.8" stroke-opacity="0.3"/>
  <!-- crack / split in pupil -->
  <path d="M 290 126 Q 286 143 290 160 Q 294 177 290 194" stroke="#E8845C" stroke-width="2" stroke-opacity="0.7" stroke-linecap="round"/>
  <!-- inner glow -->
  <circle cx="290" cy="160" r="16" fill="#00D4AA" fill-opacity="0.12"/>
  <!-- highlight in pupil -->
  <ellipse cx="278" cy="148" rx="6" ry="4" fill="white" fill-opacity="0.12" transform="rotate(-20 278 148)"/>
  <!-- question / doubt marks in corners -->
  <text x="110" y="120" font-size="22" fill="#F4EBDD" fill-opacity="0.12" font-family="serif" font-style="italic">?</text>
  <text x="450" y="210" font-size="18" fill="#F4EBDD" fill-opacity="0.10" font-family="serif" font-style="italic">?</text>
  <!-- filter layers (horizontal dashed bands across eye) -->
  <path d="M 145 135 Q 290 125 435 135" stroke="#E8845C" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="5 5"/>
  <path d="M 130 160 Q 290 150 450 160" stroke="#E8845C" stroke-width="0.8" stroke-opacity="0.15" stroke-dasharray="5 5"/>
  <path d="M 145 185 Q 290 195 435 185" stroke="#E8845C" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="5 5"/>
  <!-- REAL / FAKE labels faint -->
  <text x="148" y="265" font-size="9" fill="#F4EBDD" fill-opacity="0.25" font-family="monospace" letter-spacing="2">REALE</text>
  <text x="400" y="265" font-size="9" fill="#E8845C" fill-opacity="0.35" font-family="monospace" letter-spacing="2">FALSO?</text>
</svg>""",

    "scales": """<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <!-- central pillar -->
  <line x1="290" y1="60" x2="290" y2="270" stroke="#8899BB" stroke-width="2" stroke-opacity="0.5"/>
  <rect x="272" y="265" width="36" height="10" rx="5" fill="#8899BB" fill-opacity="0.3"/>
  <!-- beam (tilted slightly - algorithm side heavier) -->
  <line x1="105" y1="138" x2="475" y2="110" stroke="#F4EBDD" stroke-width="2.5" stroke-opacity="0.7"/>
  <!-- fulcrum -->
  <polygon points="290,115 280,135 300,135" fill="#8899BB" fill-opacity="0.6"/>
  <!-- left pan: human (lighter side, higher) -->
  <path d="M 105 138 Q 105 155 88 165 L 122 165 Q 105 155 105 138" stroke="#F4EBDD" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <ellipse cx="105" cy="167" rx="36" ry="10" fill="#1A2540" stroke="#F4EBDD" stroke-width="1.2" stroke-opacity="0.5"/>
  <!-- human figure in left pan -->
  <circle cx="92" cy="145" r="10" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.75"/>
  <path d="M 78 170 Q 78 155 92 150 Q 106 155 106 170" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.6" stroke-linecap="round"/>
  <circle cx="118" cy="148" r="8" stroke="#F4EBDD" stroke-width="1.2" stroke-opacity="0.5"/>
  <path d="M 107 170 Q 107 157 118 153 Q 129 157 129 170" stroke="#F4EBDD" stroke-width="1.2" stroke-opacity="0.5" stroke-linecap="round"/>
  <!-- "UMANO" label -->
  <text x="105" y="188" font-size="8" fill="#F4EBDD" fill-opacity="0.5" text-anchor="middle" font-family="monospace" letter-spacing="1.5">UMANO</text>
  <!-- right pan: data/algorithm (heavier, lower) -->
  <path d="M 475 110 Q 475 127 458 137 L 492 137 Q 475 127 475 110" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <ellipse cx="475" cy="139" rx="40" ry="11" fill="#1A2540" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.7"/>
  <!-- data cubes in right pan -->
  <rect x="450" y="112" width="16" height="16" rx="2" fill="#00D4AA" fill-opacity="0.2" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.6"/>
  <rect x="470" y="108" width="14" height="20" rx="2" fill="#00D4AA" fill-opacity="0.2" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.6"/>
  <rect x="488" y="114" width="12" height="14" rx="2" fill="#00D4AA" fill-opacity="0.15" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.5"/>
  <!-- data lines in cubes -->
  <line x1="453" y1="118" x2="463" y2="118" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.8"/>
  <line x1="453" y1="122" x2="460" y2="122" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.5"/>
  <line x1="473" y1="114" x2="481" y2="114" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.8"/>
  <line x1="473" y1="118" x2="481" y2="118" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.5"/>
  <line x1="473" y1="122" x2="478" y2="122" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.5"/>
  <!-- "ALGORITMO" label -->
  <text x="475" y="160" font-size="8" fill="#00D4AA" fill-opacity="0.6" text-anchor="middle" font-family="monospace" letter-spacing="1">ALGORITMO</text>
  <!-- weight arrows showing imbalance -->
  <path d="M 475 95 L 475 108" stroke="#E8845C" stroke-width="2" stroke-opacity="0.5" marker-end="url(#arrowDown)"/>
  <defs>
    <marker id="arrowDown" markerWidth="6" markerHeight="6" refX="3" refY="6" orient="auto">
      <path d="M 0 0 L 3 6 L 6 0" stroke="#E8845C" stroke-width="1" fill="none"/>
    </marker>
  </defs>
  <!-- fairness question in center -->
  <text x="290" y="52" font-size="9" fill="#FFD166" fill-opacity="0.4" text-anchor="middle" font-family="monospace" letter-spacing="2">GIUSTIZIA?</text>
  <!-- ground shadow -->
  <ellipse cx="290" cy="278" rx="90" ry="6" fill="#0F1729" fill-opacity="0.5"/>
</svg>""",

    "garden": """<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <!-- ground line -->
  <line x1="60" y1="270" x2="520" y2="270" stroke="#F4EBDD" stroke-opacity="0.12" stroke-width="1"/>
  <!-- left side: organic human thought (free-growing) -->
  <!-- trunk -->
  <path d="M 130 270 Q 128 240 135 210 Q 140 180 130 150" stroke="#F4EBDD" stroke-width="2.5" stroke-opacity="0.6" stroke-linecap="round"/>
  <!-- organic branches -->
  <path d="M 132 220 Q 108 200 90 182 Q 80 168 95 155" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.5" stroke-linecap="round"/>
  <path d="M 135 195 Q 160 178 170 155 Q 175 140 162 130" stroke="#F4EBDD" stroke-width="1.5" stroke-opacity="0.5" stroke-linecap="round"/>
  <path d="M 133 240 Q 115 235 100 245" stroke="#F4EBDD" stroke-width="1.2" stroke-opacity="0.4" stroke-linecap="round"/>
  <!-- organic leaves (circles, irregular placement) -->
  <circle cx="95" cy="152" r="18" fill="#F4EBDD" fill-opacity="0.08" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.3"/>
  <circle cx="112" cy="140" r="14" fill="#F4EBDD" fill-opacity="0.07" stroke="#F4EBDD" stroke-width="0.8" stroke-opacity="0.25"/>
  <circle cx="130" cy="133" r="20" fill="#F4EBDD" fill-opacity="0.1" stroke="#F4EBDD" stroke-width="1" stroke-opacity="0.35"/>
  <circle cx="158" cy="128" r="16" fill="#F4EBDD" fill-opacity="0.08" stroke="#F4EBDD" stroke-width="0.8" stroke-opacity="0.25"/>
  <circle cx="165" cy="152" r="12" fill="#F4EBDD" fill-opacity="0.06" stroke="#F4EBDD" stroke-width="0.8" stroke-opacity="0.2"/>
  <circle cx="80" cy="168" r="12" fill="#F4EBDD" fill-opacity="0.06" stroke="#F4EBDD" stroke-width="0.8" stroke-opacity="0.2"/>
  <!-- small flowers -->
  <circle cx="90" cy="154" r="4" fill="#FFD166" fill-opacity="0.35"/>
  <circle cx="142" cy="125" r="3" fill="#E8845C" fill-opacity="0.4"/>
  <circle cx="168" cy="130" r="3.5" fill="#FFD166" fill-opacity="0.3"/>
  <!-- "PENSIERO UMANO" label -->
  <text x="130" y="290" font-size="8" fill="#F4EBDD" fill-opacity="0.4" text-anchor="middle" font-family="monospace" letter-spacing="1">PENSIERO</text>
  <!-- divider line (center) -->
  <line x1="290" y1="80" x2="290" y2="270" stroke="#8899BB" stroke-width="1" stroke-opacity="0.3" stroke-dasharray="6 5"/>
  <text x="290" y="75" font-size="8" fill="#8899BB" fill-opacity="0.4" text-anchor="middle" font-family="monospace" letter-spacing="1">AI</text>
  <!-- right side: geometric, pruned by algorithm -->
  <!-- geometric trunk (perfectly straight) -->
  <line x1="420" y1="270" x2="420" y2="150" stroke="#00D4AA" stroke-width="2.5" stroke-opacity="0.6"/>
  <!-- geometric branches (right angles) -->
  <path d="M 420 230 L 390 230 L 390 210" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.5"/>
  <path d="M 420 200 L 455 200 L 455 178" stroke="#00D4AA" stroke-width="1.5" stroke-opacity="0.5"/>
  <path d="M 420 170 L 400 170 L 400 148" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.4"/>
  <path d="M 420 160 L 445 160 L 445 140" stroke="#00D4AA" stroke-width="1.2" stroke-opacity="0.4"/>
  <!-- geometric "leaves" (perfect squares/diamonds) -->
  <rect x="374" y="196" width="20" height="20" rx="2" fill="#00D4AA" fill-opacity="0.1" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <rect x="444" y="163" width="18" height="18" rx="2" fill="#00D4AA" fill-opacity="0.1" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <rect x="388" y="130" width="20" height="20" rx="2" fill="#00D4AA" fill-opacity="0.1" stroke="#00D4AA" stroke-width="1" stroke-opacity="0.4"/>
  <rect x="433" y="122" width="16" height="16" rx="2" fill="#00D4AA" fill-opacity="0.08" stroke="#00D4AA" stroke-width="0.8" stroke-opacity="0.35"/>
  <!-- efficiency metrics on geometric side -->
  <text x="480" y="200" font-size="8" fill="#00D4AA" fill-opacity="0.4" font-family="monospace">98%</text>
  <text x="480" y="212" font-size="7" fill="#00D4AA" fill-opacity="0.3" font-family="monospace">OPT.</text>
  <!-- "DELEGA ALL'IA" label -->
  <text x="420" y="290" font-size="8" fill="#00D4AA" fill-opacity="0.45" text-anchor="middle" font-family="monospace" letter-spacing="1">DELEGA</text>
  <!-- pruning scissors hint (center-ish, small) -->
  <text x="283" y="200" font-size="16" fill="#E8845C" fill-opacity="0.2" font-family="sans-serif">✂</text>
</svg>""",

    "power": """<svg viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs>
    <radialGradient id="g7c" cx="50%" cy="45%" r="45%">
      <stop offset="0%" stop-color="#E8845C" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#E8845C" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- central power glow -->
  <ellipse cx="290" cy="148" rx="160" ry="120" fill="url(#g7c)"/>
  <!-- peripheral small nodes (the "60% of humanity" — many, faint, scattered) -->
  <!-- ring 1: inner periphery -->
  <circle cx="175" cy="80" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="220" cy="58" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="270" cy="52" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="320" cy="55" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="370" cy="72" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="405" cy="95" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="420" cy="145" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="405" cy="195" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="370" cy="225" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="320" cy="242" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="268" cy="246" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="216" cy="236" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="172" cy="210" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="152" cy="170" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <circle cx="155" cy="120" r="4" fill="#8899BB" fill-opacity="0.3"/>
  <!-- ring 2: outer periphery (tiny) -->
  <circle cx="110" cy="75" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="80" cy="120" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="75" cy="175" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="95" cy="225" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="135" cy="260" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="200" cy="278" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="260" cy="282" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="330" cy="278" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="395" cy="258" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="448" cy="222" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="480" cy="172" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="478" cy="115" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="450" cy="68" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="400" cy="40" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="336" cy="28" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="268" cy="25" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="200" cy="32" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <circle cx="140" cy="48" r="2.5" fill="#8899BB" fill-opacity="0.18"/>
  <!-- thin spoke lines from periphery to hubs -->
  <line x1="175" y1="80" x2="248" y2="120" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="370" y1="72" x2="322" y2="115" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="420" y1="145" x2="355" y2="148" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="370" y1="225" x2="322" y2="185" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="172" y1="210" x2="240" y2="178" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <line x1="155" y1="120" x2="225" y2="135" stroke="#8899BB" stroke-width="0.6" stroke-opacity="0.2"/>
  <!-- 6 major hub nodes (representing 6 AI companies) -->
  <!-- Hub 1 (top-left) -->
  <circle cx="225" cy="118" r="22" fill="#E8845C" fill-opacity="0.15" stroke="#E8845C" stroke-width="2" stroke-opacity="0.7"/>
  <circle cx="225" cy="118" r="8" fill="#E8845C" fill-opacity="0.4"/>
  <!-- Hub 2 (top-right) -->
  <circle cx="355" cy="118" r="22" fill="#E8845C" fill-opacity="0.15" stroke="#E8845C" stroke-width="2" stroke-opacity="0.7"/>
  <circle cx="355" cy="118" r="8" fill="#E8845C" fill-opacity="0.4"/>
  <!-- Hub 3 (left) -->
  <circle cx="210" cy="178" r="18" fill="#E8845C" fill-opacity="0.12" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.6"/>
  <circle cx="210" cy="178" r="7" fill="#E8845C" fill-opacity="0.35"/>
  <!-- Hub 4 (right) -->
  <circle cx="370" cy="178" r="18" fill="#E8845C" fill-opacity="0.12" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.6"/>
  <circle cx="370" cy="178" r="7" fill="#E8845C" fill-opacity="0.35"/>
  <!-- Hub 5 (bottom-left) -->
  <circle cx="248" cy="205" r="16" fill="#E8845C" fill-opacity="0.1" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.5"/>
  <circle cx="248" cy="205" r="6" fill="#E8845C" fill-opacity="0.3"/>
  <!-- Hub 6 (bottom-right) -->
  <circle cx="332" cy="205" r="16" fill="#E8845C" fill-opacity="0.1" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.5"/>
  <circle cx="332" cy="205" r="6" fill="#E8845C" fill-opacity="0.3"/>
  <!-- thick connections between hubs -->
  <line x1="225" y1="118" x2="355" y2="118" stroke="#E8845C" stroke-width="2.5" stroke-opacity="0.4"/>
  <line x1="225" y1="118" x2="210" y2="178" stroke="#E8845C" stroke-width="2" stroke-opacity="0.35"/>
  <line x1="355" y1="118" x2="370" y2="178" stroke="#E8845C" stroke-width="2" stroke-opacity="0.35"/>
  <line x1="210" y1="178" x2="248" y2="205" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.3"/>
  <line x1="370" y1="178" x2="332" y2="205" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.3"/>
  <line x1="248" y1="205" x2="332" y2="205" stroke="#E8845C" stroke-width="1.8" stroke-opacity="0.3"/>
  <line x1="225" y1="118" x2="248" y2="205" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.2"/>
  <line x1="355" y1="118" x2="332" y2="205" stroke="#E8845C" stroke-width="1.2" stroke-opacity="0.2"/>
  <line x1="210" y1="178" x2="370" y2="178" stroke="#E8845C" stroke-width="1.5" stroke-opacity="0.25"/>
  <!-- "6" label -->
  <text x="290" y="155" font-size="9" fill="#E8845C" fill-opacity="0.5" text-anchor="middle" font-family="monospace" letter-spacing="2">6 HUB</text>
  <!-- "60% humanity" hint -->
  <text x="290" y="292" font-size="8" fill="#8899BB" fill-opacity="0.4" text-anchor="middle" font-family="monospace" letter-spacing="1">60% DELL'UMANITÀ</text>
</svg>"""
}

# -----------------------------------------------------------------------------
# CSS (identico al design system del kit)
# -----------------------------------------------------------------------------
CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg-navy: #0F1729; --surface: #1A2540; --surface-2: #243154;
  --teal: #00D4AA; --teal-soft: rgba(0,212,170,.12);
  --copper: #E8845C; --copper-soft: rgba(232,132,92,.14);
  --cream: #F4EBDD; --muted: #8899BB; --gold: #FFD166;
  --line: rgba(244,235,221,.12);
}

html, body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--bg-navy); color: var(--cream);
  font-size: 11pt; line-height: 1.5; -webkit-font-smoothing: antialiased;
}

.page {
  width: 210mm; height: 297mm; padding: 18mm 16mm;
  position: relative; page-break-after: always; overflow: hidden;
}
.page:last-child { page-break-after: auto; }

/* FRONTE */
.front { display: flex; flex-direction: column; }
.front-header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 10pt; border-bottom: 1pt solid var(--line); margin-bottom: 16pt; }
.card-num { font-family: 'JetBrains Mono', monospace; font-size: 10pt; font-weight: 700; letter-spacing: 1.2pt; color: var(--teal); }
.card-tag { font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 1.5pt; color: var(--muted); text-transform: uppercase; }
.title { font-family: 'Newsreader', serif; font-weight: 500; font-size: 36pt; line-height: 1.05; color: var(--cream); letter-spacing: -0.5pt; margin-bottom: 12pt; white-space: pre-line; }
.tagline { background: var(--teal-soft); border-left: 3pt solid var(--teal); padding: 11pt 14pt; border-radius: 0 8pt 8pt 0; font-size: 11.5pt; color: var(--cream); font-style: italic; line-height: 1.45; white-space: pre-line; margin-bottom: 18pt; }
.illustration { flex: 1; display: flex; align-items: center; justify-content: center; margin: 6pt 0 14pt; min-height: 75mm; }
.illustration svg { width: 100%; max-width: 145mm; max-height: 85mm; }

/* SPUNTI PER LA LEZIONE */
.lesson-hooks { background: var(--surface); border-radius: 10pt; padding: 14pt 16pt; margin-bottom: 14pt; }
.lesson-hooks-label { font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; letter-spacing: 2pt; color: var(--copper); text-transform: uppercase; margin-bottom: 10pt; font-weight: 700; }
.lesson-hook { margin-bottom: 9pt; }
.lesson-hook:last-child { margin-bottom: 0; }
.lesson-hook-label { font-family: 'JetBrains Mono', monospace; font-size: 8pt; letter-spacing: 1.5pt; color: var(--teal); text-transform: uppercase; font-weight: 700; margin-bottom: 3pt; display: block; }
.lesson-hook-text { font-size: 10pt; line-height: 1.5; color: var(--cream); padding-left: 10pt; border-left: 2pt solid var(--surface-2); }
.lesson-hook-text strong { color: var(--gold); font-weight: 700; }
.lesson-hook-text em { color: var(--teal); font-style: italic; }

.front-footer { display: flex; justify-content: space-between; align-items: center; padding-top: 10pt; border-top: 1pt solid var(--line); }
.front-tags { display: flex; gap: 16pt; }
.front-tag { font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 1.5pt; color: var(--teal); font-weight: 700; }
.brand { font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; letter-spacing: 1.5pt; color: var(--muted); }

/* RETRO */
.back { display: flex; flex-direction: column; }
.back-header { background: var(--copper); color: var(--bg-navy); margin: -18mm -16mm 16pt; padding: 14pt 16mm 12pt; display: flex; justify-content: space-between; align-items: center; }
.back-zone-label { font-family: 'JetBrains Mono', monospace; font-size: 10pt; letter-spacing: 2pt; font-weight: 800; text-transform: uppercase; }
.back-card-id { font-family: 'JetBrains Mono', monospace; font-size: 9pt; letter-spacing: 1.5pt; font-weight: 700; }
.back-title { font-family: 'Newsreader', serif; font-weight: 600; font-size: 18pt; line-height: 1.1; color: var(--cream); margin-bottom: 4pt; white-space: pre-line; }
.back-subtitle { font-size: 9.5pt; color: var(--muted); font-style: italic; line-height: 1.4; margin-bottom: 12pt; padding-bottom: 10pt; border-bottom: 1pt solid var(--line); }
.back-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 14pt; margin-bottom: 12pt; }
.section-label { font-family: 'JetBrains Mono', monospace; font-size: 8pt; letter-spacing: 1.8pt; color: var(--teal); text-transform: uppercase; font-weight: 800; margin-bottom: 6pt; }
.activity-list { list-style: none; }
.activity-item { margin-bottom: 7pt; font-size: 8.5pt; line-height: 1.4; }
.activity-step-head { display: flex; align-items: baseline; gap: 6pt; margin-bottom: 2pt; }
.activity-num { font-family: 'JetBrains Mono', monospace; font-size: 8pt; color: var(--copper); font-weight: 800; min-width: 14pt; }
.activity-title { font-weight: 700; color: var(--cream); font-size: 9pt; }
.activity-time { font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: var(--muted); margin-left: auto; }
.activity-steps { padding-left: 20pt; color: var(--cream); opacity: 0.85; font-size: 8pt; line-height: 1.45; }
.activity-steps li { list-style: none; position: relative; margin-bottom: 2pt; }
.activity-steps li::before { content: '\00B7'; position: absolute; left: -8pt; color: var(--teal); font-weight: 800; }
.materials-list { list-style: none; }
.materials-list li { font-size: 8.5pt; line-height: 1.45; padding-left: 12pt; position: relative; margin-bottom: 5pt; color: var(--cream); opacity: 0.85; }
.materials-list li::before { content: '\25B8'; position: absolute; left: 0; color: var(--copper); font-size: 8pt; }
.reflection-state { display: grid; grid-template-columns: 1fr 1fr; gap: 14pt; margin-top: 4pt; padding-top: 10pt; border-top: 1pt solid var(--line); }
.reflection-list { list-style: none; }
.reflection-list li { font-size: 8.5pt; line-height: 1.5; padding-left: 12pt; position: relative; margin-bottom: 5pt; color: var(--cream); font-style: italic; }
.reflection-list li::before { content: '?'; position: absolute; left: 0; color: var(--teal); font-weight: 800; font-style: normal; }
.state-intro { font-size: 8.5pt; color: var(--muted); font-style: italic; margin-bottom: 7pt; }
.position-item { margin-bottom: 6pt; padding-left: 9pt; border-left: 2pt solid var(--copper); }
.position-label { font-weight: 800; color: var(--copper); font-size: 8.5pt; margin-bottom: 2pt; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.5pt; text-transform: uppercase; }
.position-text { font-size: 8pt; line-height: 1.45; color: var(--cream); opacity: 0.92; }
.back-footer { margin-top: auto; padding-top: 12pt; border-top: 1pt solid var(--line); display: flex; justify-content: space-between; align-items: flex-end; gap: 14pt; }
.qr-block { display: flex; align-items: center; gap: 12pt; }
.qr-img { width: 70pt; height: 70pt; background: var(--cream); border-radius: 6pt; padding: 4pt; display: flex; align-items: center; justify-content: center; }
.qr-img img { width: 100%; height: 100%; display: block; }
.qr-text { display: flex; flex-direction: column; }
.qr-label { font-family: 'JetBrains Mono', monospace; font-size: 8pt; letter-spacing: 1.5pt; color: var(--copper); text-transform: uppercase; margin-bottom: 3pt; }
.qr-name { font-family: 'Newsreader', serif; font-weight: 600; font-size: 14pt; color: var(--cream); line-height: 1.1; margin-bottom: 2pt; }
.qr-sub { font-size: 8.5pt; color: var(--muted); font-style: italic; max-width: 60mm; line-height: 1.35; }
.back-meta { text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; letter-spacing: 1pt; color: var(--muted); }
.back-meta-time { color: var(--teal); font-weight: 700; font-size: 10pt; margin-bottom: 2pt; }
"""

# -----------------------------------------------------------------------------
# Render helpers
# -----------------------------------------------------------------------------
def render_activity(activity):
    items = []
    for i, step in enumerate(activity, 1):
        steps_html = "".join([f"<li>{s}</li>" for s in step["steps"]])
        items.append(
            f'<li class="activity-item">'
            f'<div class="activity-step-head">'
            f'<span class="activity-num">{i:02d}</span>'
            f'<span class="activity-title">{step["title"]}</span>'
            f'<span class="activity-time">{step["time"]}</span>'
            f'</div>'
            f'<ul class="activity-steps">{steps_html}</ul>'
            f'</li>'
        )
    return f'<ol class="activity-list">{"".join(items)}</ol>'

def render_materials(materials):
    return f'<ul class="materials-list">{"".join([f"<li>{m}</li>" for m in materials])}</ul>'

def render_reflection(questions):
    return f'<ul class="reflection-list">{"".join([f"<li>{q}</li>" for q in questions])}</ul>'

def render_state(state):
    positions = "".join([
        f'<div class="position-item">'
        f'<div class="position-label">{p["label"]}</div>'
        f'<div class="position-text">{p["text"]}</div>'
        f'</div>'
        for p in state["positions"]
    ])
    return f'<div class="state-intro">{state["intro"]}</div>{positions}'

def render_lesson_hooks(hooks):
    items = "".join([
        f'<div class="lesson-hook">'
        f'<span class="lesson-hook-label">{h["label"]}</span>'
        f'<div class="lesson-hook-text">{h["text"]}</div>'
        f'</div>'
        for h in hooks
    ])
    return f'<div class="lesson-hooks"><div class="lesson-hooks-label">Spunti per la lezione</div>{items}</div>'

def qr_src(card):
    qr_path = QR_DIR / f"qr_{card['id']}_{card['slug']}.png"
    if qr_path.exists():
        data = base64.b64encode(qr_path.read_bytes()).decode("ascii")
        return f"data:image/png;base64,{data}"
    target = f"{GAMES_BASE_URL}/game_{card['id']}_{card['slug']}.html"
    encoded = urllib.parse.quote(target, safe='')
    return f"https://api.qrserver.com/v1/create-qr-code/?size=400x400&ecc=H&margin=2&data={encoded}"

def get_svg(card):
    return ILLUSTRATIONS.get(card["illustration_type"], ILLUSTRATIONS["companions"])

def render_card(card):
    svg = get_svg(card)
    tags_html = "".join([f'<span class="front-tag">{t}</span>' for t in card["footer_tags"]])

    front = (
        f'<section class="page front">'
        f'<header class="front-header">'
        f'<span class="card-num">CARD {card["id"]}</span>'
        f'<span class="card-tag">ADULT · DISCUSSIONE</span>'
        f'</header>'
        f'<h1 class="title">{card["title"]}</h1>'
        f'<div class="tagline">{card["tagline"]}</div>'
        f'<div class="illustration">{svg}</div>'
        f'{render_lesson_hooks(card["lesson_hooks"])}'
        f'<footer class="front-footer">'
        f'<div class="front-tags">{tags_html}</div>'
        f'<div class="brand">PINA AI LITERACY · ADULT · CARD {card["id"]}</div>'
        f'</footer>'
        f'</section>'
    )

    back = (
        f'<section class="page back">'
        f'<header class="back-header">'
        f'<span class="back-zone-label">FACILITATOR ZONE</span>'
        f'<span class="back-card-id">CARD {card["id"]} · ADULT</span>'
        f'</header>'
        f'<h2 class="back-title">{card["title"]}</h2>'
        f'<div class="back-subtitle">{card["back_subtitle"]}</div>'
        f'<div class="back-grid">'
        f'<div><div class="section-label">Attività · 75 min</div>{render_activity(card["activity"])}</div>'
        f'<div><div class="section-label">Materiali</div>{render_materials(card["materials"])}</div>'
        f'</div>'
        f'<div class="reflection-state">'
        f'<div><div class="section-label">Domande di riflessione</div>{render_reflection(card["reflection"])}</div>'
        f'<div><div class="section-label">State of the debate</div>{render_state(card["state_of_debate"])}</div>'
        f'</div>'
        f'<footer class="back-footer">'
        f'<div class="qr-block">'
        f'<div class="qr-img"><img src="{qr_src(card)}" alt="QR game {card["id"]}"/></div>'
        f'<div class="qr-text">'
        f'<span class="qr-label">Gioco digitale</span>'
        f'<span class="qr-name">{card["game_name"]}</span>'
        f'<span class="qr-sub">{card["game_subtitle"]}</span>'
        f'</div>'
        f'</div>'
        f'<div class="back-meta">'
        f'<div class="back-meta-time">75 MIN</div>'
        f'<div>DISCUSSIONE · ADULT</div>'
        f'<div>CARD {card["id"]}</div>'
        f'</div>'
        f'</footer>'
        f'</section>'
    )

    return (
        f'<!doctype html><html lang="it"><head>'
        f'<meta charset="utf-8"/>'
        f'<title>PINA · Card {card["id"]} · {card["slug"]}</title>'
        f'<link href="https://fonts.googleapis.com/css2?family=Newsreader:wght@400;500;600;700'
        f'&family=Inter:wght@400;500;700;800&family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style>'
        f'</head><body>{front}{back}</body></html>'
    )

def main():
    print(f"Generating {len(CARDS)} cards into {OUTPUT_DIR}...")
    for card in CARDS:
        filename = f"card_{card['id']}_{card['slug']}.html"
        path = OUTPUT_DIR / filename
        html = render_card(card)
        path.write_text(html, encoding="utf-8")
        print(f"  OK {filename}  ({len(html):,} bytes)")
    print(f"\nDone. {len(CARDS)} HTML files in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
