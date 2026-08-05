# -*- coding: utf-8 -*-
"""Generates the Green Solar Energy website."""
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_data import SITE, SERVICES, WHY_CHOOSE, PROCESS, TESTIMONIALS, FAQS_HOME, VIDEOS, GALLERY
import build_parts as P
from build_parts import (head, header, footer, divider, sec_head, feature_strip, why_choose,
                         services_section, process_section, counters, videos_section,
                         faq_section, testimonials_section, quote_section, location_section,
                         cta_band, page_hero, M)

OUT = r"C:\Users\HP\Downloads\green energy solar"


def write(name, html):
    with io.open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, len(html))


# ------------------------------------------------------------------ hero
def hero():
    return f"""<!-- hero -->
<section class="hero">
    <video class="hero-video" src="{M}hero.mp4" autoplay muted loop playsinline preload="auto"></video>
    <div class="hero-video-overlay"></div>
    <div class="container">
        <div class="hero-inner">
            <span class="eyebrow"><i class="fas fa-sun"></i> Jaora, Madhya Pradesh</span>
            <h1>Turning Sunlight into <em>Savings</em> for Every Home &amp; Business</h1>
            <p>Rooftop, commercial, industrial and agricultural solar systems designed, installed and serviced by our own team — with complete PM Surya Ghar subsidy assistance up to ₹78,000.</p>
            <ul class="hero-points">
                <li><i class="fas fa-circle-check"></i> Free Site Survey</li>
                <li><i class="fas fa-circle-check"></i> 25 Year Panel Warranty</li>
                <li><i class="fas fa-circle-check"></i> Subsidy Paperwork Handled</li>
            </ul>
            <div class="hero-actions">
                <a href="contact.html" class="btn btn-primary btn-lg">Get a Free Quote <i class="fas fa-arrow-right"></i></a>
                <a href="{SITE['wa']}" target="_blank" rel="noopener" class="btn btn-amber btn-lg"><i class="fa-brands fa-whatsapp"></i> WhatsApp Us</a>
            </div>
        </div>
    </div>
</section>
"""


# ------------------------------------------------------------------ about
def about_section(bg="bg-mint", full=False):
    extra = ""
    if full:
        extra = """                <p>Our team has grown from a two-man installation crew into a full service EPC company with in-house engineers, certified installers, a dedicated subsidy desk and a service unit that covers the entire Malwa region. We have installed over 1,250 systems and more than 4.8 MW of capacity — and we still handle every project the same way: survey first, honest sizing, genuine components, documented commissioning.</p>
"""
    return f"""<!-- about -->
<section class="section {bg}" id="about">
    <div class="container">
        <div class="about-grid">
            <div class="about-stack reveal">
                <div class="img-1"><img src="{M}residential-rooftop-solar-1.jpg" alt="Rooftop solar installation by Green Solar Energy in Jaora"></div>
                <div class="img-2"><img src="{M}solar-panel-installation-1.jpg" alt="Green Solar Energy installation crew fixing solar panels"></div>
                <div class="exp-badge"><strong>10+</strong><span>Years of<br>Experience</span></div>
            </div>
            <div class="reveal">
                <span class="eyebrow"><i class="fas fa-leaf"></i> About Us</span>
                <h2>A Local Solar Company That Stays With You After Installation</h2>
                <p class="sub" style="font-family:var(--ff-head);color:var(--green-700);font-weight:600;font-size:1.05rem">Green Solar Energy — Turning Sunlight into Savings since day one.</p>
                <p>We are a Jaora based solar EPC company serving homes, shops, factories and farms across Madhya Pradesh. From a 1kW rooftop system to a multi-MW industrial plant, every project is designed against your real consumption, installed by our own trained crew, and backed by a service team you can actually reach.</p>
{extra}                <ul class="about-list">
                    <li><i class="fas fa-circle-check"></i><div><strong>Registered PM Surya Ghar Vendor</strong>We file your entire subsidy application and follow it until the money is in your account.</div></li>
                    <li><i class="fas fa-circle-check"></i><div><strong>Tier-1 Components, Written Warranty</strong>DCR mono PERC modules, BIS-certified inverters and a 5-year system warranty in writing.</div></li>
                    <li><i class="fas fa-circle-check"></i><div><strong>Service That Answers the Phone</strong>Local team, fast response, and AMC packages that keep your plant at full output.</div></li>
                </ul>
                <div class="about-cta">
                    <a href="about.html" class="btn btn-primary">More About Us <i class="fas fa-arrow-right"></i></a>
                    <div class="about-sign">
                        <div class="ic"><i class="fas fa-phone-volume"></i></div>
                        <div>
                            <span style="font-size:.82rem;color:var(--muted)">Talk to our engineer</span><br>
                            <strong style="font-family:var(--ff-head);color:var(--ink)"><a href="tel:{SITE['phone_tel']}">{SITE['phone_disp']}</a></strong>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{divider(bg)}"""


