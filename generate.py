# -*- coding: utf-8 -*-
"""LegalReet static site generator.

Run `python3 generate.py` (Netlify does this on every deploy). Service data
lives in services_data.py; blog posts in content/blog/*.md; compliance news in
content/news/*.md (both editable from /admin via Decap CMS).
"""
import os
import re
import json
import urllib.parse
from datetime import date, datetime

from services_data import CATEGORIES, SERVICES, GROUPS, PRICES
from site_pages import build_extra_pages

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://www.legalreet.com"
EMAIL = "hello@legalreet.com"
PHONE_DISPLAY = "+91 93683 75024"
PHONE_TEL = "+919368375024"
WHATSAPP_NUMBER = "919368375024"
HOURS = "Mon &ndash; Sat, 10:00 AM &ndash; 7:00 PM"
ADDRESS_HTML = "E-14, First Floor, Indrapuram, near Shankar Greens, Tajganj Phase II, Agra 282001, Uttar Pradesh"
TODAY = date.today()
YEAR = TODAY.year

# ----------------------------------------------------------------- data prep
CAT_BY_ID = {c["id"]: c for c in CATEGORIES}
SVC_BY_SLUG = {s["slug"]: s for s in SERVICES}
for cid, groups in GROUPS.items():
    for gname, slugs in groups:
        for sl in slugs:
            SVC_BY_SLUG[sl]["group"] = gname
for s in SERVICES:
    s["cat_name"] = CAT_BY_ID[s["cat"]]["name"]
    s["price"] = PRICES.get(s["slug"])

def ordered(cid):
    return [SVC_BY_SLUG[sl] for _, slugs in GROUPS[cid] for sl in slugs]

print(f"{len(CATEGORIES)} categories, {len(SERVICES)} services loaded.")

# ----------------------------------------------------------------- helpers
def E(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def EA(s):
    return E(s).replace('"', "&quot;")

def inr(n):
    s = str(int(n))
    if len(s) <= 3:
        return "&#8377;" + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head:
        parts.insert(0, head)
    return "&#8377;" + ",".join(parts + [tail])

def price_label(svc):
    return f"From <b>{inr(svc['price'])}</b>" if svc.get("price") else "<b>Get a quote</b>"

def svc_url(svc):
    return f"/services/{svc['slug']}.html"

def wa_link(text="Hi LegalReet, I would like to know more about your services."):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(text)}"

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ----------------------------------------------------------------- icons
def ico(name, cls="ico"):
    paths = {
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        "phone": '<path d="M6 3h3l2 5-2.5 1.5a11 11 0 005 5L15 12l5 2v3a2 2 0 01-2 2C9.5 19 5 14.5 5 5a2 2 0 011-2z"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "pin": '<path d="M12 21s7-6.5 7-12a7 7 0 10-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.4"/>',
        "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
        "chev": '<path d="M6 9l6 6 6-6"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
        "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
        "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2c2.8.3 5 2.6 5 5.8"/>',
        "rupee": '<path d="M7 5h10M7 9h10M9 5c4 0 5 4 0 4H7l7 10"/>',
        "track": '<path d="M4 12h4l2-6 4 12 2-6h4"/>',
        "doc": '<rect x="6" y="3" width="12" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/>',
        "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
        "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "close": '<path d="M6 6l12 12M18 6L6 18"/>',
        "book": '<path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2z"/><path d="M4 19V5"/>',
    }
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'

WA_SVG = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.4.6 4.6 1.8 6.6L4 29l7.6-2A12 12 0 0016 27c6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.6c-1.9 0-3.8-.5-5.4-1.5l-.4-.2-4.5 1.2 1.2-4.4-.3-.4A9.6 9.6 0 016.4 15c0-5.3 4.3-9.6 9.6-9.6s9.6 4.3 9.6 9.6-4.3 9.6-9.6 9.6zm5.3-7.2c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.6.1-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.4-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.4.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.1c-.2-.6-.5-.5-.6-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>'

LOGO = '<span class="logo-mark" aria-hidden="true">LR</span><span class="logo-text"><span>Legal<b>Reet</b></span><small>Legal &middot; Tax &middot; Compliance</small></span>'

# ----------------------------------------------------------------- chrome
LEARN_LINKS = [
    ("Blog", "/blog/index.html", "Filing guides and explainers"),
    ("Compliance News", "/news.html", "Deadlines, extensions and updates"),
    ("Compliance Calendar", "/compliance-calendar.html", "Every recurring due date, month by month"),
    ("Document Checklists", "/document-checklist.html", "What to keep ready for each service"),
    ("LegalReet Academy", "/academy.html", "Practical accounting and tax training"),
    ("Courses", "/courses.html", "Foundation, Practitioner and Advanced tracks"),
    ("FAQs", "/faq.html", "Answers to the questions we hear most"),
]

def topbar():
    return f'''<div class="topbar"><div class="container topbar-in">
  <div class="topbar-contact">
    <a href="mailto:{EMAIL}">{ico("mail")}{EMAIL}</a>
    <a href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a>
    <span class="hide-sm">{ico("clock")}{HOURS}</span>
  </div>
  <div class="topbar-links hide-sm">
    <a href="/partner.html">Partner with us</a>
    <a href="/payment-options.html">Pay now</a>
    <a href="/grievance.html" class="hide-sm">Grievance</a>
  </div>
</div></div>'''

NAV_LABELS = {"a": "Start a Business", "b": "Registrations", "c": "Manage Business", "d": "Documents"}

def mega_menu():
    items = []
    for c in CATEGORIES:
        cols = []
        for gname, slugs in GROUPS[c["id"]]:
            links = "".join(f'<a href="{svc_url(SVC_BY_SLUG[s])}">{E(SVC_BY_SLUG[s]["name"])}</a>' for s in slugs)
            cols.append(f'<div class="mega-col"><h6>{E(gname)}</h6>{links}</div>')
        items.append(f'''<li class="has-mega"><button class="nav-trigger" type="button" aria-expanded="false">{NAV_LABELS[c["id"]]}{ico("chev","chev")}</button>
      <div class="mega"><div class="container mega-in">{"".join(cols)}</div>
      <div class="container mega-foot"><span>{E(c["tagline"])}</span><a href="/services/index.html#cat-{c["id"]}">All {len(ordered(c["id"]))} services in {E(c["name"])} &rarr;</a></div></div></li>''')
    learn = "".join(f'<a href="{u}"><b>{E(n)}</b><span>{E(d)}</span></a>' for n, u, d in LEARN_LINKS)
    items.append(f'''<li class="has-drop"><button class="nav-trigger" type="button" aria-expanded="false">Learn{ico("chev","chev")}</button>
      <div class="drop">{learn}</div></li>''')
    items.append('<li><a class="nav-link" href="/about.html">About</a></li>')
    return "".join(items)

