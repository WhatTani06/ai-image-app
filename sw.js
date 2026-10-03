// PWA用 Service Worker
self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  return self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  // キャッシュ制御なしでそのままネットワークリクエストを通す
  e.respondWith(fetch(e.request));
});
