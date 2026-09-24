#!/usr/bin/env python3
"""Builds the static pages for rotem-gal.com.

Edit the data below or _src/home.html, then run: python3 build.py
Output is plain HTML at the repo root; Vercel serves it as-is.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://www.rotem-gal.com"
PERSON_ID = f"{SITE}/#person"
WEBSITE_ID = f"{SITE}/#website"
HEADSHOT = "/images/rotem-gal-square.jpg"

SHORT_BIO = (
    "Rotem Gal is a Tel Aviv-based marketer and writer focused on branding, organic growth "
    "and how brands get chosen in an agentic world. Rotem is Director of Organic Growth at ZyG "
    "and previously worked at AI21 Labs and WalkMe."
)
MEDIUM_BIO = SHORT_BIO + (
    " Rotem's writing on marketing, ecommerce, branding and customer behavior has appeared in "
    "Inc., Entrepreneur, business.com and ReferralCandy, and Rotem is a speaker at Becoming 10x, "
    "the annual summit by 10x Marketers, in Tel Aviv in November 2026."
)
LONG_BIO = MEDIUM_BIO + (
    " Across entrepreneurial ventures and larger technology companies, Rotem's work has centred "
    "on one question: how companies become known, trusted and chosen. At ZyG, which builds an "
    "agentic operating system for ecommerce brands, Rotem leads organic growth and studies how AI "
    "assistants and agents change the way consumers discover and evaluate brands. Rotem has "
    "appeared on the Voices of Search podcast and spoken at Team8 about organic growth for B2B companies."
)

SAME_AS = [
    "https://www.linkedin.com/in/rotemgal/",
    "https://x.com/gal_rotem",
    "https://www.inc.com/author/rotem-gal",
    "https://www.entrepreneur.com/author/rotem-gal",
    "https://www.referralcandy.com/author/rotemg",
]

ZYG = {"@type": "Organization", "name": "ZyG", "url": "https://www.zyg.com/"}
AI21 = {"@type": "Organization", "name": "AI21 Labs", "url": "https://www.ai21.com/"}
WALKME = {"@type": "Organization", "name": "WalkMe", "url": "https://www.walkme.com/"}

PERSON = {
    "@type": "Person",
    "@id": PERSON_ID,
    "name": "Rotem Gal",
    "alternateName": "רותם גל",
    "url": f"{SITE}/",
    "mainEntityOfPage": f"{SITE}/about",
    "description": SHORT_BIO,
    "email": "mailto:info@rotemgal.com",
    "jobTitle": "Director of Organic Growth",
    "worksFor": ZYG,
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "Netanya Academic College"},
        AI21,
        WALKME,
    ],
    "homeLocation": {"@type": "Place", "name": "Tel Aviv, Israel"},
    "nationality": {"@type": "Country", "name": "Israel"},
    "knowsLanguage": ["en", "he"],
    "knowsAbout": ["Branding", "Brand building", "Organic growth", "AI agents",
                   "Agentic commerce", "Ecommerce", "Customer behavior"],
    "sameAs": SAME_AS,
}
if HEADSHOT:
    PERSON["image"] = {"@type": "ImageObject", "url": SITE + HEADSHOT, "caption": "Rotem Gal"}

WEBSITE = {
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    "url": f"{SITE}/",
    "name": "Rotem Gal",
    "inLanguage": "en",
    "publisher": {"@id": PERSON_ID},
    "about": {"@id": PERSON_ID},
}

ARTICLES = [
    # (publication, title, url, iso date or "", display date, tag)
    ("Inc.", "How to Transform Your Email Marketing as the Pandemic Continues",
     "https://www.inc.com/rotem-gal/how-to-transform-your-email-marketing-as-pandemic-continues.html", "2021-08-29", "Aug 2021", "Email marketing"),
    ("Inc.", "4 Trends That Will Shape the Next Few Years of E-Commerce",
     "https://www.inc.com/rotem-gal/4-trends-that-will-shape-next-few-years-of-e-commerce.html", "2020-11", "Nov 2020", "Ecommerce"),
    ("Inc.", "How to Move Your Business Online in the Time of Coronavirus",
     "https://www.inc.com/rotem-gal/how-to-move-your-business-online-in-time-of-coronavirus.html", "2020-08", "Aug 2020", "Ecommerce"),
    ("Entrepreneur", "How an Ecommerce-Insights Company Uses AI to Understand Customer Sentiment",
     "https://www.entrepreneur.com/science-technology/how-an-ecommerce-insights-company-uses-ai-to-understand/358765", "2020-11-03", "Nov 2020", "AI"),
    ("Entrepreneur", "10 Popular Instagram Tools to Up Your Marketing Game",
     "https://www.entrepreneur.com/growing-a-business/10-popular-instagram-tools-to-up-your-marketing-game/366358", "", "", "Social"),
    ("Entrepreneur", "TikTok's Fate Is Uncertain. Use These 3 Trends to Own Your Audiences",
     "https://www.entrepreneur.com/business-news/tiktoks-fate-is-uncertain-use-these-3-trends-to-own-your/356296", "", "", "Audience"),
    ("Entrepreneur", "3 Tips on How to Grow and Scale Your Company During the Pandemic",
     "https://www.entrepreneur.com/growing-a-business/3-tips-on-how-to-grow-and-scale-your-company-during-the/357573", "", "", "Growth"),
    ("business.com", "8 Questions to Ask Before Connecting With Your Audience on Social Media",
     "https://www.business.com/articles/questions-before-connecting-audience-on-social-media/", "", "", "Brand voice"),
    ("ReferralCandy", "9 Stats Proving the Power of Multichannel for eCommerce",
     "https://www.referralcandy.com/blog/multichannel-statistics/", "2019-09-11", "Sep 2019", "Acquisition"),
    ("ReferralCandy", "How to Successfully Launch Your Franchise the Right Way",
     "https://www.referralcandy.com/blog/franchise-launch/", "2018-01-13", "Jan 2018", "Entrepreneurship"),
]
PUBLISHERS = {
    "Inc.": ("https://www.inc.com/", "https://www.inc.com/author/rotem-gal"),
    "Entrepreneur": ("https://www.entrepreneur.com/", "https://www.entrepreneur.com/author/rotem-gal"),
    "business.com": ("https://www.business.com/", None),
    "ReferralCandy": ("https://www.referralcandy.com/", "https://www.referralcandy.com/author/rotemg"),
}

NAV = [("/about", "About"), ("/writing", "Writing"), ("/speaking", "Speaking"), ("/media-kit", "Media kit")]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def page(path, title, desc, body, graph_extra, page_type="WebPage", crumbs=None):
    url = SITE + (path if path != "/" else "/")
    webpage = {
        "@type": page_type,
        "@id": f"{url}#webpage",
        "url": url,
        "name": title,
        "description": desc,
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": PERSON_ID},
        "inLanguage": "en",
    }
    if page_type == "ProfilePage":
        webpage["mainEntity"] = {"@id": PERSON_ID}
    graph = [WEBSITE, PERSON, webpage] + graph_extra
    if crumbs:
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p}
                for i, (p, n) in enumerate([("/", "Home")] + crumbs)
            ],
        })
        webpage["breadcrumb"] = {"@id": f"{url}#breadcrumb"}
    robots = '<meta name="robots" content="noindex">' if path == "/404" else f'<link rel="canonical" href="{url}">'
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    on = ' class="on"'
    nav = "\n".join(
        f'      <li><a href="{h}"{on if h == path else ""}>{n}</a></li>' for h, n in NAV
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<meta name="author" content="Rotem Gal">
<meta property="og:type" content="{'profile' if page_type == 'ProfilePage' or path == '/' else 'website'}">
<meta property="og:site_name" content="Rotem Gal">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@gal_rotem">
<meta name="twitter:creator" content="@gal_rotem">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-96x96.png" type="image/png" sizes="96x96">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#141a2e">
<meta property="og:image:alt" content="Rotem Gal">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>

<header>
  <nav class="wrap">
    <a href="/" class="logo">Rotem Gal<span>.</span></a>
    <ul class="nav-links">
{nav}
    </ul>
    <a href="https://www.linkedin.com/in/rotemgal/" target="_blank" rel="noopener me" class="btn btn-primary nav-cta">Follow on LinkedIn</a>
  </nav>
</header>

<main>
{body}
</main>

<footer>
  <div class="wrap">
    <span>&copy; <span id="y">2026</span> Rotem Gal · Tel Aviv</span>
    <span>
      <a href="https://www.linkedin.com/in/rotemgal/" target="_blank" rel="noopener me">LinkedIn</a>
      <a href="https://x.com/gal_rotem" target="_blank" rel="noopener me">X</a>
      <a href="https://www.inc.com/author/rotem-gal" target="_blank" rel="noopener me">Inc.</a>
      <a href="https://www.entrepreneur.com/author/rotem-gal" target="_blank" rel="noopener me">Entrepreneur</a>
      <a href="/media-kit">Media kit</a>
      <a href="mailto:info@rotemgal.com">Email</a>
    </span>
  </div>
</footer>

<script>
  document.getElementById('y').textContent = new Date().getFullYear();
  document.querySelectorAll('.filters button').forEach((b, _, all) => b.addEventListener('click', () => {{
    all.forEach(x => x.classList.remove('on')); b.classList.add('on');
    document.querySelectorAll('.article').forEach(a => {{
      a.style.display = (b.dataset.f === 'all' || a.dataset.p === b.dataset.f) ? '' : 'none';
    }});
  }}));
  document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', () => {{
    navigator.clipboard.writeText(document.getElementById(b.dataset.copy).innerText);
    b.textContent = 'Copied'; setTimeout(() => b.textContent = 'Copy', 1500);
  }}));
</script>
</body>
</html>
"""