# ------------------------------------------------------------------ PM Surya Ghar
PMSG_TABLE = [
    ("0 – 150 units", "1 – 2 kW", "₹30,000 – ₹60,000"),
    ("150 – 300 units", "2 – 3 kW", "₹60,000 – ₹78,000"),
    ("Above 300 units", "3+ kW", "₹78,000"),
]

PMSG_STRIP = [
    ("pmsg-1.webp", "PM Surya Ghar Muft Bijli Yojana rooftop solar scheme"),
    ("pmsg-2.webp", "Rooftop solar installed under PM Surya Ghar Yojana in Madhya Pradesh"),
    ("pmsg-3.jpg", "Solar panels installed for a PM Surya Ghar beneficiary"),
]

PMSG_SYSTEMS = [
    ("fa-plug", "On-Grid System",
     "Connected to the DISCOM grid with net metering. Daytime generation runs your home and every surplus unit is banked with the DISCOM. The lowest upfront cost and the highest bill savings — the usual choice under PM Surya Ghar."),
    ("fa-battery-full", "Off-Grid System",
     "Works completely independent of the grid. Batteries store the day's generation to run your home through the night — built for farms, wells, remote sites and areas where supply is unreliable."),
    ("fa-bolt", "Hybrid System",
     "Solar, battery and grid combined in one intelligent system. You get the daytime bill savings of on-grid plus instant backup — fans, lights and fridge keep running the moment supply fails."),
]

APPLY_POINTS = [
    "Up to 300 units of free electricity every month",
    "Subsidy credited directly to your bank account",
    "Sell your surplus power back to the grid",
    "Slash your electricity bills for 25+ years",
    "Increase the value of your property",
]