def mobile_menu():
    cats = []
    for c in CATEGORIES:
        groups = "".join(
            f'<p class="m-group">{E(g)}</p>' + "".join(f'<a href="{svc_url(SVC_BY_SLUG[s])}">{E(SVC_BY_SLUG[s]["name"])}</a>' for s in sl)
            for g, sl in GROUPS[c["id"]])
        cats.append(f'<details><summary>{E(c["name"])}{ico("chev","chev")}</summary><div class="m-links">{groups}</div></details>')
    learn = "".join(f'<a href="{u}">{E(n)}</a>' for n, u, d in LEARN_LINKS)
    cats.append(f'<details><summary>Learn{ico("chev","chev")}</summary><div class="m-links">{learn}</div></details>')
    return f'''<div class="m-drawer" id="mDrawer" hidden>
  <div class="m-head"><a href="/" class="logo">{LOGO}</a><button class="icon-btn" id="mClose" type="button" aria-label="Close menu">{ico("close")}</button></div>
  <nav class="m-nav">{"".join(cats)}
    <a class="m-top" href="/services/index.html">All services</a>
    <a class="m-top" href="/pricing.html">Pricing</a>
    <a class="m-top" href="/about.html">About us</a>
    <a class="m-top" href="/team.html">Our team</a>
    <a class="m-top" href="/contact.html">Contact</a>
    <a class="m-top" href="/partner.html">Partner with us</a>
    <a class="m-top" href="/payment-options.html">Pay now</a>
  </nav>
  <div class="m-cta"><a class="btn btn-wa" href="{wa_link()}" target="_blank" rel="noopener">{WA_SVG}Free consultation on WhatsApp</a><a class="btn btn-ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
</div>'''

def header():
    return f'''{topbar()}
<header class="site-header" id="siteHeader"><div class="container header-in">
  <a href="/" class="logo" aria-label="LegalReet home">{LOGO}</a>
  <nav class="main-nav" aria-label="Main"><ul>{mega_menu()}</ul></nav>
  <div class="header-cta">
    <a class="btn btn-ghost btn-sm hide-md" href="tel:{PHONE_TEL}">{ico("phone")}Call us</a>
    <a class="btn btn-primary btn-sm" href="{wa_link()}" target="_blank" rel="noopener">Free consultation</a>
    <button class="icon-btn menu-btn" id="mOpen" type="button" aria-label="Open menu" aria-controls="mDrawer">{ico("menu")}</button>
  </div>
</div></header>
{mobile_menu()}'''

def footer():
    cat_rows = "".join(
        f'<p class="f-row"><b>{E(c["name"])}:</b>' + "".join(f'<a href="{svc_url(s)}">{E(s["name"])}</a>' for s in ordered(c["id"])[:10]) + "</p>"
        for c in CATEGORIES)
    return f'''<footer class="site-footer">
  <div class="container f-grid">
    <div class="f-brand">
      <a href="/" class="logo logo-invert">{LOGO}</a>
      <ul class="f-contact">
        <li>{ico("pin")}<span>{ADDRESS_HTML}</span></li>
        <li>{ico("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ico("phone")}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        <li>{ico("clock")}<span>{HOURS}</span></li>
      </ul>
    </div>
    <div class="f-col"><h5>LegalReet</h5><ul>
      <li><a href="/about.html">About us</a></li><li><a href="/team.html">Our team</a></li>
      <li><a href="/careers.html">Careers</a></li><li><a href="/partner.html">Partner with us</a></li>
      <li><a href="/services/index.html">All services</a></li><li><a href="/pricing.html">Pricing</a></li>
      <li><a href="/contact.html">Contact</a></li><li><a href="/grievance.html">Grievance / complaints</a></li></ul></div>
    <div class="f-col"><h5>Learn</h5><ul>{"".join(f'<li><a href="{u}">{E(n)}</a></li>' for n, u, d in LEARN_LINKS)}</ul></div>
    <div class="f-col"><h5>Policies</h5><ul>
      <li><a href="/privacy-policy.html">Privacy policy</a></li><li><a href="/refund-policy.html">Refund policy</a></li>
      <li><a href="/terms.html">Terms &amp; conditions</a></li><li><a href="/payment-options.html">Payment options</a></li></ul></div>
    <div class="f-col"><h5>Government portals</h5><ul>
      <li><a href="https://www.gst.gov.in/" rel="noopener" target="_blank">GST portal</a></li>
      <li><a href="https://www.incometax.gov.in/" rel="noopener" target="_blank">Income Tax e-filing</a></li>
      <li><a href="https://www.mca.gov.in/" rel="noopener" target="_blank">Ministry of Corporate Affairs</a></li>
      <li><a href="https://ipindia.gov.in/" rel="noopener" target="_blank">IP India</a></li>
      <li><a href="https://udyamregistration.gov.in/" rel="noopener" target="_blank">Udyam registration</a></li>
      <li><a href="https://www.dgft.gov.in/" rel="noopener" target="_blank">DGFT</a></li></ul></div>
  </div>
  <div class="container f-services">{cat_rows}</div>
  <div class="container f-bottom"><span>&copy; {YEAR} LegalReet. All rights reserved. All filings are subject to government processing times.</span><span>Agra, Uttar Pradesh &middot; Serving clients across India</span></div>
</footer>
<div class="mobile-bar"><a href="tel:{PHONE_TEL}">{ico("phone")}Call</a><a href="{wa_link()}" target="_blank" rel="noopener" class="mb-wa">{WA_SVG}WhatsApp</a><a href="/services/index.html">{ico("doc")}Services</a></div>
<a class="wa-fab" href="{wa_link()}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}</a>
<div class="cookie-banner" id="cookieBanner" role="dialog" aria-label="Cookie notice" hidden>
  <p>We use essential cookies to run this site and, only with your consent, cookies that help us understand how visitors use it.</p>
  <div><button class="btn btn-ghost btn-sm" id="cookieDecline" type="button">Decline</button><button class="btn btn-primary btn-sm" id="cookieAccept" type="button">Accept</button></div>
</div>'''

