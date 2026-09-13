(function(){
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links){
    toggle.addEventListener('click', function(){
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){ links.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); });
    });
  }

  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('in'); });
  }
})();

(function(){
  var KEY = 'legalreet_consent';
  var banner = document.getElementById('cookieBanner');
  if (!banner) return;

  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}
  window.legalreetConsent = stored;

  function show(){ banner.classList.add('visible'); document.body.classList.add('cookie-banner-visible'); }
  function hide(){ banner.classList.remove('visible'); document.body.classList.remove('cookie-banner-visible'); }

  if (!stored){ show(); }

  function set(value){
    try { localStorage.setItem(KEY, value); } catch (e) {}
    window.legalreetConsent = value;
    hide();
  }

  var acceptBtn = document.getElementById('cookieAccept');
  var declineBtn = document.getElementById('cookieDecline');
  if (acceptBtn) acceptBtn.addEventListener('click', function(){ set('accepted'); });
  if (declineBtn) declineBtn.addEventListener('click', function(){ set('declined'); });
})();
