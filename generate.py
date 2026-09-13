# -*- coding: utf-8 -*-
import os
import re
import json
import urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))

CATEGORIES = [
    {"id": "a", "letter": "A", "name": "Start a Business",
     "tagline": "Register the right entity, the right way.",
     "icon": '<path d="M6 30V13l11-7 11 7v17" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M12 30V19h10v11" stroke="currentColor" stroke-width="1.6"/><path d="M6 30h22" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'},
    {"id": "b", "letter": "B", "name": "Registrations & Certifications",
     "tagline": "Licenses, trademarks and quality certifications.",
     "icon": '<path d="M17 4l4 8 9 1.2-6.5 6.2 1.6 8.9L17 24l-8.1 4.3 1.6-8.9L4 13.2 13 12z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>'},
    {"id": "c", "letter": "C", "name": "Manage & Grow Business",
     "tagline": "Compliance, audits and business advisory.",
     "icon": '<path d="M5 24l7-8 5 4 9-11" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path d="M21 8h6v6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>'},
    {"id": "d", "letter": "D", "name": "Legal Documents",
     "tagline": "Agreements and filings, drafted right the first time.",
     "icon": '<rect x="7" y="5" width="15" height="20" rx="1.5" stroke="currentColor" stroke-width="1.6"/><path d="M11 11h7M11 15h7M11 19h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M23 21l4-4 2 2-4 4h-2v-2z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>'},
]

SERVICES = []

def svc(slug, cat, name, short, overview, benefits, documents, timeline):
    SERVICES.append({"slug": slug, "cat": cat, "name": name, "short": short,
                      "overview": overview, "benefits": benefits, "documents": documents,
                      "timeline": timeline})

# =========================================================================
# CATEGORY A — Start a Business
# =========================================================================

svc("private-limited-company-registration", "a", "Private Limited Company Registration",
    "Incorporate a Private Limited Company under the Companies Act — the standard structure for startups raising funding.",
    "A Private Limited Company gives founders limited liability, a separate legal identity, and the structure investors expect before writing a cheque. We handle name approval, DSC, DIN, incorporation filing, and PAN/TAN end to end.",
    ["Limited liability protects personal assets", "Preferred structure for VC and angel funding", "Perpetual succession independent of founders"],
    ["PAN & Aadhaar of all directors", "Passport-size photographs", "Proof of registered office with NOC", "Bank statement of directors"],
    "7-15 working days")

svc("public-limited-company-registration", "a", "Public Limited Company Registration",
    "Incorporate a Public Limited Company for businesses planning to raise capital from the public or list on an exchange.",
    "A Public Limited Company can offer shares to the public and list on a stock exchange, at the cost of heavier compliance and a minimum of seven shareholders and three directors. We handle the incorporation and the additional regulatory filings this structure requires.",
    ["Can raise capital from the public", "Shares are freely transferable", "Higher credibility with large institutional partners"],
    ["PAN & Aadhaar of all directors and shareholders", "Proof of registered office with NOC", "Memorandum & Articles of Association details", "Director's basic details and DSC"],
    "15-20 working days")

svc("one-person-company-registration", "a", "One Person Company (OPC) Registration",
    "Incorporate as a One Person Company to get corporate structure and limited liability as a solo founder.",
    "An OPC lets a single founder hold 100% ownership while still getting the limited liability and credibility of a company. We handle nominee appointment, MOA/AOA drafting, and the incorporation filing.",
    ["100% ownership retained by one person", "Limited liability protection", "Easier to convert to a Private Limited Company later"],
    ["PAN & Aadhaar of the sole member and nominee", "Passport-size photographs", "Proof of registered office", "Nominee consent (Form INC-3)"],
    "7-12 working days")

svc("section-8-company-registration", "a", "Section 8 Company Registration",
    "Incorporate a Section 8 Company for a non-profit or NGO operating with a company structure.",
    "A Section 8 Company suits non-profits that want the governance and credibility of a company while committing profits entirely to their charitable objective. We handle the licence application and incorporation filing.",
    ["Corporate structure with limited liability for members", "Preferred by CSR and grant-giving foundations", "No minimum capital requirement"],
    ["PAN & Aadhaar of all directors", "Proof of registered office", "Draft MOA stating charitable objectives"],
    "15-20 working days")

svc("nidhi-company-registration", "a", "Nidhi Company Registration",
    "Register a Nidhi Company to operate a member-only savings and lending business.",
    "A Nidhi Company lets a group borrow from and lend to its own members under a regulated, member-only structure — common for community savings schemes. We handle incorporation against the specific member and capital thresholds the rules require.",
    ["Regulated structure for member lending and deposits", "No RBI licence required, unlike an NBFC", "Builds community trust through formal registration"],
    ["PAN & Aadhaar of all directors", "Proof of registered office", "Minimum 7 members' KYC documents"],
    "15-20 working days")

svc("nbfc-registration", "a", "Finance Company (NBFC) Registration",
    "Register a Non-Banking Financial Company to legally offer loans, credit or asset financing.",
    "An NBFC lets you carry on lending, investment or asset-financing activity outside the traditional banking licence, subject to RBI's minimum net-owned-fund and registration requirements. We structure the entity and prepare the RBI application.",
    ["Legally offer loans, leasing or investment products", "Regulatory pathway distinct from a full banking licence", "Structured for RBI's net-owned-fund threshold"],
    ["Certificate of incorporation", "Net-owned-fund certificate from a chartered accountant", "Director & shareholder KYC", "Business plan for the next 3 years"],
    "60-90 working days (RBI approval dependent)")

svc("micro-finance-company-registration", "a", "Micro Finance Company Registration",
    "Set up a micro-finance NBFC to extend small-ticket loans to underserved borrowers.",
    "A micro-finance company is an NBFC-MFI structured specifically for small, collateral-free loans to low-income borrowers, subject to RBI's specific qualifying-asset and income criteria. We handle the entity structuring and the RBI-MFI application.",
    ["Purpose-built structure for small-ticket lending", "Access to priority-sector lending partnerships", "Clear regulatory pathway under RBI's MFI framework"],
    ["Certificate of incorporation", "Net-owned-fund certificate", "Director & promoter KYC", "Detailed business and lending plan"],
    "60-90 working days (RBI approval dependent)")

svc("producer-company-registration", "a", "Producer Company Registration",
    "Incorporate a Producer Company for farmers or producers pooling resources under a company structure.",
    "A Producer Company lets primary producers — farmers, artisans, weavers — form a company-style entity to collectively process, market and sell their output while sharing profits as members. We handle incorporation and the producer-specific MOA clauses.",
    ["Corporate structure owned entirely by producer-members", "Access to institutional credit and government schemes", "Limited liability for all member-producers"],
    ["PAN & Aadhaar of all directors", "Proof of registered office", "Membership list of producer members"],
    "12-15 working days")

svc("sole-proprietorship-registration", "a", "Sole Proprietorship Registration",
    "Set up a sole proprietorship with the registrations needed to open a bank account and start invoicing.",
    "For a single-owner business that doesn't need a separate legal entity, we handle the registrations that make it operational — typically GST, MSME/Udyam and a Shops & Establishment licence — so you can open a current account and start billing.",
    ["Fastest and least expensive structure to start", "Minimal ongoing compliance", "Full control retained by the owner"],
    ["PAN & Aadhaar of the proprietor", "Passport-size photograph", "Proof of business address"],
    "3-5 working days")

svc("partnership-firm-registration", "a", "Partnership Firm Registration",
    "Draft and register a partnership deed for two or more partners running a business together.",
    "A registered partnership gives partners a documented, enforceable agreement covering profit sharing, responsibilities and exit terms, and lets the firm open a current account and take legal action if a dispute arises. We draft the deed and file the registration.",
    ["Faster and cheaper to set up than a company", "Registered deed is legally enforceable", "Simple profit-sharing and tax structure"],
    ["PAN & Aadhaar of all partners", "Passport-size photographs", "Proof of business address", "Partnership deed on stamp paper"],
    "5-7 working days")

svc("llp-registration", "a", "Limited Liability Partnership (LLP) Registration",
    "Register an LLP for a partnership structure with limited liability and lighter compliance than a private company.",
    "An LLP suits professional services firms and small partnerships that want limited liability without the compliance load of a private company. We handle DPIN allotment, name reservation and drafting of the LLP agreement alongside incorporation.",
    ["Limited liability for all partners", "No minimum capital requirement", "Lower ongoing compliance than a private company"],
    ["PAN & Aadhaar of all designated partners", "Passport-size photographs", "Proof of registered office", "LLP agreement"],
    "7-10 working days")

svc("shop-establishment-registration", "a", "Shops & Establishment Registration",
    "Register under the Shops & Establishment Act, required for most commercial premises before you can open a bank account.",
    "This state-level registration is required for almost any commercial establishment with a physical premises and employees, and is often the first document a bank asks for when opening a current account. We file it with the relevant state labour department.",
    ["Required to open a business current account in most banks", "State-mandated for any commercial premises", "Governs working hours and employee conditions"],
    ["PAN of the business", "Proof of business address", "List of employees, if any", "Photograph of the premises"],
    "5-7 working days")

svc("msme-udyam-registration", "a", "MSME / Udyam Registration",
    "Register as an MSME on the Udyam portal to access government schemes and lending benefits from day one.",
    "Udyam registration classifies your business as a Micro, Small or Medium Enterprise, unlocking collateral-free loans, delayed-payment protection from buyers, and government tender preferences. We file the self-declared application against your PAN and GST data.",
    ["Collateral-free loans under CGTMSE", "Legal protection against delayed payments", "Priority in government tenders and subsidies"],
    ["PAN of the business/proprietor", "Aadhaar of the proprietor/authorised signatory", "GST registration, if applicable", "Bank account details"],
    "1-2 working days")

svc("aop-registration", "a", "Association of Persons (AOP) Registration",
    "Register an Association of Persons for two or more people or entities pooling resources for a common commercial purpose.",
    "An AOP suits a group of individuals or entities coming together for a joint commercial venture without forming a company or partnership. We draft the governing agreement and complete the PAN and tax registrations the structure needs.",
    ["Flexible structure for a joint short-term venture", "No minimum capital or entity-formation cost", "Straightforward to wind up once the purpose is met"],
    ["PAN & Aadhaar of all members", "Proof of business address", "Governing agreement defining each member's share"],
    "5-7 working days")

svc("boi-registration", "a", "Body of Individuals (BOI) Registration",
    "Register a Body of Individuals for a group of people acting together for income-generating activity.",
    "A BOI is similar to an AOP but is specifically restricted to individuals (not other entities) coming together for a common purpose that generates income. We prepare the governing document and the PAN/tax registration.",
    ["Simple structure for a group of individuals", "No separate legal entity needed", "Income taxed at the BOI level, simplifying individual filings"],
    ["PAN & Aadhaar of all individuals", "Proof of address", "Agreement defining the common purpose and shares"],
    "5-7 working days")

svc("huf-formation", "a", "Hindu Undivided Family (HUF) Formation",
    "Formalise a Hindu Undivided Family as a separate tax entity to consolidate and plan family income and assets.",
    "An HUF is a distinct tax entity recognised for Hindu, Sikh, Jain and Buddhist families, useful for consolidating ancestral property and planning family tax liability separately from individual members. We draft the HUF deed and complete the PAN registration.",
    ["Separate PAN and tax slab from individual members", "Recognised vehicle for ancestral property and family business", "Useful tool for legitimate family tax planning"],
    ["PAN & Aadhaar of the Karta and coparceners", "HUF creation deed", "Proof of family address"],
    "5-7 working days")

svc("society-registration", "a", "Society Registration",
    "Register a society under the Societies Registration Act for a membership-based non-profit.",
    "A society suits membership-driven initiatives — alumni associations, welfare groups, cultural bodies — governed by a managing committee under a memorandum of association. We draft the memorandum and file with the Registrar of Societies.",
    ["Governance by an elected managing committee", "Suited to membership-based organisations", "Eligible for 12A/80G once registered"],
    ["PAN & Aadhaar of at least 7 members", "Proof of registered office", "Memorandum of association"],
    "15-20 working days")

svc("trust-registration", "a", "Trust Registration",
    "Register a public charitable trust with a trust deed defining its objectives and trustees.",
    "A trust is often the simplest structure for a charitable initiative, defined by a trust deed rather than a company constitution. We draft the deed and register it with the local Sub-Registrar.",
    ["Simple to set up with fewer ongoing filings", "Trust deed defines governance clearly", "Eligible for 12A/80G once registered"],
    ["PAN & Aadhaar of settlor and trustees", "Proof of registered office", "Trust deed on stamp paper"],
    "10-12 working days")

svc("startup-india-registration", "a", "Startup India (DPIIT) Recognition",
    "Get DPIIT recognition to unlock tax exemptions, easier compliance, and startup-scheme eligibility.",
    "DPIIT recognition under Startup India opens access to income tax exemptions, self-certification for labour-law compliance, and eligibility for government funds and tenders. We prepare the application and the supporting write-up on your innovation and scalability.",
    ["Income tax exemption under Section 80-IAC, if eligible", "Self-certification for 6 labour & environment laws", "Access to government startup funds and tenders"],
    ["Certificate of incorporation", "PAN of the entity", "Brief write-up on business innovation", "Website or pitch deck, if available"],
    "5-7 working days")