def pmsg_section(full=False):
    strip = "".join(f"""                <figure class="reveal"><img src="{M}{img}" alt="{alt}" loading="lazy"></figure>
""" for img, alt in PMSG_STRIP)

    rows = "".join(f"""                        <tr>
                            <td>{a}</td>
                            <td>{b}</td>
                            <td>{c}</td>
                        </tr>
""" for a, b, c in PMSG_TABLE)

    systems = "".join(f"""                <div class="systype reveal">
                    <div class="ic"><i class="fas {i}"></i></div>
                    <h4>{t}</h4>
                    <p>{d}</p>
                </div>
""" for i, t, d in PMSG_SYSTEMS)

    points = "".join(f'                        <li><i class="fas fa-circle-check"></i> <span>{p}</span></li>\n'
                     for p in APPLY_POINTS)

    # ---------------- A : heading, image strip, subsidy slab table
    sec_a = f"""<!-- pm surya ghar : scheme + subsidy slabs -->
<section class="section bg-white pmsg" id="pm-surya-ghar">
    <div class="container">
{sec_head("Government Scheme", "PM Surya Ghar Muft Bijli Yojana", "Free electricity for your home with up to ₹78,000 central subsidy — and we file the entire application for you")}        <div class="pmsg-strip">
{strip}        </div>
        <div class="slab-card reveal">
            <div class="slab-card-head">
                <div class="ic"><i class="fas fa-table-list"></i></div>
                <div>
                    <h3>PM Surya Ghar Yojana 2024 — Subsidy Slabs</h3>
                    <p>Get up to <strong>300 units of electricity free</strong> every month with a government-supported rooftop solar system and attractive central subsidies.</p>
                </div>
            </div>
            <div class="slab-table-wrap">
                <table class="slab-table">
                    <thead>
                        <tr>
                            <th>Monthly Consumption</th>
                            <th>System Capacity</th>
                            <th>Subsidy Amount</th>
                        </tr>
                    </thead>
                    <tbody>
{rows}                    </tbody>
                </table>
            </div>
            <p class="slab-note"><i class="fas fa-circle-info"></i> Central subsidy is ₹30,000 per kW for the first 2 kW and ₹18,000 for the 3rd kW, capped at ₹78,000. Applicable to residential connections only.</p>
        </div>
    </div>
</section>
{divider('bg-white')}"""

    # ---------------- B : three info cards
    eligibility = ""
    if full:
        eligibility = """
        <div class="grid g-2" style="margin-top:34px;align-items:start">
            <div class="info-card reveal">
                <div class="ic"><i class="fas fa-badge-check"></i></div>
                <h3>Who Is Eligible?</h3>
                <ul class="info-list">
                    <li><i class="fas fa-circle-check"></i> <span>Indian citizen owning a house with a suitable, shadow-free roof</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Valid residential electricity connection in the applicant's name</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Bank account linked with Aadhaar for direct subsidy transfer</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>No other central or state solar subsidy already availed for the same premises</span></li>
                </ul>
            </div>
            <div class="info-card reveal">
                <div class="ic"><i class="fas fa-clipboard-check"></i></div>
                <h3>Documents Required</h3>
                <ul class="info-list">
                    <li><i class="fas fa-circle-check"></i> <span>Latest electricity bill with the consumer number visible</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Aadhaar card of the applicant</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Bank passbook or a cancelled cheque</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Passport size photograph and roof ownership proof</span></li>
                </ul>
            </div>
        </div>
"""
    more_btn = "" if full else """
        <div class="text-center" style="margin-top:44px">
            <a href="pm-surya-ghar-yojana.html" class="btn btn-primary btn-lg">Full Scheme Details <i class="fas fa-arrow-right"></i></a>
        </div>
"""

    sec_b = f"""<!-- pm surya ghar : scheme explainer cards -->
<section class="section bg-cream">
    <div class="container">
        <div class="info-grid">
            <div class="info-card reveal">
                <img class="info-card-img" src="{M}{PMSG_STRIP[0][0]}" alt="{PMSG_STRIP[0][1]}" loading="lazy">
                <div class="ic"><i class="fas fa-house-chimney-window"></i></div>
                <h3>What is PM Surya Ghar Muft Bijli Yojana?</h3>
                <p>Launched by the Government of India, this flagship scheme helps households install rooftop solar and enjoy up to 300 units of free electricity every month — while a generous central subsidy is credited directly to your bank account. The mission is to bring one crore homes onto clean, low-cost solar power.</p>
            </div>
            <div class="info-card reveal">
                <img class="info-card-img" src="{M}{PMSG_STRIP[1][0]}" alt="{PMSG_STRIP[1][1]}" loading="lazy">
                <div class="ic"><i class="fas fa-seedling"></i></div>
                <h3>Why Choose Green Solar Energy?</h3>
                <ul class="info-list">
                    <li><i class="fas fa-circle-check"></i> <span>Free eligibility check &amp; portal registration</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Complete documentation &amp; DISCOM coordination</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Quality panels with certified installation</span></li>
                    <li><i class="fas fa-circle-check"></i> <span>Subsidy follow-up until it reaches your account</span></li>
                </ul>
            </div>
            <div class="info-card reveal">
                <img class="info-card-img" src="{M}{PMSG_STRIP[2][0]}" alt="{PMSG_STRIP[2][1]}" loading="lazy">
                <div class="ic"><i class="fas fa-indian-rupee-sign"></i></div>
                <h3>How Much Subsidy Can You Get?</h3>
                <p>Eligible households can receive up to <strong>₹78,000</strong> in central subsidy — roughly ₹30,000 per kW for the first 2 kW and ₹18,000 for the third kW. Our engineer sizes your system against your real consumption so you claim the maximum subsidy you qualify for.</p>
            </div>
        </div>
{eligibility}{more_btn}    </div>
</section>
{divider('bg-cream')}"""

    # ---------------- C : difference between solar systems
    sec_c = f"""<!-- pm surya ghar : system comparison -->
<section class="section bg-white">
    <div class="container">
        <div class="sec-head reveal">
            <span class="script-eyebrow">Know Your Options</span>
            <h2>Difference Between <span class="accent">Solar Systems</span></h2>
            <p>Understand the three main types of solar systems so you can choose exactly what fits your home or business.</p>
        </div>
        <div class="systype-grid">
{systems}        </div>
    </div>
</section>
{divider('bg-white')}"""

    # ---------------- D : apply for subsidy
    sec_d = f"""<!-- pm surya ghar : apply for subsidy -->
<section class="section bg-mint" id="apply">
    <div class="container">
        <div class="sec-head reveal">
            <span class="script-eyebrow">Get Started Today</span>
            <h2>Apply For Your <span class="accent">Solar Subsidy</span></h2>
            <p>Fill this form and our PM Surya Ghar experts will call you with your free subsidy estimate.</p>
        </div>
        <div class="apply-grid">
            <div class="apply-hero reveal">
                <div class="apply-sun"><i class="fas fa-sun"></i></div>
                <div class="apply-amt">₹78,000</div>
                <div class="apply-cap">Maximum Central Subsidy</div>
                <ul class="apply-list">
{points}                </ul>
            </div>
            <div class="form-card reveal">
                <form data-ajax data-subject="PM Surya Ghar Subsidy Application">
                    <div class="form-grid">
                        <div class="field">
                            <label for="s-name">Name</label>
                            <input id="s-name" name="name" type="text" placeholder="Your full name" required>
                        </div>
                        <div class="field" data-phone-repeater data-max="4">
                            <label for="s-phone">Mobile Numbers <span style="color:var(--muted);font-weight:500">(up to 4)</span></label>
                            <div class="phone-list">
                                <div class="phone-row">
                                    <input id="s-phone" name="phone1" type="tel" pattern="[0-9+ ]{{10,15}}" placeholder="10 digit mobile number" required>
                                    <button type="button" class="phone-remove" aria-label="Remove this number" hidden><i class="fas fa-xmark"></i></button>
                                </div>
                            </div>
                            <button type="button" class="phone-add"><i class="fas fa-plus"></i> Add another phone</button>
                        </div>
                        <div class="field full">
                            <label for="s-city">City / Location</label>
                            <input id="s-city" name="city" type="text" placeholder="e.g. Jaora, Madhya Pradesh" required>
                        </div>
                        <div class="field full">
                            <label for="s-bill">Monthly Electricity Bill</label>
                            <select id="s-bill" name="bill">
                                <option value="">Select your average bill</option>
                                <option>Below ₹1,000</option>
                                <option>₹1,000 – ₹3,000</option>
                                <option>₹3,000 – ₹6,000</option>
                                <option>₹6,000 – ₹15,000</option>
                                <option>Above ₹15,000</option>
                            </select>
                        </div>
                        <div class="field full">
                            <label for="s-msg">Message</label>
                            <textarea id="s-msg" name="message" placeholder="Anything you'd like to tell us? (optional)"></textarea>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary btn-lg" style="margin-top:18px;width:100%">Apply For Subsidy <i class="fas fa-paper-plane"></i></button>
                    <div class="form-msg"></div>
                    <p class="form-note"><i class="fas fa-shield-check"></i> Subsidy assistance is completely free with every residential installation.</p>
                </form>
            </div>
        </div>
    </div>
</section>
{divider('bg-mint')}"""

    return sec_a + sec_b + sec_c + sec_d


