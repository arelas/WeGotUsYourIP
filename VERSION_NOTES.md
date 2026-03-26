## Version 1.2

### Summary
Four v1.x roadmap items completed: Reverse DNS lookup, interactive geolocation map, comprehensive real DNSBL blacklist checking, and API rate limit handling with automatic fallback. Theme toggle overlap bug fixed in WGUS mode.

### New Features

#### Reverse DNS Lookup (`> REVERSE DNS`)
- PTR record lookup via `dns.google/resolve` (DNS-over-HTTPS, no API key required)
- Handles IPv4 (reversed octets → `.in-addr.arpa`) and IPv6 (nibble format → `.ip6.arpa`)
- Displays all resolved hostnames and TTL; clean "not configured" message if no PTR exists

#### Geolocation Map (`> VIEW MAP`)
- Leaflet.js 1.9.4 + OpenStreetMap tiles via cdnjs — no API key, no cost
- Custom marker uses the active theme's `--accent` CSS variable with a glow effect
- Popup shows IP, city, country; coordinates displayed in a bar below the map
- `invalidateSize()` called after reveal to prevent the blank-tile issue on first open
- Map recenters correctly on subsequent opens without re-initializing

#### Comprehensive Blacklist Check (`> CHECK BLACKLIST`)
- Replaced the previous heuristic org-name check with real DNSBL queries
- 5 lists queried in parallel via `dns.google/resolve`: Spamhaus ZEN, Barracuda Reputation, SORBS, SpamCop, UCEProtect L1
- UI updates live as each result resolves — no waiting for all 5 to complete
- CLEAN / LISTED / ERROR badge per list; overall ✓ CLEAN / ✗ N LISTED summary at top
- AbuseIPDB shown as a manual link (their API requires a paid account key)
- IPv6: DNSBL is IPv4-only by spec; shows manual links for all lists gracefully

#### API Rate Limit Handling
- Primary provider: ipapi.co (unchanged)
- On HTTP 429: visible red banner appears immediately with a 60-second live countdown
- After countdown: automatically retries with `ipwho.is` (free, HTTPS, no key required)
- ipwho.is response normalized to ipapi.co field shape — WHOIS, map, RDNS all work transparently with fallback data
- Small "Data via fallback provider" note shown in IP display if fallback was used

### Bug Fixes

#### WGUS Theme Toggle Overlap
- **Problem**: The fixed `position: fixed; top: 16px; right: 16px` theme toggle button overlapped the `self-hosted` badge in the WGUS header. Additionally, the `#wgus-header` CSS selector had been dropped in a prior edit, leaving its layout declarations as orphaned/ignored rules — causing the header to appear in both themes.
- **Fix**: Restored the `#wgus-header { display: none }` default rule and `body.theme-wgus #wgus-header { display: flex }` override. In WGUS mode, the floating fixed button is hidden (`display: none`) and a `.wgus-header-toggle` button is rendered inside the header, right-aligned alongside the `self-hosted` badge. Both buttons call the same `toggleTheme()` and `applyTheme()` keeps their labels in sync.

### Architecture Changes

#### Section Toggle Refactor
Replaced 5 separate copy-pasted toggle event listeners with a declarative `SECTIONS` registry:

```javascript
const SECTIONS = {
    whois:       { el, btn, closed, open, fn },
    rdns:        { el, btn, closed, open, fn },
    map:         { el, btn, closed, open, fn },
    blacklist:   { el, btn, closed, open, fn },
    fingerprint: { el, btn, closed, open, fn },
};
```

`toggleSection(key)` and `closeAllSections(except)` handle all open/close/label logic. Adding future sections requires one object entry.

### Dependencies Added
- **Leaflet.js 1.9.4** — loaded via cdnjs `<link>` + `<script>` in `<head>`
- **ipwho.is** — runtime fallback only, no script tag

### Roadmap Status
All v1.x items completed. Remaining future items moved to Version 2.0.

---

# We Got Us Your IP - Version History

---

## Version 1.1

### Summary
Bug fixes across WHOIS, blacklist check, browser detection, and IPv6 validation. Addition of a dual-theme system (Terminal / WGUS) with persistent preference via localStorage.

