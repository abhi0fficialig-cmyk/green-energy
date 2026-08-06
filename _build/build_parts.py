# -*- coding: utf-8 -*-
"""Shared layout components (head, header, footer, reusable sections)."""
from build_data import SITE, SERVICES, WHY_CHOOSE, PROCESS, TESTIMONIALS, FAQS_HOME, VIDEOS

M = "media/"


def head(title, desc, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="solar company Jaora, rooftop solar Madhya Pradesh, PM Surya Ghar Yojana, solar panel installation Ratlam, solar subsidy, Green Solar Energy">
<meta name="author" content="{SITE['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/logo/logo.png">
<link rel="icon" type="image/png" href="assets/img/logo/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/all-fontawesome.min.css">
<link rel="stylesheet" href="assets/css/main.css">
{extra}</head>
<body>
"""


NAV = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("services.html", "Services"),
    ("pm-surya-ghar-yojana.html", "PM Surya Ghar Yojana"),
    ("gallery.html", "Gallery"),
    ("contact.html", "Contact"),
]

SOCIALS = [
    ("https://www.facebook.com/", "fa-brands fa-facebook-f", "Facebook"),
    ("https://www.instagram.com/", "fa-brands fa-instagram", "Instagram"),
    ("https://www.youtube.com/", "fa-brands fa-youtube", "YouTube"),
    ("https://www.linkedin.com/", "fa-brands fa-linkedin-in", "LinkedIn"),
]


def header(active):
    drop = "\n".join(
        f'                            <a href="service-{s["slug"]}.html">{s["title"]}</a>'
        for s in SERVICES
    )
    items = ""
    for href, label in NAV:
        is_active = " class=\"active has-drop\"" if (href == "services.html" and active in ("services", "service-detail")) else ""
        if href == "services.html":
            cls = "has-drop active" if active in ("services", "service-detail") else "has-drop"
            items += f"""                    <li class="{cls}"><a href="services.html">Services</a>
                        <div class="dropdown">
{drop}
                        </div>
                    </li>
"""
        else:
            key = href.replace(".html", "")
            cls = ' class="active"' if key == active else ""
            items += f'                    <li{cls}><a href="{href}">{label}</a></li>\n'

    mm_sub = "\n".join(
        f'                    <a href="service-{s["slug"]}.html">{s["title"]}</a>'
        for s in SERVICES
    )
    mm_items = ""
    for href, label in NAV:
        if href == "services.html":
            mm_items += f"""            <li>
                <a href="#" class="sub-toggle">Services <i class="fas fa-chevron-down"></i></a>
                <div class="mm-sub">
                    <a href="services.html">All Services</a>
{mm_sub}
                </div>
            </li>
"""
        else:
            mm_items += f'            <li><a href="{href}">{label}</a></li>\n'

    socials = "\n".join(
        f'                        <a href="{u}" target="_blank" rel="noopener" aria-label="{n}"><i class="{i}"></i></a>'
        for u, i, n in SOCIALS
    )

    return f"""<!-- header -->
<header class="header">
    <div class="topbar">
        <div class="container">
            <div class="topbar-inner">
                <ul>
                    <li><a href="mailto:{SITE['email']}"><i class="fas fa-envelope"></i> {SITE['email']}</a></li>
                    <li class="hide-sm"><a href="tel:{SITE['phone_tel']}"><i class="fas fa-phone-volume"></i> {SITE['phone_disp']}</a></li>
                    <li class="hide-sm"><i class="fas fa-location-dot"></i> {SITE['address']}</li>
                </ul>
                <ul class="socials">
{socials}
                </ul>
            </div>
        </div>
    </div>
    <nav class="navbar">
        <div class="container">
            <div class="nav-inner">
                <a href="index.html" class="brand" aria-label="{SITE['name']} home">
                    <img src="assets/img/logo/logo.png" alt="{SITE['name']} — {SITE['tagline']}">
                </a>
                <ul class="nav-menu">
{items}                </ul>
                <div class="nav-right">
                    <div class="nav-call">
                        <div class="ic"><i class="fas fa-phone-volume"></i></div>
                        <div>
                            <span>Call us today</span>
                            <strong><a href="tel:{SITE['phone_tel']}">{SITE['phone_disp']}</a></strong>
                        </div>
                    </div>
                    <a href="contact.html" class="btn btn-primary d-none-sm">Get a Quote</a>
                    <button class="nav-toggle" data-menu-open aria-label="Open menu"><i class="fas fa-bars"></i></button>
                </div>
            </div>
        </div>
    </nav>
</header>

<!-- mobile drawer -->
<div class="mobile-menu" id="mobileMenu">
    <div class="mm-head">
        <a href="index.html" class="brand"><img src="assets/img/logo/logo.png" alt="{SITE['name']}"></a>
        <button class="mm-close" data-menu-close aria-label="Close menu"><i class="fas fa-xmark"></i></button>
    </div>
    <ul class="mm-list">
{mm_items}    </ul>
    <div class="mm-contact">
        <div><i class="fas fa-phone-volume"></i> <a href="tel:{SITE['phone_tel']}">{SITE['phone_disp']}</a></div>
        <div><i class="fas fa-envelope"></i> <a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
        <div><i class="fas fa-location-dot"></i> {SITE['address']}</div>
        <a href="contact.html" class="btn btn-primary" style="margin-top:8px">Get a Free Quote</a>
    </div>
</div>
<div class="overlay" id="overlay"></div>
"""


def footer():
    svc_links = "\n".join(
        f'                        <li><a href="service-{s["slug"]}.html">{s["title"]}</a></li>'
        for s in SERVICES[:7]
    )
    quick = "\n".join(
        f'                        <li><a href="{h}">{l}</a></li>' for h, l in NAV
    )
    socials = "\n".join(
        f'                    <a href="{u}" target="_blank" rel="noopener" aria-label="{n}"><i class="{i}"></i></a>'
        for u, i, n in SOCIALS
    )
    rail = "\n".join(
        f'    <a href="{u}" target="_blank" rel="noopener" aria-label="{n}"><i class="{i}"></i><span class="tip">{n}</span></a>'
        for u, i, n in SOCIALS
    )
    return f"""
<!-- footer -->
<footer class="footer">
    <div class="container">
        <div class="footer-grid">
            <div>
                <img src="assets/img/logo/logo-light.png" alt="{SITE['name']}" class="footer-logo">
                <p>{SITE['name']} is a Jaora based solar EPC company delivering rooftop, commercial, industrial and agricultural solar solutions across Madhya Pradesh — with full PM Surya Ghar subsidy assistance and lifetime service support.</p>
                <div class="footer-social">
{socials}
                </div>
            </div>
            <div>
                <h4>Quick Links</h4>
                <ul class="footer-links">
{quick}
                </ul>
            </div>
            <div>
                <h4>Our Services</h4>
                <ul class="footer-links">
{svc_links}
                    <li><a href="services.html">View All Services</a></li>
                </ul>
            </div>
            <div>
                <h4>Get In Touch</h4>
                <ul class="footer-contact">
                    <li><i class="fas fa-location-dot"></i> <span>{SITE['address_full']}</span></li>
                    <li><i class="fas fa-phone-volume"></i> <span><a href="tel:{SITE['phone_tel']}">{SITE['phone_disp']}</a></span></li>
                    <li><i class="fas fa-envelope"></i> <span><a href="mailto:{SITE['email']}">{SITE['email']}</a></span></li>
                    <li><i class="fas fa-clock"></i> <span>{SITE['hours']}<br>Sunday : Emergency service only</span></li>
                </ul>
                <a href="{SITE['wa']}" target="_blank" rel="noopener" class="btn btn-amber" style="margin-top:6px"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 {SITE['name']}. All rights reserved.</p>
            <p>{SITE['tagline']} · Jaora, Madhya Pradesh</p>
        </div>
    </div>
</footer>

<!-- floating side rail -->
<div class="side-rail">
{rail}
    <a href="{SITE['wa']}" class="wa" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i><span class="tip">WhatsApp Us</span></a>
    <a href="tel:{SITE['phone_tel']}" class="call" aria-label="Call"><i class="fas fa-phone-volume"></i><span class="tip">{SITE['phone_disp']}</span></a>
</div>
<a href="{SITE['wa']}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
<button class="scroll-top" aria-label="Scroll to top"><i class="fas fa-arrow-up"></i></button>

<script src="assets/js/site.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- sections

def divider(bg="bg-white"):
    return f'<div class="sec-divider {bg}"></div>\n'


def sec_head(eyebrow, title, sub=None, text=None, align="center"):
    cls = "sec-head" if align == "center" else "sec-head left"
    out = f'            <div class="{cls} reveal">\n'
    out += f'                <span class="eyebrow"><i class="fas fa-solar-panel"></i> {eyebrow}</span>\n'
    out += f'                <h2>{title}</h2>\n'
    if sub:
        out += f'                <p class="sub">{sub}</p>\n'
    if text:
        out += f'                <p>{text}</p>\n'
    out += '            </div>\n'
    return out


def feature_strip():
    cards = [
        ("fa-user-tie", "Expert Solar Team", "Certified engineers and in-house installers with 10+ years of field experience across Madhya Pradesh.", "01"),
        ("fa-wallet", "Affordable Pricing", "Transparent, itemised quotations with full PM Surya Ghar subsidy assistance — up to ₹78,000 back.", "02"),
        ("fa-headset", "24/7 Support", "Local Jaora based service team on call for breakdowns, cleaning and annual maintenance visits.", "03"),
    ]
    inner = "".join(f"""                <div class="feat-card reveal">
                    <div class="feat-ic"><i class="fas {i}"></i></div>
                    <h4>{t}</h4>
                    <p>{d}</p>
                    <span class="feat-num">{n}</span>
                </div>
""" for i, t, d, n in cards)
    return f"""<!-- feature strip -->
<section class="section section--sm feature-strip bg-white">
    <div class="container">
        <div class="grid g-3">
{inner}        </div>
    </div>
</section>
{divider('bg-white')}"""


def why_choose(bg="bg-white"):
    items = "".join(f"""                    <div class="marquee-item">
                        <div class="choose-card">
                            <div class="ic"><i class="fas {i}"></i></div>
                            <h4>{t}</h4>
                            <p>{d}</p>
                        </div>
                    </div>
""" for i, t, d in WHY_CHOOSE)
    fade = {"bg-white": "#fff", "bg-mint": "#F2FAF5", "bg-cream": "#FFF9F0",
            "bg-cool": "#F4F8F7", "bg-sand": "#FBF7EF", "bg-sky": "#F1F7FA"}[bg]
    return f"""<!-- why choose us -->
<section class="section {bg}">
    <div class="container">
{sec_head("Why Choose Us", "Reasons Families &amp; Businesses in Jaora Trust Us", "Local expertise, genuine components and service that answers the phone")}    </div>
    <div class="marquee" style="--fade:{fade}; --speed:60s">
        <div class="marquee-track">
{items}        </div>
    </div>
</section>
{divider(bg)}"""


def services_section(bg="bg-cool", limit=None, show_all_btn=True, heading=True):
    svcs = SERVICES if limit is None else SERVICES[:limit]
    cards = "".join(f"""                <article class="svc-card reveal">
                    <div class="svc-thumb">
                        <img src="{M}{s['imgs'][0]}" alt="{s['title']} in Jaora, Madhya Pradesh" loading="lazy">
                        <span class="badge">{s['badge']}</span>
                    </div>
                    <div class="svc-body">
                        <h3><a href="service-{s['slug']}.html">{s['title']}</a></h3>
                        <p>{s['short']}</p>
                        <a href="service-{s['slug']}.html" class="svc-link">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </article>
""" for s in svcs)
    head_html = sec_head(
        "Our Services",
        "Complete Solar Solutions Under One Roof",
        "From a 1kW home rooftop to a multi-MW industrial plant — designed, installed and serviced by our own team",
    ) if heading else ""
    btn = """
            <div class="text-center" style="margin-top:46px">
                <a href="services.html" class="btn btn-primary btn-lg">View All Services <i class="fas fa-arrow-right"></i></a>
            </div>
""" if show_all_btn else ""
    return f"""<!-- services -->
<section class="section {bg}" id="services">
    <div class="container">
{head_html}        <div class="grid g-3">
{cards}        </div>{btn}
    </div>
</section>
{divider(bg)}"""


def process_section(bg="bg-white"):
    cards = "".join(f"""                <div class="proc-card reveal">
                    <span class="proc-num">0{n}</span>
                    <div class="proc-ic"><i class="fas {i}"></i></div>
                    <h4>{t}</h4>
                    <p>{d}</p>
                </div>
""" for n, (i, t, d) in enumerate(PROCESS, 1))
    return f"""<!-- working process -->
<section class="section {bg}">
    <div class="container">
{sec_head("Working Process", "How We Take You From Bill Shock to Free Sunlight", "Four simple steps — and we handle the paperwork at every one of them", "Most customers go from first phone call to a running solar plant in under three weeks, subsidy application included.")}        <div class="process-grid">
{cards}        </div>
    </div>
</section>
{divider(bg)}"""


def counters(bg="bg-ink"):
    data = [
        ("fa-solar-panel", 1250, "+", "Solar Plants Installed"),
        ("fa-bolt", 4800, "kW+", "Total Capacity Commissioned"),
        ("fa-users", 1100, "+", "Happy Customers"),
        ("fa-award", 10, "+", "Years of Experience"),
    ]
    items = "".join(f"""                <div class="counter-item reveal">
                    <div class="ic"><i class="fas {i}"></i></div>
                    <div class="num"><span data-count="{n}">{n:,}</span>{sfx}</div>
                    <p>{l}</p>
                </div>
""" for i, n, sfx, l in data)
    return f"""<!-- counters -->
<section class="section section--sm {bg}">
    <div class="container">
        <div class="counter-wrap">
{items}        </div>
    </div>
</section>
{divider(bg)}"""


def videos_section(bg="bg-mint"):
    cards = "".join(f"""                <div class="video-card reveal">
                    <video src="{M}{f}" autoplay muted loop playsinline preload="metadata"></video>
                    <span class="v-cap">{c}</span>
                    <button class="v-sound" aria-label="Unmute video"><i class="fas fa-volume-xmark"></i></button>
                </div>
""" for f, c in VIDEOS)
    return f"""<!-- our videos -->
<section class="section {bg}">
    <div class="container">
{sec_head("Our Videos", "See Our Work in Motion", "Real installations, real sites, real customers across Madhya Pradesh", "Videos play automatically on mute — tap the speaker icon on any video to turn the sound on.")}        <div class="video-grid">
{cards}        </div>
    </div>
</section>
{divider(bg)}"""


def faq_section(bg="bg-white", faqs=None, eyebrow="FAQs", title="Answers to the Questions We Hear Most",
                sub="Everything a first-time solar buyer in Madhya Pradesh asks us"):
    faqs = faqs or FAQS_HOME
    items = "".join(f"""            <div class="faq-item{' open' if n == 0 else ''} reveal">
                <button class="faq-q" type="button">{q} <i class="fas fa-chevron-down"></i></button>
                <div class="faq-a"><div>{a}</div></div>
            </div>
""" for n, (q, a) in enumerate(faqs))
    return f"""<!-- faqs -->
<section class="section {bg}">
    <div class="container">
{sec_head(eyebrow, title, sub)}        <div class="faq-list">
{items}        </div>
    </div>
</section>
{divider(bg)}"""


def testimonials_section(bg="bg-sand"):
    items = "".join(f"""                    <div class="marquee-item">
                        <div class="tsm-card">
                            <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                            <p>&ldquo;{txt}&rdquo;</p>
                            <div class="tsm-who">
                                <div class="tsm-av">{name[0]}</div>
                                <div>
                                    <strong>{name}</strong>
                                    <span><i class="fas fa-location-dot"></i> {loc}</span>
                                </div>
                            </div>
                        </div>
                    </div>
""" for name, loc, txt in TESTIMONIALS)
    fade = {"bg-white": "#fff", "bg-mint": "#F2FAF5", "bg-cream": "#FFF9F0",
            "bg-cool": "#F4F8F7", "bg-sand": "#FBF7EF", "bg-sky": "#F1F7FA"}[bg]
    return f"""<!-- testimonials -->
<section class="section {bg}">
    <div class="container">
{sec_head("Testimonials", "What Our Customers Across Malwa Say", "Reviews from Jaora, Ratlam, Mandsaur, Neemuch, Ujjain, Dewas and nearby towns")}    </div>
    <div class="marquee" style="--fade:{fade}; --speed:75s">
        <div class="marquee-track">
{items}        </div>
    </div>
</section>
{divider(bg)}"""


def quote_section(bg="bg-white"):
    svc_opts = "\n".join(f'                                    <option>{s["title"]}</option>' for s in SERVICES)
    return f"""<!-- request a quote -->
<section class="section {bg}" id="quote">
    <div class="container">
{sec_head("Request A Quote", "Get a Free Site Survey &amp; Written Quotation", "Tell us your average monthly bill — we will tell you exactly what you can save")}        <div class="quote-grid">
            <div class="co-card reveal">
                <img src="assets/img/logo/logo.png" alt="{SITE['name']}" class="co-logo">
                <h3>{SITE['name']}</h3>
                <p>{SITE['tagline']} — a Jaora based solar EPC company installing rooftop, commercial, industrial and agricultural solar systems across Madhya Pradesh. Registered PM Surya Ghar vendor with in-house installation and service teams.</p>
                <ul class="co-list">
                    <li>
                        <div class="ic"><i class="fas fa-location-dot"></i></div>
                        <div><span>Office Address</span><strong>{SITE['address_full']}</strong></div>
                    </li>
                    <li>
                        <div class="ic"><i class="fas fa-phone-volume"></i></div>
                        <div><span>Call / WhatsApp</span><a href="tel:{SITE['phone_tel']}">{SITE['phone_disp']}</a></div>
                    </li>
                    <li>
                        <div class="ic"><i class="fas fa-envelope"></i></div>
                        <div><span>Email Us</span><a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
                    </li>
                    <li>
                        <div class="ic"><i class="fas fa-clock"></i></div>
                        <div><span>Working Hours</span><strong>{SITE['hours']}</strong></div>
                    </li>
                </ul>
                <div class="co-stats">
                    <div><strong>10+</strong><span>Years Experience</span></div>
                    <div><strong>1250+</strong><span>Installations</span></div>
                    <div><strong>₹78,000</strong><span>Max Subsidy</span></div>
                </div>
            </div>
            <div class="form-card reveal">
                <h3>Request Your Free Quote</h3>
                <p>Fill in the form and our engineer will call you within 24 hours with a system recommendation and price.</p>
                <form data-ajax data-subject="Free Quote Request">
                    <div class="form-grid">
                        <div class="field">
                            <label for="q-name">Full Name</label>
                            <input id="q-name" name="name" type="text" placeholder="Your name" required>
                        </div>
                        <div class="field">
                            <label for="q-phone">Mobile Number</label>
                            <input id="q-phone" name="phone" type="tel" pattern="[0-9+ ]{{10,15}}" placeholder="10 digit mobile number" required>
                        </div>
                        <div class="field">
                            <label for="q-email">Email Address</label>
                            <input id="q-email" name="email" type="email" placeholder="you@example.com">
                        </div>
                        <div class="field">
                            <label for="q-city">City / Village</label>
                            <input id="q-city" name="city" type="text" placeholder="e.g. Jaora" required>
                        </div>
                        <div class="field">
                            <label for="q-service">Service Required</label>
                            <select id="q-service" name="service">
                                <option value="">Select a service</option>
{svc_opts}
                            </select>
                        </div>
                        <div class="field">
                            <label for="q-bill">Average Monthly Bill</label>
                            <select id="q-bill" name="bill">
                                <option value="">Select range</option>
                                <option>Below ₹1,000</option>
                                <option>₹1,000 – ₹3,000</option>
                                <option>₹3,000 – ₹6,000</option>
                                <option>₹6,000 – ₹15,000</option>
                                <option>Above ₹15,000</option>
                            </select>
                        </div>
                        <div class="field full">
                            <label for="q-msg">Message</label>
                            <textarea id="q-msg" name="message" placeholder="Tell us about your roof, load or any question you have"></textarea>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary btn-lg" style="margin-top:18px;width:100%">Submit Request <i class="fas fa-arrow-right"></i></button>
                    <div class="form-msg"></div>
                    <p class="form-note"><i class="fas fa-shield-check"></i> Your details stay with us. No spam calls, ever.</p>
                </form>
            </div>
        </div>
    </div>
</section>
{divider(bg)}"""


def location_section(bg="bg-mint"):
    return f"""<!-- our location -->
<section class="section {bg}">
    <div class="container">
{sec_head("Our Location", "Find Us in Jaora, Madhya Pradesh", "Serving Jaora, Ratlam, Mandsaur, Neemuch, Ujjain, Dewas and the whole Malwa region", "Walk in for a free consultation, or ask our engineer to visit your site — there is no charge for a survey anywhere in the district.")}        <div class="map-wrap reveal">
            <iframe
                src="https://www.google.com/maps?q=Jaora,%20Ratlam,%20Madhya%20Pradesh%20457226&amp;output=embed"
                width="100%" height="460" style="border:0" allowfullscreen="" loading="lazy"
                referrerpolicy="no-referrer-when-downgrade" title="Green Solar Energy location — Jaora, Madhya Pradesh"></iframe>
        </div>
        <div class="map-cards">
            <div class="map-card reveal">
                <div class="ic"><i class="fas fa-location-dot"></i></div>
                <div>
                    <h4>Visit Our Office</h4>
                    <p>{SITE['address_full']}</p>
                </div>
            </div>
            <div class="map-card reveal">
                <div class="ic"><i class="fas fa-phone-volume"></i></div>
                <div>
                    <h4>Call or WhatsApp</h4>
                    <p><a href="tel:{SITE['phone_tel']}">{SITE['phone_disp']}</a><br><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
                </div>
            </div>
            <div class="map-card reveal">
                <div class="ic"><i class="fas fa-clock"></i></div>
                <div>
                    <h4>Working Hours</h4>
                    <p>{SITE['hours']}<br>Sunday : Emergency service only</p>
                </div>
            </div>
        </div>
    </div>
</section>
{divider(bg)}"""


def cta_band():
    return f"""<!-- cta -->
<section class="section section--sm cta-band">
    <div class="container">
        <div class="cta-inner">
            <div>
                <h2>Ready to cut your electricity bill to zero?</h2>
                <p>Free site survey, honest sizing and complete PM Surya Ghar subsidy assistance — up to ₹78,000 back in your account.</p>
            </div>
            <div style="display:flex;gap:14px;flex-wrap:wrap">
                <a href="tel:{SITE['phone_tel']}" class="btn btn-light btn-lg"><i class="fas fa-phone-volume"></i> {SITE['phone_disp']}</a>
                <a href="{SITE['wa']}" target="_blank" rel="noopener" class="btn btn-amber btn-lg"><i class="fa-brands fa-whatsapp"></i> WhatsApp Us</a>
            </div>
        </div>
    </div>
</section>
"""


def page_hero(title, crumb_label, img="hero-page.webp", sub=None):
    subhtml = f'            <p style="color:#CFE0D6;max-width:660px;margin:0 auto 14px">{sub}</p>\n' if sub else ""
    return f"""<!-- page hero -->
<section class="page-hero" style="background-image:url('{M}{img}')">
    <div class="container">
        <h1>{title}</h1>
{subhtml}        <div class="crumb"><a href="index.html">Home</a> <span>/</span> <span>{crumb_label}</span></div>
    </div>
</section>
"""