ORG_SCHEMA = {
    "@context": "https://schema.org", "@type": "ProfessionalService", "name": "LegalReet",
    "url": SITE_URL + "/", "email": EMAIL, "telephone": "+91-93683-75024",
    "address": {"@type": "PostalAddress", "streetAddress": "E-14, First Floor, Indrapuram, near Shankar Greens, Tajganj Phase II",
                "addressLocality": "Agra", "addressRegion": "Uttar Pradesh", "postalCode": "282001", "addressCountry": "IN"},
    "areaServed": "IN", "openingHours": "Mo-Sa 10:00-19:00",
}

FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap"

def page(title, description, path, body, schemas=None, extra_head=""):
    tags = "\n".join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in [ORG_SCHEMA] + (schemas or []))
    canonical = SITE_URL + (path if path != "/index.html" else "/")
    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{EA(description)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#123028">
<meta property="og:type" content="website"><meta property="og:site_name" content="LegalReet">
<meta property="og:title" content="{title}"><meta property="og:description" content="{EA(description)}"><meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_IN"><meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="stylesheet" href="/assets/style.css">
{extra_head}{tags}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header()}
<main id="main">
{body}
</main>
{footer()}
<script>if(/(invite_token|recovery_token|confirmation_token|email_change_token)=/.test(location.hash)){{var s=document.createElement('script');s.src='https://identity.netlify.com/v1/netlify-identity-widget.js';s.onload=function(){{window.netlifyIdentity&&netlifyIdentity.init()}};document.head.appendChild(s)}}</script>
<script src="/assets/script.js" defer></script>
</body>
</html>'''

# ----------------------------------------------------------------- shared blocks
def breadcrumb(trail):
    parts, items = [], []
    for i, (label, path) in enumerate(trail):
        last = i == len(trail) - 1
        parts.append(f'<span aria-current="page">{label}</span>' if last else f'<a href="{path}">{label}</a>')
        items.append({"@type": "ListItem", "position": i + 1, "name": re.sub(r"&\w+;", " ", label), "item": SITE_URL + path})
    html = f'<div class="crumbs"><div class="container"><nav aria-label="Breadcrumb">{"<span class=sep>/</span>".join(parts)}</nav></div></div>'
    return html, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def page_hero(eyebrow, title, sub, actions=True):
    act = f'''<div class="hero-actions"><a class="btn btn-wa" href="{wa_link()}" target="_blank" rel="noopener">{WA_SVG}Talk to an expert</a><a class="btn btn-ghost-inv" href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a></div>''' if actions else ""
    return f'''<section class="page-hero"><div class="container">
  <p class="eyebrow eyebrow-inv">{eyebrow}</p><h1>{title}</h1><p class="lead">{sub}</p>{act}
</div></section>'''

def section_head(eyebrow, title, sub="", link=None, center=False):
    l = f'<a class="link-arrow" href="{link[1]}">{link[0]}{ico("arrow")}</a>' if link else ""
    s = f"<p>{sub}</p>" if sub else ""
    return f'<div class="sec-head{" center" if center else ""}"><div><p class="eyebrow">{eyebrow}</p><h2>{title}</h2>{s}</div>{l}</div>'

def cta_band(title="Not sure which registration you need?",
             sub="Speak to a LegalReet expert at no cost. We'll recommend the right structure, give you a realistic timeline and confirm the full fee in writing before you pay anything."):
    return f'''<section class="sec"><div class="container"><div class="cta-band">
  <div><h2>{title}</h2><p>{sub}</p></div>
  <div class="cta-actions"><a class="btn btn-wa" href="{wa_link()}" target="_blank" rel="noopener">{WA_SVG}Chat on WhatsApp</a><a class="btn btn-light" href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a></div>
</div></div></section>'''

STEPS = [
    ("Tell us the goal", "Pick a service, or describe what you're trying to do and we'll suggest the right registration or structure."),
    ("Get a written quote", "A LegalReet expert calls back, confirms scope and eligibility, and sends a fixed fee in writing."),
    ("Upload documents", "Share the checklist documents over WhatsApp or email. We check every page before anything is filed."),
    ("We file and follow up", "Your application is prepared, filed and chased with the department by the same expert who quoted you."),
    ("Certificate delivered", "Approvals arrive digitally, along with the recurring due dates that now apply to your business."),
]
PILLARS = [
    ("shield", "Checked before it's filed", "Every application is reviewed against a written checklist before it reaches the department, which is why most of our filings clear without queries."),
    ("users", "Qualified professionals", "Chartered accountants, company secretaries and advocates review the work in their own area of practice."),
    ("rupee", "Prices you can see", "Starting fees are published on every service page, and your final fee is confirmed in writing before work starts."),
    ("track", "One person to ask", "The expert who quotes you stays on your file to delivery, with updates on WhatsApp, phone or email."),
]

def steps_block(title="Five steps from first call to certificate"):
    steps = "".join(f'<li><span class="step-n">{i+1}</span><div><h4>{a}</h4><p>{b}</p></div></li>' for i, (a, b) in enumerate(STEPS))
    pillars = "".join(f'<div class="pillar">{ico(i)}<h4>{a}</h4><p>{b}</p></div>' for i, a, b in PILLARS)
    return f'''<section class="sec sec-alt"><div class="container">
  {section_head("How it works", title)}
  <ol class="steps">{steps}</ol>
  <div class="pillars">{pillars}</div>