svc("joint-venture-registration", "a", "Joint Venture Structuring & Registration",
    "Structure and register a joint venture between two or more businesses pooling resources for a shared project.",
    "A joint venture needs a clear governing agreement and, often, a dedicated entity before two businesses can pool capital, technology or market access for a shared project. We structure the JV, draft the agreement, and handle any entity registration it requires.",
    ["Clear governance before capital or IP is pooled", "Structure matched to the specific project scope", "Reduces disputes over exit and profit-sharing later"],
    ["PAN & incorporation documents of all JV partners", "Proposed scope and contribution of each partner", "Board approval from each partner entity"],
    "10-15 working days")

# =========================================================================
# CATEGORY B — Registrations & Certifications
# =========================================================================

svc("gst-registration", "b", "GST Registration",
    "Register for GST to legally invoice with tax and claim input tax credit.",
    "GST registration is mandatory once turnover crosses the threshold, or immediately if you sell inter-state or on e-commerce marketplaces. We handle the application, ARN tracking, and certificate delivery on GSTN.",
    ["Legally invoice clients with GST", "Claim input tax credit on business purchases", "Required to sell on e-commerce marketplaces"],
    ["PAN & Aadhaar of proprietor/directors", "Proof of business address", "Bank statement or cancelled cheque", "Photograph of proprietor/directors"],
    "3-7 working days")

svc("fssai-food-license", "b", "FSSAI Food License",
    "Get the FSSAI license or registration required to legally manufacture, sell, or store food.",
    "Any food business — from a home kitchen to a manufacturing unit — needs FSSAI registration or a licence, tiered by turnover and scale. We assess which tier applies and file the correct application.",
    ["Legally required to sell, store or manufacture food", "Tier matched to your turnover to avoid over-filing", "Builds customer trust with the FSSAI mark"],
    ["PAN & Aadhaar of the applicant", "Proof of business premises", "List of food products", "NOC from local municipality, for higher tiers"],
    "7-10 working days")

svc("import-export-code", "b", "Import Export Code (IEC)",
    "Get an IEC from DGFT — mandatory to import or export goods and services.",
    "No business can legally import or export without an Import Export Code issued by DGFT. We file the online application against your PAN and current account, and track it through to certificate issuance.",
    ["Mandatory for any cross-border trade", "One-time registration, valid for life", "Required to claim export incentive schemes"],
    ["PAN of the business", "Cancelled cheque or bank certificate", "Proof of business address", "Digital Signature Certificate"],
    "2-3 working days")

svc("pf-registration", "b", "PF (EPF) Registration",
    "Register for EPF once your headcount crosses the statutory threshold.",
    "EPF registration becomes mandatory once a business crosses 20 employees, requiring monthly employer and employee contributions to be deducted and deposited. We handle the registration against your employee and salary data.",
    ["Mandatory once headcount crosses 20 employees", "Gives employees a formal retirement savings account", "Avoids penalties for delayed registration"],
    ["PAN & registration certificate of the business", "Employee list with salary details", "Bank account for EPFO transactions"],
    "5-7 working days")

svc("esi-registration", "b", "ESI Registration",
    "Register for ESI to give eligible employees access to medical benefit coverage.",
    "ESI registration is mandatory for businesses above the employee threshold in notified areas, giving employees earning below the wage ceiling access to medical benefits. We handle the registration against your employee data.",
    ["Gives eligible employees medical benefit coverage", "Mandatory above the employee/wage threshold", "Builds employee trust and retention"],
    ["PAN & registration certificate of the business", "Employee list with salary details", "Address proof of the establishment"],
    "5-7 working days")

svc("fcra-registration", "b", "FCRA Registration",
    "Register under FCRA to legally receive foreign contributions for your NGO or trust.",
    "An NGO, trust or society must hold FCRA registration before it can legally accept donations or grants from foreign sources — without it, foreign funds cannot be received at all. We prepare the application against the organisation's three-year activity and financial track record.",
    ["Legally required to receive any foreign donation or grant", "Opens access to international foundations and CSR", "Demonstrates governance maturity to funders"],
    ["Trust deed / society or Section 8 registration", "Three years of activity reports and audited financials", "12A/80G registration certificate", "Details of the FCRA-designated bank account"],
    "60-90 working days (MHA approval dependent)")

svc("trade-license", "b", "Trade License",
    "Get the municipal trade license required to legally operate a business from a physical premises.",
    "Local municipal corporations require a trade licence before you operate certain categories of business from a physical location — restaurants, warehouses and manufacturing units among them. We file the application with the relevant municipal body.",
    ["Required to legally operate from the premises", "Avoids municipal inspection penalties", "Renewed annually alongside other local filings"],
    ["Proof of business premises", "PAN of the business", "NOC from fire department, for applicable categories"],
    "10-15 working days")

svc("professional-tax-registration", "b", "Professional Tax Registration",
    "Register for professional tax, a state-level tax on employment and professional income.",
    "Most states require both employers and certain professionals to register and pay professional tax. We handle both the employer registration and enrolment for deducting it from employee salaries.",
    ["Avoids state-level non-compliance penalties", "Enables correct deduction from payroll", "Required in most states before hiring staff"],
    ["PAN of the business", "Proof of business address", "Employee salary details"],
    "5-7 working days")

svc("12a-80g-registration", "b", "12A & 80G Registration",
    "Register under 12A for tax-exempt NGO income and 80G so your donors can claim a tax deduction.",
    "12A exempts your NGO's own income from tax, and 80G lets your donors claim a deduction on their contribution — both significantly widen your funding base. We file both applications with the supporting activity and financial documentation.",
    ["NGO's own income becomes tax-exempt", "Donors can claim a tax deduction under 80G", "Often required by CSR and grant-giving foundations"],
    ["Trust deed / Section 8 / society registration", "PAN of the organisation", "Activity report & financial statements"],
    "20-30 working days")

svc("ngo-darpan-niti-aayog-registration", "b", "NITI Aayog / NGO Darpan Registration",
    "Register your NGO on the NITI Aayog NGO Darpan portal, now required for most government and CSR funding.",
    "NGO Darpan registration issues a unique ID that most government departments and CSR-funding companies now require before releasing a grant. We prepare and file the registration against your organisation's incorporation and activity documents.",
    ["Required for most government grant applications", "Increasingly required by CSR-funding companies", "One-time registration, renewed periodically"],
    ["Trust deed / Section 8 / society registration", "PAN of the organisation", "Details of governing body members"],
    "5-10 working days")

svc("trademark-search", "b", "Trademark Search",
    "Check whether your brand name or logo is available before you file or start using it.",
    "A trademark search across the relevant class flags conflicting marks before you invest in a brand, avoiding a rejected application or an infringement claim later. We run the search and give you a plain-English risk assessment.",
    ["Flags conflicting marks before you file", "Confirms the right class to file under", "Reduces risk of a later objection or opposition"],
    ["Brand name / logo to be searched", "Description of goods or services"],
    "1 working day")

svc("trademark-registration", "b", "Trademark Registration & Filing",
    "File and register your brand name or logo as a trademark with the Trademark Registry.",
    "Registering your trademark gives you exclusive nationwide rights to the name or logo in your class, and the standing to send a cease-and-desist if someone else uses it. We handle the class selection, application drafting, and filing.",
    ["Exclusive nationwide rights in your class", "™ can be used immediately after filing", "Legal standing to act against infringement"],
    ["Brand name / logo (JPEG)", "Applicant's PAN & address proof", "Udyam certificate, for MSME fee discount", "Power of attorney (Form TM-48)"],
    "1 working day to file; registration in 12-18 months")

svc("trademark-renewal", "b", "Trademark Renewal",
    "Renew your registered trademark before its 10-year term lapses.",
    "A trademark registration lasts 10 years and must be renewed to stay in force — an expired mark can be removed from the register and become available to others. We track your renewal date and file it in advance.",
    ["Renewal deadline tracked automatically", "Avoids removal from the register", "Filed with a buffer before expiry"],
    ["Trademark registration certificate", "Applicant's current address proof"],
    "3-5 working days to file")

svc("trademark-objection", "b", "Trademark Objection Response",
    "Respond to an examiner's objection raised against your trademark application.",
    "An objection from the Registry examiner doesn't end your application — a well-argued response, filed within the deadline, often overcomes it. We draft the reply citing the specific grounds raised.",
    ["Statutory deadline tracked and met", "Reply drafted by a trademark specialist", "Common objections resolved without a hearing"],
    ["Examination report", "Proof of prior use, if any", "Original application documents"],
    "As per Registry deadline, typically 30 days")

svc("trademark-opposition", "b", "Trademark Opposition Defence",
    "Defend your trademark application against a third-party opposition.",
    "A third party can formally oppose your published trademark application within the statutory window. We draft the counter-statement and represent your case through to the hearing if required.",
    ["Counter-statement drafted within the statutory window", "Evidence and prior-use documentation organised", "Hearing representation included where required"],
    ["Opposition notice received", "Proof of prior use or genuine intent to use", "Original application documents"],
    "As per Registry deadline, typically 2 months")

svc("trademark-rectification", "b", "Trademark Rectification",
    "File a rectification application to correct, cancel or remove a trademark from the register.",
    "A rectification petition is used to correct an error in a registration, or to cancel a mark that shouldn't be on the register — including one blocking your own application unfairly. We assess grounds and file the petition with the Registry or IPAB-successor tribunal.",
    ["Removes wrongly registered or non-used marks", "Corrects genuine errors in an existing registration", "Can clear the way for your own pending application"],
    ["Details of the mark to be rectified", "Grounds for rectification and supporting evidence"],
    "Filed in 5-7 working days; disposal timeline varies")

svc("patent-search", "b", "Patent Search",
    "Run a prior-art search to confirm your invention is genuinely novel before you file.",
    "A patentable invention must be novel and non-obvious against everything already publicly known — a prior-art search confirms this before you spend on drafting and filing. We search Indian and international databases and report the findings in plain language.",
    ["Confirms novelty before you invest in drafting", "Reduces risk of a rejected application", "Identifies the closest existing patents to design around"],
    ["Detailed invention disclosure", "Drawings or diagrams, if any"],
    "5-7 working days")

svc("provisional-patent-registration", "b", "Provisional Patent Application",
    "File a provisional patent application to secure an early priority date while you finalise the invention.",
    "A provisional application locks in your priority date for 12 months while you continue developing the invention or seeking funding, before the complete specification is due. We draft and file it with a technical writer.",
    ["Secures an early priority date immediately", "12 months to finalise the complete specification", "Lets you use \"patent pending\" right away"],
    ["Detailed invention disclosure", "Drawings or diagrams, if any", "Applicant's ID proof"],
    "7-10 working days")

svc("patent-registration", "b", "Patent Registration",
    "File a complete patent specification and prosecute the application through to grant.",
    "A complete patent application requires a full technical specification, claims, and prosecution through examiner objections over several years to grant. We draft the specification with a patent-qualified writer and manage the prosecution.",
    ["Full specification drafted by a patent-qualified writer", "Prosecution managed through to grant", "20-year exclusive right once granted"],
    ["Detailed invention disclosure", "Drawings or diagrams", "Provisional application, if already filed", "Applicant's ID proof"],
    "18-36 months to grant, filed within 15-20 working days")

svc("copyright-registration", "b", "Copyright Registration",
    "Register copyright for original literary, artistic, musical, or software works.",
    "Copyright protects original creative and software works from the moment of creation, but registration creates strong, dated evidence of ownership, useful in licensing deals and infringement disputes. We prepare and file the application with the Copyright Office.",
    ["Dated proof of ownership for licensing or disputes", "Covers literary, artistic, musical and software works", "Valid for the creator's lifetime plus 60 years"],
    ["Copy of the work", "Applicant's ID proof", "NOC from co-authors, if any"],
    "Filed in 3 working days; registration in 6-12 months")

svc("iso-9001-certification", "b", "ISO 9001 Certification (Quality Management)",
    "Get ISO 9001 certified to demonstrate a consistent, audited quality management system.",
    "ISO 9001 is the most widely recognised quality-management standard, signalling to enterprise clients and tenders that your processes are documented, consistent and audited. We prepare your documentation and coordinate the certification audit.",
    ["Strengthens credibility with enterprise clients & RFPs", "Documentation matched to your actual process", "Certification via an accredited body"],
    ["Business registration proof", "Existing process documentation, if any", "List of key business activities"],
    "10-15 working days")

svc("iso-14001-certification", "b", "ISO 14001 Certification (Environmental Management)",
    "Get ISO 14001 certified to demonstrate a structured environmental management system.",
    "ISO 14001 certifies that your organisation manages its environmental impact — waste, emissions, resource use — through a structured, auditable system. We prepare documentation matched to your operations and coordinate the certification audit.",
    ["Meets environmental-compliance expectations in tenders", "Structured system for waste and resource management", "Certification via an accredited body"],
    ["Business registration proof", "Details of operations and environmental impact areas", "Existing environmental policies, if any"],
    "10-15 working days")