### Bug Fixes

#### WHOIS Lookup — API Replaced
- **Problem**: `getWhoisData()` used `ipwhois.app`, which is unreliable on the free tier (CORS failures, aggressive rate limiting, silent errors with no loading state)
- **Fix**: Switched to `ipapi.co/{ip}/json/` — the same provider as the main IP lookup, already confirmed to work in this context. Field mappings updated (`country_name`, `utc_offset`, `currency_name`, `calling_code`, etc.). A loading indicator now shows while the request is in-flight and errors are surfaced visually.

#### Blacklist Check — Dead Code Removed
- **Problem**: `checkBlacklist()` made a fetch to `ipqualityscore.com/api/json/ip/YOUR_KEY_HERE/{ip}` — a literal placeholder that was never replaced, causing the request to always fail silently. It then fell through to a second call to `ipwhois.app` (also unreliable).
- **Fix**: Both broken calls replaced with a single clean `ipapi.co` fetch. Loading state added. Heuristic check updated to use `org` field.

#### Browser Detection — Edge Misidentification Fixed
- **Problem**: The user-agent string for Edge contains `"Chrome"`, so the original `if Chrome → else if Edge` chain always matched Chrome first for Edge users.
- **Fix**: Check order corrected to `Edg/ → Edge/ → Firefox → Chrome → Safari`.

#### IPv6 Validation — Compressed Notation Fixed
- **Problem**: The IPv6 regex (`/^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}$/`) required exactly 8 full groups, rejecting any compressed address like `::1` or `2001:db8::1`.
- **Fix**: Replaced with a full RFC-compliant regex supporting all valid IPv6 forms including compressed, loopback, link-local, and IPv4-mapped addresses.

### New Features

#### Dual Theme System
- **Terminal** (default) — original dark hacker aesthetic unchanged
- **WGUS** — brand-consistent theme matching wegotussome.com and qrcodes.wegotussome.com, built from the actual QR tool source:
  - Accent: `#e8ff47` (yellow-green)
  - Text: `#f0f0f0`, Muted: `#666`, Border: `#222`
  - Syne (headings/values) + JetBrains Mono (labels/UI)
  - SVG fractalNoise texture overlay (matching QR tool)
  - Breadcrumb nav header: `wegotussome / ip` with animated pulse dot and `self-hosted` badge
  - Hover states: accent-fill with black text (matching `.generate-btn` pattern)
  - Scanlines and vignette disabled
  - 4px border-radius throughout
- **Toggle button** fixed top-right, adapts its appearance per theme (animated dot in WGUS mode)
- **Preference persisted** via `localStorage` key `wgus-ip-theme`

### CSS Architecture Change
All hardcoded color values replaced with CSS custom properties:

| Variable | Terminal | WGUS |
|---|---|---|
| `--accent` | `#00ff66` | `#e8ff47` |
| `--text` | `#00ff66` | `#f0f0f0` |
| `--muted` | `rgba(0,255,102,0.5)` | `#666666` |
| `--border` | `#00ff66` | `#222222` |
| `--page-bg` | `#0a0a0a` | `#0a0a0a` |
| `--surface` | `#0d0d0d` | `#111111` |
| `--inner-bg` | `#000000` | `#111111` |
| `--danger` | `#ff0000` | `#e05252` |
| `--font-body` | `Courier New` | `JetBrains Mono` |
| `--font-head` | `Courier New` | `Syne` |
| `--scanlines` | CRT gradient | `none` |
| `--vignette` | radial gradient | `none` |

### API Changes
- **Removed**: `ipwhois.app` (WHOIS), `ipqualityscore.com` (blacklist)
- **Now using**: `ipapi.co` for all lookups (IP info, WHOIS, blacklist heuristic)

### File Size
~35KB (up from ~30KB due to theme CSS and Google Fonts link)

---

## Version 1.0 (Initial Release)

### Site Information
- **URL**: ip.wegotussome.com
- **Name**: We Got Us Your IP
- **Theme**: Dark hacker/terminal aesthetic
- **Status**: Baseline version

### Core Features