def article_schema(a):
    pub, title, url, iso, _, _ = a
    node = {
        "@type": "Article",
        "headline": title,
        "url": url,
        "author": {"@id": PERSON_ID},
        "publisher": {"@type": "Organization", "name": pub, "url": PUBLISHERS[pub][0]},
    }
    if iso:
        node["datePublished"] = iso
    return node


# ---------- Home ----------
home_body = (ROOT / "_src/home.html").read_text()
home_body = home_body.replace(
    '    <div class="articles">',
    '    <div class="articles">', 1
).replace(
    "  </div>\n</section>\n\n<!-- SPEAKING -->",
    '    <p style="margin-top:28px"><a href="/writing" class="btn btn-ghost">All writing &rarr;</a></p>\n  </div>\n</section>\n\n<!-- SPEAKING -->', 1
).replace(
    "  </div>\n</section>\n\n<!-- CONTACT -->",
    '    <p style="margin-top:28px"><a href="/speaking" class="btn btn-ghost">Speaking and podcasts &rarr;</a></p>\n  </div>\n</section>\n\n<!-- CONTACT -->', 1
)

pages = {}
pages["index.html"] = page(
    "/", "Rotem Gal - Branding and Organic Growth in an Agentic World",
    "Rotem Gal writes and speaks about branding, organic growth and how to build brands in an agentic world. Director of Organic Growth at ZyG, previously AI21 Labs and WalkMe.",
    home_body, [], page_type="ProfilePage",
)