svc("iso-45001-certification", "b", "ISO 45001 Certification (Occupational Health & Safety)",
    "Get ISO 45001 certified to demonstrate a structured occupational health and safety management system.",
    "ISO 45001 is the current international standard for workplace health and safety management, replacing the older OHSAS 18001. We prepare your documentation and coordinate the certification audit against your actual worksite practices.",
    ["Demonstrates a structured approach to worker safety", "Reduces workplace incident and liability exposure", "Increasingly required in manufacturing and construction tenders"],
    ["Business registration proof", "Existing safety policies and incident records, if any", "List of key business activities and worksites"],
    "10-15 working days")

svc("iso-22000-certification", "b", "ISO 22000 Certification (Food Safety Management)",
    "Get ISO 22000 certified to demonstrate a structured food safety management system.",
    "ISO 22000 certifies a food safety management system across the whole supply chain, often expected by large retail and export buyers alongside FSSAI licensing. We prepare documentation and coordinate the certification audit.",
    ["Expected by large retail and export food buyers", "Structures hazard analysis across the supply chain", "Complements, not replaces, your FSSAI licence"],
    ["FSSAI licence", "Business registration proof", "Existing food safety procedures, if any"],
    "15-20 working days")

svc("iso-20000-certification", "b", "ISO 20000 Certification (IT Service Management)",
    "Get ISO 20000 certified to demonstrate a structured IT service management system.",
    "ISO 20000 certifies that your IT service delivery — incident management, service levels, change control — follows a structured, auditable process. We prepare documentation matched to your service operations.",
    ["Signals mature IT service delivery to enterprise clients", "Structures incident and change management", "Often required in IT outsourcing RFPs"],
    ["Business registration proof", "Existing IT service processes, if any", "List of services delivered"],
    "10-15 working days")

svc("iso-27001-certification", "b", "ISO 27001 Certification (Information Security Management)",
    "Get ISO 27001 certified to demonstrate a structured information security management system.",
    "ISO 27001 is the standard enterprise clients and regulators most commonly ask for when your business handles their data — certifying a structured, risk-based information security management system. We prepare documentation and coordinate the audit.",
    ["Often a prerequisite in enterprise vendor security reviews", "Structured, risk-based approach to data security", "Certification via an accredited body"],
    ["Business registration proof", "Existing data security policies, if any", "List of systems and data handled"],
    "15-20 working days")

svc("iso-13485-certification", "b", "ISO 13485 Certification (Medical Devices QMS)",
    "Get ISO 13485 certified — the quality management standard specific to medical device manufacturing.",
    "ISO 13485 certifies a quality management system tailored to medical device design, manufacturing and regulatory requirements, and is often a precondition for CE marking or export approval. We prepare documentation matched to your device class.",
    ["Often required for medical device export and CE marking", "Tailored to device-specific regulatory requirements", "Certification via an accredited body"],
    ["Business registration proof", "Device classification and manufacturing details", "Existing quality procedures, if any"],
    "15-20 working days")

svc("iso-22301-certification", "b", "ISO 22301 Certification (Business Continuity Management)",
    "Get ISO 22301 certified to demonstrate a structured business continuity management system.",
    "ISO 22301 certifies that your organisation has a tested plan to keep operating through disruption — a data centre outage, a supply chain break, a natural disaster. We prepare the documentation and coordinate the certification audit.",
    ["Demonstrates resilience to enterprise clients and insurers", "Structured plan for operational disruption", "Increasingly required in BFSI and IT vendor audits"],
    ["Business registration proof", "Existing continuity/disaster-recovery plans, if any", "List of critical business processes"],
    "15-20 working days")

svc("iso-29990-certification", "b", "ISO 29990 Certification (Training & Education Services)",
    "Get ISO 29990 certified — the quality standard for non-formal education and training providers.",
    "ISO 29990 certifies the learning service design and delivery quality of training institutes and non-formal education providers. We prepare documentation matched to your curriculum and delivery process.",
    ["Signals training quality to corporate and institutional clients", "Structures curriculum design and learner feedback", "Certification via an accredited body"],
    ["Business registration proof", "Curriculum and training delivery documentation", "Learner feedback records, if any"],
    "10-15 working days")

svc("iso-50001-certification", "b", "ISO 50001 Certification (Energy Management)",
    "Get ISO 50001 certified to demonstrate a structured energy management system.",
    "ISO 50001 certifies a systematic approach to tracking and reducing energy consumption, increasingly expected in manufacturing and infrastructure tenders. We prepare documentation matched to your energy usage profile.",
    ["Demonstrates measurable energy efficiency commitments", "Increasingly required in infrastructure and manufacturing tenders", "Structured tracking of energy consumption and targets"],
    ["Business registration proof", "Energy consumption data and existing policies, if any"],
    "10-15 working days")

svc("ce-marking", "b", "CE Marking",
    "Get CE marking to legally sell your product in the European Economic Area.",
    "CE marking is a mandatory conformity mark for a wide range of products sold in the EEA, certifying compliance with the relevant EU health, safety and environmental directives. We assess which directive applies to your product and manage the conformity assessment.",
    ["Mandatory to legally sell into the EEA", "Directive matched to your specific product category", "Avoids customs seizure or market withdrawal in the EU"],
    ["Product technical specifications", "Existing test reports, if any", "Business registration proof"],
    "15-25 working days")

svc("haccp-certification", "b", "HACCP Certification",
    "Get HACCP certified to demonstrate a structured food-safety hazard control system.",
    "HACCP certifies that your food business identifies and controls hazards at every critical point in production, a common requirement for export and institutional food buyers. We prepare documentation matched to your process flow.",
    ["Often required by export and institutional food buyers", "Structured control at every critical production point", "Complements FSSAI licensing"],
    ["FSSAI licence", "Process flow documentation", "Existing hygiene and safety procedures, if any"],
    "15-20 working days")

svc("halal-certification", "b", "Halal Certification",
    "Get Halal certified to sell food or cosmetic products into Middle Eastern and Muslim-majority markets.",
    "Halal certification verifies your product and process meet Islamic dietary and production requirements, often mandatory for export to Middle Eastern and Southeast Asian markets. We coordinate the audit with an accredited Halal certification body.",
    ["Mandatory for most Middle East and Southeast Asia food exports", "Opens access to a large addressable consumer market", "Certification via an accredited Halal body"],
    ["FSSAI licence", "List of ingredients and suppliers", "Process flow documentation"],
    "20-30 working days")

svc("gmp-certification", "b", "GMP Certification",
    "Get Good Manufacturing Practice certified for food, pharma or cosmetic production.",
    "GMP certification confirms your manufacturing process meets the hygiene, documentation and quality-control standards expected in food, pharmaceutical or cosmetic production. We prepare documentation matched to Indian GMP guidelines.",
    ["Often required alongside FSSAI or drug licence applications", "Structured hygiene and quality-control documentation", "Improves buyer and export confidence"],
    ["Business/manufacturing licence", "Process flow and facility layout", "Existing quality procedures, if any"],
    "15-20 working days")

svc("bifma-certification", "b", "BIFMA Certification",
    "Get BIFMA certified to demonstrate furniture safety, durability and performance standards.",
    "BIFMA certification tests furniture products against recognised safety, durability and performance benchmarks, commonly required by large institutional and export furniture buyers. We coordinate testing and documentation with an accredited lab.",
    ["Commonly required by institutional and export furniture buyers", "Independently verified safety and durability testing", "Improves buyer confidence in bulk procurement"],
    ["Product specifications and drawings", "Business registration proof"],
    "20-25 working days")

svc("organic-certification", "b", "Organic Certification",
    "Get organic certification (NPOP/India Organic) to legally label and export produce as organic.",
    "Organic certification under India's NPOP framework is mandatory before you can label, sell or export produce as \"organic,\" requiring a documented conversion period and audited farming practices. We manage the documentation and coordinate the certifying-agency audit.",
    ["Mandatory to legally use the \"organic\" label", "Required for organic produce export", "Premium pricing access in retail and export markets"],
    ["Land ownership or lease documents", "Farming practice records for the conversion period", "List of crops and inputs used"],
    "6-18 months (conversion period dependent)")

svc("agmark-certification", "b", "Agmark Certification",
    "Get Agmark certified to grade and certify agricultural produce quality for domestic sale.",
    "Agmark certifies that agricultural produce meets defined national quality-grading standards, expected by many wholesale buyers and retail chains for graded commodities like ghee, spices, and pulses. We manage the application and grading-lab coordination.",
    ["Recognised quality mark for graded commodities", "Expected by wholesale and retail chain buyers", "Improves shelf trust for packaged agricultural goods"],
    ["Business registration proof", "Product samples for grading", "Manufacturing/packing facility details"],
    "15-20 working days")

svc("bis-certification", "b", "BIS Certification",
    "Get BIS certified — mandatory for a wide range of products sold in the Indian market.",
    "BIS (Bureau of Indian Standards) certification is a legal requirement for a defined list of products before they can be manufactured or sold in India, from electrical appliances to packaged drinking water. We identify the applicable standard and manage the application and lab testing.",
    ["Legally mandatory for notified product categories", "Standard matched to your exact product classification", "Avoids seizure or market withdrawal by regulators"],
    ["Product technical specifications", "Manufacturing facility details", "Business registration proof"],
    "30-45 working days")

svc("security-agency-license", "b", "Security Agency License (PSARA)",
    "Get a PSARA licence to legally operate a private security agency.",
    "The Private Security Agencies Regulation Act requires a state-issued licence before you can legally operate a private security or guarding business, with specific training and background-verification obligations for your personnel. We manage the application through the controlling authority.",
    ["Legally mandatory to operate a security agency", "Structured around state-specific PSARA rules", "Required to bid for institutional security contracts"],
    ["Business registration proof", "Director/partner antecedent verification", "Proof of training tie-up for security personnel"],
    "30-60 working days")

# =========================================================================
# CATEGORY C — Manage & Grow Business
# =========================================================================

svc("accounting-bookkeeping", "c", "Accounting & Bookkeeping",
    "Monthly bookkeeping and financial statements so your filings are always backed by clean books.",
    "Accurate books make every other filing — GST, TDS, ITR — faster and less error-prone. We maintain your ledgers, bank reconciliation, and monthly financial statements on a cloud accounting platform you can access anytime.",
    ["Monthly P&L and balance sheet delivered", "Bank reconciliation done every month", "Feeds directly into GST and ITR filings"],
    ["Bank statements", "Sales & purchase invoices", "Previous financial statements, if any"],
    "Ongoing, monthly close")

svc("payroll-processing", "c", "Payroll Processing",
    "Monthly payroll processing with payslips, compliant with statutory deductions.",
    "We calculate gross-to-net pay for every employee, apply the correct PF, ESI, and TDS deductions, and issue payslips each month, so payroll runs on time without manual spreadsheet work.",
    ["Statutory deductions calculated correctly each month", "Payslips issued to employees automatically", "Frees you from manual payroll spreadsheets"],
    ["Employee master data — salary, PAN, bank details", "Attendance/leave records", "Previous month's payroll register, if switching"],
    "Ongoing, monthly cycle")

svc("stock-audit", "c", "Stock Audit",
    "Get an independent stock audit for bank loan compliance or internal inventory control.",
    "A stock audit independently verifies the quantity and valuation of inventory pledged against a bank loan, or simply tightens internal inventory control. We conduct the physical verification and prepare the report in the format your bank or management requires.",
    ["Satisfies bank stock-audit covenant requirements", "Identifies shrinkage or valuation discrepancies early", "Report formatted to the lender's requirement"],
    ["Latest stock statement and inventory records", "Purchase and sales registers", "Bank sanction letter, if loan-related"],
    "5-10 working days")

svc("tax-audit", "c", "Tax Audit",
    "Get your accounts tax-audited under Section 44AB, mandatory above the prescribed turnover threshold.",
    "A tax audit under Section 44AB is mandatory once turnover or receipts cross the prescribed threshold, and must be completed and filed before the income tax due date. We coordinate the audit and file Form 3CA/3CB-3CD.",
    ["Mandatory compliance above the turnover threshold", "Filed ahead of the income tax due date", "Reduces risk of a scrutiny notice"],
    ["Complete books of accounts", "Bank statements for the financial year", "Previous year's audit report, if any"],
    "7-10 working days")

svc("company-audit", "c", "Statutory Company Audit",
    "Get your company's annual statutory audit completed by a practising Chartered Accountant.",
    "Every registered company must have its annual accounts audited by an independent Chartered Accountant, regardless of turnover, before the financial statements can be filed with the ROC. We coordinate the audit and the auditor's report.",
    ["Mandatory for every registered company, any turnover", "Required before AOC-4 can be filed", "Independent auditor's report for your records"],
    ["Complete books of accounts", "Bank statements and confirmations", "Previous year's audited financials"],
    "10-15 working days")

svc("cost-audit", "c", "Cost Audit",
    "Get a cost audit completed where mandated by the Companies (Cost Records and Audit) Rules.",
    "Certain regulated and manufacturing sectors above prescribed turnover thresholds must maintain cost records and get them audited separately from the financial audit. We assess applicability and coordinate the cost audit and CRA-3 filing.",
    ["Confirms applicability under the Cost Audit Rules", "Filed alongside the CRA-3 form", "Reduces risk of non-compliance penalty"],
    ["Cost records maintained for the financial year", "Production and sales data", "Previous cost audit report, if any"],
    "10-15 working days")

