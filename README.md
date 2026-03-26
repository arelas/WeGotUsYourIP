# We Got Us Your IP

> A single-page IP analysis tool with a terminal hacker aesthetic and an optional WGUS brand theme. Instantly detects your IP address and provides comprehensive network information including WHOIS data, VPN detection, security checks, and browser fingerprinting.

[![Version](https://img.shields.io/badge/version-1.1-green.svg)](https://github.com/arelas/ip_wegotussome_com)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE)

**Live Demo**: [ip.wegotussome.com](https://ip.wegotussome.com)

![Screenshot](https://ip.wegotussome.com/screenshot.png)

## Overview

**We Got Us Your IP** is a single-page web application that provides comprehensive IP address analysis and network information. It ships with two visual themes: the original dark terminal aesthetic and an optional WGUS brand theme that matches the look and feel of the broader wegotussome.com toolset. All features run entirely client-side with no build process required.

### Key Features

- **Instant IP Detection** - Automatically displays your IP address on page load
- **VPN/Proxy Detection** - Identifies if you're behind a VPN or proxy
- **One-Click Copy** - Copy your IP to clipboard instantly
- **WHOIS Lookup** - Detailed network registration information for any IP
- **Blacklist Check** - Basic security scanning with links to comprehensive tools
- **Browser Fingerprinting** - Detailed analysis of your device and browser
- **Export Data** - Download all collected data as JSON
- **Quick Tools** - Direct links to speed tests, DNS checks, and more
- **Dual Theme** - Toggle between Terminal and WGUS brand themes, preference persisted via localStorage

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
- Helps identify masked connections

### WHOIS Lookup
Query detailed registration information for any IP address:
- Geographic coordinates (latitude/longitude)
- Complete organization details
- ASN information
- Timezone and UTC offset
- Currency information
- Calling code
- Continent, region, city details

Powered by **ipapi.co** (same provider as the main IP lookup, ensuring reliability).

### Blacklist Security Check
- Basic heuristic security analysis against org/ASN data
- Status indicator (Clean/Suspicious)
- Links to comprehensive blacklist services:
  - AbuseIPDB
  - MXToolbox
  - Spamhaus

### Browser Fingerprint
Comprehensive device and browser analysis:
- Browser type and version (Edge/Chrome/Firefox/Safari correctly detected)
- Operating system
- Screen resolution and color depth
- CPU core count
- Device memory
- Touch capabilities
- Language settings
- Cookie and tracking preferences

### Data Export
- Download complete analysis as JSON
- Includes IP data, browser fingerprint, and timestamp
- Filename format: `ip-report-{IP}-{timestamp}.json`

### Theme Toggle
Switch between two visual themes via the button in the top-right corner. Your preference is saved to `localStorage` and restored on the next visit.

- **Terminal** — Original dark hacker aesthetic: terminal green (#00ff66) on pure black, CRT scanlines, phosphor glow, Courier New
- **WGUS** — Brand-consistent theme matching wegotussome.com and qrcodes.wegotussome.com: Syne + JetBrains Mono, yellow-green accent (#e8ff47), warm dark surfaces, SVG noise texture, breadcrumb header

## Design Philosophy

### Terminal Theme
Embraces a **dark hacker/terminal aesthetic** with:
- Terminal green (#00ff66) on pure black
- CRT scanline effects
- Retro phosphor text glow
- Monospace typography (Courier New)
- Command-line style interface

### WGUS Theme
Matches the **We Got Us Some Industries** brand system:
- Syne (headings) + JetBrains Mono (body/labels)
- Yellow-green accent (#e8ff47) on near-black surfaces (#0a0a0a / #111111)
- Three-tier color system: text (#f0f0f0), muted (#666), border (#222)
- SVG fractalNoise texture overlay
- 4px border-radius throughout
- Navigation breadcrumb header (`wegotussome / ip`)

## Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom properties (CSS variables), animations, flexbox, media queries
- **Vanilla JavaScript** - ES6+, async/await, no frameworks

### APIs
- **ipapi.co** - Primary IP geolocation data and WHOIS lookups

### Fonts (WGUS theme)
- **Syne** (Google Fonts) - Headings and values
- **JetBrains Mono** (Google Fonts) - Labels and UI text

### Browser APIs
- Clipboard API (copy functionality)
- Navigator API (device fingerprinting)
- localStorage (theme preference)
- Intl API (timezone detection)

## Installation

### Quick Deploy (Recommended)

Simply upload `index.html` to your web server. That's it — no build process, no dependencies.

```bash
scp index.html user@yourserver.com:/var/www/ip.wegotussome.com/
```

### Local Development

```bash
git clone https://github.com/wegotussome/ip.git
cd ip
open index.html

# Or use a local server
python -m http.server 8000
# Visit http://localhost:8000
```

### Requirements

- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- Internet connection for API calls
- HTTPS recommended (required for Clipboard API)

## Usage

### Basic Usage

1. **Visit the site** — Your IP is automatically detected and displayed
2. **Copy your IP** — Click the "COPY IP" button
3. **Explore features** — Use the four main buttons:
   - **WHOIS MY IP** — Detailed lookup of your IP
   - **CHECK BLACKLIST** — Security reputation check
   - **BROWSER INFO** — Device fingerprint analysis
   - **EXPORT DATA** — Download JSON report

### Custom IP Lookup

1. Enter any IP address in the input field (IPv4 or IPv6)
2. Click "WHOIS LOOKUP"
3. View detailed information about that IP

### Theme Toggle

Click the button in the top-right corner to switch between Terminal and WGUS themes. The choice is saved automatically.

### Quick Tools

Use the bottom toolbar for instant access to:
- **Speed Test** — fast.com
- **DNS Check** — dnschecker.org
- **MX Toolbox** — Email and network diagnostics
- **Port Scanner** — whatismyip.com port scanner

## Configuration

### API Keys

The site uses ipapi.co's free public tier by default. For production deployments with high traffic:

```javascript
// In getIPInfo() and getWhoisData()
const response = await fetch('https://ipapi.co/json/?key=YOUR_KEY_HERE');
const response = await fetch(`https://ipapi.co/${ip}/json/?key=YOUR_KEY_HERE`);
```

### Customization

#### Terminal Theme Colors
Edit the `:root` CSS variables block:

```css
:root {
    --accent:    #00ff66;  /* terminal green — change to any color */
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
    --accent:   #e8ff47;  /* yellow-green */
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

- **Load Time**: < 1 second (excluding API calls)
- **File Size**: ~35KB (single HTML file)
- **API Calls**: 1 per page load (ipapi.co)
- **No External JS Dependencies**: Pure vanilla JavaScript

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

## Troubleshooting

### Common Issues

**Issue**: IP not detecting  
**Solution**: Check internet connection and ensure ipapi.co is accessible

**Issue**: Copy button not working  
**Solution**: Ensure you're on HTTPS or localhost (Clipboard API requirement)

**Issue**: WHOIS data not loading  
**Solution**: Verify ipapi.co is accessible from your network; check browser console for errors

**Issue**: WGUS theme fonts not loading  
**Solution**: Ensure Google Fonts is reachable; the site falls back gracefully to system fonts

**Issue**: Mobile layout broken  
**Solution**: Clear browser cache and hard refresh (Ctrl+Shift+R)

## Roadmap

### Version 1.x (Planned)
- [ ] Reverse DNS lookup
- [ ] IP geolocation map integration
- [ ] Historical data charts
- [ ] More comprehensive blacklist checking
- [ ] API rate limit handling with user feedback

### Version 2.0 (Future)
- [ ] Multi-language support
- [ ] PWA capabilities (offline mode)
- [ ] Bulk IP lookup

## Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Maintain single-file structure
- Ensure both themes remain fully functional
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
- [ipapi.co](https://ipapi.co) — IP Geolocation & WHOIS

### Fonts
- [Syne](https://fonts.google.com/specimen/Syne) — Google Fonts
- [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) — Google Fonts

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