# ---------- About ----------
faqs = [
    ("Who is Rotem Gal?", SHORT_BIO),
    ("Where is Rotem Gal based?", "Rotem Gal is based in Tel Aviv, Israel."),
    ("What does Rotem Gal write and speak about?",
     "Rotem Gal writes and speaks about branding, organic growth, and how brands get discovered, trusted and chosen when AI assistants and agents do more of the research for the buyer."),
    ("Where has Rotem Gal's writing been published?",
     "Rotem Gal's articles have been published in Inc., Entrepreneur, business.com and ReferralCandy, covering marketing, ecommerce, branding and customer behavior."),
    ("Where does Rotem Gal work?",
     "Rotem Gal is Director of Organic Growth at ZyG, a Tel Aviv company building an agentic operating system for ecommerce brands. Rotem previously worked at AI21 Labs and WalkMe."),
    ("How can I invite Rotem Gal to speak or contribute?",
     "Email info@rotemgal.com with the event, podcast or publication, the audience and the date. Bios and topics are on the media kit page."),
]
faq_html = "\n".join(
    f"        <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs
)
about_body = f"""<section class="page-hero">
  <div class="wrap">
    <div class="eyebrow">About</div>
    <h1>Rotem Gal</h1>
    <p>{esc(SHORT_BIO)}</p>
  </div>
</section>

<section>
  <div class="wrap two-col">
    <div class="prose">
      <h2>How companies become known, trusted and chosen</h2>
      <p>I've spent my career between entrepreneurial ventures and larger technology companies. Working on both sides taught me how to connect the way a brand positions itself with the way it actually wins customers.</p>
      <p>I led organic growth at WalkMe and AI21 Labs. Today I run organic growth at <a href="https://www.zyg.com/" target="_blank" rel="noopener">ZyG</a>, a Tel Aviv company building an agentic operating system for ecommerce brands. That puts me close to the question I care about most: what does it take to build a brand when AI agents do more of the discovering, comparing and recommending?</p>

      <h2>What I write about</h2>
      <p>Branding, organic growth and building brands in an agentic world. My articles have appeared in <a href="https://www.inc.com/author/rotem-gal" target="_blank" rel="noopener">Inc.</a>, <a href="https://www.entrepreneur.com/author/rotem-gal" target="_blank" rel="noopener">Entrepreneur</a>, <a href="https://www.business.com/articles/questions-before-connecting-audience-on-social-media/" target="_blank" rel="noopener">business.com</a> and <a href="https://www.referralcandy.com/author/rotemg" target="_blank" rel="noopener">ReferralCandy</a>, covering marketing, ecommerce, branding and customer behavior. The full list is on the <a href="/writing">writing page</a>.</p>
      <p>I try to share what I've learned from building and testing: what worked, what failed, and what other founders and marketers can apply.</p>

      <h2>Speaking</h2>
      <p>In November 2026 I'm speaking at <a href="https://www.becoming10x.com/" target="_blank" rel="noopener">Becoming 10x</a>, the annual summit by 10x Marketers at the Tel Aviv Cinematheque. I've also spoken at Team8 and been a guest on the Voices of Search podcast. More on the <a href="/speaking">speaking page</a>.</p>

      <h2>Questions people ask</h2>
      <div class="faq">
{faq_html}
      </div>
    </div>

    <aside class="facts">
      <img class="facts-photo" src="/images/rotem-gal-square.jpg" alt="Rotem Gal" width="1000" height="1000" loading="lazy">
      <h2>At a glance</h2>
      <dl>
        <dt>Name</dt><dd>Rotem Gal</dd>
        <dt>Based in</dt><dd>Tel Aviv, Israel</dd>
        <dt>Role</dt><dd>Director of Organic Growth, <a href="https://www.zyg.com/" target="_blank" rel="noopener">ZyG</a></dd>
        <dt>Previously</dt><dd>AI21 Labs, WalkMe</dd>
        <dt>Education</dt><dd>Netanya Academic College</dd>
        <dt>Topics</dt><dd>Branding, organic growth, agentic commerce</dd>
        <dt>Published in</dt><dd>Inc., Entrepreneur, business.com, ReferralCandy</dd>
        <dt>Languages</dt><dd>English, Hebrew</dd>
        <dt>Profiles</dt><dd><a href="https://www.linkedin.com/in/rotemgal/" target="_blank" rel="noopener me">LinkedIn</a> · <a href="https://x.com/gal_rotem" target="_blank" rel="noopener me">X</a></dd>
        <dt>Contact</dt><dd><a href="mailto:info@rotemgal.com">info@rotemgal.com</a></dd>
      </dl>
    </aside>
  </div>
</section>"""
faq_schema = {
    "@type": "FAQPage",
    "@id": f"{SITE}/about#faq",
    "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
    ],
}
pages["about.html"] = page(
    "/about", "About Rotem Gal - Director of Organic Growth at ZyG",
    SHORT_BIO, about_body, [faq_schema], page_type="ProfilePage", crumbs=[("/about", "About")],
)

