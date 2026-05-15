const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const HTML_DIR = path.join(ROOT, 'cards', 'html');
const PDF_DIR = path.join(ROOT, 'cards', 'pdf');

if (!fs.existsSync(PDF_DIR)) fs.mkdirSync(PDF_DIR, { recursive: true });

(async () => {
  const browser = await puppeteer.launch();
  const files = fs.readdirSync(HTML_DIR).filter(f => f.endsWith('.html'));
  console.log(`Converting ${files.length} HTML files to PDF...`);

  for (const file of files) {
    const htmlPath = path.join(HTML_DIR, file);
    const pdfPath = path.join(PDF_DIR, file.replace('.html', '.pdf'));
    const page = await browser.newPage();
    await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 1500));
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 }
    });
    console.log(`  ✓ ${path.basename(pdfPath)}`);
    await page.close();
  }
  await browser.close();
  console.log('Done.');
})();
