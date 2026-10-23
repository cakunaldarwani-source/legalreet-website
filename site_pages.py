# -*- coding: utf-8 -*-
"""Supporting pages for the LegalReet site (about, team, policies, learning pages...).

Each builder receives `c`, a dict of shared helpers from generate.py.
"""

# Recurring monthly due dates: (day, what, who it applies to)
MONTHLY_DUE = [
    ("7th", "TDS / TCS deposit for the previous month", "Every deductor (March deductions: 30 April)"),
    ("10th", "GSTR-7 and GSTR-8", "GST TDS deductors and e-commerce operators"),
    ("11th", "GSTR-1 (monthly filers)", "Regular GST taxpayers not under QRMP"),
    ("13th", "GSTR-1 / IFF (quarterly filers) and GSTR-6", "QRMP taxpayers and input service distributors"),
    ("15th", "PF and ESI contributions", "Employers registered with EPFO / ESIC"),
    ("18th", "CMP-08 (quarter end months +1)", "Composition taxpayers"),
    ("20th", "GSTR-3B (monthly filers)", "Regular GST taxpayers not under QRMP"),
    ("22nd / 24th", "GSTR-3B (quarterly filers)", "QRMP taxpayers, by state group"),
    ("25th", "PMT-06 GST payment", "QRMP taxpayers for the first two months of a quarter"),
]

ANNUAL_DUE = [
    ("30 April", "MSME-1 (Oct&ndash;Mar half year)", "Companies with dues to micro/small suppliers beyond 45 days"),
    ("30 May", "LLP Form 11 (annual return)", "Every LLP"),
    ("31 May", "TDS / TCS return for Jan&ndash;Mar quarter", "Every deductor"),
    ("15 June", "Advance tax &mdash; 1st instalment (15%)", "Taxpayers with tax liability above Rs 10,000"),
    ("30 June", "DPT-3 (return of deposits)", "Companies, other than government companies"),
    ("31 July", "TDS / TCS return for Apr&ndash;Jun quarter", "Every deductor"),
    ("31 July", "Income tax return &mdash; individuals without business income", "Salaried and similar individuals (ITR-1 etc.)"),
    ("31 August", "Income tax return &mdash; non-audit business and profession cases", "ITR-3 / ITR-4 filers not requiring audit"),
    ("15 September", "Advance tax &mdash; 2nd instalment (45%)", "Taxpayers liable to advance tax"),
    ("30 September", "DIR-3 KYC; AGM to be held", "Directors holding a DIN; companies"),
    ("30 September", "Tax audit report", "Businesses and professions requiring audit"),
    ("Within 30 days of AGM", "AOC-4 (financial statements)", "Every company"),
    ("Within 60 days of AGM", "MGT-7 / MGT-7A (annual return)", "Every company"),
    ("30 October", "LLP Form 8 (statement of accounts &amp; solvency)", "Every LLP"),
    ("31 October", "TDS / TCS return for Jul&ndash;Sep quarter; MSME-1 (Apr&ndash;Sep)", "Deductors; specified companies"),
    ("31 October", "Income tax return &mdash; audit cases", "Companies and audited businesses"),
    ("30 November", "Income tax return &mdash; transfer pricing cases", "Assessees filing Form 3CEB"),
    ("15 December", "Advance tax &mdash; 3rd instalment (75%)", "Taxpayers liable to advance tax"),
    ("31 December", "GSTR-9 / GSTR-9C annual return", "GST taxpayers above the prescribed turnover"),
    ("31 January", "TDS / TCS return for Oct&ndash;Dec quarter", "Every deductor"),
    ("15 March", "Advance tax &mdash; 4th instalment (100%)", "Taxpayers liable to advance tax"),
]