# ---------- Writing ----------
groups = []
for pub in PUBLISHERS:
    items = [a for a in ARTICLES if a[0] == pub]
    cards = "\n".join(
        f"""      <a class="article" href="{a[2]}" target="_blank" rel="noopener">
        <div><div class="pub">{esc(a[0])}</div><h3>{esc(a[1])}</h3></div>
        <div class="meta"><span>{esc(a[5])}</span><span>{a[4]}</span></div>
      </a>""" for a in items
    )
    author_page = PUBLISHERS[pub][1]
    link = (f'<a class="pub-link" href="{author_page}" target="_blank" rel="noopener me">Author page on {esc(pub)} &rarr;</a>'
            if author_page else '<span class="pub-link">&nbsp;</span>')
    groups.append(f"""  <div class="pub-group">
    <h2>{esc(pub)}</h2>
    {link}
    <div class="articles">
{cards}
    </div>
  </div>""")
writing_body = f"""<section class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Writing</div>
    <h1>Published work by Rotem Gal</h1>
    <p>Articles on marketing, ecommerce, branding and customer behavior, published in Inc., Entrepreneur, business.com and ReferralCandy.</p>
  </div>
</section>
<section>
  <div class="wrap">
{chr(10).join(groups)}
  </div>
</section>"""
writing_list = {
    "@type": "ItemList",
    "@id": f"{SITE}/writing#articles",
    "name": "Articles by Rotem Gal",
    "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": article_schema(a)} for i, a in enumerate(ARTICLES)
    ],
}
pages["writing.html"] = page(
    "/writing", "Writing - Articles by Rotem Gal in Inc., Entrepreneur and more",
    "Articles by Rotem Gal on marketing, ecommerce, branding and customer behavior, published in Inc., Entrepreneur, business.com and ReferralCandy.",
    writing_body, [writing_list], page_type="CollectionPage", crumbs=[("/writing", "Writing")],
)

