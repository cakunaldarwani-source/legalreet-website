(function(){
  // ---- desktop mega menu / dropdowns (click + hover)
  var items = document.querySelectorAll('.has-mega, .has-drop');
  function closeAll(except){ items.forEach(function(li){ if(li!==except){ li.classList.remove('open'); var b=li.querySelector('.nav-trigger'); if(b) b.setAttribute('aria-expanded','false'); } }); }
  items.forEach(function(li){
    var btn = li.querySelector('.nav-trigger'); var t;
    btn.addEventListener('click', function(e){ e.stopPropagation(); var open = !li.classList.contains('open'); closeAll(li); li.classList.toggle('open', open); btn.setAttribute('aria-expanded', open); });
    li.addEventListener('mouseenter', function(){ if(window.matchMedia('(hover:hover)').matches){ clearTimeout(t); closeAll(li); li.classList.add('open'); btn.setAttribute('aria-expanded','true'); } });
    li.addEventListener('mouseleave', function(){ if(window.matchMedia('(hover:hover)').matches){ t=setTimeout(function(){ li.classList.remove('open'); btn.setAttribute('aria-expanded','false'); },140); } });
  });
  document.addEventListener('click', function(e){ if(!e.target.closest('.has-mega, .has-drop')) closeAll(); });
  document.addEventListener('keydown', function(e){ if(e.key==='Escape'){ closeAll(); closeDrawer(); } });

  // ---- mobile drawer
  var drawer = document.getElementById('mDrawer'), openBtn = document.getElementById('mOpen'), closeBtn = document.getElementById('mClose');
  function openDrawer(){ if(!drawer) return; drawer.hidden=false; document.body.style.overflow='hidden'; closeBtn && closeBtn.focus(); }
  function closeDrawer(){ if(!drawer || drawer.hidden) return; drawer.hidden=true; document.body.style.overflow=''; openBtn && openBtn.focus(); }
  openBtn && openBtn.addEventListener('click', openDrawer);
  closeBtn && closeBtn.addEventListener('click', closeDrawer);

  // ---- package tabs
  document.querySelectorAll('.tabs').forEach(function(tabs){
    var btns = tabs.querySelectorAll('[role=tab]');
    btns.forEach(function(b){ b.addEventListener('click', function(){
      btns.forEach(function(x){ x.setAttribute('aria-selected','false'); var p=document.getElementById(x.dataset.tab); if(p) p.hidden=true; });
      b.setAttribute('aria-selected','true'); var p=document.getElementById(b.dataset.tab); if(p) p.hidden=false;
    }); });
  });

  // ---- service search (needs search-index.js, loaded lazily)
  var forms = document.querySelectorAll('[data-search]');
  if (forms.length){
    var s = document.createElement('script'); s.src='/assets/search-index.js'; s.onload=init; document.head.appendChild(s);
  }
  function norm(x){ return (x||'').toLowerCase(); }
  function init(){
    var data = window.LR_SERVICES || [];
    forms.forEach(function(form){
      var input = form.querySelector('input[type=search]'), box = form.querySelector('.search-results'), filter = form.hasAttribute('data-filter');
      var params = new URLSearchParams(location.search); if(params.get('q') && filter){ input.value = params.get('q'); }
      function run(){
        var q = norm(input.value.trim()), words = q.split(/\s+/).filter(Boolean);
        var hits = !words.length ? [] : data.filter(function(d){ var hay = norm(d.n+' '+d.c+' '+d.g+' '+d.k); return words.every(function(w){ return hay.indexOf(w) > -1; }); });
        if (filter){
          var cards = document.querySelectorAll('.cat-block .svc-card'), shown = 0, set = {};
          hits.forEach(function(h){ set[h.u]=1; });
          cards.forEach(function(card){ var ok = !words.length || set[card.getAttribute('href')]; card.classList.toggle('is-hidden', !ok); if(ok) shown++; });
          document.querySelectorAll('.cat-block').forEach(function(b){ b.classList.toggle('is-hidden', !b.querySelector('.svc-card:not(.is-hidden)')); });
          document.querySelectorAll('.grp-title').forEach(function(h){ var g=h.nextElementSibling; h.classList.toggle('is-hidden', g && !g.querySelector('.svc-card:not(.is-hidden)')); });
          var nr = document.querySelector('.no-results'); if(nr) nr.hidden = shown>0;
          return;
        }
        if (!hits.length){ box.hidden = true; box.innerHTML=''; return; }
        box.innerHTML = hits.slice(0,8).map(function(h){ return '<a href="'+h.u+'"><b>'+h.n+'</b><small>'+h.c+' · '+h.g+'</small></a>'; }).join('');
        box.hidden = false;
      }
      input.addEventListener('input', run);
      if (filter) run();
      form.addEventListener('submit', function(e){
        var first = box && box.querySelector('a');
        if (filter){ e.preventDefault(); return; }
        if (first){ e.preventDefault(); location.href = first.getAttribute('href'); }
      });
      document.addEventListener('click', function(e){ if(box && !form.contains(e.target)) box.hidden = true; });
    });
  }

  // ---- cookie consent
  var KEY='legalreet_consent', banner=document.getElementById('cookieBanner'), stored=null;
  try { stored = localStorage.getItem(KEY); } catch(e){}
  window.legalreetConsent = stored;
  if (banner && !stored) banner.hidden = false;
  function set(v){ try{ localStorage.setItem(KEY,v); }catch(e){} window.legalreetConsent=v; if(banner) banner.hidden=true; }
  var a=document.getElementById('cookieAccept'), d=document.getElementById('cookieDecline');
  a && a.addEventListener('click', function(){ set('accepted'); });
  d && d.addEventListener('click', function(){ set('declined'); });
})();