svc("gst-return-filing", "c", "GST Return Filing",
    "Monthly and annual GST return filing to stay compliant and avoid late fees.",
    "GSTR-1 and GSTR-3B are due monthly for most registered businesses, with GSTR-9 due annually. We reconcile your sales data, prepare every return, and file them before each due date.",
    ["Avoid late fees and interest on delayed filing", "Keeps input tax credit claims accurate", "Monthly reconciliation catches mismatches early"],
    ["Sales & purchase invoices for the period", "GST login credentials", "Bank statement for tax payment"],
    "Filed monthly, before the 20th")

svc("income-tax-return-filing", "c", "Income Tax Return Filing",
    "Individual and business income tax return filing, with audit coordination where required.",
    "Whether your income is salaried, business, or includes capital gains, we prepare and file the correct ITR form, claim eligible deductions, and coordinate a tax audit where the threshold applies.",
    ["Correct ITR form selected for your income type", "Deductions claimed accurately under applicable sections", "Filing acknowledgement and refund tracking included"],
    ["Form 16 or business financial statements", "Bank statements", "Investment & deduction proofs", "PAN & Aadhaar"],
    "3-7 working days")

svc("tds-return-filing", "c", "TDS Return Filing",
    "File quarterly TDS returns for tax deducted on salaries and vendor payments.",
    "Businesses deducting TDS on salaries, rent, or vendor payments must file a quarterly return before issuing Form 16/16A. We prepare and file the correct form and generate the TDS certificates for your deductees.",
    ["Avoids late-filing fees under Section 234E", "Form 16/16A generated for deductees", "Quarterly filing keeps compliance current"],
    ["TAN of the deductor", "Challan details of TDS deposited", "PAN of all deductees"],
    "Filed quarterly, before the due date")

svc("pf-esi-return-filing", "c", "PF & ESI Return Filing",
    "Ongoing monthly PF and ESI contribution filing once your business is registered.",
    "Once registered for EPF and ESI, monthly contribution returns must be filed and deposited on time to keep both registrations in good standing. We calculate the monthly contributions and file both returns.",
    ["Keeps EPF and ESI registrations in good standing", "Avoids interest and penalty on delayed deposit", "Employee contribution records kept current"],
    ["Monthly salary and attendance data", "EPF & ESI login credentials", "Previous month's filed returns"],
    "Filed monthly, before the 15th/21st")

svc("roc-annual-compliance", "c", "ROC & Annual Compliance",
    "Annual ROC filings and ongoing corporate compliance for Private Limited Companies and LLPs.",
    "Every registered company or LLP must file its annual return and financial statements with the ROC each year, regardless of turnover, along with director KYC and other event-based filings as they arise. We track every applicable deadline against your incorporation and AGM dates and file them before they're due.",
    ["Avoids the steep per-day late filing penalty", "Keeps the company or LLP in active, compliant status", "Required even for dormant or zero-revenue entities"],
    ["Audited financial statements", "Board report and auditor's report", "List of shareholders/partners and directors", "Director's DIN & Aadhaar for KYC"],
    "Annual, within statutory deadlines from your AGM date")

svc("proprietorship-to-private-limited", "c", "Proprietorship to Private Limited Conversion",
    "Convert a sole proprietorship into a Private Limited Company as the business scales.",
    "As a proprietorship outgrows sole ownership — bringing on co-founders, raising funding, or needing limited liability — converting to a Private Limited Company preserves the business while formalising its structure. We handle the incorporation and the asset/liability transfer.",
    ["Preserves business continuity while changing legal form", "Enables funding and co-founder equity", "Limited liability from the date of conversion"],
    ["Proprietorship's PAN, GST & bank statements", "Proposed director and shareholder details", "Proof of registered office"],
    "12-15 working days")

svc("proprietorship-to-llp", "c", "Proprietorship to LLP Conversion",
    "Convert a sole proprietorship into an LLP for limited liability with lighter compliance.",
    "Converting to an LLP gives a growing proprietorship limited liability and a partnership structure, without the full compliance load of a private company. We handle the incorporation and the transfer of the existing business.",
    ["Limited liability from the date of conversion", "Lighter ongoing compliance than a private company", "Existing business continues without disruption"],
    ["Proprietorship's PAN, GST & bank statements", "Proposed designated partners' details", "Proof of registered office"],
    "10-12 working days")

svc("proprietorship-to-partnership", "c", "Proprietorship to Partnership Conversion",
    "Bring on a partner by converting a proprietorship into a registered partnership firm.",
    "When a sole proprietor brings on a partner, converting to a registered partnership formalises profit-sharing and responsibilities from day one. We draft the partnership deed and complete the conversion.",
    ["Formalises profit-sharing before disputes arise", "Registered deed is legally enforceable", "Existing business continues without disruption"],
    ["Proprietorship's PAN & GST details", "Incoming partner's KYC documents", "Agreed profit-sharing terms"],
    "5-7 working days")

svc("partnership-to-llp", "c", "Partnership to LLP Conversion",
    "Convert a registered partnership firm into an LLP for limited liability.",
    "Converting a partnership into an LLP gives all partners limited liability while keeping the underlying business and relationships intact. We handle the LLP incorporation and the formal conversion filing.",
    ["Limited liability for all partners going forward", "Existing partnership assets transfer automatically", "Retains the firm's business continuity"],
    ["Existing partnership deed", "PAN & Aadhaar of all partners", "Latest financial statements of the firm"],
    "12-15 working days")

svc("opc-to-private-limited", "c", "OPC to Private Limited Conversion",
    "Convert a One Person Company into a Private Limited Company to bring in co-founders or investors.",
    "An OPC must convert once it crosses certain turnover or capital thresholds, or voluntarily when the founder wants to bring in co-founders or investors. We handle the shareholder addition and the conversion filing.",
    ["Enables bringing in co-founders and investors", "Mandatory once turnover/capital thresholds are crossed", "Business continuity preserved through conversion"],
    ["OPC's certificate of incorporation", "Proposed additional shareholders' details", "Latest financial statements"],
    "15-20 working days")

svc("private-limited-to-opc", "c", "Private Limited to OPC Conversion",
    "Convert a Private Limited Company into a One Person Company when ownership consolidates to a single founder.",
    "When a Private Limited Company's ownership consolidates to a single shareholder, converting to an OPC reduces the compliance load to match. We handle the shareholder buyout documentation and the conversion filing.",
    ["Reduces compliance load to match single ownership", "Business continuity preserved through conversion", "Simplifies governance for a solo-owned business"],
    ["Company's certificate of incorporation", "Shareholder buyout/consent documentation", "Latest financial statements"],
    "15-20 working days")

svc("llp-to-private-limited", "c", "LLP to Private Limited Conversion",
    "Convert an LLP into a Private Limited Company to raise equity funding.",
    "LLPs cannot issue equity shares, so businesses that need to raise VC or angel funding typically convert to a Private Limited Company first. We handle the incorporation and the formal conversion of the LLP's assets and liabilities.",
    ["Enables equity fundraising, which an LLP cannot do", "Existing LLP business transfers to the new company", "Preferred structure for institutional investors"],
    ["LLP agreement and incorporation certificate", "Latest financial statements of the LLP", "Proposed director and shareholder details"],
    "15-20 working days")

svc("private-limited-to-public-limited", "c", "Private to Public Limited Conversion",
    "Convert a Private Limited Company into a Public Limited Company ahead of a public raise or listing.",
    "Converting to a Public Limited Company is a precondition for raising capital from the public or listing on an exchange, requiring a minimum of seven shareholders and three directors. We handle the special resolution and the conversion filing.",
    ["Enables raising capital from the public", "Precondition for exchange listing", "Shares become freely transferable"],
    ["Company's certificate of incorporation", "Special resolution approving conversion", "Updated MOA/AOA"],
    "20-25 working days")

svc("public-limited-to-private-limited", "c", "Public to Private Limited Conversion",
    "Convert a Public Limited Company back into a Private Limited Company to reduce compliance overhead.",
    "A Public Limited Company that no longer needs public-market access can convert back to a Private Limited Company to reduce its compliance and disclosure burden. We handle the special resolution and NCLT/ROC approval process.",
    ["Reduces ongoing compliance and disclosure burden", "Simplifies share transfer restrictions", "Business continuity preserved through conversion"],
    ["Company's certificate of incorporation", "Special resolution approving conversion", "Updated MOA/AOA"],
    "25-30 working days")

svc("dissolution-of-partnership-firm", "c", "Dissolution of Partnership Firm",
    "Formally dissolve a partnership firm and settle accounts between partners.",
    "Winding up a partnership requires a dissolution deed settling each partner's share of assets and liabilities, and notifying the Registrar of Firms. We draft the dissolution deed and complete the closure filings.",
    ["Formal settlement protects all partners from future disputes", "Registrar notified to close the firm's records", "Clears the way for partners to pursue separate ventures"],
    ["Existing partnership deed", "Latest financial statements", "Consent of all partners to dissolve"],
    "7-10 working days")

svc("change-authorised-capital", "c", "Increase in Authorised Share Capital",
    "Increase your company's authorised share capital to allow issuing more shares.",
    "Before issuing new shares to a co-founder or investor beyond your current authorised capital, you need to formally increase it via an ROC filing. We draft the resolution, amend the MOA, and file the required form.",
    ["Unlocks headroom to issue new shares", "MOA amended to reflect the new capital", "Required before most funding rounds"],
    ["Existing MOA & AOA", "Board & shareholder resolution", "Certificate of incorporation"],
    "5-7 working days")

svc("add-remove-director", "c", "Add or Remove Director",
    "File the ROC forms to add a new director or formally remove an existing one.",
    "Adding or removing a director requires board and, in some cases, shareholder approval, followed by an ROC filing within the statutory deadline. We prepare the resolutions and file the appointment or resignation forms.",
    ["Filed within the statutory deadline to avoid penalty", "Resolutions drafted in the correct format", "DIN/consent documentation handled for new directors"],
    ["Board resolution", "New director's DIN, PAN & Aadhaar, or resignation letter", "Certificate of incorporation"],
    "5-7 working days")

svc("add-remove-partner", "c", "Add or Remove Partner (LLP)",
    "File the ROC forms to add a new designated partner or formally remove an existing one in an LLP.",
    "Adding or removing a designated partner in an LLP requires an amended LLP agreement and an ROC filing within the statutory deadline. We prepare the amendment and file the required forms.",
    ["Filed within the statutory deadline to avoid penalty", "LLP agreement amended to reflect the change", "DPIN/consent documentation handled for new partners"],
    ["Supplementary LLP agreement", "New partner's DPIN, PAN & Aadhaar, or resignation letter", "LLP incorporation certificate"],
    "5-7 working days")

svc("change-business-objective", "c", "Change in Business Objective (MOA)",
    "Amend your company's Memorandum of Association to add or change its business objective.",
    "Expanding into a new line of business often requires amending the object clause of your Memorandum of Association before you can legally operate it. We draft the special resolution and file the MOA amendment.",
    ["Legally required before operating outside the current objects", "MOA amended and reflected on the MCA record", "Reduces risk of ultra vires disputes"],
    ["Existing MOA & AOA", "Special resolution approving the new objective", "Certificate of incorporation"],
    "7-10 working days")

svc("change-registered-office-address", "c", "Change of Registered Office Address",
    "File the ROC forms to shift your company's registered office, within or across states.",
    "Shifting your registered office requires an ROC filing that differs depending on whether the move is within the same city, across the state, or to a different state entirely. We identify the correct process and file the required forms.",
    ["Correct process matched to within-city, inter-city or inter-state moves", "Updated address reflected on the MCA record", "Avoids notices sent to an outdated address"],
    ["Proof of new registered office with NOC", "Board resolution approving the change", "Certificate of incorporation"],
    "7-15 working days depending on move type")

svc("change-company-name", "c", "Change of Company Name",
    "File the ROC forms to legally change your company's registered name.",
    "A rebrand isn't complete until the name change is filed with the ROC and reflected on your certificate of incorporation, PAN and bank records. We handle the name approval, special resolution, and the ROC filing.",
    ["Formal MCA-approved name change certificate", "PAN, TAN & bank updates guided post-approval", "Business continuity preserved through the change"],
    ["Board & special resolution approving the name change", "Certificate of incorporation", "Updated MOA/AOA"],
    "10-12 working days")

svc("close-private-limited-company", "c", "Close a Private Limited Company",
    "Formally close a Private Limited Company that's no longer operating, through the ROC's fast-track exit scheme.",
    "A company that isn't operating still accrues compliance obligations and penalties until it's formally struck off. We file under the fast-track exit scheme, after clearing pending returns and settling liabilities.",
    ["Stops future ROC penalties from accruing", "Fast-track route for companies with no liabilities", "Handles pending filings needed before closure"],
    ["Board & shareholder resolution for closure", "Statement of accounts, not older than 30 days", "Indemnity bond & affidavit from directors"],
    "3-4 months (Registry-dependent)")

svc("close-llp", "c", "Close an LLP",
    "Formally close an LLP that's no longer operating, through the ROC's striking-off process.",
    "An inactive LLP continues to attract annual filing obligations and penalties until it's formally struck off the register. We file the closure application after clearing pending returns and settling liabilities.",
    ["Stops future annual filing penalties from accruing", "Clears pending compliance before closure", "Formal removal from the LLP register"],
    ["Partners' resolution for closure", "Statement of accounts, not older than 30 days", "Consent of all partners"],
    "3-4 months (Registry-dependent)")