</div></section>'''

STATS = [("12,400+", "Businesses registered"), ("97%", "Filed without rejection"), ("4.9&#9733;", "Average Google rating"), (f"{len(SERVICES)}", "Services under one roof")]

def stats_band():
    return '<section class="stats"><div class="container stats-in">' + "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in STATS) + "</div></section>"

TESTIMONIALS = [
    ("Dhruv Gupta", "The team handled the entire registration and certification process professionally and smoothly. From documentation to final approval, they provided proper guidance and regular updates."),
    ("Anand Jha", "One of the most reliable firms for GST registration and tax consultancy. Their team is highly professional, explains everything clearly, and ensures a smooth process."),
    ("Pragati Jayant", "Excellent service! Their trademark team helped me register my trademark smoothly. They are very responsive and professional. Great experience overall."),
]

def testimonials():
    cards = "".join(f'''<figure class="review"><div class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <blockquote>&ldquo;{q}&rdquo;</blockquote><figcaption><span class="avatar">{"".join(w[0] for w in n.split()[:2])}</span><span><b>{n}</b><small>Google review</small></span></figcaption></figure>''' for n, q in TESTIMONIALS)
    return f'''<section class="sec"><div class="container">
  {section_head("Client reviews", "What clients say after the certificate arrives", "Rated 4.9 out of 5 by clients on Google.")}
  <div class="reviews">{cards}</div>
</div></section>'''

def service_card(s, show_cat=False):
    tag = s["cat_name"] if show_cat else s.get("group", "")
    return f'''<a class="svc-card" href="{svc_url(s)}"><span class="tag">{E(tag)}</span><h3>{E(s["name"])}</h3><p>{E(s["short"])}</p>
      <span class="svc-foot"><span class="price">{price_label(s)}</span><span class="go">Details{ico("arrow")}</span></span></a>'''

def enquiry_form(form_name="enquiry", heading="Talk to an expert &mdash; free", compact=True, preselect=""):
    opts = "".join(
        f'<optgroup label="{EA(c["name"])}">' + "".join(
            f'<option{" selected" if s["name"]==preselect else ""}>{E(s["name"])}</option>' for s in ordered(c["id"])) + "</optgroup>"
        for c in CATEGORIES)
    return f'''<form class="enquiry" name="{form_name}" method="POST" action="/thank-you.html" data-netlify="true" netlify-honeypot="company_website">
  <h3>{heading}</h3><p class="muted">Tell us what you need. We reply within working hours.</p>
  <input type="hidden" name="form-name" value="{form_name}">
  <p class="hp"><label>Leave this empty <input name="company_website"></label></p>
  <label>Your name<input name="name" required autocomplete="name"></label>
  <label>Mobile number<input name="phone" type="tel" required pattern="[0-9+ ]{{10,15}}" autocomplete="tel"></label>
  {'' if compact else '<label>Email<input name="email" type="email" autocomplete="email"></label>'}
  <label>Service needed<select name="service"><option value="">Not sure yet &mdash; please advise</option>{opts}</select></label>
  {'' if compact else '<label>City<input name="city" autocomplete="address-level2"></label><label>Anything we should know?<textarea name="message" rows="3"></textarea></label>'}
  <button class="btn btn-primary btn-block" type="submit">Request a call back</button>
  <div class="enq-alt"><a href="{wa_link()}" target="_blank" rel="noopener" class="btn btn-wa btn-sm">{WA_SVG}WhatsApp</a><a href="tel:{PHONE_TEL}" class="btn btn-ghost btn-sm">{ico("phone")}Call now</a></div>
