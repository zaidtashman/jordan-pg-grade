#!/usr/bin/env python3
"""
enhance_map.py — Aesthetic enhancer for the Folium-generated Jordan PG Grade Map.

Reads the original Folium HTML, injects custom CSS and JavaScript to improve:
  • Layer control panel (modern glassmorphism, compact toggle)
  • Popup / tooltip styling (rounded, shadowed, modern typography)
  • Map marker redesign (cleaner icons, subtle animations)
  • AURCA branding overlay (sleeker look)
  • Overall map container (smooth zoom, attribution cleanup)

Usage:
    python3 enhance_map.py

Outputs:
    Jordan-PG-Grade-Map-98_enhanced.html
"""

import re
import sys
from pathlib import Path

# ────────────────────────────────────────────────────────────
# Configuration
# ────────────────────────────────────────────────────────────
INPUT_FILE = "Jordan-PG-Grade-Map-98_valid.html"
OUTPUT_FILE = "Jordan-PG-Grade-Map-98_enhanced.html"

# ────────────────────────────────────────────────────────────
# Custom CSS to inject
# ────────────────────────────────────────────────────────────
CUSTOM_CSS = """
<style>
/* ═══════════════════════════════════════════════════════════
   Enhanced Map Aesthetics — Injected by enhance_map.py
   ═══════════════════════════════════════════════════════════ */

/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ── Base Overrides ── */
body, html {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.leaflet-container {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    font-size: 0.875rem !important;
}

/* ── Smooth Zoom Animation ── */
.leaflet-fade-anim .leaflet-tile,
.leaflet-fade-anim .leaflet-popup {
    transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* ── Map Attribution — Minimal ── */
.leaflet-control-attribution {
    background: rgba(255, 255, 255, 0.75) !important;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-radius: 6px 0 0 0 !important;
    padding: 3px 8px !important;
    font-size: 10px !important;
    color: #666 !important;
    border: none !important;
    box-shadow: none !important;
}

.leaflet-control-attribution a {
    color: #007A3D !important;
}

/* ── Zoom Control ── */
.leaflet-control-zoom {
    border: none !important;
    border-radius: 10px !important;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.12),
                0 1px 4px rgba(0, 0, 0, 0.08) !important;
}

.leaflet-control-zoom a {
    background: rgba(255, 255, 255, 0.92) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    color: #1a1d21 !important;
    width: 36px !important;
    height: 36px !important;
    line-height: 36px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    border: none !important;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06) !important;
    transition: background 0.15s ease, color 0.15s ease;
}

.leaflet-control-zoom a:last-child {
    border-bottom: none !important;
}

.leaflet-control-zoom a:hover {
    background: rgba(0, 122, 61, 0.1) !important;
    color: #007A3D !important;
}

/* ── Layer Control — Modern Glassmorphism ── */
.leaflet-control-layers {
    border: none !important;
    border-radius: 10px !important;
    background: rgba(255, 255, 255, 0.88) !important;
    backdrop-filter: blur(16px) saturate(1.5);
    -webkit-backdrop-filter: blur(16px) saturate(1.5);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1),
                0 1px 6px rgba(0, 0, 0, 0.06) !important;
    padding: 0 !important;
    overflow: hidden;
    min-width: 180px;
}

.leaflet-control-layers-expanded {
    padding: 0 !important;
}

.leaflet-control-layers-list {
    padding: 10px 14px 10px 14px !important;
}

.leaflet-control-layers-base,
.leaflet-control-layers-overlays {
    padding: 2px 0;
}

.leaflet-control-layers-separator {
    border-top: 1px solid rgba(0, 0, 0, 0.06) !important;
    margin: 4px 0 !important;
}

.leaflet-control-layers label {
    font-size: 12px !important;
    font-weight: 500 !important;
    color: #2c3e50 !important;
    padding: 4px 4px 4px 0 !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    border-radius: 5px;
    transition: background 0.15s ease;
}

.leaflet-control-layers label:hover {
    background: rgba(0, 122, 61, 0.05);
}

.leaflet-control-layers label span {
    padding: 0 !important;
}

.leaflet-control-layers input[type="radio"],
.leaflet-control-layers input[type="checkbox"] {
    accent-color: #007A3D;
    width: 14px;
    height: 14px;
    margin: 0 !important;
    cursor: pointer;
}

/* Layer control toggle icon */
.leaflet-control-layers-toggle {
    width: 36px !important;
    height: 36px !important;
    background-size: 20px 20px !important;
    border-radius: 10px !important;
    background-color: rgba(255, 255, 255, 0.92) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.12) !important;
    transition: transform 0.15s ease;
}

.leaflet-control-layers-toggle:hover {
    transform: scale(1.05);
}

/* ── Popup Styling — Modern Card ── */
.leaflet-popup-content-wrapper {
    border-radius: 12px !important;
    padding: 0 !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15),
                0 2px 8px rgba(0, 0, 0, 0.08) !important;
    background: rgba(255, 255, 255, 0.96) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    overflow: hidden;
    border: 1px solid rgba(0, 0, 0, 0.06);
}

.leaflet-popup-content {
    margin: 0 !important;
    padding: 0 !important;
    font-family: 'Inter', sans-serif !important;
    line-height: 1.5 !important;
    min-width: 240px;
}

.leaflet-popup-content iframe {
    border-radius: 12px !important;
    display: block;
}

.leaflet-popup-tip {
    background: rgba(255, 255, 255, 0.96) !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1) !important;
}

.leaflet-popup-close-button {
    color: #8B95A2 !important;
    font-size: 20px !important;
    font-weight: 300 !important;
    padding: 6px 8px 0 0 !important;
    width: 28px !important;
    height: 28px !important;
    transition: color 0.15s ease;
    z-index: 10;
}

.leaflet-popup-close-button:hover {
    color: #CE1126 !important;
}

/* ── Marker Styling ── */
.leaflet-marker-icon {
    transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.leaflet-marker-icon:hover {
    transform: scale(1.12) !important;
    z-index: 10000 !important;
}

/* Awesome marker overrides for cleaner look */
.awesome-marker {
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.25));
}

.awesome-marker i {
    font-size: 13px !important;
}

/* ── AURCA Branding Overlay — Refined ── */
body > div[style*="position: fixed"][style*="z-index: 1000"] {
    background: rgba(255, 255, 255, 0.88) !important;
    backdrop-filter: blur(12px) saturate(1.5) !important;
    -webkit-backdrop-filter: blur(12px) saturate(1.5) !important;
    border-radius: 8px !important;
    padding: 8px 14px !important;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1),
                0 1px 4px rgba(0, 0, 0, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    font-family: 'Inter', sans-serif !important;
    transition: opacity 0.2s ease, transform 0.2s ease;
}

body > div[style*="position: fixed"][style*="z-index: 1000"]:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.14),
                0 2px 6px rgba(0, 0, 0, 0.08) !important;
}

body > div[style*="position: fixed"][style*="z-index: 1000"] div[style*="font-weight: bold"] {
    font-weight: 700 !important;
    font-size: 12px !important;
    letter-spacing: -0.01em !important;
    color: #1a1d21 !important;
}

body > div[style*="position: fixed"][style*="z-index: 1000"] a {
    color: #007A3D !important;
    font-weight: 500 !important;
    font-size: 11px !important;
    text-decoration: none !important;
    transition: color 0.15s ease;
}

body > div[style*="position: fixed"][style*="z-index: 1000"] a:hover {
    color: #00994D !important;
}

/* ── Polygon Hover Effect ── */
.leaflet-interactive {
    transition: fill-opacity 0.2s ease;
}

.leaflet-interactive:hover {
    fill-opacity: 0.85 !important;
}

/* ── Custom Scrollbar inside popups ── */
.leaflet-popup-content::-webkit-scrollbar {
    width: 4px;
}

.leaflet-popup-content::-webkit-scrollbar-track {
    background: transparent;
}

.leaflet-popup-content::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.15);
    border-radius: 4px;
}

/* ── Loading Transition ── */
.leaflet-tile-container {
    transition: opacity 0.3s ease;
}

/* ── Scale Control ── */
.leaflet-control-scale-line {
    border: none !important;
    border-bottom: 2px solid rgba(0, 0, 0, 0.4) !important;
    border-left: 2px solid rgba(0, 0, 0, 0.4) !important;
    border-right: 2px solid rgba(0, 0, 0, 0.4) !important;
    background: rgba(255, 255, 255, 0.7) !important;
    backdrop-filter: blur(4px);
    border-radius: 0 0 4px 4px !important;
    font-size: 10px !important;
    font-weight: 500 !important;
    color: #555 !important;
    padding: 2px 6px !important;
    line-height: 1.3 !important;
}

</style>
"""

