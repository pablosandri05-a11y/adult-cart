# -*- coding: utf-8 -*-
"""Genera 7 QR code PNG con URL adult-cart (NON pina-games)."""
import sys
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H

sys.path.insert(0, str(Path(__file__).parent))
from cards_data import CARDS, GAMES_BASE_URL

QR_DIR = Path(__file__).parent.parent / "qr"
QR_DIR.mkdir(parents=True, exist_ok=True)

for card in CARDS:
    url = f"{GAMES_BASE_URL}/game_{card['id']}_{card['slug']}.html"
    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0F1729", back_color="#F4EBDD")
    out = QR_DIR / f"qr_{card['id']}_{card['slug']}.png"
    img.save(out)
    print(f"  OK {out.name}  ->  {url}")