GENERAL_FAQS = [
    ("Is LegalReet a government portal?", "No. LegalReet is a private professional services firm. We prepare and file applications on official government portals on your behalf. Government fees are paid to the department and shown separately in your quote."),
    ("Are your fees fixed?", "Yes. Starting fees are published on each service page and your final professional fee is confirmed in writing before we start. If the scope changes during the work, we tell you before doing anything extra."),
    ("Can I complete everything online?", "Almost always. You share documents over WhatsApp or email, sign with Aadhaar e-sign or a DSC, and receive approvals digitally. A few services, such as property registration, need a personal visit to a government office."),
    ("Do you serve clients outside Agra?", "Yes. Our office is in Agra, Uttar Pradesh, and we handle filings for clients across India. State-specific registrations are filed with the authority of the state where your business operates."),
    ("How soon will someone contact me?", "Within working hours (Monday to Saturday, 10 AM to 7 PM) we usually call back the same day. Enquiries received later are answered the next working morning."),
    ("Which structure should I register?", "It depends on how many owners you have, whether you plan to raise investment, your expected turnover and how much compliance you can manage. A short call is enough for us to recommend one, at no cost."),
    ("What happens if my application gets a query or objection?", "Replying to department queries on applications we filed is part of the service. Formal hearings, oppositions or appeals are separate services and quoted separately."),
    ("Is my data safe with you?", "Documents are used only for your filing, shared only with the authority concerned, and access is limited to the people working on your file. See our privacy policy for details."),
    ("How do I pay?", "We share a payment request or the firm's account details in writing from our official number or email. Pay only to accounts in the name of LegalReet's billing entity as confirmed in your invoice."),
    ("Do you provide invoices with GST?", "Yes. A tax invoice is issued for every payment of professional fees. Government fees paid on your behalf are shown separately at actual cost."),
    ("Can you handle my annual compliance as well?", "Yes. Many clients move to an annual engagement after registration, covering accounting, GST and TDS returns, ROC filings and income tax. Ask for an annual compliance quote."),
    ("Can I cancel after paying?", "You can. Our refund policy explains what is refundable depending on how far the work has progressed and whether government fees have been paid."),
]


