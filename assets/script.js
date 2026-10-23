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


  // ---- compliance calendar (shared with kunaldarwani.com)
  var MON=['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var today=new Date(); today.setHours(0,0,0,0);
  function dt(s){ var p=s.split('-'); return new Date(+p[0],+p[1]-1,+p[2]); }
  var ledger=document.querySelector('.ledger'), table=document.querySelector('.cal-dated'), showPast=document.getElementById('showPast'), lawSel='all';
  function el(tag,cls,txt){ var e=document.createElement(tag); if(cls) e.className=cls; if(txt!=null) e.textContent=txt; return e; }
  function applyLedger(){
    if(!ledger) return; var n=+ledger.getAttribute('data-upcoming')||6, shown=0;
    ledger.querySelectorAll('li').forEach(function(li){ var ok=dt(li.dataset.date)>=today && shown<n; if(ok) shown++; li.hidden=!ok; });
  }
  function applyTable(){
    if(!table) return; var any=false;
    table.querySelectorAll('tr[data-date]').forEach(function(tr){
      var past=dt(tr.dataset.date)<today; tr.classList.toggle('is-past',past);
      var hide=(past && !(showPast&&showPast.checked)) || (lawSel!=='all' && tr.dataset.law!==lawSel);
      tr.hidden=hide; if(!hide) any=true;
    });
  }
  function render(items){
    items=items.filter(function(i){ return i && /^\d{4}-\d{2}-\d{2}$/.test(i.date) && i.law && i.what; }).sort(function(a,b){ return a.date<b.date?-1:1; });
    if(!items.length) return;
    if(ledger){ ledger.textContent=''; items.forEach(function(i){
      var li=el('li'); li.dataset.date=i.date; li.dataset.law=i.law;
      var t=el('time'); t.setAttribute('datetime',i.date); t.appendChild(el('b',null,i.date.slice(8,10))); t.appendChild(document.createTextNode(MON[+i.date.slice(5,7)]));
      var sp=el('span'); sp.appendChild(el('small',null,i.law)); sp.appendChild(document.createTextNode(i.what));
      li.appendChild(t); li.appendChild(sp); ledger.appendChild(li); }); applyLedger(); }
    if(table){ var tb=table.querySelector('tbody'); tb.textContent=''; items.forEach(function(i){
      var tr=el('tr'); tr.dataset.date=i.date; tr.dataset.law=i.law; var d=dt(i.date);
      tr.appendChild(el('td','day',('0'+d.getDate()).slice(-2)+' '+MON[d.getMonth()+1]+' '+d.getFullYear()));
      var td=el('td'); td.appendChild(el('span','tag',i.law)); tr.appendChild(td); tr.appendChild(el('td',null,i.what)); tb.appendChild(tr); }); applyTable(); }
  }
  applyLedger(); applyTable();
  showPast && showPast.addEventListener('change', applyTable);
  document.querySelectorAll('[data-law-filter]').forEach(function(b){ b.addEventListener('click', function(){
    lawSel=b.getAttribute('data-law-filter'); document.querySelectorAll('[data-law-filter]').forEach(function(x){ x.classList.toggle('is-on', x===b); }); applyTable(); }); });
  var src=(ledger||table)&&(ledger||table).getAttribute('data-compliance-src');
  if(src && window.fetch){ fetch(src,{cache:'no-cache'}).then(function(r){ return r.ok?r.json():null; }).then(function(d){ if(d&&d.items) render(d.items); }).catch(function(){}); }

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
