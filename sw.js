/* sw.js - le foto gia' viste restano in memoria nel browser (e si aggiornano in silenzio);
   pagine e script vengono sempre presi freschi dalla rete, cosi' le modifiche al sito si vedono subito. */
var CACHE="tyche-img-v1";
self.addEventListener("install",function(){ self.skipWaiting(); });
self.addEventListener("activate",function(e){
  e.waitUntil(caches.keys().then(function(k){ return Promise.all(k.filter(function(n){ return n!==CACHE; }).map(function(n){ return caches.delete(n); })); }).then(function(){ return self.clients.claim(); }));
});
self.addEventListener("fetch",function(e){
  var req=e.request, url=new URL(req.url);
  if(req.method!=="GET"||url.origin!==location.origin) return;
  if(!/\.(webp|png|jpe?g)$/i.test(url.pathname)) return;   /* solo immagini: tutto il resto va in rete normalmente */
  e.respondWith(caches.open(CACHE).then(function(c){
    return c.match(req).then(function(hit){
      var net=fetch(req).then(function(res){ if(res&&res.ok) c.put(req,res.clone()); return res; }).catch(function(){ return hit; });
      return hit||net;
    });
  }));
});