# ------------------------------------------------------------------ pages
def build_index():
    h = head("Green Solar Energy — Solar Panel Company in Jaora, Madhya Pradesh",
             "Green Solar Energy, Jaora — rooftop, commercial, industrial and agricultural solar installation across Madhya Pradesh with full PM Surya Ghar subsidy assistance up to ₹78,000.")
    return (h + header("index") + hero() + feature_strip() + about_section("bg-mint")
            + why_choose("bg-white") + services_section("bg-cool") + pmsg_section()
            + process_section("bg-white") + counters("bg-ink") + videos_section("bg-mint")
            + faq_section("bg-white") + testimonials_section("bg-sand") + quote_section("bg-white")
            + location_section("bg-mint") + cta_band() + footer())


def build_about():
    h = head("About Us — Green Solar Energy, Jaora",
             "Learn about Green Solar Energy — a Jaora based solar EPC company with 10+ years of experience, 1250+ installations and complete PM Surya Ghar subsidy assistance.")
    return (h + header("about")
            + page_hero("About Us", "About Us", "hero-services.webp",
                        "A local solar company built on honest sizing, genuine components and service that lasts the life of your plant.")
            + about_section("bg-white", full=True)
            + why_choose("bg-mint")
            + process_section("bg-white")
            + counters("bg-ink")
            + faq_section("bg-cream")
            + testimonials_section("bg-white")
            + quote_section("bg-mint")
            + cta_band() + footer())


