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

svc("roc-annual-compliance", "c", "ROC Compliance Filings",
    "Event-based and annual ROC filings for companies and LLPs — AOC-4, MGT-7, LLP Form 8 & 11, ADT-1, DIR-3 KYC and more.",
    "Beyond the yearly return, the Registrar expects a form every time something changes — a new auditor, a director's KYC, a share allotment, a charge on assets. We maintain a filing register against your incorporation and AGM dates and lodge each form before the additional-fee clock starts.",
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

svc("digital-signature-certificate", "d", "Class 3 DSC (Signing)",
    "Get a Class 3 signing Digital Signature Certificate for MCA, GST, income tax and e-tender filings.",
    "Class 3 is now the only class issued by licensed certifying authorities for individuals, and it is what every director and authorised signatory uses to sign forms on the MCA, GST and Income Tax portals. We handle the application, paperless video verification and token dispatch.",
    ["Required for MCA, GST and income tax e-filings", "Valid for 2 years once issued", "Video KYC handled remotely"],
    ["PAN card", "Aadhaar card", "Passport-size photograph", "Active mobile number & email for verification"],
    "1-2 working days")

# =========================================================================
# Added in the 2026 redesign so LegalReet carries the full service line
# =========================================================================

svc("ngo-section-8-company-registration", "a", "NGO Registration as a Section 8 Company",
    "Set up your NGO as a licensed Section 8 Company — the non-profit structure most trusted by CSR funders.",
    "Many NGOs start as a trust or society and later discover that CSR committees and foreign donors prefer the audited, board-governed format of a Section 8 Company. Registering this way from day one avoids a costly conversion later. We draft charitable objects that survive the licence review, file SPICe+ with the Section 8 licence, and plan your 12A, 80G and CSR-1 sequence alongside.",
    ["Eligible for CSR-1 registration and CSR funding", "Board-run governance with personal liability limited", "Smooth path to 12A, 80G and NGO Darpan enrolment"],
    ["PAN & Aadhaar of at least two directors", "Proof of the NGO's registered office", "Statement of charitable objects and planned activities", "Projected income and expenditure for three years"],
    "20-25 working days")

svc("msme-registration-offer", "a", "MSME Registration — Festive Offer",
    "Udyam registration at an offer fee, bundled with a classification check and a certificate walkthrough.",
    "Udyam registration unlocks priority-sector lending, protection against delayed payments from buyers and access to several state and central schemes. Under this limited offer we file your Udyam registration, confirm whether you fall in the micro, small or medium bracket on investment and turnover, and explain which benefits you can actually claim.",
    ["Udyam certificate filed on the official portal", "Classification checked against investment and turnover", "Guidance on delayed-payment protection and subsidies"],
    ["Aadhaar of the proprietor, partner or director", "PAN of the business", "Bank account details of the business", "Approximate investment in plant, machinery or equipment"],
    "1-2 working days")

svc("private-limited-company-offer", "a", "Private Limited Company — Launch Offer",
    "Incorporate a Private Limited Company at a launch-offer fee, with DSC, DIN, PAN and TAN handled for two directors.",
    "This offer is for founders who are ready to incorporate now and have their KYC in order. We take two directors through DSC, name reservation and SPICe+ filing with standard MOA and AOA, and hand over the incorporation certificate, PAN and TAN. Stamp duty above the standard capital slab and state-specific variations are quoted before you pay.",
    ["Two DSCs and two DINs included", "Standard MOA and AOA drafted for your objects", "Certificate of incorporation, PAN and TAN delivered digitally"],
    ["PAN & Aadhaar of both directors", "Recent photographs of both directors", "Registered office proof with owner's NOC", "Latest bank statement or utility bill of each director"],
    "10-15 working days")

svc("lmpc-certificate", "b", "LMPC Certificate",
    "Register as a packer or importer of pre-packaged goods under the Legal Metrology (Packaged Commodities) Rules.",
    "Anyone who packs, imports or labels pre-packaged goods for retail sale in India must register with the Legal Metrology department before the goods reach shelves, and importers need it before customs clearance. We check your labels against the declaration rules, prepare the application and coordinate with the state or central controller.",
    ["Mandatory before importing or retailing pre-packed goods", "Label declarations reviewed before filing", "Reduces the risk of seizure and compounding penalties"],
    ["Certificate of incorporation or firm registration", "GST certificate and IEC (for importers)", "Address proof of the packing or storage unit", "Sample product labels"],
    "15-30 working days")

svc("epr-certificate", "b", "EPR Certificate",
    "Register for Extended Producer Responsibility under the plastic, e-waste or battery waste rules.",
    "Producers, importers and brand owners who place plastic packaging, electronics or batteries on the market must register with the Central Pollution Control Board and meet annual recycling targets. We identify which EPR regime applies, file the CPCB portal application and set up your annual target and return calendar.",
    ["Required to sell or import covered products", "Category-wise targets mapped at registration", "Annual return calendar set up from day one"],
    ["GST certificate, PAN and incorporation certificate", "IEC (for importers)", "Product and packaging category details", "Previous year's sales or import quantities"],
    "15-25 working days")

svc("cpwd-contractor-registration", "b", "CPWD Contractor Registration",
    "Enlist as a contractor with the Central Public Works Department to bid for government civil and electrical works.",
    "CPWD enlistment is a prerequisite for bidding on most central government construction tenders, and the class you are enlisted in caps the value of work you can bid for. We assess the class you qualify for on turnover, experience and engineering staff, compile the work-experience records and file the enlistment application.",
    ["Eligibility to bid on central government tenders", "Enlistment class matched to your track record", "Paperwork prepared for future class upgrades"],
    ["Firm or company registration documents", "Work orders and completion certificates", "Audited financials for recent years", "Details of engineers and technical staff"],
    "30-60 working days")

svc("duns-certificate", "b", "DUNS Number & Certificate",
    "Obtain a D-U-N-S number — the business identifier global buyers, platforms and app stores ask for.",
    "A Data Universal Numbering System number is a nine-digit identifier that multinational buyers, government procurement portals, Apple and Google developer programmes use to verify that your business is real. We submit your company profile, respond to verification calls and arrange the DUNS registered certificate and seal for your website.",
    ["Accepted by global buyers and supplier portals", "Required for many app-store and export programmes", "Verified business profile with registered seal"],
    ["Certificate of incorporation or registration", "GST certificate and PAN", "Address proof of the business", "Contact details of the authorised person"],
    "7-15 working days")

svc("annual-compliance-private-limited", "c", "Annual Compliance Package — Private Limited Company",
    "One fixed-scope package covering a Private Limited Company's statutory year — board meetings, AGM, audit coordination, AOC-4, MGT-7 and ITR.",
    "Most penalties small companies pay come from the annual cycle — a missed AGM, a late AOC-4, a forgotten DIR-3 KYC. This package bundles the whole year: four board meetings and the AGM with minutes, auditor appointment and coordination, financial statement and annual return filing with the ROC, director KYC and the company's income tax return, all tracked against one calendar.",
    ["Every annual company-law filing in one engagement", "Minutes and statutory registers kept up to date", "Company ITR filed alongside the ROC returns"],
    ["Certificate of incorporation, MOA and AOA", "Books of accounts or trial balance for the year", "Directors' DIN, PAN and Aadhaar", "Bank statements for the financial year"],
    "Runs across the financial year")

svc("no-objection-certificate", "d", "No Objection Certificate (NOC) Drafting",
    "Draft a property owner's or employer's NOC for GST, company registration, passport or loan applications.",
    "An NOC is a short document but a common reason applications get rejected — the wrong owner signs, the address does not match the utility bill, or the purpose is left vague. We draft the NOC for its specific use, whether it is a landlord's consent for a registered office, an employer's NOC for higher studies or a society's NOC for a property transfer.",
    ["Worded for the authority that will rely on it", "Address and ownership details matched to proofs", "Ready to sign and use the same day"],
    ["Name and address of the person issuing the NOC", "Purpose of the NOC and receiving authority", "Property or employment details", "Owner's ID proof where needed"],
    "1 working day")

svc("dsc-signing-encryption", "d", "Class 3 DSC (Signing + Encryption)",
    "A combined signing and encryption Class 3 DSC for e-tenders, e-auctions and portals that require encrypted bids.",
    "Government e-procurement portals such as CPPP and GeM-linked tenders ask bidders to encrypt their bids, which a signing-only certificate cannot do. The combo DSC carries two key pairs on one token. We issue it in the bidder's or organisation's name, complete video verification and help you map it to the tender portal.",
    ["Sign and encrypt bids on e-tender portals", "Both key pairs on a single USB token", "Available for individuals and organisations"],
    ["PAN and Aadhaar of the applicant", "Organisation documents and authorisation letter (for organisation DSC)", "Photograph and active mobile number", "Email ID for verification"],
    "1-2 working days")

svc("dgft-dsc", "d", "DGFT Digital Signature (Importer-Exporter)",
    "A Class 3 organisation DSC linked to your IEC for filing on the DGFT portal.",
    "Applications for IEC modification, export incentive scrips and authorisations on the DGFT portal must be signed with a DSC registered against the firm's IEC. We issue a Class 3 organisation certificate in the firm's name and help register it on the DGFT portal so your team can file without delays.",
    ["Signs IEC, RoDTEP and authorisation filings", "Issued in the firm's name against its IEC", "Registration on the DGFT portal assisted"],
    ["IEC certificate and firm PAN", "Authorisation letter for the signatory", "PAN, Aadhaar and photograph of the signatory", "GST certificate of the firm"],
    "1-3 working days")

# -------------------------------------------------------------------------
# Sub-groups (mirror the four-by-four menu structure)
# -------------------------------------------------------------------------
GROUPS = {
    "a": [("Company Incorporation", ["private-limited-company-registration","public-limited-company-registration","one-person-company-registration","section-8-company-registration","nidhi-company-registration","nbfc-registration","micro-finance-company-registration","producer-company-registration"]),
          ("Firms & Other Formations", ["sole-proprietorship-registration","partnership-firm-registration","llp-registration","shop-establishment-registration","msme-udyam-registration","aop-registration","boi-registration","huf-formation"]),
          ("NGOs & Special Entities", ["society-registration","trust-registration","ngo-section-8-company-registration","startup-india-registration","joint-venture-registration"]),
          ("Current Offers", ["msme-registration-offer","private-limited-company-offer"])],
    "b": [("Business Licences", ["gst-registration","fssai-food-license","import-export-code","pf-registration","esi-registration","fcra-registration","trade-license","professional-tax-registration","12a-80g-registration","ngo-darpan-niti-aayog-registration","lmpc-certificate","epr-certificate","cpwd-contractor-registration","duns-certificate"]),
          ("Trademark, Patent & Copyright", ["trademark-search","trademark-registration","trademark-renewal","trademark-objection","trademark-opposition","trademark-rectification","patent-search","provisional-patent-registration","patent-registration","copyright-registration"]),
          ("ISO Standards", ["iso-9001-certification","iso-14001-certification","iso-45001-certification","iso-22000-certification","iso-20000-certification","iso-27001-certification","iso-13485-certification","iso-22301-certification","iso-29990-certification","iso-50001-certification"]),
          ("Product & Industry Certifications", ["ce-marking","haccp-certification","halal-certification","gmp-certification","bifma-certification","organic-certification","agmark-certification","bis-certification","security-agency-license"])],
    "c": [("Accounts, Audit & Tax", ["accounting-bookkeeping","payroll-processing","stock-audit","tax-audit","company-audit","cost-audit","gst-return-filing","income-tax-return-filing","tds-return-filing","pf-esi-return-filing"]),
          ("Entity Conversions", ["proprietorship-to-private-limited","proprietorship-to-llp","proprietorship-to-partnership","partnership-to-llp","opc-to-private-limited","private-limited-to-opc","llp-to-private-limited","private-limited-to-public-limited","public-limited-to-private-limited","dissolution-of-partnership-firm"]),
          ("Company Secretarial", ["annual-compliance-private-limited","roc-annual-compliance","close-private-limited-company","close-llp","change-authorised-capital","add-remove-partner","add-remove-director","change-business-objective","change-registered-office-address","change-company-name"]),
          ("Finance & Advisory", ["business-loan-assistance","project-finance","wealth-management","investment-planning","corporate-advisory","project-report-preparation"])],
    "d": [("Property & Personal", ["rent-agreement-drafting","sale-deed-drafting","lease-deed-drafting","gift-deed-drafting","will-drafting","employment-contract-drafting","legal-notice-drafting-reply","no-objection-certificate"]),
          ("Business Contracts", ["partnership-deed-drafting","trust-deed-drafting","franchise-agreement-drafting","joint-venture-agreement-drafting","memorandum-of-understanding","consultancy-agreement-drafting","freelancer-agreement-drafting","vendor-service-agreement"]),
          ("Corporate Records", ["appointment-resignation-letter","notice-of-agm-egm","board-resolution-drafting","shareholder-resolution-drafting","minutes-of-meeting-drafting","shareholders-agreement-drafting","share-purchase-agreement","strategic-alliance-agreement"]),
          ("Digital Signatures", ["digital-signature-certificate","dsc-signing-encryption","dgft-dsc"])],
}

# Starting professional fees (INR). Services not listed here are quoted.
PRICES = {
    "private-limited-company-registration": 10000, "one-person-company-registration": 9999,
    "nidhi-company-registration": 31999, "sole-proprietorship-registration": 2499,
    "section-8-company-registration": 24999, "partnership-firm-registration": 3999,
    "llp-registration": 7499, "producer-company-registration": 39499,
    "public-limited-company-registration": 23999, "private-limited-company-offer": 6499,
    "msme-udyam-registration": 1499,
    "gst-registration": 2500, "import-export-code": 3999, "fssai-food-license": 2499,
    "cpwd-contractor-registration": 4999, "epr-certificate": 2499, "professional-tax-registration": 10499,
    "duns-certificate": 50000,
    "trademark-search": 7499, "trademark-registration": 8500, "trademark-objection": 2899,
    "trademark-rectification": 5899,
    "iso-9001-certification": 4500, "iso-14001-certification": 6499, "iso-45001-certification": 7499,
    "iso-22000-certification": 10999, "iso-20000-certification": 11999, "iso-27001-certification": 10999,
    "iso-13485-certification": 10999, "iso-22301-certification": 11999, "iso-29990-certification": 11999,
    "iso-50001-certification": 16499,
    "ce-marking": 11999, "haccp-certification": 11999, "halal-certification": 11999, "gmp-certification": 11999,
    "accounting-bookkeeping": 5999, "income-tax-return-filing": 1499, "project-report-preparation": 4500,
}