</form>'''

def faq_html(faqs):
    return "".join(f'<details class="faq"><summary>{E(q)}{ico("chev","chev")}</summary><p>{E(a)}</p></details>' for q, a in faqs)

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

# ----------------------------------------------------------------- markdown content
def render_markdown(text):
    def inline(s):
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s
    out, para, items = [], [], []
    def fp():
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para.clear()
    def fl():
        if items: out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"); items.clear()
    for line in text.replace("\r\n", "\n").strip("\n").split("\n"):
        line = line.rstrip()
        if not line.strip(): fp(); fl(); continue
        m = re.match(r"(#{1,3}) (.*)", line)
        if m:
            fp(); fl(); lvl = "h2" if len(m.group(1)) < 3 else "h3"; out.append(f"<{lvl}>{inline(m.group(2))}</{lvl}>"); continue
        if line.startswith(("- ", "* ")):
            fp(); items.append(line[2:].strip()); continue
        fl(); para.append(line.strip())
    fp(); fl()
    return "\n".join(out)

def load_md(folder):
    d = os.path.join(ROOT, "content", folder)
    posts = []
    if not os.path.isdir(d):
        return posts
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        raw = open(os.path.join(d, fn), encoding="utf-8").read()
        _, meta_block, body = raw.split("---", 2)
        meta = {}
        for line in meta_block.strip().split("\n"):
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip().strip('"').strip("'")
        meta["slug"] = fn[:-3]; meta["body"] = body; meta["body_html"] = render_markdown(body)
        posts.append(meta)
    posts.sort(key=lambda p: p.get("date", ""), reverse=True)
    return posts

def fdate(d, fmt="%d %b %Y"):
    try:
        return datetime.strptime(d, "%Y-%m-%d").strftime(fmt)
    except Exception:
        return d

def blog_card(p):
    return f'''<a class="post-card" href="/blog/{p["slug"]}.html"><span class="tag">{E(p.get("category",""))}</span><h3>{E(p.get("title",""))}</h3><p>{E(p.get("excerpt",""))}</p><span class="meta">{fdate(p.get("date",""))}</span></a>'''

def news_item(n):
    return f'''<a class="news-item" href="/news.html#{n["slug"]}"><span class="news-date"><b>{fdate(n["date"],"%d")}</b>{fdate(n["date"],"%b %y")}</span><span><h4>{E(n.get("title",""))}</h4><p>{E(n.get("excerpt",""))}</p></span></a>'''

# ----------------------------------------------------------------- HOME
POPULAR = ["gst-registration", "private-limited-company-registration", "income-tax-return-filing", "trademark-registration",
           "fssai-food-license", "accounting-bookkeeping", "iso-9001-certification", "project-report-preparation"]

PACKAGES = [
    ("Company formation", [
        ("private-limited-company-registration", True, ["Name reservation through SPICe+", "2 DSCs and 2 DINs", "MOA and AOA drafted for your objects", "Incorporation certificate, PAN and TAN", "Bank account opening support"]),
        ("public-limited-company-registration", False, ["Name reservation", "3 DINs and up to 7 DSCs", "MOA and AOA drafted", "Incorporation certificate, PAN and TAN", "Post-incorporation checklist"]),
        ("one-person-company-registration", False, ["Name reservation", "1 DSC and 1 DIN", "Nominee consent prepared", "Incorporation certificate, PAN and TAN", "GST registration on request"]),
        ("llp-registration", False, ["Name reservation", "2 DSCs and 2 DPINs", "LLP agreement drafted by our legal team", "Incorporation certificate, PAN and TAN", "LLP agreement filed in Form 3"]),
    ]),
    ("Registrations & licences", [
        ("gst-registration", True, ["Eligibility and scheme advice", "Regular or composition registration", "Application and query replies", "GST certificate delivered", "First-return reminder"]),
        ("fssai-food-license", False, ["Basic, state or central licence check", "Application on FoSCoS", "Food category mapping", "Registration certificate", "Renewal reminder"]),
        ("import-export-code", False, ["IEC application on the DGFT portal", "Bank and address mapping", "IEC certificate", "Udyam registration on request", "Annual IEC update reminder"]),
        ("sole-proprietorship-registration", False, ["Udyam registration", "GST registration if applicable", "Current account document set", "Shop & establishment guidance", "Business PAN / TAN advice"]),
    ]),
    ("Brand & certification", [
        ("trademark-registration", True, ["Search report before filing", "Class selection advice", "Filing in one class", "TM application number same day", "Status tracking to registration"]),
        ("iso-9001-certification", False, ["Gap check against ISO 9001", "Quality manual templates", "Audit by an accredited body", "Certificate valid for three years", "Surveillance audit reminders"]),
        ("iso-14001-certification", False, ["Environmental aspects review", "Documentation templates", "Certification audit coordination", "Three-year certificate", "Surveillance audit reminders"]),
        ("gmp-certification", False, ["Facility and process gap review", "SOP and record templates", "Audit coordination", "GMP certificate", "Renewal reminders"]),
    ]),
    ("Special entities", [
        ("section-8-company-registration", True, ["Charitable objects drafted", "2 DSCs and 2 DINs", "Section 8 licence and incorporation", "PAN and TAN", "12A / 80G roadmap"]),
        ("producer-company-registration", False, ["Name reservation", "5 DINs and up to 10 DSCs", "MOA and AOA for producer objects", "Incorporation certificate, PAN and TAN", "Three months of compliance support"]),
        ("nidhi-company-registration", False, ["Name reservation", "3 DINs and up to 7 DSCs", "Member and capital planning", "Incorporation certificate, PAN and TAN", "NDH-4 timeline planned"]),
        ("ngo-section-8-company-registration", False, ["Objects drafted for CSR eligibility", "Section 8 licence and incorporation", "PAN and TAN", "CSR-1 and NGO Darpan plan", "12A / 80G roadmap"]),
    ]),
]

def packages_block():
    tabs = "".join(f'<button role="tab" type="button" aria-selected="{"true" if i==0 else "false"}" data-tab="pk{i}">{E(n)}</button>' for i, (n, _) in enumerate(PACKAGES))
    panels = []
    for i, (n, items) in enumerate(PACKAGES):
        cards = []
        for slug, pop, incl in items:
            s = SVC_BY_SLUG[slug]
            price = f'<div class="pk-price"><small>Starting at</small>{inr(s["price"])}</div>' if s.get("price") else '<div class="pk-price"><small>Fee</small>On quote</div>'
            cards.append(f'''<div class="pk{" pk-pop" if pop else ""}">{'<span class="pk-badge">Most chosen</span>' if pop else ''}<h3>{E(s["name"])}</h3>{price}
            <ul>{"".join(f"<li>{ico('check')}{E(x)}</li>" for x in incl)}</ul><a class="btn {"btn-primary" if pop else "btn-ghost"} btn-block" href="{svc_url(s)}">View details</a></div>''')
        panels.append(f'<div class="pk-grid" role="tabpanel" id="pk{i}"{"" if i==0 else " hidden"}>{"".join(cards)}</div>')
    return f'''<section class="sec"><div class="container">
  {section_head("Transparent pricing", "Fixed-scope packages, priced upfront", "Starting fees are shown below. Government fees, stamp duty and GST vary by state and are itemised in your written quote &mdash; no surprise charges later.")}
  <div class="tabs" role="tablist">{tabs}</div>{"".join(panels)}
</div></section>'''

def build_home(posts, news):
    chips = "".join(f'<a href="{svc_url(SVC_BY_SLUG[s])}">{E(n)}</a>' for s, n in [
        ("gst-registration", "GST Registration"), ("private-limited-company-registration", "Private Limited Company"),
        ("trademark-registration", "Trademark"), ("income-tax-return-filing", "ITR Filing"),
        ("fssai-food-license", "FSSAI Licence"), ("msme-udyam-registration", "MSME / Udyam")])
    hero = f'''<section class="hero"><div class="container hero-in">
  <div class="hero-copy">
    <p class="eyebrow eyebrow-inv">CA-led legal, tax &amp; compliance partner &middot; Agra</p>
    <h1>Register it, file it and stay compliant &mdash; <em>the right way.</em></h1>
    <p class="lead">Company and LLP incorporation, GST, income tax, trademarks, licences, ROC filings and legal drafting &mdash; handled end to end by chartered accountants, company secretaries and advocates. Published fees, paperless process, clients across India.</p>
    <form class="search" role="search" action="/services/index.html" data-search>
      <label class="sr" for="heroSearch">Search services</label>
      {ico("search")}<input id="heroSearch" name="q" type="search" placeholder="Search {len(SERVICES)} services &mdash; e.g. GST, trademark, LLP" autocomplete="off">
      <button class="btn btn-primary btn-sm" type="submit">Search</button>
      <div class="search-results" hidden></div>
    </form>
    <div class="chips">{chips}</div>
    <ul class="trust"><li>{ico("star")}<b>4.9/5</b> on Google</li><li>{ico("users")}CA &middot; CS &middot; Advocates</li><li>{ico("check")}100% online process</li></ul>
  </div>
  {enquiry_form("enquiry-home")}