#### 1. IP Address Display
- Automatically detects and displays user's IP address on page load
- Shows basic information:
  - ISP
  - Location (City, Region)
  - Country
  - Timezone
  - Postal Code
  - Protocol (IPv4/IPv6)
  - Connection Type
  - ASN Number

#### 2. VPN/Proxy Detection
- Real-time detection badge
- Red badge: VPN/Proxy detected
- Green badge: Clean connection
- Based on ISP name analysis

#### 3. Connection Type Detection
- Automatically categorizes connection as:
  - Residential
  - Mobile
  - Data Center
  - Corporate

#### 4. Copy IP Button
- One-click copy to clipboard
- Visual confirmation ("COPIED!" feedback)
- Large, prominent button on desktop
- Full-width on mobile

#### 5. WHOIS Lookup
- Toggle button to show/hide detailed WHOIS data
- Works with user's own IP
- Custom IP address lookup via input field
- Displays comprehensive data:
  - Geographic coordinates (latitude/longitude)
  - Organization details
  - ASN information
  - UTC offset
  - Currency information
  - Continent, region, city details

#### 6. Blacklist Check
- Basic heuristic security check
- Status indicator (Clean/Suspicious)
- Links to external blacklist checking services:
  - AbuseIPDB
  - MXToolbox
  - Spamhaus

#### 7. Browser Fingerprint
- Detailed device and browser information:
  - Browser type
  - Operating System
  - Platform
  - Language settings
  - Screen resolution & color depth
  - CPU cores
  - Device memory
  - Touch points
  - Cookie settings
  - Do Not Track status
  - Timezone information

#### 8. Export Functionality
- Download all collected data as JSON
- Includes:
  - IP data
  - Browser fingerprint
  - Timestamp
- Filename format: `ip-report-{IP}-{timestamp}.json`

#### 9. Quick Tools
- External links to useful network tools:
  - Speed Test (fast.com)
  - DNS Check (dnschecker.org)
  - MX Toolbox
  - Port Scanner

### Design Elements

#### Color Scheme
- Primary: Terminal Green (#00ff66)
- Background: Pure Black (#0a0a0a)
- Containers: Dark Gray (#0d0d0d, #1a1a1a)
- Accent: Red for VPN/warnings (#ff0000)

#### Visual Effects
- CRT scanline effect
- Screen flicker animation on title
- Green phosphor glow on text and borders
- Blinking cursor in subtitle
- Smooth transitions and hover effects
- Terminal-style loading animations

#### Typography
- Font: Courier New (monospace)
- Terminal-style brackets and arrows (>, [, ])
- Upper-case labels for emphasis
- Letter-spacing for readability

#### Responsive Design
- Desktop optimized layout
- Mobile-friendly (tested on 768px and 480px breakpoints)
- Buttons stack vertically on mobile
- IP address scales appropriately
- Touch-friendly button sizes

### Technical Implementation

#### APIs Used
- **ipapi.co**: Primary IP geolocation data
- **ipwhois.app**: WHOIS data lookup *(replaced in v1.1)*

#### Browser APIs
- Clipboard API (copy functionality)
- Navigator API (browser fingerprinting)
- LocalStorage (theme preference, added in v1.1)
- Intl API (timezone detection)

#### JavaScript Features
- Async/await for API calls
- Error handling with user feedback
- IP validation (IPv4 and IPv6)
- Dynamic content generation
- Event listeners for interactivity
- Real-time timestamp updates

### Known Limitations (at v1.0)
1. Blacklist check is basic heuristic (not comprehensive)
2. VPN detection based on ISP name patterns (not foolproof)
3. Requires API availability
4. WHOIS used unreliable provider *(fixed in v1.1)*
5. Edge browser misidentified as Chrome *(fixed in v1.1)*
6. IPv6 compressed notation rejected by validator *(fixed in v1.1)*

### File Structure
```
index.html (single-file application)
├── HTML Structure
├── CSS Styling (embedded)
└── JavaScript Logic (embedded)
```

### Copyright & Attribution
© 2025 We Got Us Some Industries  
Website: https://wegotussome.com  
All packets reserved.
