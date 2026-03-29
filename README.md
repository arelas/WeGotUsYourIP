# We Got Us Your IP

> A single-page network analysis toolkit — IP detection, WHOIS, traceroute, port scanner, ASN lookup, ping latency, blacklist checks, and more. 25 themes, PWA-ready, entirely client-side.

[![Version](https://img.shields.io/badge/version-26.3.29.1452-green.svg)](https://github.com/arelas/WeGotUsYourIP)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Live Demo**: [ip.wegotussome.com](https://ip.wegotussome.com)

## Theme Gallery

| | | |
|---|---|---|
| <img src="screenshots/catppuccin-latte.png" width="400" alt="catppuccin-latte"> | <img src="screenshots/catppuccin-mocha.png" width="400" alt="catppuccin-mocha"> | <img src="screenshots/commodore64.png" width="400" alt="commodore64"> |
| **Catppuccin Latte** | **Catppuccin Mocha** | **Commodore 64** |
| <img src="screenshots/crt-amber.png" width="400" alt="crt-amber"> | <img src="screenshots/crt-cga.png" width="400" alt="crt-cga"> | <img src="screenshots/crt-cyan.png" width="400" alt="crt-cyan"> |
| **CRT-Amber** | **CRT-CGA** | **CRT-Cyan** |
| <img src="screenshots/crt-green.png" width="400" alt="crt-green"> | <img src="screenshots/crt-magenta.png" width="400" alt="crt-magenta"> | <img src="screenshots/crt-vortex.png" width="400" alt="crt-vortex"> |
| **CRT-Green** | **CRT-Magenta** | **CRT-Vortex** |
| <img src="screenshots/crt-white.png" width="400" alt="crt-white"> | <img src="screenshots/dracula.png" width="400" alt="dracula"> | <img src="screenshots/dracula-dark.png" width="400" alt="dracula-dark"> |
| **CRT-White** | **Dracula** | **Dracula Dark** |
| <img src="screenshots/fusion.png" width="400" alt="fusion"> | <img src="screenshots/github-dark.png" width="400" alt="github-dark"> | <img src="screenshots/github-light.png" width="400" alt="github-light"> |
| **Fusion** | **GitHub Dark** | **GitHub Light** |
| <img src="screenshots/gruvbox-dark.png" width="400" alt="gruvbox-dark"> | <img src="screenshots/monokai.png" width="400" alt="monokai"> | <img src="screenshots/nord.png" width="400" alt="nord"> |
| **Gruvbox Dark** | **Monokai** | **Nord** |
| <img src="screenshots/one-dark.png" width="400" alt="one-dark"> | <img src="screenshots/solarized-dark.png" width="400" alt="solarized-dark"> | <img src="screenshots/solarized-light.png" width="400" alt="solarized-light"> |
| **One Dark** | **Solarized Dark** | **Solarized Light** |
| <img src="screenshots/tokyo-night.png" width="400" alt="tokyo-night"> | <img src="screenshots/vortex.png" width="400" alt="vortex"> | <img src="screenshots/wgus-dark.png" width="400" alt="wgus-dark"> |
| **Tokyo Night** | **Vortex** | **WGUS Dark** |
| <img src="screenshots/wgus-light.png" width="400" alt="wgus-light"> |  |  |
| **WGUS Light** |  |  |

## Overview

**We Got Us Your IP** is a single-page web application that provides comprehensive IP address analysis and network information. It ships with a library of 25 community themes — from the default hacker terminal green to WGUS brand themes, retro CRT palettes, Commodore 64, and popular developer themes like Dracula, Nord, and Catppuccin. Themes are defined as plain JSON files and can be added or customized without touching the application code. All features run entirely client-side with no build process required.

### Key Features

- **Instant IP Detection** — Automatically displays your IP address on page load
- **VPN/Proxy Detection** — Identifies if you're behind a VPN or proxy
- **One-Click Copy** — Copy your IP to clipboard instantly
- **WHOIS Lookup** — Detailed network registration information for any IP
- **Reverse DNS** — PTR record lookup via DNS-over-HTTPS for any IP
- **Geolocation Map** — Interactive Leaflet.js map pinned to the IP's coordinates
- **Traceroute Visualization** — Network hops plotted on a live map via GlobalPing API
- **ASN Lookup** — Dedicated Autonomous System info panel powered by RIPEstat
- **IP Comparison** — Look up two IPs side by side with diff highlighting
- **Bulk IP Lookup** — Look up up to 20 IPs in one go, exportable as CSV
- **Comprehensive Blacklist Check** — Real DNSBL queries across 5 lists in parallel
- **Browser Fingerprinting** — Detailed analysis of your device and browser
- **CIDR / Subnet Calculator** — Fully client-side network math
- **Lookup History** — Activity chart, IP address history, and recent lookup log stored locally
- **Share / Permalink** — `?ip=x.x.x.x` auto-runs a lookup on page load
- **Export Data** — Download all collected data as JSON
- **API Rate Limit Handling** — Automatic fallback chain across three providers with live countdown
- **Theme Library** — 25 themes via JSON theme files; add your own without touching app code
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

### Traceroute Visualization
- Runs a real traceroute using the [GlobalPing API](https://www.globalping.io/) — no API key required
- Network hops are plotted as connected markers on a Leaflet map
- Private/RFC-1918 hops are detected and skipped gracefully
- Falls back to a text-only hop list if fewer than 2 public hops can be geolocated

### ASN Lookup
- Fetches Autonomous System details from [RIPEstat](https://stat.ripe.net/) — authoritative, CORS-friendly, no key required
- Displays AS name, description, country, abuse contact, and registered prefixes
- Pre-fills the ASN from the current IP on open; also accepts manual entry

### IP Comparison
- Enter two IP addresses and compare their data side by side
- Fields that differ between the two IPs are highlighted for quick scanning
- Uses the same fallback provider chain as the main lookup

### Bulk IP Lookup
- Paste up to 20 IP addresses (one per line) for sequential lookup
- Results shown in a summary table with ISP, location, and ASN per IP
- Export all results as a CSV file

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

### CIDR / Subnet Calculator
- Parses any CIDR notation (e.g. `192.168.1.0/24`)
- Displays network address, broadcast, subnet mask, host range, and usable host count
- Fully client-side — no network requests

### Lookup History
- Every IP lookup is automatically recorded to `localStorage` (`wgusip-history`, max 200 entries)
- **Activity chart** — SVG bar chart of lookups over the last 14 days
- **Your IP addresses** — own-IP lookups grouped by IP with location, org, date range, and count
- **Recent lookups log** — scrollable list of the last 50 lookups with timestamp, IP, and location
- Clear history button wipes all stored entries

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

### Theme System

Themes are selected via a hamburger menu (top-right corner). Your preference is saved to `localStorage` and restored on next visit. A preload script in `<head>` caches and re-applies your theme's CSS variables synchronously before first paint, preventing any flash of the default green theme.

Themes are defined as plain JSON files in the `themes/` directory and loaded dynamically at runtime. Adding a new theme requires only a JSON file — no code changes needed.

#### Included Themes (25)

| Theme | Style |
|---|---|
| **WGUS Dark** | Default brand dark — yellow-green accent, warm dark surfaces |
| **WGUS Light** | Brand light — electric indigo accent, off-white surfaces |
| **Catppuccin Latte** | Warm creamy light, mauve accent |
| **Catppuccin Mocha** | Soothing pastel dark, mauve accent |
| **Commodore 64** | Light-blue on deep royal blue, Courier New |
| **CRT-Amber** | Phosphor amber on black |
| **CRT-CGA** | Full IBM CGA palette — cyan accents, magenta borders |
| **CRT-Cyan** | IBM CGA cyan on black |
| **CRT-Green** | Classic terminal green on black |
| **CRT-Magenta** | IBM CGA magenta on black |
| **CRT-Vortex** | Electric green text, magenta borders — inspired by Vortex BBS ANSI art |
| **CRT-White** | Monochrome white phosphor |
| **Dracula** | Purple/pink on dark grey, the classic dark theme |
| **Fusion** | WGUS Fusion brand theme |
| **GitHub Dark** | Familiar dark interface from github.com |
| **GitHub Light** | Clean white interface from github.com |
| **Gruvbox Dark** | Warm retro ochre and earth tones |
| **Monokai** | Neon greens and pinks on near-black |
| **Nord** | Arctic cool blues and grey-greens |
| **One Dark** | Atom's signature muted blue-grey dark |
| **Solarized Dark** | Precision-designed dark with warm tones |
| **Solarized Light** | Warm cream background light palette |
| **Tokyo Night** | Neon purple-blue midnight city aesthetic |
| **Vortex** | WGUS style — electric green on black with magenta accents |

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
- **GlobalPing API** — Traceroute measurements (no key required)
- **RIPEstat** — ASN / Autonomous System data (no key required)

### Libraries
- **Leaflet.js 1.9.4** (cdnjs) — Interactive maps (geolocation and traceroute)

### Fonts
- **JetBrains Mono** (Google Fonts) — WGUS and developer themes
- **Courier New** — CRT and retro themes (system font, no external load)

### Browser APIs
- Clipboard API (copy functionality)
- Navigator API (device fingerprinting)
- localStorage (theme preference, lookup history)
- Intl API (timezone detection)

## Installation

### Quick Deploy (Recommended)

Upload the project files to your web server — no build process, no dependencies.

```bash
# Copy all files including the themes directory
scp -r index.html manifest.json sw.js icon.svg themes/ user@yourserver.com:/var/www/ip.wegotussome.com/
```

### Local Development

```bash
git clone https://github.com/arelas/WeGotUsYourIP
cd WeGotUsYourIP

# Use a local server (required for Clipboard API and service worker)
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
   - `> TRACEROUTE` — Visualize network hops on a map
   - `> ASN INFO` — Autonomous System details
   - `> CHECK BLACKLIST` — Real-time DNSBL checks across 5 lists
   - `> BROWSER INFO` — Device fingerprint analysis
   - `> CIDR CALC` — Subnet calculator
   - `> COMPARE IPs` — Side-by-side comparison of two IPs
   - `> BULK LOOKUP` — Look up multiple IPs at once
   - `> HISTORY` — Activity chart and recent lookup log
   - `> SHARE / PERMALINK` — Copy a shareable URL for this IP
   - `> EXPORT DATA` — Download JSON report

### Custom IP Lookup

1. Enter any IPv4 or IPv6 address in the input field below the action buttons
2. Click `> WHOIS LOOKUP` (or press Enter)
3. View detailed WHOIS information for that IP

### Permalink / Share

Append `?ip=x.x.x.x` to the URL and share it — the page will automatically run a lookup for that IP on load.

### Switching Themes

Click the hamburger icon (≡) in the top-right corner to open the theme picker. Your selection is saved automatically and restored on next visit with no flash of the default theme.

### Quick Tools

Bottom toolbar links to:
- **Speed Test** — speed.cloudflare.com
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

### Adding a Custom Theme

Create a JSON file in the `themes/` directory:

```json
{
  "name": "My Theme",
  "id": "my-theme",
  "description": "A brief description",
  "author": "Your Name",
  "base": "wgus",
  "variables": {
    "accent":      "#ff6600",
    "accent-rgb":  "255, 102, 0",
    "accent-dim":  "#cc5200",
    "page-bg":     "#1a1a1a",
    "surface":     "#242424",
    "inner-bg":    "#111111",
    "danger":      "#ff4444",
    "text":        "#f0f0f0",
    "muted":       "#666666",
    "border":      "#333333",
    "font-body":   "'JetBrains Mono', monospace",
    "font-head":   "'JetBrains Mono', monospace",
    "scanlines":   "none",
    "vignette":    "none"
  }
}
```

Then add an entry to `themes/index.json` and `sw.js` APP_SHELL, and bump the `CACHE_NAME` version:

```json
{ "id": "my-theme", "file": "my-theme.json" }
```

**`base` values:**
- `"wgus"` — WGUS layout: breadcrumb header, card surfaces, JetBrains Mono styling
- `"terminal"` — Terminal layout: full-screen CRT aesthetic, scanlines, phosphor glow

**`border` vs `accent`:** In terminal-base themes, `--border` controls structural panel borders while `--accent` controls text, glows, and interactive highlights. Set them to the same value for single-color themes; use distinct values (like CRT-CGA) to create multi-color palettes.

**Light themes:** Any theme with a `page-bg` brightness above `#888` is automatically detected as light and receives subtle structural adjustments (reduced noise opacity, soft container shadow).

**`logo_href`:** Optionally set `"logo_href": "https://example.com/"` in a theme file to make the header logo and breadcrumb link to a custom URL instead of the default.

### Funny Messages

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
- **External JS**: Leaflet.js via cdnjs (map, loaded at page start)
- **API Calls on Load**: 1 (ipapi.co); all other calls are user-initiated
- **Theme Loading**: All theme JSON files fetched in parallel on first load; cached by the service worker

## Security & Privacy

### What We Collect
- Your IP address (via API, not stored by us)
- Browser/device information (client-side only)
- Lookup history stored locally in your own browser's `localStorage` — never sent anywhere

### What We Don't Do
- ❌ No tracking cookies
- ❌ No analytics
- ❌ No server-side data storage
- ❌ No third-party tracking
- ❌ No authentication required

### API Privacy
- **ipapi.co** — [Privacy Policy](https://ipapi.co/privacy/)
- **ipwho.is** — [Privacy Policy](https://ipwho.is/)
- **ipinfo.io** — [Privacy Policy](https://ipinfo.io/privacy-policy)
- **dns.google** — [Google Privacy Policy](https://policies.google.com/privacy)
- **OpenStreetMap** — [Privacy Policy](https://wiki.osmfoundation.org/wiki/Privacy_Policy)
- **GlobalPing** — [Privacy Policy](https://www.globalping.io/privacy)
- **RIPEstat** — [RIPE NCC Privacy Statement](https://www.ripe.net/about-us/legal/ripe-ncc-privacy-statement/)

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

**Issue**: Traceroute shows no map
**Solution**: The GlobalPing API requires at least 2 public (non-private) hops with resolvable geolocation; a text hop list is always shown as a fallback

**Issue**: Fonts not loading
**Solution**: Ensure fonts.googleapis.com is reachable; site falls back to system monospace fonts gracefully

**Issue**: Mobile layout broken
**Solution**: Clear browser cache and hard refresh (Ctrl+Shift+R)

**Issue**: Theme not appearing after adding a custom JSON file
**Solution**: Confirm the entry is added to `themes/index.json` and `sw.js` APP_SHELL, the `CACHE_NAME` version is bumped, and the filename matches; check the browser console for fetch errors

## Roadmap

### Completed
- [x] PWA capabilities (offline mode) — service worker, manifest, installable
- [x] Wider desktop layout — container expanded to 1000px
- [x] Multi-provider fallback — ipapi.co → ipwho.is → ipinfo.io for both IP detection and WHOIS
- [x] WHOIS fallback resilience — isolated per-provider error handling
- [x] Dark / light mode — WGUS Dark and WGUS Light themes
- [x] JSON theme file system — community themes loadable without code changes
- [x] Theme library — 25 themes including CRT, retro, and popular developer palettes
- [x] Hamburger theme menu — clean dropdown replacing the inline toggle button
- [x] Share / permalink — `?ip=1.2.3.4` auto-runs lookup on page load
- [x] CIDR / subnet calculator
- [x] Traceroute visualization — hops plotted on map via GlobalPing API
- [x] ASN lookup — dedicated AS info panel via RIPEstat
- [x] IP comparison — two IPs side by side with diff highlighting
- [x] Bulk IP lookup — up to 20 IPs, CSV export
- [x] Lookup history — activity chart, IP address history, recent lookups log

## Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Ensure all themes remain fully functional after any CSS changes
- Ensure mobile responsiveness
- Test on multiple browsers
- New themes: add JSON file + entry in `themes/index.json` + entry in `sw.js` APP_SHELL + bump cache version

## License

This project is licensed under the **MIT License**.

**✅ You CAN:** use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies — including commercially
**📋 Requirements:** include the original copyright notice and license text in any distribution

For the full license text, see the [LICENSE](LICENSE) file.

## Credits

### Built By
**We Got Us Some Industries** — [wegotussome.com](https://wegotussome.com)

### APIs & Services
- [ipapi.co](https://ipapi.co) — Primary IP geolocation & WHOIS
- [ipwho.is](https://ipwho.is) — Fallback provider #1
- [ipinfo.io](https://ipinfo.io) — Fallback provider #2
- [dns.google](https://dns.google) — DNS-over-HTTPS (PTR records, DNSBL)
- [OpenStreetMap](https://openstreetmap.org) — Map tiles
- [GlobalPing](https://www.globalping.io/) — Traceroute measurements
- [RIPEstat](https://stat.ripe.net/) — ASN / Autonomous System data

### Libraries
- [Leaflet.js](https://leafletjs.com) — Interactive maps
- [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) — Google Fonts

### Inspiration
- Retro terminal aesthetics
- Hacker culture / command-line interfaces
- 1980s CRT monitors and home computers

## Support

- **Issues**: [GitHub Issues](https://github.com/arelas/WeGotUsYourIP/issues)

---

**© 2026 We Got Us Some Industries. All packets reserved.**

Made with 💚 and terminal green

> "We got us your IP... but don't worry, we're white hat... probably."