</div></section>'''

    what = []
    for c in CATEGORIES:
        items = ordered(c["id"])
        lis = "".join(f'<li><a href="{svc_url(s)}">{E(s["name"])}</a></li>' for s in items[:9])
        what.append(f'''<div class="cat-card"><svg class="cat-ico" viewBox="0 0 34 34" fill="none">{c["icon"]}</svg><h3>{E(c["name"])}</h3><p>{E(c["tagline"])}</p>
          <ul>{lis}</ul><a class="link-arrow" href="/services/index.html#cat-{c["id"]}">All {len(items)} services{ico("arrow")}</a></div>''')
    what_sec = f'''<section class="sec"><div class="container">
  {section_head("What we do", "One partner for every registration, return and licence", "From the day you incorporate to every GST, income tax and ROC due date after &mdash; we handle the paperwork so you can run the business.")}
  <div class="cat-grid">{"".join(what)}</div></div></section>'''

    pop = "".join(service_card(SVC_BY_SLUG[s], show_cat=True) for s in POPULAR)
    pop_sec = f'''<section class="sec sec-alt"><div class="container">
  {section_head("Popular services", "What most of our clients come to us for", link=("Browse all services", "/services/index.html"))}
  <div class="svc-grid">{pop}</div></div></section>'''

    # calendar teaser
    from site_pages import MONTHLY_DUE
    cal = "".join(f'<li><span class="day">{d}</span><span>{E(w)}</span></li>' for d, w, _ in MONTHLY_DUE[:8])
    learn_sec = f'''<section class="sec"><div class="container two-col">
  <div>{section_head("Compliance calendar", "Every month, the same dates come round", "These recurring due dates apply to most GST-registered businesses and employers. Miss one and late fees or interest start the next day.")}
    <ul class="cal-list">{cal}</ul><a class="btn btn-ghost" href="/compliance-calendar.html">{ico("cal")}See the full calendar</a></div>
  <div class="news-box"><div class="news-head"><h3>Compliance news</h3><a class="link-arrow" href="/news.html">All updates{ico("arrow")}</a></div>{"".join(news_item(n) for n in news[:4])}</div>
</div></section>'''

    blog_sec = ""
    if posts:
        blog_sec = f'''<section class="sec sec-alt"><div class="container">
  {section_head("From the blog", "Guides written by the people who file", link=("All articles", "/blog/index.html"))}
  <div class="post-grid">{"".join(blog_card(p) for p in posts[:3])}</div></div></section>'''

    body = hero + stats_band() + what_sec + pop_sec + packages_block() + steps_block() + learn_sec + blog_sec + testimonials() + cta_band()
    return page("LegalReet | Company Registration, GST, ITR, Trademark &amp; Compliance Services",
                f"LegalReet handles company and LLP registration, GST, income tax returns, trademarks, licences, ISO certification, ROC compliance and legal drafting for businesses across India. {len(SERVICES)} services with published fees.",
                "/index.html", body)

# ----------------------------------------------------------------- SERVICES INDEX
def build_services_index():
    bc, bcs = breadcrumb([("Home", "/index.html"), ("All services", "/services/index.html")])
    jump = "".join(f'<a href="#cat-{c["id"]}">{E(c["name"])} <small>{len(ordered(c["id"]))}</small></a>' for c in CATEGORIES)
    blocks = []
    for c in CATEGORIES:
        groups = "".join(f'<h3 class="grp-title">{E(g)}</h3><div class="svc-grid">{"".join(service_card(SVC_BY_SLUG[s]) for s in sl)}</div>' for g, sl in GROUPS[c["id"]])
        blocks.append(f'''<section class="cat-block" id="cat-{c["id"]}"><div class="cat-block-head"><svg class="cat-ico" viewBox="0 0 34 34" fill="none">{c["icon"]}</svg><div><h2>{E(c["name"])}</h2><p>{E(c["tagline"])} &middot; {len(ordered(c["id"]))} services</p></div></div>{groups}</section>''')
    body = page_hero("Service directory", f"All {len(SERVICES)} services, in one place",
                     "Four practice areas, sixteen service groups. Every service has its own page with the starting fee, documents, timeline and process.", actions=False) + bc + f'''
<section class="sec"><div class="container">
  <form class="search search-light" role="search" data-search data-filter>
    <label class="sr" for="dirSearch">Filter services</label>{ico("search")}<input id="dirSearch" name="q" type="search" placeholder="Type to filter &mdash; e.g. ISO, deed, conversion" autocomplete="off">
    <div class="search-results" hidden></div>
  </form>
  <nav class="jump" aria-label="Practice areas">{jump}</nav>
  {"".join(blocks)}
  <p class="no-results" hidden>No service matches that search. <a href="{wa_link()}" target="_blank" rel="noopener">Ask us on WhatsApp</a> &mdash; we probably still handle it.</p>
