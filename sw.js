const CACHE_NAME = 'wegotusyourip-v2';

const APP_SHELL = [
    './',
    './index.html',
    './manifest.json',
    './icon.svg',
    './themes/index.json',
    './themes/wgus-dark.json',
    './themes/wgus-light.json',
    './themes/dracula.json',
    './themes/nord.json',
    './themes/gruvbox-dark.json',
    './themes/tokyo-night.json',
    './themes/amber.json',
    './themes/white.json',
    './themes/terminal.json',
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js',
    'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap',
];

// API hostnames that should always be network-first (no offline cache)
const API_HOSTS = ['ipapi.co', 'ipwho.is', 'ipinfo.io', 'dns.google'];

// Tile/CDN hosts to cache aggressively (map tiles, fonts)
const CACHE_HOSTS = [
    'tile.openstreetmap.org',
    'a.tile.openstreetmap.org',
    'b.tile.openstreetmap.org',
    'c.tile.openstreetmap.org',
    'fonts.gstatic.com',
    'cdnjs.cloudflare.com',
    'fonts.googleapis.com',
];

// ── Install: pre-cache app shell ─────────────────────────────────────────────
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(APP_SHELL))
            .then(() => self.skipWaiting())
    );
});

// ── Activate: purge old caches ───────────────────────────────────────────────
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys()
            .then(keys => Promise.all(
                keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
            ))
            .then(() => self.clients.claim())
    );
});

// ── Fetch: routing strategies ────────────────────────────────────────────────
self.addEventListener('fetch', event => {
    const url = new URL(event.request.url);

    // API calls: network-only, return offline JSON on failure
    if (API_HOSTS.some(h => url.hostname.includes(h))) {
        event.respondWith(
            fetch(event.request).catch(() =>
                new Response(JSON.stringify({ error: 'offline', message: 'No network connection' }), {
                    status: 503,
                    headers: { 'Content-Type': 'application/json' },
                })
            )
        );
        return;
    }

    // Cacheable external resources: network-first, cache fallback
    if (CACHE_HOSTS.some(h => url.hostname.includes(h))) {
        event.respondWith(
            caches.open(CACHE_NAME).then(cache =>
                fetch(event.request)
                    .then(response => {
                        if (response.ok) cache.put(event.request, response.clone());
                        return response;
                    })
                    .catch(() => cache.match(event.request))
            )
        );
        return;
    }

    // App shell (same-origin): cache-first, network fallback
    if (url.origin === self.location.origin) {
        event.respondWith(
            caches.match(event.request).then(cached => {
                if (cached) return cached;
                return fetch(event.request).then(response => {
                    if (response.ok) {
                        caches.open(CACHE_NAME).then(cache => cache.put(event.request, response.clone()));
                    }
                    return response;
                });
            })
        );
        return;
    }
});