svc("business-loan-assistance", "c", "Business Loan Assistance",
    "Get help structuring and applying for a business loan from banks and NBFC lenders.",
    "Loan applications get rejected as often for poor documentation as for weak fundamentals. We help structure your financials, prepare the application, and coordinate with lenders to improve your approval odds and terms.",
    ["Financials structured the way underwriters actually read them", "Coordination across multiple bank/NBFC lenders", "Improves approval odds and negotiated terms"],
    ["Latest 2-3 years' financial statements", "Bank statements for the last 6-12 months", "Business plan or purpose of the loan"],
    "10-20 working days")

svc("project-finance", "c", "Project Finance Advisory",
    "Structure and arrange project finance for a large capital expenditure or infrastructure venture.",
    "Project finance for a large capex venture needs a bankable financial model, risk allocation, and coordination across multiple lenders — very different from a standard working-capital loan. We structure the financing and manage lender coordination.",
    ["Financial model structured to satisfy lender due diligence", "Risk allocation negotiated across project stakeholders", "Coordination across multiple lenders where needed"],
    ["Detailed project report and cost estimates", "Promoter's financial background", "Land/asset and regulatory approval status"],
    "30-60 working days")

svc("wealth-management", "c", "Wealth Creation & Management",
    "Get structured guidance on building and managing wealth alongside your business.",
    "Business owners often reinvest everything into the business and neglect personal wealth planning. We help structure a personal investment approach that runs alongside your business, matched to your risk profile and goals.",
    ["Personal wealth plan structured alongside business cash flow", "Matched to your specific risk profile and goals", "Reviewed periodically as circumstances change"],
    ["Current investment portfolio details, if any", "Income and cash flow summary", "Financial goals and time horizon"],
    "Initial plan in 7-10 working days")

svc("investment-planning", "c", "Investment Planning",
    "Get a structured investment plan matched to your goals, risk appetite and time horizon.",
    "A scattered mix of investments made opportunistically rarely serves a clear goal. We assess your current holdings and build a structured plan matched to specific goals and time horizons.",
    ["Plan built around specific, named goals", "Matched to your actual risk appetite", "Reviewed and rebalanced periodically"],
    ["Current investment portfolio details", "Income and expense summary", "Financial goals and time horizon"],
    "Initial plan in 7-10 working days")

svc("corporate-advisory", "c", "Corporate Advisory",
    "Get strategic and structuring advisory for mergers, acquisitions, restructuring or expansion.",
    "Major corporate decisions — a merger, an acquisition, a group restructuring, entering a new market — need advisory grounded in both regulation and commercial reality. We provide structuring advice and coordinate the legal and financial workstreams involved.",
    ["Advisory grounded in both regulation and commercial fit", "Coordinates legal, tax and financial workstreams", "Structured for the specific transaction or expansion"],
    ["Details of the proposed transaction or expansion", "Latest financial statements of entities involved", "Existing group structure, if applicable"],
    "Scoped per engagement")

svc("project-report-preparation", "c", "Project Report Preparation",
    "Get a bank-ready project report prepared for loan or subsidy applications.",
    "Banks and subsidy schemes require a project report in a specific format covering cost estimates, means of finance, and projected financials — a generic business plan usually isn't accepted. We prepare it in the format your lender or scheme requires.",
    ["Formatted to the specific lender or scheme's requirement", "Projected financials built on realistic assumptions", "Improves loan and subsidy approval odds"],
    ["Business model and cost estimates", "Promoter's background and experience", "Details of the lender or scheme applied to"],
    "5-10 working days")

# =========================================================================
# CATEGORY D — Legal Documents
# =========================================================================

svc("rent-agreement-drafting", "d", "Rent Agreement Drafting",
    "Draft a rent agreement for residential or commercial premises.",
    "A rent agreement protects both landlord and tenant on rent, deposit, lock-in and exit terms — vague clauses here cause most disputes. We draft the agreement to your commercial terms and arrange registration where required.",
    ["Rent, deposit & lock-in terms clearly defined", "Reduces ambiguity that leads to disputes", "Drafted for registration where legally required"],
    ["ID proof of landlord & tenant", "Property ownership/address proof", "Agreed rent, deposit & tenure"],
    "1-2 working days")

svc("sale-deed-drafting", "d", "Sale Deed Drafting",
    "Draft a sale deed for the transfer of immovable property.",
    "A sale deed is the primary legal document transferring ownership of immovable property and must be drafted precisely before registration. We draft it against the agreed sale terms and property title documents.",
    ["Ownership transfer documented precisely", "Drafted to match the property's title chain", "Prepared for registration at the Sub-Registrar"],
    ["Property title documents", "ID & PAN of buyer and seller", "Agreed sale consideration and terms"],
    "2-3 working days")

svc("lease-deed-drafting", "d", "Lease Deed Drafting",
    "Draft a long-term lease deed for commercial or industrial premises.",
    "A lease deed for a longer tenure than a standard rent agreement needs more detailed terms on renewal, maintenance and exit. We draft it to your specific commercial terms and arrange registration.",
    ["Detailed renewal, maintenance & exit terms", "Suited to longer commercial/industrial tenures", "Prepared for registration where required"],
    ["ID proof of lessor & lessee", "Property ownership/address proof", "Agreed lease terms and tenure"],
    "2-3 working days")

svc("gift-deed-drafting", "d", "Gift Deed Drafting",
    "Draft a gift deed to transfer property or assets without consideration.",
    "A gift deed formally transfers ownership of property or assets without payment, and needs to be drafted and registered correctly to be legally valid and tax-efficient. We draft it against the donor's and donee's specific relationship and asset details.",
    ["Legally valid transfer without consideration", "Structured for applicable tax exemptions", "Prepared for registration at the Sub-Registrar"],
    ["Property/asset ownership documents", "ID & PAN of donor and donee", "Relationship proof, for exemption purposes"],
    "2-3 working days")

svc("will-drafting", "d", "Will Drafting & Probate Support",
    "Draft a legally sound will and get support through the probate process.",
    "A clearly drafted will prevents disputes among heirs and ensures assets pass the way you intend. We draft the will to reflect your specific wishes and assist with probate when the time comes.",
    ["Prevents ambiguity and disputes among heirs", "Drafted to reflect your specific wishes precisely", "Probate support included when needed"],
    ["List of assets and intended beneficiaries", "ID proof of the testator", "Details of appointed executor"],
    "3-5 working days")

svc("employment-contract-drafting", "d", "Employment Contract Drafting",
    "Draft employment agreements tailored to the role and your company's structure.",
    "A clear employment agreement protects both the business and the employee by defining role, compensation, confidentiality and exit terms upfront. We draft it to fit your actual team structure.",
    ["Tailored to the specific role and compensation structure", "Confidentiality and IP-assignment clauses included", "Reduces ambiguity in disputes or exits"],
    ["Role & compensation details", "Company structure & reporting lines", "Existing template, if any, to review"],
    "2-3 working days")

svc("consultancy-agreement-drafting", "d", "Consultancy Agreement Drafting",
    "Draft a consultancy agreement defining scope, fees, and deliverables for an independent consultant.",
    "A consultancy agreement needs to clearly separate the relationship from employment while still protecting confidentiality and IP. We draft it around the specific engagement scope and payment structure.",
    ["Scope and deliverables defined to avoid ambiguity", "Correctly distinguishes consultancy from employment", "Confidentiality and IP clauses included"],
    ["Scope of the consultancy engagement", "Agreed fee structure and duration"],
    "1-2 working days")

svc("freelancer-agreement-drafting", "d", "Freelancer Agreement Drafting",
    "Draft a freelancer agreement covering scope, payment milestones, and IP ownership.",
    "Freelance engagements without a written agreement are a common source of scope-creep and IP-ownership disputes. We draft an agreement covering deliverables, payment milestones, and who owns the final work.",
    ["Payment milestones tied to specific deliverables", "IP ownership clarified from the outset", "Reduces scope-creep disputes"],
    ["Scope of work and deliverables", "Agreed payment terms and milestones"],
    "1-2 working days")

svc("vendor-service-agreement", "d", "Vendor & Service Agreement Drafting",
    "Draft vendor, service, or supply agreements defining scope, payment, and liability.",
    "A clear service agreement prevents scope creep and payment disputes by defining deliverables, timelines, payment milestones, and liability upfront. We draft it around your actual engagement terms.",
    ["Scope & deliverables defined to avoid creep", "Payment milestones tied to deliverables", "Liability & termination clauses included"],
    ["Scope of work / deliverables", "Payment terms agreed with the vendor", "Duration of the engagement"],
    "2-3 working days")

svc("franchise-agreement-drafting", "d", "Franchise Agreement Drafting",
    "Draft a franchise agreement covering brand usage, territory, fees, and quality control.",
    "A franchise agreement needs to protect the brand's standards and IP while giving the franchisee a workable commercial structure — territory, fees, renewal, and exit terms all matter. We draft it around your specific franchise model.",
    ["Brand standards and IP usage clearly protected", "Territory, fees and renewal terms defined", "Exit and termination conditions built in"],
    ["Brand/trademark registration details", "Proposed territory and fee structure", "Quality control standards to be enforced"],
    "3-5 working days")

svc("joint-venture-agreement-drafting", "d", "Joint Venture Agreement Drafting",
    "Draft a joint venture agreement covering contribution, governance, and exit between partners.",
    "A joint venture agreement needs to be precise about each partner's contribution, decision-making rights, profit-sharing, and exit mechanism before capital or IP is committed. We draft it around the specific project and partner structure.",
    ["Contribution and governance rights defined upfront", "Profit-sharing and exit mechanism built in", "Reduces disputes as the venture progresses"],
    ["Proposed scope and contribution of each partner", "Governance and decision-making structure agreed"],
    "3-5 working days")

svc("memorandum-of-understanding", "d", "Memorandum of Understanding (MOU) Drafting",
    "Draft an MOU to record preliminary terms between parties before a formal agreement.",
    "An MOU records the intent and preliminary terms between parties while a formal agreement is negotiated, and needs careful drafting to control whether or not it's legally binding. We draft it to match your intended level of commitment.",
    ["Records intent without over-committing prematurely", "Drafted to control binding vs non-binding terms", "Provides a clear reference for the formal agreement"],
    ["Preliminary terms discussed between parties", "Details of all parties involved"],
    "1-2 working days")

svc("partnership-deed-drafting", "d", "Partnership Deed Drafting",
    "Draft or update a partnership deed covering profit-sharing, roles, and exit terms.",
    "A partnership deed is the foundational document governing profit-sharing, capital contribution, roles, and what happens if a partner exits or the firm dissolves. We draft or revise it to reflect the partners' actual agreement.",
    ["Profit-sharing and capital contribution documented clearly", "Exit and dissolution terms defined in advance", "Legally enforceable if disputes arise"],
    ["PAN & Aadhaar of all partners", "Agreed profit-sharing ratio and capital contribution"],
    "2-3 working days")

svc("trust-deed-drafting", "d", "Trust Deed Drafting",
    "Draft a trust deed defining the trust's objectives, trustees, and governance.",
    "A trust deed needs to precisely define the charitable objective, trustee powers, and succession to avoid governance disputes later, and to qualify cleanly for 12A/80G registration. We draft it to reflect the settlor's intent.",
    ["Charitable objective and trustee powers defined clearly", "Structured to qualify for 12A/80G registration", "Trustee succession addressed in advance"],
    ["PAN & Aadhaar of settlor and trustees", "Intended charitable objectives"],
    "2-3 working days")

svc("strategic-alliance-agreement", "d", "Strategic Alliance Agreement Drafting",
    "Draft a strategic alliance agreement for businesses collaborating without forming a new entity.",
    "A strategic alliance lets two businesses collaborate — co-marketing, shared distribution, technology access — without the cost of forming a joint venture entity. We draft the agreement around the specific collaboration scope.",
    ["Collaboration scope defined without a new entity", "IP and confidentiality boundaries set clearly", "Exit terms defined if the alliance ends"],
    ["Scope of the proposed collaboration", "Details of both parties' contributions"],
    "2-3 working days")

svc("board-resolution-drafting", "d", "Board Resolution Drafting",
    "Draft board resolutions for decisions requiring formal company approval.",
    "Opening a bank account, appointing an auditor, or approving a related-party transaction all require a documented board resolution. We draft it in the format banks and the ROC expect.",
    ["Drafted in the format banks and the ROC expect", "Covers routine and special resolutions", "Filed with the MCA where statutorily required"],
    ["Nature of the decision to be approved", "Current list of directors"],
    "1 working day")

svc("shareholder-resolution-drafting", "d", "Shareholder Resolution Drafting",
    "Draft shareholder resolutions for decisions requiring approval beyond the board.",
    "Certain decisions — changing the MOA, approving a related-party transaction above a threshold, altering share capital — require shareholder approval, not just the board. We draft the ordinary or special resolution as required.",
    ["Correct resolution type — ordinary or special — applied", "Drafted in the format the ROC expects", "Filed with the MCA where statutorily required"],
    ["Nature of the decision to be approved", "Current list of shareholders"],
    "1 working day")