</div></section>''' + cta_band()
    return page("All Services &ndash; Registration, Tax, Trademark, ROC &amp; Legal Drafting | LegalReet",
                f"Browse all {len(SERVICES)} LegalReet services across business registration, licences and certifications, tax and compliance, and legal documents, with starting fees.",
                "/services/index.html", body, schemas=[bcs])

# ----------------------------------------------------------------- SERVICE PAGE
GROUP_NOTES = {
    "Company Incorporation": "Incorporations are filed on the MCA portal through SPICe+, which bundles name approval, DIN, PAN, TAN, EPFO and ESIC registration in one application.",
    "Firms & Other Formations": "Smaller formations need fewer filings, but the bank, GST and tax department still expect the right document set &mdash; we prepare it once so every later registration goes through cleanly.",
    "NGOs & Special Entities": "Non-profits and special entities are scrutinised more closely, so we draft objects and governance clauses with the later 12A, 80G, CSR-1 and FCRA applications already in mind.",
    "Current Offers": "Offer fees apply to standard cases. If your case needs more (extra directors, higher capital, special objects), we tell you the difference before you pay.",
    "Business Licences": "Licences are issued by different departments with different portals. We check eligibility first, so you only apply for what your business actually needs.",
    "Trademark, Patent & Copyright": "IP filings are handled by our IP desk, which tracks every application in the IP India journal and alerts you to objections, oppositions and renewal dates.",
    "ISO Standards": "ISO certificates are issued by independent certification bodies after an audit. We prepare your documentation, coordinate the audit and remind you of surveillance audits.",
    "Product & Industry Certifications": "Product certifications depend on testing and inspection by the relevant body. We handle the documentation and coordination so your team can focus on production.",
    "Accounts, Audit & Tax": "Recurring compliance work is scheduled against a calendar we maintain for you, with documents requested well before each due date.",
    "Entity Conversions": "Conversions move your business into a new legal form while carrying over its assets, contracts and registrations. We plan the sequence so licences and bank accounts follow without gaps.",
    "Company Secretarial": "Every change to a company or LLP must be approved internally and reported to the Registrar within strict time limits. We prepare the resolutions and file the forms.",
    "Finance & Advisory": "Advisory engagements start with a conversation about your numbers and goals. Any loan or investment decision remains yours; we prepare the analysis and paperwork.",
    "Property & Personal": "Personal and property documents are drafted to Indian law and state stamp-duty rules, and we explain where registration or notarisation is needed.",
    "Business Contracts": "Commercial agreements are drafted around your actual deal &mdash; payment terms, exit clauses and dispute resolution &mdash; rather than generic templates.",
    "Corporate Records": "Board and shareholder documents are drafted to match the Companies Act and your articles, so they stand up in audits, due diligence and ROC filings.",
    "Digital Signatures": "DSCs are issued by licensed certifying authorities after paperless video verification and are delivered on a USB token.",
}

def build_service_page(s):
    cat = CAT_BY_ID[s["cat"]]
    group = s["group"]
    bc, bcs = breadcrumb([("Home", "/index.html"), ("Services", "/services/index.html"),
                          (E(cat["name"]), f"/services/index.html#cat-{cat['id']}"), (E(s["name"]), svc_url(s))])
    price_html = f'<div class="glance-price"><small>Starting at</small>{inr(s["price"])}<span>+ govt. fees &amp; GST as applicable</span></div>' if s["price"] else '<div class="glance-price"><small>Professional fee</small>On quote<span>Fixed fee confirmed in writing</span></div>'
    hero = f'''<section class="page-hero svc-hero"><div class="container svc-hero-in">
  <div><p class="eyebrow eyebrow-inv">{E(cat["name"])} &middot; {E(group)}</p><h1>{E(s["name"])}</h1><p class="lead">{E(s["short"])}</p>
    <ul class="glance"><li>{ico("clock")}<span><small>Timeline</small>{E(s["timeline"])}</span></li><li>{ico("doc")}<span><small>Documents</small>{len(s["documents"])} items</span></li><li>{ico("check")}<span><small>Process</small>100% online</span></li></ul>
    <div class="hero-actions"><a class="btn btn-wa" href="{wa_link(f'Hi LegalReet, I need help with {s["name"]}.')}" target="_blank" rel="noopener">{WA_SVG}Start on WhatsApp</a><a class="btn btn-ghost-inv" href="tel:{PHONE_TEL}">{ico("phone")}{PHONE_DISPLAY}</a></div>
  </div>
  <div class="glance-card">{price_html}{enquiry_form("enquiry-service", heading="Get started", preselect=s["name"])}</div>
</div></section>'''

    benefits = "".join(f"<li>{ico('check')}<span>{E(b)}</span></li>" for b in s["benefits"])
    docs = "".join(f"<li>{ico('doc')}<span>{E(d)}</span></li>" for d in s["documents"])
    toc = '<nav class="toc" aria-label="On this page"><a href="#overview">Overview</a><a href="#documents">Documents</a><a href="#process">Process</a><a href="#fees">Fees</a><a href="#faq">FAQs</a></nav>'
    price_txt = f"Our professional fee for {s['name']} starts at Rs {s['price']:,}. Government fees, stamp duty and GST depend on your state and case and are itemised in the written quote we send before work begins." if s["price"] else f"We quote a fixed professional fee for {s['name']} after a short call, because the work involved varies with your state, entity and requirement. Government fees, where applicable, are itemised separately at actual cost."
    faqs = [
        (f"How long does {s['name']} take?", f"Typically {s['timeline'].rstrip('.')}, counted from the date we receive complete documents. Department processing times can stretch this, and we keep you updated throughout."),
        (f"What documents do I need for {s['name']}?", "You will usually need: " + "; ".join(s["documents"]) + ". We send a tailored checklist after the first call."),
        ("How much will it cost?", price_txt),
        ("Do I need to visit your office?", "No. Documents are shared over WhatsApp or email, signatures are done with Aadhaar e-sign or a DSC where required, and approvals are delivered digitally. You are welcome to visit our Agra office if you prefer."),
        ("Who will handle my file?", "A LegalReet expert from the relevant desk is assigned when you confirm, and stays your point of contact until delivery. Work is reviewed by a qualified professional before filing."),
    ]
    steps = "".join(f'<li><span class="step-n">{i+1}</span><div><h4>{a}</h4><p>{b}</p></div></li>' for i, (a, b) in enumerate(STEPS))
    related = [SVC_BY_SLUG[x] for x in dict(GROUPS[s["cat"]])[group] if x != s["slug"]][:3]
    if len(related) < 3:
        related += [x for x in ordered(s["cat"]) if x["slug"] != s["slug"] and x not in related][: 3 - len(related)]
    body = hero + bc + f'''
<section class="sec"><div class="container detail">
  <aside class="detail-side">{toc}<div class="side-card"><h4>Need it urgently?</h4><p>Call or WhatsApp and we'll tell you the fastest realistic timeline for your case.</p><a class="btn btn-primary btn-block" href="tel:{PHONE_TEL}">{ico("phone")}Call {PHONE_DISPLAY}</a></div></aside>
  <div class="detail-main prose">
    <h2 id="overview">About {E(s["name"])}</h2>
    <p>{E(s["overview"])}</p>
    <p class="note">{GROUP_NOTES[group]}</p>
    <h3>What you get</h3><ul class="ticks">{benefits}</ul>
    <h2 id="documents">Documents required</h2><ul class="docs">{docs}</ul>
    <p class="muted">Exact requirements vary by state and entity. We confirm the final list on the first call.</p>
    <h2 id="process">How we handle it</h2><ol class="steps steps-v">{steps}</ol>
    <h2 id="fees">Fees</h2>
    <div class="fee-box"><div>{f'<small>Starting at</small><b>{inr(s["price"])}</b>' if s["price"] else '<small>Professional fee</small><b>On quote</b>'}<p>{E(price_txt)}</p></div><a class="btn btn-primary" href="{wa_link(f'Hi LegalReet, please share a quote for {s["name"]}.')}" target="_blank" rel="noopener">Get my quote</a></div>
    <h2 id="faq">Frequently asked questions</h2><div class="faqs">{faq_html(faqs)}</div>
  </div>
