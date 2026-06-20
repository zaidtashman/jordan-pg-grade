# Jordan Performance Grade (PG) Map
**Official Asphalt Pavement Performance Grading Map with 98% Reliability**

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](https://zaidtashman.github.io/jordan-pg-grade/index.html)

This repository hosts the official interactive Performance Grade (PG) map for the Hashemite Kingdom of Jordan. Developed and published in coordination with the **Ministry of Transportation**, this tool provides civil engineers, contractors, and public infrastructure planners with critical asphalt binder specifications derived from statistical analysis of long-term climate data.

## 🗺 What is this map?

The map displays the Performance Grade (PG) classification of asphalt binders across various regions in Jordan. PG grading is a core component of the Superpave system, which specifies the required binder grade to withstand the full spectrum of high and low temperatures that a road surface will experience at a given location.

Utilizing a 98% reliability factor, this map ensures pavement durability, rutting resistance at high summer temperatures, and thermal cracking resistance during winter freezes across Jordan's diverse topography.

## 🔄 How to Update the Map

Follow these steps **in order** whenever the map needs to be updated:

### 1. Run the Analysis
Run the PG analysis pipeline to produce the original Folium map:
```
→ Output: Jordan-PG-Grade-Map-98_valid.html
```

### 2. Update the Configuration
Edit [`data/config.js`](data/config.js) with the new PG adjustment table values (zones, traffic conditions, and grades).

### 3. Run the Enhancement Script
Run the aesthetic enhancement script to generate the styled version used by the webpage:
```bash
/usr/bin/python3 enhance_map.py
```
```
→ Output: Jordan-PG-Grade-Map-98_enhanced.html
```

### 4. Copy `index.html` → `map.html`
```bash
cp index.html map.html
```

### 5. Push to Git
```bash
git add .
git commit -m "Update PG map"
git push
```

## 🎨 Favicon Generation Prompt

Use this prompt with an image generation model (e.g. Gemini, Imagen) to regenerate the favicon:

> A clean, minimal favicon icon on a pure dark background (#0F1419). Center a flat-style hexagon filled with rich green (#007A3D) and a thin white outline. Inside the hexagon, the letters "PG" in bold white sans-serif font (Inter or Helvetica style), perfectly centered. No gradients, no 3D effects, no shadows, no extra decoration. The hexagon should fill about 75% of the square canvas. Flat vector style, sharp edges, suitable for use as a 256×256 favicon.

Save the output to `img/favicon.png`.