def build_services():
    h = head("Our Services — Solar Solutions in Madhya Pradesh | Green Solar Energy",
             "Residential, commercial, industrial and agricultural solar services — installation, inverters, batteries, water heaters, pumps, street lights, AMC and subsidy assistance.")
    return (h + header("services")
            + page_hero("Our Services", "Services", "hero-services.webp",
                        "Twelve complete solar services — designed, installed and serviced by our own team across Madhya Pradesh.")
            + services_section("bg-white", show_all_btn=False)
            + process_section("bg-mint")
            + why_choose("bg-white")
            + faq_section("bg-cool")
            + quote_section("bg-white")
            + cta_band() + footer())


def build_pmsg_page():
    h = head("PM Surya Ghar Muft Bijli Yojana 2024 — Subsidy up to ₹78,000 | Green Solar Energy",
             "PM Surya Ghar Muft Bijli Yojana subsidy slabs, eligibility, documents and free application support from Green Solar Energy, Jaora, Madhya Pradesh.")
    faqs = [
        ("Is the subsidy paid to me or to the installer?",
         "The subsidy is credited directly into the beneficiary's own bank account by the government after the system is installed and the net meter is commissioned. It never passes through the vendor."),
        ("How much roof area do I need for a 3kW system?",
         "Roughly 250–300 sq. ft. of shadow-free roof. We confirm the exact layout during the free site survey before you commit to anything."),
        ("How long does the whole process take?",
         "Portal registration and DISCOM feasibility take about a week, installation 2–4 days, and the net meter plus inspection another 1–2 weeks. Subsidy is usually credited 30–45 days after commissioning."),
        ("Can a commercial or industrial connection claim this subsidy?",
         "No — PM Surya Ghar is for residential connections only. Commercial and industrial consumers benefit instead from accelerated depreciation and net metering, which we also handle."),
    ]
    return (h + header("pm-surya-ghar-yojana")
            + page_hero("PM Surya Ghar Muft Bijli Yojana", "PM Surya Ghar Yojana", "pmsg-3.jpg",
                        "Free electricity for your home with up to ₹78,000 central subsidy — and we file the entire application for you.")
            + pmsg_section(full=True)
            + why_choose("bg-white")
            + process_section("bg-cool")
            + faq_section("bg-cream", faqs, "Scheme FAQs", "PM Surya Ghar Yojana — Common Questions",
                          "What every applicant in Madhya Pradesh asks before applying")
            + testimonials_section("bg-white")
            + location_section("bg-mint")
            + cta_band() + footer())