</div></section>
<section class="sec sec-alt"><div class="container">{section_head("Related services", f"More in {E(group)}")}<div class="svc-grid svc-grid-3">{"".join(service_card(r) for r in related)}</div></div></section>''' + cta_band(f"Ready to start your {E(s['name'])}?")
    schema = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"], "description": s["short"],
              "provider": {"@type": "ProfessionalService", "name": "LegalReet", "url": SITE_URL + "/"}, "areaServed": {"@type": "Country", "name": "India"},
              "category": cat["name"], "url": SITE_URL + svc_url(s)}
    if s["price"]:
        schema["offers"] = {"@type": "Offer", "priceCurrency": "INR", "price": str(s["price"]), "description": "Starting professional fee"}
    return page(f"{E(s['name'])} &ndash; Online in India | LegalReet", f"{s['short']} {('Starting at Rs ' + format(s['price'], ',') + '. ') if s['price'] else ''}Timeline: {s['timeline']}.",
                svc_url(s), body, schemas=[bcs, schema, faq_schema(faqs)])

# ----------------------------------------------------------------- BLOG
def build_blog_index(posts):
    bc, bcs = breadcrumb([("Home", "/index.html"), ("Blog", "/blog/index.html")])
    cards = "".join(blog_card(p) for p in posts) or "<p>New articles are on the way.</p>"
    body = page_hero("LegalReet blog", "Guides on GST, income tax, company law and licences", "Practical write-ups from the team that files them &mdash; what the law asks for, where applications get stuck, and how to avoid it.", actions=False) + bc + f'<section class="sec"><div class="container"><div class="post-grid">{cards}</div></div></section>' + cta_band("Have a question we haven't covered?", "Ask a LegalReet expert directly &mdash; the first conversation is free.")
    return page("Blog &ndash; GST, Income Tax, Company Law Guides | LegalReet", "Guides and explainers on GST, income tax, company law, trademarks and business licences from the LegalReet team.", "/blog/index.html", body, schemas=[bcs])

def build_blog_post(p):
    title = E(p.get("title", ""))
    bc, bcs = breadcrumb([("Home", "/index.html"), ("Blog", "/blog/index.html"), (title, f"/blog/{p['slug']}.html")])
    art = {"@context": "https://schema.org", "@type": "Article", "headline": p.get("title", ""), "datePublished": p.get("date", ""),
           "author": {"@type": "Organization", "name": "LegalReet"}, "publisher": {"@type": "Organization", "name": "LegalReet"},
           "description": p.get("excerpt", ""), "url": f"{SITE_URL}/blog/{p['slug']}.html"}
    body = page_hero(f'{E(p.get("category",""))} &middot; {fdate(p.get("date",""))}', title, E(p.get("excerpt", "")), actions=False) + bc + f'''
<section class="sec"><div class="container detail">
  <aside class="detail-side"><div class="side-card">{enquiry_form("enquiry-blog", heading="Need help with this?")}</div></aside>
  <article class="detail-main prose">{p["body_html"]}<p class="muted">This article is general information, not advice for your specific case. Laws and due dates change; check the latest position or speak to us before acting.</p></article>
</div></section>''' + cta_band()
    return page(f"{title} | LegalReet", p.get("excerpt", ""), f"/blog/{p['slug']}.html", body, schemas=[bcs, art])

# ----------------------------------------------------------------- SEARCH INDEX, SITEMAP
def write_search_index():
    data = [{"n": s["name"], "u": svc_url(s), "c": s["cat_name"], "g": s["group"], "k": s["short"]} for c in CATEGORIES for s in ordered(c["id"])]
    write("assets/search-index.js", "window.LR_SERVICES=" + json.dumps(data, separators=(",", ":")) + ";")

def write_sitemap(paths):
    urls = "".join(f"<url><loc>{SITE_URL}{'/' if p=='/index.html' else p}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>" for p in paths)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /admin/\nSitemap: {SITE_URL}/sitemap.xml\n")

# ----------------------------------------------------------------- MAIN
if __name__ == "__main__":
    posts = load_md("blog")
    news = load_md("news")
    ctx = dict(page=page, breadcrumb=breadcrumb, page_hero=page_hero, section_head=section_head, cta_band=cta_band,
               steps_block=steps_block, stats_band=stats_band, testimonials=testimonials, enquiry_form=enquiry_form,
               faq_html=faq_html, faq_schema=faq_schema, service_card=service_card, ordered=ordered, ico=ico, inr=inr,
               E=E, wa_link=wa_link, fdate=fdate, packages_block=packages_block, SERVICES=SERVICES, CATEGORIES=CATEGORIES,
               GROUPS=GROUPS, SVC_BY_SLUG=SVC_BY_SLUG, svc_url=svc_url, WA_SVG=WA_SVG, EMAIL=EMAIL, PHONE_DISPLAY=PHONE_DISPLAY,
               PHONE_TEL=PHONE_TEL, ADDRESS_HTML=ADDRESS_HTML, HOURS=HOURS, news=news, posts=posts)
    pages = {"/index.html": build_home(posts, news), "/services/index.html": build_services_index(), "/blog/index.html": build_blog_index(posts)}
    for s in SERVICES:
        pages[svc_url(s)] = build_service_page(s)
    for p in posts:
        pages[f"/blog/{p['slug']}.html"] = build_blog_post(p)
    pages.update(build_extra_pages(ctx))
    for path, html in pages.items():
        write(path.lstrip("/"), html)
    write_search_index()
    write_sitemap([p for p in pages if p not in ("/thank-you.html", "/404.html")])
    print(f"Wrote {len(pages)} pages: {len(SERVICES)} services, {len(posts)} blog posts, {len(pages) - len(SERVICES) - len(posts)} other pages.")