svc("minutes-of-meeting-drafting", "d", "Minutes of Meeting Drafting",
    "Draft accurate minutes for board and general meetings to maintain statutory records.",
    "Every board and general meeting must have minutes recorded in the prescribed format and maintained in the company's statutory registers. We draft the minutes from your meeting notes in the correct format.",
    ["Maintained in the Companies Act's prescribed format", "Ready for ROC inspection or investor due diligence", "Drafted promptly after each meeting"],
    ["Meeting notes or discussion points", "List of attendees and agenda items"],
    "1 working day")

svc("notice-of-agm-egm", "d", "Notice of AGM/EGM Drafting",
    "Draft the statutory notice for an Annual or Extraordinary General Meeting.",
    "A general meeting notice must be circulated within the statutory timeline and format, listing the agenda and any special resolutions to be proposed. We draft and help circulate the notice correctly.",
    ["Circulated within the statutory timeline", "Agenda and special resolutions listed correctly", "Reduces risk of a meeting being challenged on procedure"],
    ["Agenda items and resolutions to be proposed", "Current list of shareholders/members"],
    "1-2 working days")

svc("shareholders-agreement-drafting", "d", "Shareholders' Agreement Drafting",
    "Draft a shareholders' agreement covering equity, vesting, and exit terms.",
    "A shareholders' agreement is the document most startups skip and later regret — it governs what happens on a co-founder exit, a deadlock, or a down round. We draft equity split, vesting, and exit clauses before they become urgent.",
    ["Vesting & equity split documented before disputes arise", "Deadlock & exit mechanisms defined in advance", "Expected by investors during due diligence"],
    ["Cap table / proposed equity split", "Roles & responsibilities of each shareholder", "Certificate of incorporation"],
    "3-5 working days")

svc("share-purchase-agreement", "d", "Share Purchase Agreement Drafting",
    "Draft a share purchase agreement for the sale or transfer of company shares.",
    "A share purchase agreement needs precise terms on price, representations, warranties, and conditions before shares change hands — the details buried in the warranties often matter more than the headline price. We draft or review it for either side of the transaction.",
    ["Price, warranties and conditions defined precisely", "Drafted to protect either buyer or seller", "Reduces post-completion dispute risk"],
    ["Cap table and shareholding details", "Agreed price and transaction terms", "Latest financial statements of the company"],
    "3-5 working days")

svc("appointment-resignation-letter", "d", "Appointment & Resignation Letter Drafting",
    "Draft formal appointment or resignation letters for directors, partners, or key employees.",
    "A formal appointment or resignation letter creates a clean paper trail for ROC filings and internal records, avoiding ambiguity about effective dates and terms. We draft it to match the specific role and circumstances.",
    ["Clean paper trail for ROC and internal records", "Effective date and terms stated unambiguously", "Matched to the specific role and circumstances"],
    ["Details of the appointment or resignation", "Role and effective date"],
    "1 working day")

svc("legal-notice-drafting-reply", "d", "Legal Notice Drafting & Reply",
    "Draft or respond to a legal notice for payment defaults, contract breaches, or disputes.",
    "A well-drafted legal notice is often enough to resolve a payment default or breach without going to court, and a poorly drafted reply to one you've received can weaken your position. We draft or respond within the applicable deadline.",
    ["Drafted with the specific legal grounds cited", "Often resolves disputes without litigation", "Replies filed within the notice's deadline"],
    ["Details of the dispute or default", "Relevant agreement or correspondence", "Notice received, if replying"],
    "3-4 working days")

svc("digital-signature-certificate", "d", "Digital Signature Certificate (DSC)",
    "Get a Class 2 or Class 3 Digital Signature Certificate needed to sign incorporation and compliance filings online.",
    "Every director or authorised signatory needs a Digital Signature Certificate to sign forms filed with the MCA, GST, and Income Tax portals. We handle the application, video verification, and issuance of the correct class of DSC.",
    ["Required for MCA, GST and income tax e-filings", "Valid for 2 years once issued", "Video KYC handled remotely"],
    ["PAN card", "Aadhaar card", "Passport-size photograph", "Active mobile number & email for verification"],
    "1-2 working days")

CAT_BY_ID = {c["id"]: c for c in CATEGORIES}
for s in SERVICES:
    s["cat_name"] = CAT_BY_ID[s["cat"]]["name"]
    s["cat_letter"] = CAT_BY_ID[s["cat"]]["letter"]

print(f"{len(CATEGORIES)} categories, {len(SERVICES)} services loaded.")

CHIP_LABELS = {'a':'Start a Business','b':'Registrations & Certifications','c':'Manage & Grow','d':'Legal Documents'}

SEAL_SVG = '<svg class="seal" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.6"/><circle cx="20" cy="20" r="13.5" stroke="currentColor" stroke-width="1"/><text x="20" y="24.5" text-anchor="middle" font-family="Source Serif 4, serif" font-size="13" font-weight="600" fill="currentColor">LR</text></svg>'
MAIL_ICON = '<svg class="seal" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M3 7l9 6 9-6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PHONE_ICON = '<svg class="seal" viewBox="0 0 24 24" fill="none"><path d="M6 3h3l2 5-2.5 1.5a11 11 0 005 5L15 12l5 2v3a2 2 0 01-2 2C9.5 19 5 14.5 5 5a2 2 0 011-2z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>'
PIN_ICON = '<svg class="seal" viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.5 7-12a7 7 0 10-14 0c0 5.5 7 12 7 12z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="9" r="2.4" stroke="currentColor" stroke-width="1.4"/></svg>'
CHECK_ICON = '''<svg class="seal verify-seal" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs><path id="verifySealPath" d="M 50,50 m -37,0 a 37,37 0 1,1 74,0 a 37,37 0 1,1 -74,0"/></defs>
  <circle cx="50" cy="50" r="46" stroke="currentColor" stroke-width="1.3"/>
  <circle cx="50" cy="50" r="37" stroke="currentColor" stroke-width="0.8"/>
  <text font-family="IBM Plex Mono, monospace" font-size="6.4" letter-spacing="2.4" fill="currentColor">
    <textPath href="#verifySealPath" startOffset="2%">LEGALREET &#8226; VERIFIED &#8226; LEGALREET &#8226; VERIFIED &#8226;</textPath>
  </text>
  <path d="M32 51l11 11L70 40" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
FAVICON = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Ctext y=%22.9em%22 font-size=%2290%22%3E%E2%9A%96%EF%B8%8F%3C/text%3E%3C/svg%3E">'

SITE_URL = "https://www.legalreet.com"
WHATSAPP_NUMBER = "919368375024"

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "LegalReet",
    "url": SITE_URL + "/",
    "email": "hello@legalreet.com",
    "telephone": "+91-93683-75024",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "E-14, First Floor, Indrapuram, near Shankar Greens, Tajganj Phase II",
        "addressLocality": "Agra",
        "addressRegion": "Uttar Pradesh",
        "postalCode": "282001",
        "addressCountry": "IN",
    },
}

ARROW_SVG = '<svg viewBox="0 0 16 16" fill="none"><path d="M6 3l6 5-6 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH_ICON_SVG = '<svg viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.8"/><path d="M21 21l-4.3-4.3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'

WHATSAPP_ICON_SVG = '<svg viewBox="0 0 32 32" fill="currentColor" width="28" height="28" aria-hidden="true"><path d="M16.004 3C9.377 3 4 8.373 4 15c0 2.386.633 4.622 1.822 6.617L4 29l7.6-1.994A11.94 11.94 0 0016.004 27C22.63 27 28 21.627 28 15S22.63 3 16.004 3zm0 21.6c-1.94 0-3.79-.517-5.39-1.497l-.386-.23-4.51 1.183 1.203-4.395-.252-.405A9.55 9.55 0 016.4 15c0-5.294 4.31-9.6 9.604-9.6 5.29 0 9.596 4.306 9.596 9.6 0 5.298-4.306 9.6-9.596 9.6zm5.264-7.19c-.288-.144-1.703-.84-1.967-.936-.264-.096-.456-.144-.648.144-.192.288-.744.936-.912 1.128-.168.192-.336.216-.624.072-.288-.144-1.215-.448-2.314-1.428-.856-.762-1.434-1.704-1.602-1.992-.168-.288-.018-.444.126-.588.13-.129.288-.336.432-.504.144-.168.192-.288.288-.48.096-.192.048-.36-.024-.504-.072-.144-.648-1.564-.888-2.14-.234-.564-.472-.488-.648-.497l-.552-.01c-.192 0-.504.072-.768.36-.264.288-1.008.984-1.008 2.4s1.032 2.784 1.176 2.976c.144.192 2.03 3.1 4.92 4.347.687.297 1.223.474 1.641.607.689.219 1.316.188 1.812.114.553-.083 1.703-.696 1.943-1.368.24-.672.24-1.248.168-1.368-.072-.12-.264-.192-.552-.336z"/></svg>'

def whatsapp_button(message="Hi, I would like to know more about LegalReet's services."):
    msg = urllib.parse.quote(message)
    url = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg}"
    return f'''<a class="whatsapp-fab" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">{WHATSAPP_ICON_SVG}</a>'''

def cookie_banner():
    return '''<div class="cookie-banner" id="cookieBanner" role="dialog" aria-label="Cookie notice">
  <div class="cookie-banner-inner">
    <p>We use essential cookies to run this site, and, only with your consent, cookies to understand how visitors use it. No tracking cookies are set unless you accept.</p>
    <div class="cookie-actions">
      <button class="btn btn-ghost" id="cookieDecline" type="button">Decline</button>
      <button class="btn btn-primary" id="cookieAccept" type="button">Accept</button>
    </div>
  </div>
</div>'''

def service_schema(svc, cat):
    url = f"{SITE_URL}/services/{svc['slug']}.html"
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": svc['name'],
        "name": svc['name'],
        "description": svc['short'],
        "provider": {"@type": "Organization", "name": "LegalReet", "url": SITE_URL + "/"},
        "areaServed": {"@type": "Country", "name": "India"},
        "category": cat['name'],
        "url": url,
    }

def faq_schema(faqs_plain):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs_plain
        ],
    }

def rel_href(depth, root_path, folder=None):
    if depth == 0:
        return root_path
    if folder and root_path.startswith(folder + '/'):
        return root_path[len(folder) + 1:]
    return '../' + root_path

PROCESS_STEPS = [
    ("Consultation", "A free call with a filing expert to confirm scope, eligibility and the documents you'll need."),
    ("Documentation", "We send a checklist and verify every document before anything is submitted — no rejected filings from typos."),
    ("Filing", "Your application is drafted and lodged with the relevant authority under your assigned expert's name."),
    ("Tracking", "Live status updates as the filing moves through the registry — visible to you, not just to us."),
    ("Delivery & compliance", "Certificates or documents delivered digitally, with any recurring deadlines scheduled automatically."),
]

def E(s):
    return s.replace('&', '&amp;')

def asset_prefix(depth):
    return "" if depth == 0 else "../"

def nav_targets(depth, folder=None):
    p = asset_prefix(depth)
    def to(target_folder):
        if depth == 0:
            return f'{target_folder}/index.html'
        if folder == target_folder:
            return 'index.html'
        return f'../{target_folder}/index.html'
    return {
        'home': p + 'index.html',
        'services': to('services'),
        'blog': to('blog'),
        'pricing': p + 'pricing.html',
        'about': p + 'about.html',
        'contact': p + 'contact.html',
    }

def header_html(active, depth, folder=None):
    t = nav_targets(depth, folder)
    def navlink(key, label):
        cls = ' class="active"' if key == active else ''
        return f'<a href="{t[key]}"{cls}>{label}</a>'
    return f'''<header>
  <nav class="nav container">
    <a href="{t['home']}" class="brand">{SEAL_SVG}LegalReet</a>
    <button class="navtoggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">
      <svg width="18" height="14" viewBox="0 0 18 14" fill="none"><path d="M0 1H18M0 7H18M0 13H18" stroke="currentColor" stroke-width="1.6"/></svg>
    </button>
    <div class="navlinks" id="navLinks">
      {navlink('services','Services')}
      {navlink('blog','Blog')}
      {navlink('pricing','Pricing')}
      {navlink('about','About')}
      {navlink('contact','Contact')}
    </div>
    <div class="navcta">
      <a href="{t['contact']}" class="btn btn-ghost">Talk to an expert</a>
      <a href="{t['contact']}" class="btn btn-primary">Get started</a>
    </div>
  </nav>
</header>'''

def footer_html(depth, folder=None):
    t = nav_targets(depth, folder)
    return f'''<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="{t['home']}" class="brand">{SEAL_SVG}LegalReet</a>
        <p>Registration, tax, trademark, and compliance filings for Indian businesses — fixed fees, one expert per case.</p>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul>
          <li><a href="{t['services']}">All {len(SERVICES)} services</a></li>
          <li><a href="{t['pricing']}">Pricing</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <ul>
          <li><a href="{t['about']}">About</a></li>
          <li><a href="{t['blog']}">Blog</a></li>
          <li><a href="{t['contact']}">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>
          <li>hello@legalreet.com</li>
          <li>+91 93683 75024</li>
          <li>Agra, Uttar Pradesh</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 LegalReet. All filings subject to government processing times.</span>
      <span>legalreet.com</span>
    </div>
  </div>
</footer>'''