def build_gallery():
    h = head("Gallery — Solar Installations by Green Solar Energy, Jaora",
             "Photo gallery of rooftop, commercial, industrial and agricultural solar installations completed by Green Solar Energy across Madhya Pradesh.")
    cats = [("*", "All Projects"), ("residential", "Residential"), ("commercial", "Commercial"),
            ("industrial", "Industrial"), ("installation", "Installation"), ("products", "Solar Products")]
    filters = "".join(f'            <button type="button" data-filter="{c}"{" class=\"active\"" if c == "*" else ""}>{l}</button>\n'
                      for c, l in cats)
    items = "".join(f"""            <div class="gal-item reveal" data-cat="{cat}" data-full="{M}{img}">
                <img src="{M}{img}" alt="{cap}" loading="lazy">
                <div class="ov">{cap}</div>
            </div>
""" for img, cap, cat in GALLERY)
    gal = f"""<!-- gallery -->
<section class="section bg-white">
    <div class="container">
{sec_head("Our Gallery", "Projects We Have Delivered Across Malwa", "Rooftops in Jaora, factories in Ratlam, farms in Mandsaur — a look at our recent work")}        <div class="gal-filter">
{filters}        </div>
        <div class="gal-grid">
{items}        </div>
    </div>
</section>
{divider('bg-white')}
<div class="lightbox" id="lightbox">
    <button class="lb-close" aria-label="Close"><i class="fas fa-xmark"></i></button>
    <button class="lb-prev" aria-label="Previous"><i class="fas fa-angle-left"></i></button>
    <img src="" alt="Gallery image">
    <button class="lb-next" aria-label="Next"><i class="fas fa-angle-right"></i></button>
</div>
"""
    return (h + header("gallery")
            + page_hero("Our Gallery", "Gallery", "hero-services.webp",
                        "A selection of the rooftops, factories, farms and streets we have powered with sunlight.")
            + gal
            + videos_section("bg-mint")
            + counters("bg-ink")
            + quote_section("bg-white")
            + cta_band() + footer())


def build_contact():
    h = head("Contact Us — Green Solar Energy, Jaora, Madhya Pradesh",
             "Contact Green Solar Energy in Jaora, Madhya Pradesh. Call +91 74411 76223 or email Greenenergy51@gmail.com for a free solar site survey and quotation.")
    cards = f"""<!-- contact cards -->
<section class="section bg-white">
    <div class="container">
{sec_head("Contact Us", "Talk to a Real Solar Engineer, Not a Call Centre", "Free survey, honest advice and a written quotation — anywhere in Ratlam district and beyond")}        <div class="contact-cards">
            <div class="contact-card reveal">
                <div class="ic"><i class="fas fa-phone-volume"></i></div>
                <h4>Call or WhatsApp</h4>
                <p><a href="tel:{SITE['phone_tel']}">{SITE['phone_disp']}</a></p>
                <p><a href="{SITE['wa']}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
            </div>
            <div class="contact-card reveal">
                <div class="ic"><i class="fas fa-envelope"></i></div>
                <h4>Email Us</h4>
                <p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
                <p>We reply within one working day</p>
            </div>
            <div class="contact-card reveal">
                <div class="ic"><i class="fas fa-location-dot"></i></div>
                <h4>Visit Our Office</h4>
                <p>{SITE['address_full']}</p>
                <p>{SITE['hours']}</p>
            </div>
        </div>
    </div>
</section>
{divider('bg-white')}"""
    return (h + header("contact")
            + page_hero("Contact Us", "Contact", "hero-services.webp",
                        "Call, WhatsApp or send us a message — we will arrange a free site survey at your convenience.")
            + cards
            + quote_section("bg-mint")
            + location_section("bg-white")
            + faq_section("bg-cream")
            + cta_band() + footer())