def build_extra_pages(c):
    page, bc_, hero, sh, cta = c["page"], c["breadcrumb"], c["page_hero"], c["section_head"], c["cta_band"]
    ico, E, inr, wa = c["ico"], c["E"], c["inr"], c["wa_link"]
    SERVICES, CATEGORIES, GROUPS, SVC, ordered, svc_url = c["SERVICES"], c["CATEGORIES"], c["GROUPS"], c["SVC_BY_SLUG"], c["ordered"], c["svc_url"]
    EMAIL, PHONE, TEL, ADDR, HOURS, WA_SVG = c["EMAIL"], c["PHONE_DISPLAY"], c["PHONE_TEL"], c["ADDRESS_HTML"], c["HOURS"], c["WA_SVG"]
    pages = {}

    def simple(path, crumb, eyebrow, title, sub, content, meta_title, meta_desc, schemas=None, actions=True, show_cta=True):
        bc, bcs = bc_([("Home", "/index.html"), (crumb, path)])
        body = hero(eyebrow, title, sub, actions) + bc + content + (cta() if show_cta else "")
        pages[path] = page(meta_title, meta_desc, path, body, schemas=[bcs] + (schemas or []))

    def prose(html, side=None):
        side_html = side if side is not None else f'<div class="side-card"><h4>Questions?</h4><p>Speak to our team on WhatsApp or call during working hours.</p><a class="btn btn-wa btn-block" href="{wa()}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a><a class="btn btn-ghost btn-block" href="tel:{TEL}">{ico("phone")}{PHONE}</a></div>'
        return f'<section class="sec"><div class="container detail"><aside class="detail-side">{side_html}</aside><div class="detail-main prose">{html}</div></div></section>'

    # ------------------------------------------------------------ PRICING
    rows = []
    for cat in CATEGORIES:
        for g, sl in GROUPS[cat["id"]]:
            trs = "".join(f'<tr><td><a href="{svc_url(SVC[s])}">{E(SVC[s]["name"])}</a></td><td>{E(SVC[s]["timeline"])}</td><td class="num">{"From " + inr(SVC[s]["price"]) if SVC[s]["price"] else "On quote"}</td></tr>' for s in sl)
            rows.append(f'<tr class="grp"><th colspan="3">{E(cat["name"])} &middot; {E(g)}</th></tr>{trs}')
    table = f'<div class="table-wrap"><table class="price-table"><thead><tr><th>Service</th><th>Typical timeline</th><th class="num">Professional fee</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
    content = c["packages_block"]() + f'''<section class="sec sec-alt"><div class="container">
  {sh("Full fee list", f"Starting fees for all {len(SERVICES)} services", "Professional fees are exclusive of government fees, stamp duty and GST, which vary by state and case and are itemised in your written quote. Where a fee is shown as &lsquo;on quote&rsquo;, the scope varies too much to publish one number.")}
  {table}
</div></section>'''
    simple("/pricing.html", "Pricing", "Pricing", "Published fees, written quotes, no surprises",
           "Every service shows its starting fee. Before we begin, you get the exact fee in writing &mdash; professional fee, government fees and taxes listed separately.",
           content, "Pricing &ndash; Company Registration, GST, Trademark &amp; Compliance Fees | LegalReet",
           f"Starting fees for all {len(SERVICES)} LegalReet services: company and LLP registration, GST, trademark, ISO, ROC compliance, tax returns and legal documents.")

    # ------------------------------------------------------------ ABOUT
    about = f'''<section class="sec"><div class="container two-col">
  <div>{sh("About LegalReet", "Reet means &lsquo;the right way&rsquo;. It is also how we file.")}
    <div class="prose"><p>LegalReet is a legal, tax and compliance practice based in Agra, Uttar Pradesh, serving founders, traders, manufacturers, professionals and non-profits across India. The practice grew out of Indian Salahkar, and carries the same team and the same commitment: do the filing properly the first time.</p>
    <p>Most of our clients are running a business, not studying company law. They need someone who knows which registration applies, which document the department will reject, and which due date is coming next. That is the job we do &mdash; from the first incorporation to the hundredth GST return.</p>
    <p>Every engagement is quoted in writing before it starts, handled by one expert from start to finish, and reviewed by a qualified professional before anything is filed.</p></div></div>
  <div class="value-grid">
    <div class="pillar">{ico("shield")}<h4>Accuracy first</h4><p>A written checklist for every service, so applications clear without avoidable queries.</p></div>
    <div class="pillar">{ico("rupee")}<h4>Honest pricing</h4><p>Starting fees published openly; government fees shown at actual cost.</p></div>
    <div class="pillar">{ico("users")}<h4>Real professionals</h4><p>Chartered accountants, company secretaries and advocates on the team.</p></div>
    <div class="pillar">{ico("track")}<h4>Plain answers</h4><p>We explain what is happening in plain language, in English or Hindi.</p></div>
  </div>
</div></section>''' + c["stats_band"]() + c["steps_block"]() + c["testimonials"]()
    simple("/about.html", "About us", "About us", "A compliance partner that files it right the first time",
           "LegalReet brings registration, tax, compliance and legal drafting under one roof, for businesses that want it done properly and on time.",
           about, "About LegalReet &ndash; Legal, Tax &amp; Compliance Firm in Agra", "LegalReet is a legal, tax and compliance practice in Agra serving businesses across India with registrations, tax filings, ROC compliance and legal drafting.")

    # ------------------------------------------------------------ TEAM
    desks = [
        ("Incorporation desk", "Company secretaries and company-law specialists who handle incorporations, conversions, closures and every change filed with the Registrar of Companies."),
        ("Tax &amp; GST desk", "Chartered accountants and tax associates handling GST registration and returns, income tax returns, TDS, tax audits and department notices."),
        ("Accounts &amp; payroll desk", "Accountants who maintain books, run payroll and keep PF and ESI filings on schedule for our retainer clients."),
        ("Intellectual property desk", "Trademark and IP specialists who run searches, file applications, answer examination reports and track the IP India journal."),
        ("Licences &amp; certifications desk", "Specialists in FSSAI, IEC, EPR, ISO and product certifications who coordinate with departments and certification bodies."),
        ("Legal drafting desk", "Advocates who draft and review agreements, deeds, notices and corporate resolutions to Indian law and state stamp rules."),
        ("Advisory desk", "Senior professionals who work with clients on structuring, project reports, business finance and planning."),
        ("Client success", "The first people you speak to: they understand your requirement, share a written quote and keep you updated until delivery."),
    ]
    team = f'''<section class="sec"><div class="container">
  {sh("How we're organised", "Specialists for each kind of work", "Your file is handled by the desk that does that work every day, and reviewed by a qualified professional before anything is filed.")}
  <div class="desk-grid">{"".join(f'<div class="desk"><h3>{a}</h3><p>{b}</p></div>' for a, b in desks)}</div>
  <div class="note-card"><h3>Qualified professionals on every file</h3><p>The LegalReet team includes chartered accountants, company secretaries, advocates and experienced compliance associates. We follow the professional standards that apply to each of these roles, and work that requires a certifying professional is signed only by a professional qualified to do so.</p></div>
</div></section>'''
    simple("/team.html", "Our team", "Our team", "The people behind your filings",
           "Desks organised by practice area, so the person handling your file does that kind of work every day.",
           team, "Our Team &ndash; CAs, CSs and Advocates | LegalReet", "Meet the LegalReet desks: incorporation, tax and GST, accounts, intellectual property, licences, legal drafting and advisory.")

    # ------------------------------------------------------------ CAREERS
    roles = [
        ("Compliance associate (GST &amp; income tax)", "B.Com / M.Com, CA Inter or semi-qualified; comfortable with GST and income tax portals."),
        ("Company secretarial associate", "CS executive or professional, or graduates with MCA filing experience."),
        ("Accounts executive", "Commerce graduates with working knowledge of Tally or similar accounting software."),
        ("Trademark &amp; IP associate", "Law graduates interested in trademark searches, filings and examination replies."),
        ("Client success executive", "Graduates with clear spoken English and Hindi who enjoy helping people."),
        ("Articled and semi-qualified trainees", "Students looking for hands-on exposure to real filings, under supervision."),
    ]
    careers = f'''<section class="sec"><div class="container two-col">
  <div>{sh("Why work here", "Real filings from your first week")}
    <ul class="ticks">{"".join(f"<li>{ico('check')}<span>{x}</span></li>" for x in ["Work across company law, GST, income tax, IP and licensing", "Learn from qualified professionals who review your work", "A structured checklist for every service, so you learn the right way", "Office in Agra, with clients from across India"])}</ul></div>
  <div><h3 class="h3">Roles we regularly hire for</h3><div class="role-list">{"".join(f'<div class="role"><h4>{a}</h4><p>{b}</p></div>' for a, b in roles)}</div>
    <div class="note-card"><h4>How to apply</h4><p>Email your CV to <a href="mailto:{EMAIL}?subject=Career%20application">{EMAIL}</a> with the role in the subject line. We review every application and contact shortlisted candidates for an interview at our Agra office.</p></div></div>
</div></section>'''
    simple("/careers.html", "Careers", "Careers", "Build your career in tax and compliance",
           "We hire people who want to learn properly and do careful work.", careers,
           "Careers at LegalReet &ndash; Tax, Compliance &amp; Legal Jobs in Agra", "Career opportunities at LegalReet for compliance associates, CS associates, accounts executives, IP associates and trainees.", actions=False)

    # ------------------------------------------------------------ PARTNER
    partner = f'''<section class="sec"><div class="container">
  {sh("Who partners with us", "Grow your practice without growing your back office")}
  <div class="desk-grid">{"".join(f'<div class="desk"><h3>{a}</h3><p>{b}</p></div>' for a, b in [
        ("Accountants and tax practitioners", "Offer incorporations, trademarks, ISO and licences to your clients while we handle the filing."),
        ("Lawyers and consultants", "Refer registration and compliance work you don't want to run in-house."),
        ("Banks, DSAs and loan advisors", "Get your borrowers registered and their project reports ready before they apply."),
        ("Startup incubators and associations", "A single compliance partner for every member business, at agreed fees.")])}</div>
  <div class="two-col" style="margin-top:40px">
    <div><h3 class="h3">How the partnership works</h3><ol class="steps steps-v">{"".join(f'<li><span class="step-n">{i+1}</span><div><h4>{a}</h4><p>{b}</p></div></li>' for i, (a, b) in enumerate([
        ("Register your interest", "Fill the form and tell us about your practice and the services your clients need."),
        ("Agree terms", "We agree partner pricing or referral terms in writing, with clear ownership of the client relationship."),
        ("Share requirements", "Send client requirements on WhatsApp or email. We take it from documents to delivery."),
        ("Stay informed", "You get status updates on every file you send, so you can keep your client informed.")]))}</ol></div>
    {c["enquiry_form"]("partner", heading="Become a LegalReet partner", compact=False)}
  </div>
</div></section>'''
    simple("/partner.html", "Partner with us", "Partner programme", "Partner with LegalReet",
           f"Offer all {len(SERVICES)} of our services to your clients, with LegalReet handling the filing.", partner,
           "Partner With Us &ndash; Referral &amp; White-Label Compliance | LegalReet", "Partner programme for accountants, consultants, DSAs and incubators to offer registration and compliance services through LegalReet.", show_cta=False)

    # ------------------------------------------------------------ CONTACT
    contact = f'''<section class="sec"><div class="container two-col">
  <div>{sh("Get in touch", "Talk to a LegalReet expert")}
    <ul class="contact-list">
      <li>{ico("pin")}<div><b>Office</b><span>{ADDR}</span></div></li>
      <li>{ico("phone")}<div><b>Phone</b><a href="tel:{TEL}">{PHONE}</a></div></li>
      <li>{ico("mail")}<div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
      <li>{ico("clock")}<div><b>Working hours</b><span>{HOURS}</span></div></li>
    </ul>
    <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{WA_SVG}Chat on WhatsApp</a>
    <div class="map"><iframe title="LegalReet office map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Shankar%20Greens%20Tajganj%20Agra&output=embed"></iframe></div>
  </div>
  {c["enquiry_form"]("contact", heading="Send us your requirement", compact=False)}
</div></section>'''
    simple("/contact.html", "Contact", "Contact us", "We reply within working hours",
           "Call, WhatsApp, email or send the form &mdash; whichever is easiest for you.", contact,
           "Contact LegalReet &ndash; Agra Office, Phone, WhatsApp &amp; Email", "Contact LegalReet in Agra for company registration, GST, income tax, trademark and compliance services.", actions=False, show_cta=False)

    # ------------------------------------------------------------ NEWS
    news = c["news"]
    items = "".join(f'''<article class="news-full" id="{n["slug"]}"><div class="news-date"><b>{c["fdate"](n["date"],"%d")}</b>{c["fdate"](n["date"],"%b %Y")}</div>
      <div class="prose"><span class="tag">{E(n.get("category",""))}</span><h2>{E(n["title"])}</h2>{n["body_html"]}</div></article>''' for n in news)
    simple("/news.html", "Compliance news", "Compliance news", "Deadlines, extensions and regulatory updates",
           "Short, dated updates on changes that affect GST, income tax, company law and licences. Always check the official notification before acting.",
           f'<section class="sec"><div class="container narrow">{items}</div></section>',
           "Compliance News &ndash; GST, Income Tax &amp; MCA Updates | LegalReet", "Latest due dates, extensions and regulatory updates on GST, income tax, TDS and company law from LegalReet.", actions=False)

    # ------------------------------------------------------------ CALENDAR
    mrows = "".join(f'<tr><td class="day">{d}</td><td>{w}</td><td>{who}</td></tr>' for d, w, who in MONTHLY_DUE)
    arows = "".join(f'<tr><td class="day">{d}</td><td>{w}</td><td>{who}</td></tr>' for d, w, who in ANNUAL_DUE)
    cal = f'''<section class="sec"><div class="container narrow">
  <div class="note-card warn"><h4>Current extension (AY 2026-27)</h4><p>CBDT Circular No. 07/2026 extended the tax audit report due date to 21 October 2026 and the income tax return due date for covered audit cases to 21 November 2026. Transfer-pricing cases are not covered. <a href="/news.html">Read the update</a>.</p></div>
  {sh("Every month", "Recurring monthly due dates")}
  <div class="table-wrap"><table class="cal-table"><thead><tr><th>Due by</th><th>Compliance</th><th>Applies to</th></tr></thead><tbody>{mrows}</tbody></table></div>
  {sh("Through the year", "Key annual and quarterly due dates")}
  <div class="table-wrap"><table class="cal-table"><thead><tr><th>Due by</th><th>Compliance</th><th>Applies to</th></tr></thead><tbody>{arows}</tbody></table></div>
  <p class="muted">Dates shown are the standard statutory due dates and are often extended by notification. Returns for AY 2026-27 are filed under the Income-tax Act, 1961; the Income-tax Act, 2025 applies from tax year 2026-27 onwards and may change some forms and dates. Confirm your specific dates with us or on the official portal.</p>
</div></section>'''
    simple("/compliance-calendar.html", "Compliance calendar", "Compliance calendar", "GST, TDS, income tax and ROC due dates",
           "The monthly and annual dates most Indian businesses need to track, in one place.", cal,
           "Compliance Calendar 2026 &ndash; GST, TDS, ITR &amp; ROC Due Dates | LegalReet", "Monthly and annual due dates for GST returns, TDS, PF/ESI, advance tax, income tax returns, ROC and LLP filings.", actions=False)

    # ------------------------------------------------------------ DOCUMENT CHECKLIST
    blocks = []
    DOC = ico("doc")
    for cat in CATEGORIES:
        inner = "".join(f'<details class="faq"><summary>{E(s["name"])}{ico("chev","chev")}</summary><ul class="docs">{"".join(f"<li>{DOC}<span>{E(d)}</span></li>" for d in s["documents"])}</ul><p><a class="link-arrow" href="{svc_url(s)}">Service details{ico("arrow")}</a></p></details>' for s in ordered(cat["id"]))
        blocks.append(f'<h2 class="grp-title" id="dc-{cat["id"]}">{E(cat["name"])}</h2><div class="faqs">{inner}</div>')
    jump = "".join(f'<a href="#dc-{x["id"]}">{E(x["name"])}</a>' for x in CATEGORIES)
    simple("/document-checklist.html", "Document checklists", "Document checklists", f"What to keep ready for each of our {len(SERVICES)} services",
           "Open any service to see the documents usually required. We send a tailored list after the first call.",
           f'<section class="sec"><div class="container narrow"><nav class="jump">{jump}</nav>{"".join(blocks)}</div></section>',
           "Document Checklists for Registration, GST, Trademark &amp; ROC | LegalReet", "Documents required for company registration, GST, trademark, FSSAI, ISO, ROC filings, conversions and legal drafting.", actions=False)

    # ------------------------------------------------------------ FAQ
    simple("/faq.html", "FAQs", "FAQs", "Answers to the questions we hear most",
           "About our fees, process, timelines and how we work.",
           f'<section class="sec"><div class="container narrow"><div class="faqs">{c["faq_html"](GENERAL_FAQS)}</div></div></section>',
           "Frequently Asked Questions | LegalReet", "Answers to common questions about LegalReet fees, process, timelines, payments and online filing.", schemas=[c["faq_schema"](GENERAL_FAQS)], actions=False)

    # ------------------------------------------------------------ ACADEMY
    academy = f'''<section class="sec"><div class="container two-col">
  <div>{sh("LegalReet Academy", "Learn accounting and taxation the way it's actually done")}
    <div class="prose"><p>Degrees teach the law; offices expect you to file. LegalReet Academy is practical training for commerce students, graduates, accountants and small business owners who want to work confidently on real GST, income tax, TDS and company-law portals.</p>
    <p>Sessions are taught by working professionals using live-style case files: a trader's GST returns, a salaried client's ITR with capital gains, a small company's annual ROC filing. You practise on the same checklists our own team uses.</p></div>
    <ul class="ticks">{"".join(f"<li>{ico('check')}<span>{x}</span></li>" for x in ["Small batches, in Agra and online", "Hands-on assignments on every topic", "Doubt-solving with practising professionals", "Certificate of completion", "Internship opportunities for top performers"])}</ul>
    <a class="btn btn-primary" href="/courses.html">See course tracks</a></div>
  <div class="value-grid">
    <div class="pillar">{ico("book")}<h4>Who it's for</h4><p>B.Com / M.Com students and graduates, CA and CS students, accountants and business owners.</p></div>
    <div class="pillar">{ico("doc")}<h4>Case-file learning</h4><p>Each topic is taught through a realistic client file, from documents to filed return.</p></div>
    <div class="pillar">{ico("users")}<h4>Taught by practitioners</h4><p>Faculty who file returns and handle notices every week.</p></div>
    <div class="pillar">{ico("cal")}<h4>Flexible timings</h4><p>Weekday and weekend batches, with recordings for missed sessions.</p></div>
  </div>
</div></section>'''
    simple("/academy.html", "LegalReet Academy", "Learn with us", "Practical accounting, GST and income tax training",
           "Job-ready skills on real portals and real case files, taught by practising professionals.", academy,
           "LegalReet Academy &ndash; Practical GST, Income Tax &amp; Accounting Training in Agra", "Practical training in accounting, GST, income tax, TDS and company law compliance for students, graduates and business owners.")

    # ------------------------------------------------------------ COURSES
    tracks = [
        ("Foundation", "For students and beginners", ["Accounting fundamentals and journal entries", "Bookkeeping in accounting software", "GST basics: registration, invoices, input tax credit", "Filing GSTR-1 and GSTR-3B", "Income tax basics and ITR-1 filing", "TDS concepts for small businesses"]),
        ("Practitioner", "For working accountants", ["GST reconciliation (GSTR-2B vs books)", "E-way bills and e-invoicing", "ITR-2, ITR-3 and ITR-4 with capital gains and business income", "TDS returns and correction statements", "Payroll, PF and ESI filings", "Finalisation of accounts for proprietors and firms"]),
        ("Advanced", "For senior accountants and CA/CS students", ["Company law compliance: AOC-4, MGT-7, DIR-3 KYC, ADT-1", "LLP annual filings and event-based forms", "Tax audit (Form 3CD) preparation", "GST annual return and reconciliation", "Replying to GST and income tax notices", "Project reports and CMA data for bank finance"]),
    ]
    cards = "".join(f'''<div class="pk{" pk-pop" if i==1 else ""}">{'<span class="pk-badge">Most chosen</span>' if i==1 else ''}<h3>{n}</h3><p class="muted">{w}</p><ul>{"".join(f"<li>{ico('check')}{m}</li>" for m in mods)}</ul>
      <a class="btn {"btn-primary" if i==1 else "btn-ghost"} btn-block" href="{wa(f"Hi LegalReet, I would like details of the {n} course.")}" target="_blank" rel="noopener">Ask for batch dates &amp; fees</a></div>''' for i, (n, w, mods) in enumerate(tracks))
    simple("/courses.html", "Courses", "Courses", "Three tracks, from first entry to final filing",
           "Choose the track that matches where you are. Each one builds on the last.",
           f'<section class="sec"><div class="container"><div class="pk-grid pk-grid-3">{cards}</div><p class="muted center">Batch dates and fees are shared on request. Syllabus is updated for changes in GST and the Income-tax Act, 2025.</p></div></section>',
           "Courses &ndash; GST, Income Tax &amp; Company Law Training | LegalReet", "Foundation, Practitioner and Advanced courses in accounting, GST, income tax, TDS and company law compliance.")

    # ------------------------------------------------------------ PAYMENT OPTIONS
    pay = prose(f'''<h2>How to pay LegalReet</h2>
<p>We accept payment by UPI, bank transfer (NEFT, RTGS, IMPS), debit or credit card through a secure payment link, and cheque for retainer clients. Payment details are always shared with your written quote.</p>
<h3>Before you pay</h3>
<ul><li>Only pay against a written quote or invoice received from <a href="mailto:{EMAIL}">{EMAIL}</a> or our official number {PHONE}.</li>
<li>Payments are accepted only into accounts in the name of LegalReet's billing entity as printed on your invoice. We never ask you to pay into an individual's personal account.</li>
<li>If anything about a payment request looks unusual, call us on {PHONE} before paying.</li></ul>
<h3>Government fees</h3>
<p>Government fees and stamp duty are paid to the department concerned, either directly by you or by us on your behalf at actual cost. They are shown separately in your quote and invoice.</p>
<h3>Invoices</h3>
<p>A tax invoice is issued for every payment of professional fees. If you need the invoice in your company's name with its GSTIN, share the details before payment.</p>
<h3>EMI</h3>
<p>For larger engagements, ask about paying in instalments. Instalment plans are agreed in writing before work begins.</p>''')
    simple("/payment-options.html", "Payment options", "Pay now", "Payment options",
           "Simple, secure ways to pay &mdash; and how to make sure you're paying LegalReet.", pay,
           "Payment Options | LegalReet", "How to pay LegalReet by UPI, bank transfer, card or cheque, and how to verify a payment request.")

    # ------------------------------------------------------------ GRIEVANCE
    griev = prose(f'''<h2>Raising a complaint</h2>
<p>If something has gone wrong with your service, we want to hear about it and fix it. Please write to <a href="mailto:{EMAIL}?subject=Grievance">{EMAIL}</a> with &ldquo;Grievance&rdquo; in the subject line, or call {PHONE}.</p>
<h3>Please include</h3>
<ul><li>Your name and registered mobile number</li><li>The service and approximate date you engaged us</li><li>What went wrong and what you would like us to do</li><li>Copies of any relevant messages, invoices or documents</li></ul>
<h3>What happens next</h3>
<ul><li><strong>Within 2 working days:</strong> we acknowledge your complaint and share a reference number.</li>
<li><strong>Within 7 working days:</strong> a senior member of the team reviews the file and responds with findings and a proposed resolution.</li>
<li><strong>Within 15 working days:</strong> we aim to close the complaint. If it depends on a government department, we tell you what is pending and with whom.</li></ul>
<h3>Escalation</h3>
<p>If you are not satisfied with the response, reply to the same email asking for escalation. Your complaint will then be reviewed by the firm's leadership, who will respond in writing.</p>''')
    simple("/grievance.html", "Grievance", "Grievance redressal", "Grievance and complaints",
           "A clear, time-bound process for resolving complaints.", griev,
           "Grievance Redressal | LegalReet", "How to raise a complaint with LegalReet and the timelines for acknowledgement, review and resolution.", actions=False)

    # ------------------------------------------------------------ POLICIES
    privacy = prose(f'''<p class="muted">Last updated: 23 October 2026</p>
<h2>Who we are</h2><p>This policy explains how LegalReet (&ldquo;we&rdquo;, &ldquo;us&rdquo;) collects and uses personal information through legalreet.com and when providing our services. We process personal data in line with the Digital Personal Data Protection Act, 2023 and other applicable Indian law.</p>
<h2>What we collect</h2><ul><li><strong>Enquiry details</strong> you submit: name, mobile number, email, city and the service you need.</li><li><strong>Documents and information</strong> you share for a filing, such as PAN, Aadhaar, address proofs, photographs, financial statements and business details.</li><li><strong>Technical data</strong> such as browser type and pages visited. Analytics cookies are set only if you accept them.</li></ul>
<h2>How we use it</h2><ul><li>To respond to your enquiry and prepare a quote.</li><li>To prepare and file applications and returns with government authorities on your instructions.</li><li>To send you service updates and reminders of due dates relevant to the services you use.</li><li>To meet our legal, tax and professional record-keeping obligations.</li></ul>
<h2>Who we share it with</h2><p>We share your information only with the government authority, certifying body or certifying authority needed to complete your service, with service providers who help us operate (such as email, hosting and payment providers) under confidentiality obligations, or where the law requires. We do not sell personal data.</p>
<h2>How long we keep it</h2><p>We keep records for as long as needed to provide the service and to meet statutory retention periods under tax and company law, after which they are deleted or anonymised.</p>
<h2>Your rights</h2><p>You may ask to access, correct or erase your personal data, withdraw consent for optional processing, or nominate someone to exercise these rights. Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. Some records must be retained by law even after a request to erase.</p>
<h2>Security</h2><p>Access to client documents is restricted to people working on your file. We use reasonable technical and organisational safeguards, but no transmission over the internet is completely secure.</p>
<h2>Contact</h2><p>Questions or complaints about this policy can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a> or by post to {ADDR}.</p>''')
    simple("/privacy-policy.html", "Privacy policy", "Policies", "Privacy policy", "How we collect, use and protect your information.", privacy,
           "Privacy Policy | LegalReet", "LegalReet privacy policy: what personal data we collect, how we use and protect it, and your rights.", actions=False, show_cta=False)

    refund = prose(f'''<p class="muted">Last updated: 23 October 2026</p>
<h2>Our approach</h2><p>We want you to pay only for work that has been done. Refunds depend on how far your service has progressed when you cancel.</p>
<h2>Professional fees</h2><ul>
<li><strong>Before work starts:</strong> if you cancel before we have begun preparing your documents or application, the professional fee is refunded in full.</li>
<li><strong>After work starts, before filing:</strong> we refund the professional fee after deducting a fair charge for work already done, which we explain in writing.</li>
<li><strong>After filing:</strong> once an application or return has been filed with an authority, the professional fee is not refundable.</li></ul>
<h2>Government fees and third-party costs</h2><p>Government fees, stamp duty, DSC charges and certification-body fees that have already been paid on your behalf cannot be refunded by us, as they are paid to third parties.</p>
<h2>Rejections</h2><p>Approval is decided by the authority concerned and cannot be guaranteed. If an application is rejected because of an error on our part, we refile it at no additional professional fee. Rejections caused by incorrect or incomplete information supplied to us, or by the authority's own policy, are not grounds for a refund.</p>
<h2>How to request a refund</h2><p>Email <a href="mailto:{EMAIL}?subject=Refund%20request">{EMAIL}</a> with your invoice number. Approved refunds are processed to the original payment method within 10 working days.</p>''')
    simple("/refund-policy.html", "Refund policy", "Policies", "Refund and cancellation policy", "What is refundable, and how to ask for it.", refund,
           "Refund Policy | LegalReet", "LegalReet refund and cancellation policy for professional fees and government fees.", actions=False, show_cta=False)

    terms = prose(f'''<p class="muted">Last updated: 23 October 2026</p>
<h2>Using this website</h2><p>Information on legalreet.com is general information about our services and Indian law. It is not advice for your specific situation and may not reflect changes made after publication. Do not act on it without speaking to us or another qualified professional.</p>
<h2>Our services</h2><ul><li>The scope, fee and timeline of each engagement are confirmed in writing before work begins. Work outside that scope is quoted separately.</li><li>Timelines are estimates. Processing by government authorities and certification bodies is outside our control.</li><li>We act on the information and documents you give us. You are responsible for their accuracy and authenticity.</li><li>Approvals, registrations and certificates are granted at the discretion of the authority concerned and cannot be guaranteed.</li></ul>
<h2>Your responsibilities</h2><p>You agree to provide complete and truthful information, respond to requests for documents in time, and pay fees as agreed. Delays in providing information may delay filings and lead to late fees imposed by authorities.</p>
<h2>Fees</h2><p>Published fees are starting fees and exclude government fees, stamp duty and GST unless stated otherwise. Our <a href="/refund-policy.html">refund policy</a> forms part of these terms.</p>
<h2>Confidentiality</h2><p>We keep your information confidential and use it only to deliver your services, subject to our <a href="/privacy-policy.html">privacy policy</a> and our obligations under law.</p>
<h2>Liability</h2><p>Our liability for any claim relating to a service is limited to the professional fee paid for that service. We are not liable for losses caused by delays or decisions of authorities, or by inaccurate information supplied to us.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of India. Courts at Agra, Uttar Pradesh have jurisdiction over any dispute.</p>
<h2>Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> &middot; {PHONE} &middot; {ADDR}</p>''')
    simple("/terms.html", "Terms &amp; conditions", "Policies", "Terms and conditions", "The terms that apply when you use this website and our services.", terms,
           "Terms &amp; Conditions | LegalReet", "Terms and conditions for using legalreet.com and LegalReet services.", actions=False, show_cta=False)

    # ------------------------------------------------------------ THANK YOU / 404
    pages["/thank-you.html"] = page("Thank you | LegalReet", "We have received your request.", "/thank-you.html",
        hero("Request received", "Thank you &mdash; we'll call you shortly", f"A LegalReet expert will contact you within working hours ({HOURS}). For anything urgent, message us on WhatsApp.") +
        f'<section class="sec"><div class="container center"><a class="btn btn-primary" href="/services/index.html">Browse services</a></div></section>')
    pages["/404.html"] = page("Page not found | LegalReet", "This page could not be found.", "/404.html",
        hero("404", "We couldn't find that page", "The page may have moved. Try searching our services or head back to the home page.", actions=False) +
        f'<section class="sec"><div class="container center"><a class="btn btn-primary" href="/">Go to home page</a> <a class="btn btn-ghost" href="/services/index.html">All services</a></div></section>')
    return pages