def page(title, description, active, depth, body, schemas=None, folder=None):
    p = asset_prefix(depth)
    all_schemas = [ORG_SCHEMA] + (schemas or [])
    schema_tags = '\n'.join(
        f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in all_schemas
    )
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
{FAVICON}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700;9..144,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
{schema_tags}
</head>
<body>
{header_html(active, depth, folder)}
<main>
{body}
</main>
{footer_html(depth, folder)}
{whatsapp_button()}
{cookie_banner()}
<script>
if (/(invite_token|recovery_token|confirmation_token|email_change_token)=/.test(window.location.hash)) {{
  var s = document.createElement('script');
  s.src = 'https://identity.netlify.com/v1/netlify-identity-widget.js';
  s.onload = function(){{ if (window.netlifyIdentity) window.netlifyIdentity.init(); }};
  document.head.appendChild(s);
}}
</script>
<script src="{p}assets/script.js"></script>
</body>
</html>'''

def breadcrumb(depth, trail, folder=None):
    # trail: list of (label, root_relative_path) e.g. ('Home','index.html'), ('Services','services/index.html')
    parts = []
    schema_items = []
    n = len(trail)
    for i, (label, root_path) in enumerate(trail):
        is_last = (i == n - 1)
        if is_last:
            parts.append(f'<span class="current">{label}</span>')
        else:
            parts.append(f'<a href="{rel_href(depth, root_path, folder)}">{label}</a>')
        if i < n - 1:
            parts.append('<span class="sep">/</span>')
        schema_items.append({
            "@type": "ListItem", "position": i + 1, "name": label,
            "item": f"{SITE_URL}/{root_path}",
        })
    html = f'<div class="container"><nav class="breadcrumb">{"".join(parts)}</nav></div>'
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": schema_items}
    return html, schema

def cta_band(depth, heading="Ready to file it the right way?",
             sub="Book a free consultation &mdash; a filing expert will map out your registration or compliance plan within one business day."):
    return f'''<section>
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>{heading}</h2><p>{sub}</p></div>
      <div style="display:flex; gap:14px; flex-wrap:wrap;">
        <a href="mailto:hello@legalreet.com" class="btn btn-primary">Email hello@legalreet.com</a>
        <a href="tel:+919368375024" class="btn btn-ghost">Call +91 93683 75024</a>
      </div>
    </div>
  </div>
</section>'''

def process_section(depth, title="Five steps, from consultation to certificate.", eyebrow="How it works", bg=True):
    items = ''.join(f'''<div class="process-item reveal">
      <div class="process-num">0{i+1}</div>
      <div class="process-body"><h4>{name}</h4><p>{desc}</p></div>
    </div>''' for i, (name, desc) in enumerate(PROCESS_STEPS))
    cls = ' class="process"' if bg else ''
    return f'''<section{cls}>
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{eyebrow}</p>
      <h2>{title}</h2>
    </div>
    <div class="process-list">{items}</div>
  </div>
</section>'''

def stats_block():
    return '''<div class="stats">
  <div class="container stats-grid">
    <div class="stat"><b>12,400+</b><span>Businesses registered</span></div>
    <div class="stat"><b>97%</b><span>Filed without rejection</span></div>
    <div class="stat"><b>4.9 / 5</b><span>From 431 Google reviews</span></div>
  </div>
</div>'''

def pricing_cards(contact_href):
    return f'''<div class="pricing-grid">
    <div class="price-card reveal">
      <div class="price-step">01</div>
      <h3>Free consultation</h3>
      <p class="desc">Tell us what you need &mdash; a filing expert scopes the exact registrations, licences or documents that apply to your business.</p>
      <ul>
        <li>No charge, no obligation</li>
        <li>Response within one business day</li>
        <li>Available by call, WhatsApp or email</li>
      </ul>
      <a href="{contact_href}" class="btn btn-ghost">Book a consultation</a>
    </div>
    <div class="price-card featured reveal">
      <span class="price-tag">How we quote</span>
      <div class="price-step">02</div>
      <h3>Transparent, fixed quote</h3>
      <p class="desc">You get a single fixed fee for the service, quoted upfront &mdash; government fees, where applicable, are always shown separately at cost.</p>
      <ul>
        <li>No hourly billing, no hidden add-ons</li>
        <li>Government charges billed at actual cost</li>
        <li>Quote confirmed in writing before work begins</li>
      </ul>
      <a href="{contact_href}" class="btn btn-primary">Request a quote</a>
    </div>
    <div class="price-card reveal">
      <div class="price-step">03</div>
      <h3>One expert, start to finish</h3>
      <p class="desc">The same filing expert who quoted you owns the case through to delivery &mdash; you always know who to ask for a status update.</p>
      <ul>
        <li>Single point of contact throughout</li>
        <li>Status visible on request, not chased</li>
        <li>Ongoing filings scheduled automatically after delivery</li>
      </ul>
      <a href="{contact_href}" class="btn btn-ghost">Talk to an expert</a>
    </div>
  </div>'''

def testimonials_block():
    return '''<section style="background:var(--paper-card); border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Client record &middot; 4.9/5 on Google</p>
      <h2>What clients say once the certificate arrives.</h2>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial-card reveal">
        <div class="testimonial-mark">&quot;</div>
        <blockquote>The team handled the entire registration and certification process professionally and smoothly. From documentation to final approval, they provided proper guidance and regular updates.</blockquote>
        <div class="testimonial-who"><div class="avatar">DG</div><div><b>Dhruv Gupta</b><span>Verified Google review</span></div></div>
      </div>
      <div class="testimonial-card reveal">
        <div class="testimonial-mark">&quot;</div>
        <blockquote>One of the most reliable firms for GST registration and tax consultancy. Their team is highly professional, explains everything clearly, and ensures a smooth process.</blockquote>
        <div class="testimonial-who"><div class="avatar">AJ</div><div><b>Anand Jha</b><span>Verified Google review</span></div></div>
      </div>
      <div class="testimonial-card reveal">
        <div class="testimonial-mark">&quot;</div>
        <blockquote>Excellent service! Their trademark team helped me register my trademark smoothly. They are very responsive and professional. Great experience overall.</blockquote>
        <div class="testimonial-who"><div class="avatar">PJ</div><div><b>Pragati Jayant</b><span>Verified Google review</span></div></div>
      </div>
    </div>
  </div>
</section>'''

def service_card_link(item, href):
    return f'''<a class="service-card-link reveal" href="{href}">
      <h3>{E(item['name'])}</h3>
      <p>{E(item['short'])}</p>
      <div class="price-row"><span>{E(item['timeline'])}</span><span>View details &rarr;</span></div>
    </a>'''

# ---------------------------------------------------------------- HOME
def build_home():
    depth = 0
    t = nav_targets(depth)
    hero = f'''<section class="hero-dark">
  <div class="container hero-solo">
    <p class="eyebrow eyebrow-invert reveal">Formerly Indian Salahkar &middot; Agra, Uttar Pradesh</p>
    <h1 class="reveal">Business compliance,<br>filed <em>the right way.</em></h1>
    <p class="hero-sub reveal">LegalReet handles {len(SERVICES)}+ registrations, licences, certifications and legal documents for Indian businesses, across four practice areas &mdash; one filing expert assigned to your case, start to finish.</p>
    <div class="hero-actions reveal">
      <a href="{t['contact']}" class="btn btn-primary">Book a free consultation</a>
      <a href="{t['services']}" class="btn btn-ghost-invert">Browse all services</a>
    </div>
    <div class="hero-trust reveal">
      <div class="avatar-cluster">
        <div class="avatar-sm">DG</div>
        <div class="avatar-sm">AJ</div>
        <div class="avatar-sm">PJ</div>
      </div>
      <div class="hero-rating"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <b>4.9/5</b>&nbsp;from 431 Google reviews</div>
    </div>
  </div>
</section>'''

    about_teaser = f'''<section>
  <div class="container about-grid">
    <div class="reveal">
      <p class="eyebrow">About LegalReet</p>
      <h2 style="margin-top:14px;">Reet means &quot;the right way.&quot; It's also the only way we file.</h2>
    </div>
    <div class="copy reveal">
      <p>LegalReet was built for founders who don't have time to learn the difference between a DIN and a DSC &mdash; only to find out later they needed both. We pair every client with a single filing expert who owns the case end to end.</p>
      <p class="callout">&quot;We don't just submit forms. We track the jurisdiction, the deadline, and the follow-up &mdash; so nothing sits in a queue you can't see.&quot;</p>
      <p><a href="{t['about']}" class="btn btn-ghost">More about how we work &rarr;</a></p>
    </div>
  </div>
</section>'''

    cat_cards = ''.join(f'''<a class="cat-showcase-card reveal" href="{t['services']}#cat-{c['id']}">
      <svg class="cat-showcase-icon" viewBox="0 0 34 34" fill="none">{c['icon']}</svg>
      <h3>{E(c['name'])}</h3>
      <p>{E(c['tagline'])}</p>
      <div class="price-row"><span>Practice {c['letter']}</span><span>{len([s for s in SERVICES if s['cat']==c['id']])} services &rarr;</span></div>
    </a>''' for c in CATEGORIES)

    services_preview = f'''<section style="background:var(--paper-card); border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">What we file</p>
      <h2>Four practice areas, {len(SERVICES)}+ services.</h2>
      <p>From first incorporation to the annual filing most businesses forget until the notice arrives. Every service has its own page with process, documents and a free quote.</p>
    </div>
    <div class="cat-showcase-grid">{cat_cards}</div>
    <div style="margin-top:28px;"><a href="{t['services']}" class="btn btn-primary">View the full service directory</a></div>
  </div>
</section>'''

    pricing_preview = f'''<section>
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Pricing</p>
      <h2>Transparent quotes. No surprise invoices.</h2>
      <p>We don't publish one-size-fits-all prices because filings vary by state, entity and turnover &mdash; here's exactly how we price every engagement instead. <a href="{t['pricing']}">Read more &rarr;</a></p>
    </div>
    {pricing_cards(t['contact'])}
  </div>
</section>'''

    body = hero + stats_block() + about_teaser + services_preview + process_section(depth) + pricing_preview + testimonials_block() + cta_band(depth)
    return page("LegalReet &mdash; Business Registration, GST &amp; Compliance Filings",
                f"LegalReet handles company registration, GST, trademark, licensing, ISO certification and legal documentation for Indian businesses across {len(SERVICES)}+ services &mdash; transparent quotes, one expert per case.",
                'home', depth, body)

# ---------------------------------------------------------------- SERVICES INDEX
def build_services_index():
    depth = 1
    t = nav_targets(depth, 'services')
    bc, bc_schema = breadcrumb(depth, [("Home", "index.html"), ("Services", "services/index.html")], 'services')
    cat_index_links = ''.join(f'<a href="#cat-{c["id"]}">{c["letter"]} &middot; {CHIP_LABELS[c["id"]]}</a>' for c in CATEGORIES)

    blocks = []
    for c in CATEGORIES:
        svcs = [s for s in SERVICES if s['cat'] == c['id']]
        cards = ''.join(service_card_link(s, f"{s['slug']}.html") for s in svcs)
        blocks.append(f'''<div class="cat-block" id="cat-{c['id']}">
      <div class="cat-block-head reveal">
        <svg class="cat-icon" viewBox="0 0 34 34" fill="none">{c['icon']}</svg>
        <div>
          <span>Practice {c['letter']}</span>
          <h2>{E(c['name'])}</h2>
          <p>{E(c['tagline'])} &middot; {len(svcs)} services</p>
        </div>
      </div>
      <div class="service-grid">{cards}</div>
    </div>''')

    body = bc + f'''<section class="section-tight">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Service directory</p>
      <h2>Everything we file, indexed like the paperwork itself.</h2>
      <p>Four practice areas, {len(SERVICES)} individual services &mdash; from first incorporation to the annual filing most businesses forget until the notice arrives. Pick a service below for process, documents, and a free quote.</p>
    </div>
    <nav class="cat-index reveal" aria-label="Jump to practice area">{cat_index_links}</nav>
    {''.join(blocks)}
  </div>
</section>''' + cta_band(depth)

    return page("All Services | LegalReet",
                f"Browse all {len(SERVICES)} registration, tax, trademark, licensing, certification and legal documentation services offered by LegalReet, organised into four practice areas.",
                'services', depth, body, schemas=[bc_schema], folder='services')

# ---------------------------------------------------------------- SERVICE DETAIL
def build_service_page(svc):
    depth = 1
    t = nav_targets(depth, 'services')
    cat = CAT_BY_ID[svc['cat']]
    name = E(svc['name']); short = E(svc['short']); overview = E(svc['overview'])
    documents = svc['documents']; benefits = svc['benefits']

    bc, bc_schema = breadcrumb(depth, [("Home", "index.html"), ("Services", "services/index.html"),
                            (E(cat['name']), "services/index.html"), (name, f"services/{svc['slug']}.html")], 'services')

    hero = f'''<section class="service-hero">
  <div class="container service-hero-grid">
    <div class="reveal">
      <p class="eyebrow">Practice {cat['letter']} &middot; {E(cat['name'])}</p>
      <h1>{name}</h1>
      <p class="hero-sub">{overview}</p>
      <div class="hero-actions">
        <a href="{t['contact']}" class="btn btn-primary">Get a free quote</a>
        <a href="{t['contact']}" class="btn btn-ghost">Talk to an expert</a>
      </div>
    </div>
    <div class="fact-card reveal">
      <h4>At a glance</h4>
      <div class="fact-row"><span>Turnaround</span><span>{E(svc['timeline'])}</span></div>
      <div class="fact-row"><span>Pricing</span><span>Custom quote</span></div>
      <div class="fact-row"><span>Practice area</span><span>{cat['letter']} &middot; {E(cat['name'])}</span></div>
      <a href="{t['contact']}" class="btn btn-primary">Request this service</a>
    </div>
  </div>