# ────────────────────────────────────────────────────────────
# Custom JS to inject (runs after Folium's own scripts)
# ────────────────────────────────────────────────────────────
CUSTOM_JS = """
<script>
// ═══════════════════════════════════════════════════════════
// Enhanced Map Behaviour — Injected by enhance_map.py
// ═══════════════════════════════════════════════════════════

(function() {
    'use strict';

    // Helper: wait for the Leaflet map instance to be available
    function getMapInstance() {
        // Folium names the map variable map_<hash>
        for (var key in window) {
            if (key.startsWith('map_') && window[key] && window[key]._leaflet_id) {
                return window[key];
            }
        }
        return null;
    }

    var map = getMapInstance();
    if (!map) return;

    // 1) Enable smoother zoom
    map.options.zoomSnap = 0.25;
    map.options.zoomDelta = 0.5;
    map.options.wheelPxPerZoomLevel = 120;

    // 2) Add a subtle scale control
    L.control.scale({
        position: 'bottomleft',
        imperial: false,
        maxWidth: 140
    }).addTo(map);

    // 3) Make sure the map properly redraws when embedded in an iframe
    window.addEventListener('resize', function() {
        setTimeout(function() { map.invalidateSize(); }, 100);
    });

    // 5) Send a ready signal for parent window integration
    if (window.parent && window.parent !== window) {
        window.parent.postMessage({ type: 'mapReady' }, '*');
    }

})();
</script>
"""


def main():
    script_dir = Path(__file__).parent
    input_path = script_dir / INPUT_FILE
    output_path = script_dir / OUTPUT_FILE

    if not input_path.exists():
        print(f"❌  Input file not found: {input_path}")
        sys.exit(1)

    print(f"📖  Reading: {input_path.name}")
    html = input_path.read_text(encoding="utf-8")

    # ── Inject custom CSS just before </head> ──
    if "</head>" in html:
        html = html.replace("</head>", CUSTOM_CSS + "\n</head>", 1)
        print("✅  Injected custom CSS")
    else:
        print("⚠️   Could not find </head> tag — CSS not injected")

    # ── Inject custom JS just before </html> ──
    if "</html>" in html:
        html = html.replace("</html>", CUSTOM_JS + "\n</html>", 1)
        print("✅  Injected custom JS")
    else:
        print("⚠️   Could not find </html> tag — JS not injected")

    # ── Write the enhanced file ──
    output_path.write_text(html, encoding="utf-8")
    print(f"🎉  Enhanced map saved to: {output_path.name}")
    print(f"    File size: {output_path.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