# ---------- Speaking ----------
TALKS = [
    ("Nov 26, 2026", "Upcoming · Summit", "Becoming 10x 2026",
     "The annual summit by 10x Marketers, a morning for marketers and GTM leaders turning AI into a practical operating system. Tel Aviv Cinematheque.",
     "https://www.becoming10x.com/#speakers"),
    ("May 7, 2025", "Talk · Team8", "Organic growth for B2B companies",
     "A session at Team8 on why organic growth still matters for B2B companies.",
     "https://www.linkedin.com/posts/rotemgal_spoke-at-team8-yesterday-about-why-seo-still-activity-7326237999241867264-Nn3J"),
    ("", "Podcast · Voices of Search", "How to Manage a Cross-Functional Team",
     "Aligning writers, developers and marketers around one growth goal.",
     "https://www.ivoox.com/en/how-to-manage-a-cross-functional-team-audios-mp3_rf_137171899_1.html"),
]
talk_html = "\n".join(
    f"""      <a class="talk" href="{u}" target="_blank" rel="noopener">
        <div class="date">{d or "&nbsp;"}</div>
        <div><div class="kind">{esc(k)}</div><h3>{esc(t)}</h3><p>{esc(p)}</p></div>
      </a>""" for d, k, t, p, u in TALKS
)
speaking_body = f"""<section class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Speaking and podcasts</div>
    <h1>Talks by Rotem Gal</h1>
    <p>Keynotes, panels and podcast conversations on branding, organic growth and how brands get chosen when AI agents do the research.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="prose"><h2>Talks and appearances</h2></div>
    <div class="talk-list">
{talk_html}
    </div>

    <div class="prose" style="margin-top:64px">
      <h2>Topics I speak about</h2>
    </div>
    <div class="topics">
      <span>Building brands in an agentic world</span>
      <span>How AI assistants decide which brands to recommend</span>
      <span>Organic growth that compounds</span>
      <span>Brand credibility and earned mentions</span>
      <span>Organic growth for B2B and ecommerce</span>
    </div>

    <div class="prose" style="margin-top:64px">
      <h2>Invite me</h2>
      <p>For conferences, panels, podcasts and internal team sessions, email <a href="mailto:info@rotemgal.com?subject=Speaking%20invitation">info@rotemgal.com</a> with the event, audience and date. Speaker bios are on the <a href="/media-kit">media kit page</a>.</p>
    </div>
  </div>
</section>"""
speaking_schema = [
    {
        "@type": "Event",
        "@id": f"{SITE}/speaking#becoming-10x-2026",
        "name": "Becoming 10x 2026",
        "description": "The annual summit by 10x Marketers.",
        "startDate": "2026-11-26",
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "location": {"@type": "Place", "name": "Tel Aviv Cinematheque",
                     "address": {"@type": "PostalAddress", "addressLocality": "Tel Aviv", "addressCountry": "IL"}},
        "organizer": {"@type": "Organization", "name": "10x Marketers", "url": "https://www.becoming10x.com/"},
        "performer": {"@id": PERSON_ID},
        "url": "https://www.becoming10x.com/",
    },
    {
        "@type": "Event",
        "@id": f"{SITE}/speaking#team8-2025",
        "name": "Organic growth for B2B companies, talk at Team8",
        "startDate": "2025-05-07",
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "location": {"@type": "Place", "name": "Team8"},
        "organizer": {"@type": "Organization", "name": "Team8", "url": "https://team8.vc/"},
        "performer": {"@id": PERSON_ID},
    },
    {
        "@type": "PodcastEpisode",
        "name": "How To Manage A Cross-Functional Team",
        "url": TALKS[2][4],
        "partOfSeries": {"@type": "PodcastSeries", "name": "Voices of Search"},
        "actor": {"@id": PERSON_ID},
    },
]
pages["speaking.html"] = page(
    "/speaking", "Speaking - Rotem Gal on Branding and Organic Growth",
    "Talks and podcast appearances by Rotem Gal on branding, organic growth and building brands in an agentic world. Speaker at Becoming 10x 2026 in Tel Aviv.",
    speaking_body, speaking_schema, page_type="CollectionPage", crumbs=[("/speaking", "Speaking")],
)

