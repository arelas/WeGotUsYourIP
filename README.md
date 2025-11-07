# We Got Us Your IP

> A terminal-styled IP address lookup and network analysis tool with hacker aesthetics

[![Version](https://img.shields.io/badge/version-1.0-green.svg)](https://github.com/arelas/ip_wegotussome_com)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE)

**Live Demo**: [ip.wegotussome.com](https://ip.wegotussome.com)

![Screenshot](https://ip.wegotussome.com/screenshot.png)

## Overview

**We Got Us Your IP** is a single-page web application that provides comprehensive IP address analysis and network information. Built with a dark terminal aesthetic, it offers instant IP detection, WHOIS lookups, security checks, and browser fingerprinting - all in a sleek, retro-futuristic interface.

### Key Features

- 🎯 **Instant IP Detection** - Automatically displays your IP address on page load
- 🔒 **VPN/Proxy Detection** - Identifies if you're behind a VPN or proxy
- 📋 **One-Click Copy** - Copy your IP to clipboard instantly
- 🔍 **WHOIS Lookup** - Detailed network registration information for any IP
- 🛡️ **Blacklist Check** - Basic security scanning with links to comprehensive tools
- 🖥️ **Browser Fingerprinting** - Detailed analysis of your device and browser
- 📊 **Export Data** - Download all collected data as JSON
- 🚀 **Quick Tools** - Direct links to speed tests, DNS checks, and more

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
- Timezone and UTC offset
- Currency information
- Network type and usage classification

### Blacklist Security Check
- Basic heuristic security analysis
- Links to comprehensive blacklist services:
  - AbuseIPDB
  - MXToolbox
  - Spamhaus
- Quick reputation assessment

### Browser Fingerprint
Comprehensive device and browser analysis:
- Browser type and version
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
- Perfect for documentation and record-keeping

## Design Philosophy

The site embraces a **dark hacker/terminal aesthetic** with:
- Terminal green (#00ff66) on pure black
- CRT scanline effects
- Retro phosphor text glow
- Monospace typography (Courier New)
- Command-line style interface
- Smooth animations and transitions

## Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom animations, flexbox, media queries
- **Vanilla JavaScript** - ES6+, async/await, no frameworks

### APIs
- **ipapi.co** - Primary IP geolocation data
- **ipwhois.app** - WHOIS lookup information

### Browser APIs
- Clipboard API (copy functionality)
- Navigator API (device fingerprinting)
- Intl API (timezone detection)

## Installation

### Quick Deploy (Recommended)

Simply upload `index.html` to your web server. That's it! No build process, no dependencies.

```bash
# Upload to your server
scp index.html user@yourserver.com:/var/www/ip.wegotussome.com/

# Or use FTP, cPanel, or any file transfer method
```

### Local Development

```bash
# Clone the repository
git clone https://github.com/wegotussome/ip.git
cd ip

# Open in browser
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

1. **Visit the site** - Your IP is automatically detected and displayed
2. **Copy your IP** - Click the "COPY IP" button
3. **Explore features** - Use the four main buttons:
   - **WHOIS MY IP** - Detailed lookup of your IP
   - **CHECK BLACKLIST** - Security reputation check
   - **BROWSER INFO** - Device fingerprint analysis
   - **EXPORT DATA** - Download JSON report

### Custom IP Lookup

1. Enter any IP address in the input field
2. Click "WHOIS LOOKUP"
3. View detailed information about that IP

### Quick Tools

Use the bottom toolbar for instant access to:
- **Speed Test** - Check your connection speed
- **DNS Check** - Verify DNS propagation
- **MX Toolbox** - Email and network diagnostics
- **Port Scanner** - Check open ports

## Configuration

### API Keys

The site uses free public APIs by default. For production use with high traffic, consider:

1. **ipapi.co** - Get an API key at [ipapi.co](https://ipapi.co)
2. **ipwhois.app** - No API key required

To add an API key, update the fetch URLs in `index.html`:

```javascript
// Line ~960
const response = await fetch('https://ipapi.co/json/?key=YOUR_KEY_HERE');
```

### Customization

#### Change Color Scheme
Edit CSS variables around line 20:

```css
/* Primary color (terminal green) */
color: #00ff66;
border: 1px solid #00ff66;

/* Change to blue */
color: #00bfff;
border: 1px solid #00bfff;
```

#### Modify Funny Messages
Edit the `funnyMessages` array around line 715:

```javascript
const funnyMessages = [
    "> ACCESS GRANTED. Welcome to the system...",
    "> Add your own messages here!",
];
```

## Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Fully Supported |
| Firefox | 88+ | ✅ Fully Supported |
| Safari | 14+ | ✅ Fully Supported |
| Edge | 90+ | ✅ Fully Supported |
| Opera | 76+ | ✅ Fully Supported |

**Note**: Clipboard API requires HTTPS in production.

## Mobile Support

Fully responsive design optimized for:
- ✅ Desktop (1920px+)
- ✅ Tablets (768px - 1024px)
- ✅ Mobile (320px - 767px)

Touch-friendly interface with:
- Full-width buttons on mobile
- Optimized font sizes
- Vertical stacking for better readability

## Performance

- **Load Time**: < 1 second (excluding API calls)
- **File Size**: ~30KB (single HTML file)
- **API Calls**: 1-2 per page load
- **No External Dependencies**: Pure vanilla JavaScript

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
Data is fetched from:
- **ipapi.co** - [Privacy Policy](https://ipapi.co/privacy/)
- **ipwhois.app** - [Privacy Policy](https://ipwhois.app/privacy)

## Troubleshooting

### Common Issues

**Issue**: IP not detecting  
**Solution**: Check internet connection and ensure APIs are accessible

**Issue**: Copy button not working  
**Solution**: Ensure you're using HTTPS or localhost (Clipboard API requirement)

**Issue**: WHOIS data not loading  
**Solution**: Verify ipwhois.app API is accessible, try a different IP

**Issue**: Mobile layout broken  
**Solution**: Clear browser cache and hard refresh (Ctrl+Shift+R)

## Roadmap

### Version 1.x (Planned)
- [ ] Reverse DNS lookup
- [ ] IP geolocation map integration
- [ ] Historical data charts
- [ ] More comprehensive blacklist checking
- [ ] API rate limit handling

### Version 2.0 (Future)
- [ ] Multi-language support
- [ ] Dark/light theme toggle
- [ ] PWA capabilities (offline mode)
- [ ] User accounts (optional)
- [ ] Bulk IP lookup

## Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Maintain the terminal aesthetic
- Keep the single-file structure
- Ensure mobile responsiveness
- Test on multiple browsers
- Update VERSION_NOTES.md

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** (CC BY-NC-SA 4.0).

### What This Means:

**✅ You CAN:**
- Use the site for personal, educational, or non-commercial purposes
- Modify and adapt the code
- Share the code with others
- Create derivative works

**❌ You CANNOT:**
- Use it for commercial purposes
- Sell the code or derivatives
- Monetize it in any way
- Remove attribution to We Got Us Some Industries

**📋 Requirements:**
- Give appropriate credit
- Link to the license
- Indicate if changes were made
- Share derivatives under the same license

For the full license text, see the [LICENSE](LICENSE) file or visit:  
https://creativecommons.org/licenses/by-nc-sa/4.0/

**Have a legitimate commercial use case?** Contact us to discuss licensing options.

## Credits

### Built By
**We Got Us Some Industries**  
Website: [wegotussome.com](https://wegotussome.com)

### APIs & Services
- [ipapi.co](https://ipapi.co) - IP Geolocation
- [ipwhois.app](https://ipwhois.app) - WHOIS Data

### Inspiration
- Retro terminal aesthetics
- Hacker culture
- Command-line interfaces
- 1980s CRT monitors

## Support

- **Website**: [wegotussome.com](https://wegotussome.com)
- **Issues**: [GitHub Issues](https://github.com/wegotussome/ip/issues)
- **Email**: support@wegotussome.com

## Acknowledgments

Thanks to:
- The open-source community
- API providers (ipapi.co, ipwhois.app)
- All contributors and users
- Coffee ☕

---

**© 2025 We Got Us Some Industries. All packets reserved.**

Made with 💚 and terminal green

> "We got us your IP... but don't worry, we're white hat... probably."