def build_service_page(s):
    others = "".join(f"""                        <li{' class="active"' if o['slug'] == s['slug'] else ''}><a href="service-{o['slug']}.html">{o['title']} <i class="fas fa-angle-right"></i></a></li>
""" for o in SERVICES)
    intro = "".join(f"                <p>{p}</p>\n" for p in s["intro"])
    ficons = ["fa-clipboard-check", "fa-screwdriver-wrench", "fa-gauge-high", "fa-shield-check"]
    feats = "".join(f"""                    <div class="feat-card" style="box-shadow:none">
                        <div class="feat-ic"><i class="fas {ficons[n % 4]}"></i></div>
                        <h4>{t}</h4>
                        <p>{d}</p>
                    </div>
""" for n, (t, d) in enumerate(s["features"]))
    bens = "".join(f'                    <li><i class="fas fa-circle-check"></i> <span>{b}</span></li>\n' for b in s["benefits"])
    gal = "".join(f'                <img src="{M}{im}" alt="{s["title"]} — Green Solar Energy" loading="lazy">\n' for im in s["imgs"][1:4])
    faqs = "".join(f"""                <div class="faq-item{' open' if n == 0 else ''}">
                    <button class="faq-q" type="button">{q} <i class="fas fa-chevron-down"></i></button>
                    <div class="faq-a"><div>{a}</div></div>
                </div>
""" for n, (q, a) in enumerate(s["faqs"]))

    body = f"""<!-- service detail -->
<section class="section bg-white">
    <div class="container">
        <div class="svc-detail">
            <div class="reveal">
                <div class="svc-hero-img"><img src="{M}{s['imgs'][0]}" alt="{s['title']} in Jaora, Madhya Pradesh"></div>
                <span class="eyebrow"><i class="fas {s['icon']}"></i> {s['badge']}</span>
                <h2>{s['title']}</h2>
{intro}
                <h3>What You Get With This Service</h3>
                <div class="grid g-2" style="margin-top:20px">
{feats}                </div>

                <div class="svc-gal">
{gal}                </div>

                <h3>Key Benefits</h3>
                <ul class="check-list">
{bens}                </ul>

                <h3>Frequently Asked Questions</h3>
                <div class="faq-list" style="margin-top:18px">
{faqs}                </div>
            </div>
            <aside class="sidebar">
                <div class="side-box">
                    <h4>All Services</h4>
                    <ul class="side-nav">
{others}                    </ul>
                </div>
                <div class="side-cta">
                    <div class="ic"><i class="fas fa-headset"></i></div>
                    <h4>Need Help Deciding?</h4>
                    <p>Talk to our engineer for a free site survey and an honest recommendation — no obligation.</p>
                    <a href="tel:{SITE['phone_tel']}" class="btn btn-light" style="margin-bottom:10px"><i class="fas fa-phone-volume"></i> {SITE['phone_disp']}</a>
                    <a href="{SITE['wa']}" target="_blank" rel="noopener" class="btn btn-amber"><i class="fa-brands fa-whatsapp"></i> WhatsApp Us</a>
                </div>
                <div class="side-box">
                    <h4>PM Surya Ghar Subsidy</h4>
                    <p style="font-size:.94rem">Residential customers can claim up to <strong>₹78,000</strong> central subsidy. We file the full application for you — free.</p>
                    <a href="pm-surya-ghar-yojana.html" class="btn btn-primary" style="margin-top:14px;width:100%">Check Eligibility</a>
                </div>
            </aside>
        </div>
    </div>
</section>
{divider('bg-white')}"""

    h = head(f"{s['title']} in Jaora, Madhya Pradesh | Green Solar Energy",
             f"{s['short']} Green Solar Energy, Jaora — free site survey, genuine components and complete subsidy assistance.")
    return (h + header("service-detail")
            + page_hero(s["title"], s["title"], s["imgs"][0], s["short"])
            + body
            + process_section("bg-mint")
            + services_section("bg-white", limit=6, show_all_btn=True)
            + quote_section("bg-cream")
            + cta_band() + footer())


def build_404():
    h = head("Page Not Found — Green Solar Energy", "The page you are looking for does not exist.")
    body = """<section class="section bg-white" style="padding:120px 0;text-align:center">
    <div class="container">
        <div style="font-family:var(--ff-head);font-size:clamp(5rem,16vw,10rem);font-weight:800;color:var(--green);line-height:1">404</div>
        <h2>This page has gone off-grid</h2>
        <p style="max-width:520px;margin:0 auto 30px">The page you were looking for does not exist or has been moved. Let's get you back to something useful.</p>
        <a href="index.html" class="btn btn-primary btn-lg">Back to Home <i class="fas fa-arrow-right"></i></a>
    </div>
</section>
"""
    return h + header("") + body + cta_band() + footer()


if __name__ == "__main__":
    write("index.html", build_index())
    write("about.html", build_about())
    write("services.html", build_services())
    write("pm-surya-ghar-yojana.html", build_pmsg_page())
    write("gallery.html", build_gallery())
    write("contact.html", build_contact())
    write("404.html", build_404())
    for s in SERVICES:
        write(f"service-{s['slug']}.html", build_service_page(s))
    print("\nDone —", 7 + len(SERVICES), "pages")