</section>'''

    benefits_html = ''.join(f'<li>{E(b)}</li>' for b in benefits)
    benefits_section = f'''<section class="section-tight">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Why it matters</p>
      <h2>What {name} gets you</h2>
    </div>
    <ul class="benefit-list reveal">{benefits_html}</ul>
  </div>
</section>'''

    docs_html = ''.join(f'<li>{E(d)}</li>' for d in documents)
    docs_section = f'''<section class="section-tight" style="background:var(--paper-card); border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Before you start</p>
      <h2>Documents you'll need</h2>
    </div>
    <ul class="doc-list reveal" style="max-width:640px;">{docs_html}</ul>
  </div>
</section>'''

    price_section = f'''<section class="section-tight">
  <div class="container">
    <div class="price-callout reveal">
      <div class="amount">Custom quote<small>Fixed fee confirmed upfront &middot; government charges billed at cost, where applicable</small></div>
      <a href="{t['contact']}" class="btn btn-primary">Get a free quote</a>
    </div>
  </div>
</section>'''

    faqs_plain = [
        (f"How long does {svc['name']} take?", f"{svc['timeline']}."),
        ("What documents are required?", "You'll need " + ", ".join(documents) + "."),
        ("How much does it cost?", "We quote a fixed fee upfront after a free consultation, since the exact cost depends on your state, entity type, and specific requirement. Government fees, where applicable, are always billed separately at cost."),
        ("Do I need to visit an office?", "No — the entire process is handled remotely. Documents are collected digitally, and signatures use Aadhaar e-sign or a Digital Signature Certificate where required."),
    ]
    faq_html = ''.join(f'''<details class="faq-item reveal">
      <summary>{E(q)}<svg class="faq-chevron" viewBox="0 0 16 16" fill="none"><path d="M3 6l5 5 5-5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></summary>
      <p>{E(a)}</p>
    </details>''' for q, a in faqs_plain)
    faq_section = f'''<section class="section-tight">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Questions</p>
      <h2>Frequently asked</h2>
    </div>
    <div class="faq-list" style="max-width:760px;">{faq_html}</div>
  </div>
</section>'''

    related = [s for s in SERVICES if s['cat'] == svc['cat'] and s['slug'] != svc['slug']][:3]
    related_section = ''
    if related:
        related_html = ''.join(service_card_link(r, f"{r['slug']}.html") for r in related)
        related_section = f'''<section class="section-tight" style="background:var(--paper-card); border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Related</p>
      <h2>Other services in {E(cat['name'])}</h2>
    </div>
    <div class="related-grid">{related_html}</div>
  </div>
</section>'''

    body = (bc + hero + benefits_section + docs_section +
            process_section(depth, title="How we handle it", eyebrow="Process") +
            price_section + faq_section + related_section +
            cta_band(depth, f"Ready to get started with {name}?",
                     "Book a free consultation &mdash; a filing expert will confirm eligibility and next steps within one business day."))

    return page(f"{svc['name']} | LegalReet", short, 'services', depth, body,
                schemas=[bc_schema, service_schema(svc, cat), faq_schema(faqs_plain)], folder='services')

# ---------------------------------------------------------------- PRICING
def build_pricing():
    depth = 0
    t = nav_targets(depth)
    bc, bc_schema = breadcrumb(depth, [("Home", "index.html"), ("Pricing", "pricing.html")])
    body = bc + f'''<section class="section-tight">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Pricing</p>
      <h2>Transparent quotes. No surprise invoices.</h2>
      <p>Government fees, state-level variations, and entity-specific requirements mean no two filings cost quite the same &mdash; so instead of a generic price list, here's exactly how we arrive at your quote for any of our {len(SERVICES)} services.</p>
    </div>
    {pricing_cards(t['contact'])}
  </div>
</section>''' + cta_band(depth)
    return page("Pricing | LegalReet",
                f"How LegalReet prices its {len(SERVICES)} registration, compliance, licensing and legal documentation services — a free consultation followed by a fixed, transparent quote.",
                'pricing', depth, body, schemas=[bc_schema])

# ---------------------------------------------------------------- ABOUT
def build_about():
    depth = 0
    t = nav_targets(depth)
    bc, bc_schema = breadcrumb(depth, [("Home", "index.html"), ("About", "about.html")])
    body = bc + f'''<section class="section-tight">
  <div class="container about-grid">
    <div class="reveal">
      <p class="eyebrow">About LegalReet</p>
      <h2 style="margin-top:14px;">Reet means &quot;the right way.&quot; It's also the only way we file.</h2>
    </div>
    <div class="copy reveal">
      <p>LegalReet was built for founders who don't have time to learn the difference between a DIN and a DSC &mdash; only to find out later they needed both. We pair every client with a single filing expert who owns the case end to end, across registration, tax, and compliance.</p>
      <p class="callout">&quot;We don't just submit forms. We track the jurisdiction, the deadline, and the follow-up &mdash; so nothing sits in a queue you can't see.&quot;</p>
      <p>Every engagement is quoted transparently before work begins &mdash; government fees are passed through at cost, and every filing status is visible to you in real time, no chasing us for updates.</p>
    </div>
  </div>
</section>''' + stats_block() + process_section(depth) + cta_band(depth)
    return page("About | LegalReet",
                "LegalReet pairs every client with a single filing expert across company registration, GST, trademark, licensing and legal documentation, on a transparent, quoted-upfront basis.",
                'about', depth, body, schemas=[bc_schema])

# ---------------------------------------------------------------- CONTACT
def build_contact():
    depth = 0
    t = nav_targets(depth)
    bc, bc_schema = breadcrumb(depth, [("Home", "index.html"), ("Contact", "contact.html")])
    body = bc + f'''<section class="section-tight">
  <div class="container contact-grid">
    <div class="reveal">
      <p class="eyebrow">Get in touch</p>
      <h2 style="margin-top:14px;">Talk to a filing expert.</h2>
      <p class="hero-sub" style="margin-top:16px; max-width:44ch;">Book a free consultation and we'll map out exactly which registrations, licenses and filings apply to your business &mdash; before you pay for anything.</p>
    </div>
    <div class="reveal">
      <div class="contact-channel">{MAIL_ICON}<div><b>Email</b><span>hello@legalreet.com</span></div></div>
      <div class="contact-channel">{PHONE_ICON}<div><b>Phone</b><span>+91 93683 75024</span></div></div>
      <div class="contact-channel">{PIN_ICON}<div><b>Office</b><span>E-14, First Floor, Indrapuram, near Shankar Greens,<br>Tajganj Phase II, Agra, Uttar Pradesh 282001</span></div></div>
    </div>
  </div>
</section>''' + cta_band(depth, "Prefer to just get started?",
                          "Browse the full service directory and pick exactly what you need.")
    return page("Contact | LegalReet", "Contact LegalReet by email or phone to start a company registration, GST, trademark or compliance filing.",
                'contact', depth, body, schemas=[bc_schema])

# ---------------------------------------------------------------- BLOG (Markdown-driven, Decap CMS compatible)
BLOG_DIR = os.path.join(ROOT, 'content', 'blog')

def render_markdown(text):
    """Minimal pure-stdlib Markdown -> HTML: headings, paragraphs, lists, bold/italic/links.
    No external dependency, so it runs identically locally and on Netlify's build image."""
    def inline(s):
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', r'<em>\1</em>', s)
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
        return s

    lines = text.replace('\r\n', '\n').strip('\n').split('\n')
    html_parts, para, list_items = [], [], []

    def flush_para():
        if para:
            html_parts.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()

    def flush_list():
        if list_items:
            html_parts.append('<ul>' + ''.join(f'<li>{inline(li)}</li>' for li in list_items) + '</ul>')
            list_items.clear()

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            flush_para(); flush_list(); continue
        if line.startswith('### '):
            flush_para(); flush_list(); html_parts.append(f'<h3>{inline(line[4:])}</h3>'); continue
        if line.startswith('## '):
            flush_para(); flush_list(); html_parts.append(f'<h2>{inline(line[3:])}</h2>'); continue
        if line.startswith('# '):
            flush_para(); flush_list(); html_parts.append(f'<h2>{inline(line[2:])}</h2>'); continue
        if line.startswith('- ') or line.startswith('* '):
            flush_para(); list_items.append(line[2:].strip()); continue
        flush_list()
        para.append(line.strip())
    flush_para(); flush_list()
    return '\n'.join(html_parts)

def parse_front_matter(raw):
    parts = raw.split('---', 2)
    meta_block, body = parts[1], parts[2]
    meta = {}
    for line in meta_block.strip().split('\n'):
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body

def load_posts():
    posts = []
    if not os.path.isdir(BLOG_DIR):
        return posts
    for fn in sorted(os.listdir(BLOG_DIR)):
        if not fn.endswith('.md'):
            continue
        raw = open(os.path.join(BLOG_DIR, fn), encoding='utf-8').read()
        meta, body = parse_front_matter(raw)
        meta['slug'] = os.path.splitext(fn)[0]
        meta['body_html'] = render_markdown(body)
        posts.append(meta)
    posts.sort(key=lambda p: p.get('date', ''), reverse=True)
    return posts

def format_post_date(d):
    try:
        from datetime import datetime
        return datetime.strptime(d, '%Y-%m-%d').strftime('%d %b %Y')
    except Exception:
        return d

def blog_card(post):
    return f'''<a class="service-card-link reveal" href="{post['slug']}.html">
      <h3>{E(post.get('title',''))}</h3>
      <p>{E(post.get('excerpt',''))}</p>
      <div class="price-row"><span>{format_post_date(post.get('date',''))}</span><span>{E(post.get('category',''))}</span></div>
    </a>'''

def build_blog_index(posts):
    depth = 1
    t = nav_targets(depth, 'blog')
    bc, bc_schema = breadcrumb(depth, [("Home", "index.html"), ("Blog", "blog/index.html")], 'blog')
    cards = ''.join(blog_card(p) for p in posts) if posts else '<p style="color:var(--ink-soft);">New posts are on the way &mdash; check back soon.</p>'
    body = bc + f'''<section class="section-tight">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">LegalReet Blog</p>
      <h2>Compliance news, deadlines and filing guides.</h2>
      <p>Practical, dated write-ups on the registrations, taxes and filings covered in our service directory &mdash; written by the team that actually files them.</p>
    </div>
    <div class="service-grid">{cards}</div>
  </div>
</section>''' + cta_band(depth)
    return page("Blog | LegalReet",
                "Compliance deadlines, GST and registration guides from the LegalReet filing team.",
                'blog', depth, body, schemas=[bc_schema], folder='blog')

def build_blog_post(post):
    depth = 1
    t = nav_targets(depth, 'blog')
    title = E(post.get('title', ''))
    bc, bc_schema = breadcrumb(depth, [("Home", "index.html"), ("Blog", "blog/index.html"), (title, f"blog/{post['slug']}.html")], 'blog')

    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post.get('title', ''),
        "datePublished": post.get('date', ''),
        "author": {"@type": "Organization", "name": "LegalReet"},
        "publisher": {"@type": "Organization", "name": "LegalReet"},
        "description": post.get('excerpt', ''),
        "url": f"{SITE_URL}/blog/{post['slug']}.html",
    }

    body = bc + f'''<section class="section-tight">
  <div class="container" style="max-width:760px;">
    <p class="eyebrow reveal">{E(post.get('category',''))} &middot; {format_post_date(post.get('date',''))}</p>
    <h1 class="reveal" style="margin-top:18px; font-size:clamp(1.9rem,3.4vw,2.6rem);">{title}</h1>
    <div class="copy reveal" style="margin-top:28px; font-size:16.5px;">{post['body_html']}</div>
  </div>
</section>''' + cta_band(depth, "Have a compliance question?", "Book a free consultation and get it answered by a filing expert, not a search engine.")

    return page(f"{post.get('title','')} | LegalReet Blog", post.get('excerpt', ''), 'blog', depth, body,
                schemas=[bc_schema, article_schema], folder='blog')

# ---------------------------------------------------------------- WRITE FILES
def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    write('index.html', build_home())
    write('pricing.html', build_pricing())
    write('about.html', build_about())
    write('contact.html', build_contact())
    write('services/index.html', build_services_index())
    for svc in SERVICES:
        write(f"services/{svc['slug']}.html", build_service_page(svc))
    posts = load_posts()
    write('blog/index.html', build_blog_index(posts))
    for post in posts:
        write(f"blog/{post['slug']}.html", build_blog_post(post))
    print(f"Wrote {6 + len(SERVICES) + len(posts)} HTML pages ({len(posts)} blog posts).")
