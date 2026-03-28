# We Got Us Your IP

> A single-page IP analysis tool with a terminal hacker aesthetic and an optional WGUS brand theme. Instantly detects your IP address and provides comprehensive network information including WHOIS data, reverse DNS, VPN detection, real-time DNSBL blacklist checks, geolocation mapping, and browser fingerprinting.

[![Version](https://img.shields.io/badge/version-1.2-green.svg)](https://github.com/arelas/ip_wegotussome_com)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE)

**Live Demo**: [ip.wegotussome.com](https://ip.wegotussome.com)

![Screenshot](https://ip.wegotussome.com/screenshot.png)

## Overview

**We Got Us Your IP** is a single-page web application that provides comprehensive IP address analysis and network information. It ships with two visual themes: the original dark terminal aesthetic and an optional WGUS brand theme that matches the look and feel of the broader wegotussome.com toolset. All features run entirely client-side with no build process required.

### Key Features

- **Instant IP Detection** — Automatically displays your IP address on page load
- **VPN/Proxy Detection** — Identifies if you're behind a VPN or proxy
- **One-Click Copy** — Copy your IP to clipboard instantly
- **WHOIS Lookup** — Detailed network registration information for any IP
- **Reverse DNS** — PTR record lookup via DNS-over-HTTPS for any IP
- **Geolocation Map** — Interactive Leaflet.js map pinned to the IP's coordinates
- **Comprehensive Blacklist Check** — Real DNSBL queries across 5 lists in parallel
- **Browser Fingerprinting** — Detailed analysis of your device and browser
- **Export Data** — Download all collected data as JSON
- **Quick Tools** — Direct links to speed tests, DNS checks, and more
- **API Rate Limit Handling** — Automatic fallback chain across three providers with live countdown
- **Dual Theme** — Toggle between Terminal and WGUS brand themes, persisted via localStorage
- **PWA / Offline Support** — Installable as a web app; app shell cached via service worker for offline use

## Features in Detail

### IP Address Display
- Real-time detection of your public IP address
- ISP and organization information
- Geographic location (city, region, country)
- Connection type detection (Residential/Mobile/Data Center/Corporate)
- ASN (Autonomous System Number)
- Timezone and postal code
- IPv4/IPv6 protocol information

### VPN/Proxy Detection
- Automatic detection based on ISP patterns
- Visual badge indicator (Green = Clean, Red = VPN/Proxy)

### WHOIS Lookup
Query detailed registration information for any IP address:
- Geographic coordinates (latitude/longitude)
- Complete organization and ASN details
- Timezone and UTC offset
- Currency and calling code
- Continent, region, city details

Uses the same three-provider fallback chain as the main IP lookup (ipapi.co → ipwho.is → ipinfo.io), so WHOIS continues to work even when the primary provider is rate-limited.

### Reverse DNS
- PTR record lookup via `dns.google/resolve` — no API key, no cost
- Handles both IPv4 (reversed octets → `.in-addr.arpa`) and IPv6 (nibble format → `.ip6.arpa`)
- Displays resolved hostname(s) and TTL, or a clean message if no PTR record is configured

### Geolocation Map
- Interactive map powered by **Leaflet.js** + **OpenStreetMap** tiles (via cdnjs — no API key)
- Custom marker styled with the active theme's accent color
- Popup shows IP, city, and country; coordinates displayed below the map
- Correctly handles the hidden-to-visible transition (`invalidateSize`)

### Comprehensive Blacklist Check
Real DNSBL queries against 5 blacklists via DNS-over-HTTPS (`dns.google/resolve`):

| List | Zone |
|---|---|
| Spamhaus ZEN | `zen.spamhaus.org` |
| Barracuda Reputation | `b.barracudacentral.org` |
| SORBS | `dnsbl.sorbs.net` |
| SpamCop | `bl.spamcop.net` |
| UCEProtect L1 | `dnsbl-1.uceprotect.net` |

- All 5 checks fire in parallel; the UI updates live as each result resolves
- CLEAN / LISTED badge per list, plus an overall summary score at the top
- AbuseIPDB included as a manual link (requires account for API access)
- Gracefully degrades to manual links for IPv6 (DNSBL is IPv4-only by spec)

### API Rate Limit Handling
Three-provider fallback chain for both IP detection and WHOIS lookups:

1. **ipapi.co** — primary provider; handles both hard HTTP 429s (60-second countdown before retry) and soft 200+error rate-limit responses
2. **ipwho.is** — first fallback (free tier, HTTPS, no key required)
3. **ipinfo.io** — second fallback (free tier, 50k req/month, no key required)

All provider responses are normalised to the same internal shape — WHOIS, map, reverse DNS, and blacklist checks continue to work transparently regardless of which provider served the data. The UI indicates which provider was used when falling back.

### Browser Fingerprint
- Browser type and version (Edge/Chrome/Firefox/Safari correctly detected)
- Operating system, platform, language
- Screen resolution and color depth
- CPU cores, device memory, touch points
- Cookie and Do Not Track settings

### Data Export
- Download complete analysis as JSON
- Includes IP data, browser fingerprint, and timestamp
- Filename format: `ip-report-{IP}-{timestamp}.json`

### Theme Toggle
Switch between two visual themes. Your preference is saved to `localStorage` and restored on next visit.

- **Terminal** (default) — Dark hacker aesthetic: terminal green (#00ff66) on pure black, CRT scanlines, phosphor glow, Courier New. Toggle button is a fixed pill in the top-right corner.
- **WGUS** — Brand-consistent theme matching wegotussome.com and qrcodes.wegotussome.com: JetBrains Mono throughout, yellow-green accent (#e8ff47), warm dark surfaces, SVG noise texture. Includes a full breadcrumb navigation header (`wegotussome / ip`) with the toggle button integrated on the right side of the header — no floating button overlapping the UI.

## Design Philosophy

### Terminal Theme
- Terminal green (#00ff66) on pure black
- CRT scanline overlay and radial vignette
- Phosphor text glow on borders and values
- Courier New monospace throughout
- Command-line style labels (`[ISP]`, `[LOCATION]`, etc.)

### WGUS Theme
Matches the **We Got Us Some Industries** brand system, built from the actual QR tool source:
- JetBrains Mono throughout
- Yellow-green accent (#e8ff47), text #f0f0f0, muted #666, border #222
- SVG fractalNoise texture overlay
- 4px border-radius throughout
- Breadcrumb nav header with animated pulse dot and `self-hosted` badge

## Technology Stack

### Frontend
- **HTML5** — Semantic markup
- **CSS3** — Custom properties (CSS variables), animations, flexbox, media queries
- **Vanilla JavaScript** — ES6+, async/await, no frameworks

### APIs
- **ipapi.co** — Primary IP geolocation and WHOIS
- **ipwho.is** — Fallback provider #1 (rate limit handling)
- **ipinfo.io** — Fallback provider #2 (rate limit handling)
- **dns.google/resolve** — DNS-over-HTTPS for PTR records and DNSBL queries

### Libraries
- **Leaflet.js 1.9.4** (cdnjs) — Interactive map

### Fonts (WGUS theme)
- **JetBrains Mono** (Google Fonts) — All text

### Browser APIs
- Clipboard API (copy functionality)
- Navigator API (device fingerprinting)
- localStorage (theme preference)
- Intl API (timezone detection)

## Installation

### Quick Deploy (Recommended)

Upload all four files to your web server — no build process, no dependencies.

```bash
scp index.html manifest.json sw.js icon.svg user@yourserver.com:/var/www/ip.wegotussome.com/
```

### Local Development

```bash
git clone https://github.com/wegotussome/ip.git
cd ip
open index.html

# Or use a local server (recommended for Clipboard API)
python -m http.server 8000
# Visit http://localhost:8000
```

### Requirements

- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- Internet connection for API and map tile calls
- HTTPS required for Clipboard API and PWA/service worker installation

## Usage

### Basic Usage

1. **Visit the site** — Your IP is automatically detected and displayed
2. **Copy your IP** — Click the `> COPY IP` button
3. **Explore features** — Use the action buttons:
   - `> WHOIS MY IP` — Detailed registration lookup
   - `> REVERSE DNS` — PTR record for your IP
   - `> VIEW MAP` — Interactive geolocation map
   - `> CHECK BLACKLIST` — Real-time DNSBL checks across 5 lists
   - `> BROWSER INFO` — Device fingerprint analysis
   - `> EXPORT DATA` — Download JSON report

### Custom IP Lookup

1. Enter any IPv4 or IPv6 address in the input field
2. Click `> WHOIS LOOKUP` (or press Enter)
3. View detailed WHOIS information for that IP

### Theme Toggle

- **Terminal mode**: click `⬡ TERMINAL` in the top-right corner
- **WGUS mode**: click `⬡ TERMINAL` in the right side of the navigation header

The choice is saved automatically and restored on next visit.

### Quick Tools

Bottom toolbar links to:
- **Speed Test** — fast.com
- **DNS Check** — dnschecker.org
- **MX Toolbox** — mxtoolbox.com
- **Port Scanner** — whatismyip.com port scanner

## Configuration

### API Keys

The site uses free public tiers by default. For high-traffic production deployments:

```javascript
// In fetchWithFallback() — primary provider
const primary = await fetch('https://ipapi.co/json/?key=YOUR_KEY_HERE');

// In getWhoisData() — WHOIS lookups
const response = await fetch(`https://ipapi.co/${ip}/json/?key=YOUR_KEY_HERE`);
```

### Customization

#### Terminal Theme Colors
Edit the `:root` CSS variables block:

```css
:root {
    --accent:    #00ff66;  /* change to any color */
    --page-bg:   #0a0a0a;
    --surface:   #0d0d0d;
    --inner-bg:  #000000;
    --danger:    #ff0000;
}
```

#### WGUS Theme Colors
Edit the `body.theme-wgus` CSS variables block:

```css
body.theme-wgus {
    --accent:   #e8ff47;
    --text:     #f0f0f0;
    --muted:    #666666;
    --border:   #222222;
}
```

#### Funny Messages
Edit the `funnyMessages` array near the top of the `<script>` block:

```javascript
const funnyMessages = [
    "> ACCESS GRANTED. Welcome to the system...",
    "> Add your own messages here!",
];
```

## Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | 90+     | ✅ Fully Supported |
| Firefox | 88+     | ✅ Fully Supported |
| Safari  | 14+     | ✅ Fully Supported |
| Edge    | 90+     | ✅ Fully Supported |
| Opera   | 76+     | ✅ Fully Supported |

**Note**: Clipboard API requires HTTPS in production.

## Mobile Support

Fully responsive design optimized for:
- ✅ Desktop (1920px+)
- ✅ Tablets (768px–1024px)
- ✅ Mobile (320px–767px)

## Performance

- **Load Time**: < 1 second (excluding API and map tile calls)
- **File Size**: ~40KB (single HTML file)
- **External JS**: Leaflet.js via cdnjs (map, loaded at page start)
- **API Calls on Load**: 1 (ipapi.co); all other calls are user-initiated

## Security & Privacy

### What We Collect
- Your IP address (via API, not stored by us)
- Browser/device information (client-side only)

### What We Don't Do
- ❌ No tracking cookies
- ❌ No analytics
- ❌ No data storage
- ❌ No third-party tracking
- ❌ No authentication required

### API Privacy
- **ipapi.co** — [Privacy Policy](https://ipapi.co/privacy/)
- **ipwho.is** — [Privacy Policy](https://ipwho.is/)
- **ipinfo.io** — [Privacy Policy](https://ipinfo.io/privacy-policy)
- **dns.google** — [Google Privacy Policy](https://policies.google.com/privacy)
- **OpenStreetMap** — [Privacy Policy](https://wiki.osmfoundation.org/wiki/Privacy_Policy)

## Troubleshooting

### Common Issues

**Issue**: IP not detecting  
**Solution**: Check internet connection; if rate limited, the countdown banner will appear and retry automatically

**Issue**: Copy button not working  
**Solution**: Ensure you're on HTTPS or localhost (Clipboard API requirement)

**Issue**: WHOIS data not loading
**Solution**: The app will automatically try ipwho.is then ipinfo.io if ipapi.co is rate-limited; check the browser console for `[WGUSIP]` log entries if all three fail

**Issue**: Map not rendering  
**Solution**: Ensure cdnjs.cloudflare.com is reachable for Leaflet.js; confirm the IP has valid coordinates

**Issue**: Blacklist check shows all ERROR  
**Solution**: Verify dns.google is accessible from your network

**Issue**: WGUS theme font not loading
**Solution**: Ensure fonts.googleapis.com is reachable; site falls back to system monospace fonts gracefully

**Issue**: Mobile layout broken  
**Solution**: Clear browser cache and hard refresh (Ctrl+Shift+R)

## Roadmap

### Completed
- [x] PWA capabilities (offline mode) — service worker, manifest, installable
- [x] Wider desktop layout — container expanded to 1000px
- [x] Multi-provider fallback — ipapi.co → ipwho.is → ipinfo.io for both IP detection and WHOIS
- [x] WHOIS fallback resilience — isolated per-provider error handling

### Version 2.0 (Future)
- [ ] Historical data charts
- [ ] Multi-language support
- [ ] Bulk IP lookup
- [ ] IP comparison — look up two IPs side by side
- [ ] Share / permalink — `?ip=1.2.3.4` auto-runs lookup on page load
- [ ] Traceroute visualisation — show network hops plotted on the map
- [ ] ASN lookup — dedicated Autonomous System info panel
- [ ] CIDR / subnet calculator — fits the network tool theme
- [ ] Clipboard history — remember the last N IPs looked up
- [ ] Dark / light mode — true light theme variant alongside the existing Terminal and WGUS themes

## Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Maintain single-file structure
- Ensure both themes remain fully functional after any changes
- Ensure mobile responsiveness
- Test on multiple browsers
- Update VERSION_NOTES.md

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** (CC BY-NC-SA 4.0).

**✅ You CAN:** use for personal/educational/non-commercial purposes, modify, share, create derivatives  
**❌ You CANNOT:** use commercially, sell, monetize, remove attribution  
**📋 Requirements:** give credit, link to license, indicate changes, share derivatives under same license

For the full license text, see the [LICENSE](LICENSE) file or visit https://creativecommons.org/licenses/by-nc-sa/4.0/

## Credits

### Built By
**We Got Us Some Industries** — [wegotussome.com](https://wegotussome.com)

### APIs & Services
- [ipapi.co](https://ipapi.co) — Primary IP geolocation & WHOIS
- [ipwho.is](https://ipwho.is) — Fallback provider #1
- [ipinfo.io](https://ipinfo.io) — Fallback provider #2
- [dns.google](https://dns.google) — DNS-over-HTTPS (PTR records, DNSBL)
- [OpenStreetMap](https://openstreetmap.org) — Map tiles

### Libraries
- [Leaflet.js](https://leafletjs.com) — Interactive maps
- [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) — Google Fonts (WGUS theme)

### Inspiration
- Retro terminal aesthetics
- Hacker culture / command-line interfaces
- 1980s CRT monitors

## Support

- **Issues**: [GitHub Issues](https://github.com/arelas/ip_wegotussome_com/issues)

---

**© 2026 We Got Us Some Industries. All packets reserved.**

Made with 💚 and terminal green

> "We got us your IP... but don't worry, we're white hat... probably."