# ---------- Media kit ----------
def bio_block(label, bid, text):
    return f"""      <div class="bio-block">
        <div class="bio-label"><span>{label}</span><button data-copy="{bid}">Copy</button></div>
        <p id="{bid}">{esc(text)}</p>
      </div>"""

media_body = f"""<section class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Media kit</div>
    <h1>Bios, photos and facts</h1>
    <p>For event organizers, podcast hosts and editors. Use any of the bios below as written.</p>
  </div>
</section>
<section>
  <div class="wrap two-col">
    <div>
      <div class="prose"><h2>Bios</h2></div>
{bio_block("One line", "bio-line", "Rotem Gal is Director of Organic Growth at ZyG and writes about branding, organic growth and building brands in an agentic world.")}
{bio_block("Short", "bio-short", SHORT_BIO)}
{bio_block("Medium", "bio-medium", MEDIUM_BIO)}
{bio_block("Long", "bio-long", LONG_BIO)}

      <div class="prose" style="margin-top:48px"><h2>Photos</h2></div>
      <div class="shots">
        <a class="shot shot-img" href="/images/rotem-gal.jpg" download><img src="/images/rotem-gal-800.jpg" alt="Rotem Gal headshot" loading="lazy"><span>Download headshot</span></a>
        <div class="shot">Headshot, black and white<br>(coming soon)</div>
        <div class="shot">On stage<br>(coming soon)</div>
      </div>
    </div>
    <aside class="facts">
      <h2>Quick facts</h2>
      <dl>
        <dt>Name</dt><dd>Rotem Gal</dd>
        <dt>Title</dt><dd>Director of Organic Growth, ZyG</dd>
        <dt>Based in</dt><dd>Tel Aviv, Israel</dd>
        <dt>Topics</dt><dd>Branding, organic growth, agentic commerce</dd>
        <dt>Published in</dt><dd>Inc., Entrepreneur, business.com, ReferralCandy</dd>
        <dt>X</dt><dd><a href="https://x.com/gal_rotem" target="_blank" rel="noopener me">@gal_rotem</a></dd>
        <dt>LinkedIn</dt><dd><a href="https://www.linkedin.com/in/rotemgal/" target="_blank" rel="noopener me">in/rotemgal</a></dd>
        <dt>Contact</dt><dd><a href="mailto:info@rotemgal.com?subject=Media%20inquiry">info@rotemgal.com</a></dd>
      </dl>
    </aside>
  </div>
</section>"""
pages["media-kit.html"] = page(
    "/media-kit", "Media Kit - Rotem Gal",
    "Official bios, photos and quick facts about Rotem Gal for event organizers, podcast hosts and editors.",
    media_body, [], crumbs=[("/media-kit", "Media kit")],
)

# ---------- 404 ----------
pages["404.html"] = page(
    "/404", "Page not found - Rotem Gal", "This page does not exist.",
    """<section class="notfound"><div class="wrap">
  <div class="eyebrow">404</div>
  <h1 style="font-size:clamp(2.4rem,5vw,3.6rem);margin:16px 0">This page doesn't exist.</h1>
  <p style="color:var(--ink-2);margin-bottom:28px">Try the <a href="/">home page</a>, <a href="/writing">my writing</a> or <a href="/about">about me</a>.</p>
</div></section>""", [],
)

for name, html in pages.items():
    (ROOT / name).write_text(html)

# ---------- sitemap ----------
urls = ["/", "/about", "/writing", "/speaking", "/media-kit"]
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls)
    + "</urlset>\n"
)
print("built", ", ".join(pages))
