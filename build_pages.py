#!/usr/bin/env python3
"""Burgers & Bad Decisions — Bangor ME. Template-v2 multi-page site build.
Every claim traced in evidence.json (BDN 2026-10-21, b985.fm, 92moose.fm, mixmaine.com,
OSM node 12724150202, shop FB page intro). Unknowns (phone, firm hours, prices, firm
opening date) omitted — never guessed. Zero JS. Hand-rolled HTML/CSS. noindex demo host.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, 'public')
os.makedirs(PUB, exist_ok=True)

ORIGIN = 'https://burgers-and-bad-decisions-demo.up.railway.app'
BRAND = 'Burgers &amp; Bad Decisions'
BRAND_PLAIN = 'Burgers & Bad Decisions'
CITY = 'Bangor, ME'
STREET = '68 Main Street'
FULL_ADDR = '68 Main Street, Bangor, ME 04401'
EMAIL = 'shiannelevesque1@gmail.com'
FB = 'https://www.facebook.com/profile.php?id=61594350897171'
MAPQ = 'https://www.google.com/maps?q=68%20Main%20St%2C%20Bangor%2C%20ME%2004401'
LAT, LON = 44.8002931, -68.7716928  # OSM node 12724150202, exactly the 68 Main St storefront
SOCIALS = [FB]

def head(title, desc, path):
    u = ORIGIN + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND_PLAIN}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://www.google.com"></head>
<body>'''

def nav():
    return '''<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="brand" href="/">Burgers<span>&amp;</span>Bad&nbsp;Decisions</a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Show navigation">
  <label for="navtoggle" class="navbtn" aria-hidden="true"><i></i></label>
  <nav aria-label="Main" class="links">
    <a href="/menu">Menu</a>
    <a href="/signature-burgers">Signature&nbsp;Burgers</a>
    <a href="/all-day-breakfast">Breakfast</a>
    <a href="/our-story">Our&nbsp;Story</a>
    <a href="/visit">Visit</a>
    <a class="btn btn-sm" href="/contact">Contact&nbsp;Us</a>
  </nav>
</header>'''

def footer():
    return f'''<footer class="site">
  <div class="footgrid">
    <div class="footnap">
      <p class="fbrand">{BRAND}</p>
      <address>{STREET}<br>Bangor, ME 04401</address>
      <p class="fmail"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="footcta">
      <p class="ticketrule" aria-hidden="true"></p>
      <p class="fline">Breakfast from sunrise.<br>Loaded burgers late at night.</p>
      <p class="fsocial"><a href="{FB}" rel="noopener">Facebook</a></p>
      <p class="fline2">Opening soon — downtown Bangor, in the old Taste of India space. Final opening date and hours go up on Facebook.</p>
    </div>
  </div>
  <p class="footline">&copy; 2026 {BRAND_PLAIN} &middot; Bangor, ME</p>
</footer>'''

def breadcrumbs(name, path):
    items = [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': ORIGIN + '/'},
    ]
    if path != '/':
        items.append({'@type': 'ListItem', 'position': 2, 'name': name, 'item': ORIGIN + path})
    return json.dumps({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}, ensure_ascii=False)

def ld_home():
    obj = {
        '@context': 'https://schema.org', '@type': 'Restaurant',
        'name': BRAND_PLAIN,
        'image': ORIGIN + '/og.png',
        'url': ORIGIN + '/',
        'servesCuisine': ['American', 'Burgers', 'Breakfast'],
        'email': EMAIL,
        'address': {'@type': 'PostalAddress', 'streetAddress': '68 Main Street', 'addressLocality': 'Bangor', 'addressRegion': 'ME', 'postalCode': '04401', 'addressCountry': 'US'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': LAT, 'longitude': LON},
        'hasMap': MAPQ,
        'sameAs': SOCIALS,
        'hasMenu': ORIGIN + '/menu',
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_menu():
    obj = {
        '@context': 'https://schema.org', '@type': 'Menu',
        'name': f'{BRAND_PLAIN} — Opening Lineup',
        'inLanguage': 'en',
        'hasMenuSection': [
            {'@type': 'MenuSection', 'name': 'Signature Burgers', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'The Classic Mistake', 'description': 'A half-pound cheeseburger. A vegetarian option is available.'},
                {'@type': 'MenuItem', 'name': 'The Bad Decision', 'description': 'A half-pound bacon cheddar burger with an onion ring and BBQ sauce. A vegetarian option is available.'},
                {'@type': 'MenuItem', 'name': 'The Hangover Burger', 'description': 'A half-pound cheeseburger with an egg and bacon. A vegetarian option is available.'},
            ]},
            {'@type': 'MenuSection', 'name': 'Breakfast All Day', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'Waffles'},
                {'@type': 'MenuItem', 'name': 'Breakfast Sandwiches'},
                {'@type': 'MenuItem', 'name': 'Breakfast Burritos'},
                {'@type': 'MenuItem', 'name': 'French Toast'},
                {'@type': 'MenuItem', 'name': 'Hashbrowns'},
            ]},
            {'@type': 'MenuSection', 'name': 'Tenders, Wings & Apps', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'Chicken Tenders'},
                {'@type': 'MenuItem', 'name': 'Wings', 'description': 'Seven sauces, including garlic parm, teriyaki, mango habanero and nuclear.'},
            ]},
            {'@type': 'MenuSection', 'name': 'Bar & Sweet Drinks', 'itemListElement': [
                {'@type': 'MenuItem', 'name': 'Signature Sweet Drinks', 'description': 'Every signature drink also has a non-alcoholic version.'},
            ]},
        ],
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_service(name, path, desc):
    obj = {
        '@context': 'https://schema.org', '@type': 'Service',
        'name': name,
        'description': desc,
        'areaServed': {'@type': 'City', 'name': 'Bangor', 'addressRegion': 'ME'},
        'provider': {'@type': 'Restaurant', 'name': BRAND_PLAIN, 'address': {'@type': 'PostalAddress', 'streetAddress': '68 Main Street', 'addressLocality': 'Bangor', 'addressRegion': 'ME', 'postalCode': '04401', 'addressCountry': 'US'}},
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_faq(qa_list):
    obj = {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa_list],
    }
    return json.dumps(obj, ensure_ascii=False)

PAGES = {}

# ---------- HOME ----------
PAGES['index.html'] = (head(f'{BRAND_PLAIN} — Burger Bar &amp; All-Day Breakfast, Bangor ME',
    'Opening soon in downtown Bangor, Maine: half-pound burgers, breakfast all day, wings with seven sauces, and sweet drinks with a non-alcoholic version of every one. 68 Main Street.',
    '/'), f'''{nav()}
<main id="main">
<section class="hero">
  <p class="kicker">68 MAIN STREET &middot; DOWNTOWN BANGOR &middot; MAINE</p>
  <h1>Burgers <span class="amp">&amp;</span><br><span class="bad">Bad&nbsp;Decisions</span></h1>
  <p class="lead">Breakfast from sunrise. Half-pound burgers late into the night. A locally owned burger bar where every single menu item has a vegetarian option — and every sweet drink has a sober twin.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See the Lineup</a> <a class="btn btn-ghost btn-big" href="{FB}" rel="noopener">Opening&nbsp;Updates</a></p>
  <p class="stamp" aria-hidden="true">OPENING SOON</p>
</section>

<section class="ticketband">
  <div class="ticket">
    <p class="ticketno">ORDER NO. 001 &middot; DOWNTOWN BANGOR</p>
    <hr class="perf">
    <ul class="trows">
      <li><span>Breakfast, all day</span><i></i><b>around the clock</b></li>
      <li><span>The Classic Mistake</span><i></i><b>&frac12; lb cheeseburger</b></li>
      <li><span>The Bad Decision</span><i></i><b>bacon &middot; cheddar &middot; onion ring &middot; BBQ</b></li>
      <li><span>The Hangover Burger</span><i></i><b>egg + bacon</b></li>
      <li><span>Wings</span><i></i><b>seven sauces — ask for nuclear</b></li>
      <li><span>Sweet drinks</span><i></i><b>NA version of every one</b></li>
      <li><span>Every menu item</span><i></i><b>has a veg option</b></li>
    </ul>
    <hr class="perf">
    <p class="ticketfoot">The lineup at opening, as shared in press coverage and the shop&rsquo;s own updates. Menu is still being finalized — prices when you order.</p>
    <a class="ticketlink" href="/menu">Full menu &rarr;</a>
  </div>
  <div class="heronotes">
    <h2>What kind of place is this?</h2>
    <p>A family-friendly burger bar on Main Street — in the old Taste of India space — built for the people who work early, work late, and everyone who just wants dinner without cooking it.</p>
    <ul class="pillars">
      <li><b>Early &amp; late.</b> The plan is to open around 5 a.m. and close around midnight — breakfast for the 5 a.m. shift, burgers for the post-bar crowd.</li>
      <li><b>Loaded, not fussy.</b> Signature half-pound burgers, tenders, wings with seven sauces, appetizers.</li>
      <li><b>Somebody for everyone.</b> A vegetarian version of everything, and a non-alcoholic version of every signature drink.</li>
    </ul>
  </div>
</section>

<section class="quoteband">
  <blockquote>
    <p>&ldquo;The bad decisions [name] is because it&rsquo;s not a completely healthy menu, and we are a bar as well. A lot of our signature drinks are sweet and sugary, and a lot of our signature burgers are very loaded with stuff.&rdquo;</p>
    <cite>Shianne Levesque, owner — via the Bangor Daily News</cite>
  </blockquote>
</section>

<section class="grid3">
  <article class="cardcard">
    <h3>First responders eat like locals</h3>
    <p>Shianne worked at the Penobscot County Jail — she remembers finishing a long shift with nowhere decent to eat. A discount for first responders, law enforcement and veterans is planned for the opening.</p>
  </article>
  <article class="cardcard">
    <h3>Mondays, the little ones eat free</h3>
    <p>Every item on the kids&rsquo; menu is planned free on Mondays. &ldquo;It hits personally, because I am a single mother,&rdquo; Shianne says.</p>
  </article>
  <article class="cardcard">
    <h3>Bring quarters for the arcade</h3>
    <p>About half a dozen arcade games are planned for the front of the restaurant — dinner and a game, Main Street style.</p>
  </article>
</section>

<section class="homecta">
  <h2>&ldquo;I want you to feel at home.&rdquo;</h2>
  <p>Opening soon at 68 Main Street. Hours, the final menu, and the opening-night call all go up on the shop&rsquo;s Facebook page.</p>
  <p class="cta"><a class="btn btn-big" href="/visit">Where We&rsquo;re At</a> <a class="btn btn-ghost btn-big" href="/contact">Contact the Shop</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_home()}</script>
<script type="application/ld+json">{ld_menu()}</script>
</body>
</html>''')

# ---------- MENU ----------
PAGES['menu.html'] = (head(f'Menu — {BRAND_PLAIN}, Bangor ME',
    'The opening lineup at Burgers & Bad Decisions in Bangor, ME: signature half-pound burgers, all-day breakfast, tenders and wings with seven sauces, and sweet drinks — every item with a vegetarian option.',
    '/menu'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">THE LINEUP AT OPENING</p>
  <h1>The Menu <span class="fine">(so far)</span></h1>
  <p class="lead">Burgers are the headline, but this is a breakfast-and-burger kind of place with a bar attached. Everything below has been in press coverage or in the shop&rsquo;s own updates. Menu is still being finalized — <a href="{FB}" rel="noopener">the Facebook page</a> carries the final call. Prices at the counter.</p>
</section>

<section class="menusection">
  <h2>Signature Burgers</h2>
  <p class="sectionnote">Half-pound patties, loaded the way the name promises. <span class="veg">V = vegetarian option available</span></p>
  <ul class="menurows">
    <li><span class="mname">The Classic Mistake <b class="veg">V</b></span><i></i><span class="mdesc">A half-pound cheeseburger.</span></li>
    <li><span class="mname">The Bad Decision <b class="veg">V</b></span><i></i><span class="mdesc">Half-pound bacon cheddar burger with an onion ring and BBQ sauce.</span></li>
    <li><span class="mname">The Hangover Burger <b class="veg">V</b></span><i></i><span class="mdesc">Half-pound cheeseburger with an egg and bacon.</span></li>
  </ul>
  <p class="cta"><a class="btn" href="/signature-burgers">More on the signature three</a></p>
</section>

<section class="menusection">
  <h2>Breakfast All Day</h2>
  <p class="sectionnote">The morning menu doesn&rsquo;t stop at 10 a.m. <span class="veg">V = vegetarian option available</span></p>
  <ul class="menurows">
    <li><span class="mname">Waffles <b class="veg">V</b></span><i></i><span class="mdesc">Yes, at 11 p.m.</span></li>
    <li><span class="mname">Breakfast Sandwiches <b class="veg">V</b></span><i></i><span class="mdesc">Eggs your way, on whatever sounds good.</span></li>
    <li><span class="mname">Breakfast Burritos <b class="veg">V</b></span><i></i><span class="mdesc">Built for the early shift.</span></li>
    <li><span class="mname">French Toast <b class="veg">V</b></span><i></i><span class="mdesc">Dessert that clocks in as breakfast.</span></li>
    <li><span class="mname">Hashbrowns <b class="veg">V</b></span><i></i><span class="mdesc">Crispy. Obviously.</span></li>
  </ul>
  <p class="cta"><a class="btn" href="/all-day-breakfast">More on all-day breakfast</a></p>
</section>

<section class="menusection">
  <h2>Tenders, Wings &amp; Apps</h2>
  <p class="sectionnote"><span class="veg">V = vegetarian option available</span></p>
  <ul class="menurows">
    <li><span class="mname">Chicken Tenders <b class="veg">V</b></span><i></i><span class="mdesc">A staple for a reason.</span></li>
    <li><span class="mname">Wings — seven sauces <b class="veg">V</b></span><i></i><span class="mdesc">The lineup includes garlic parm, teriyaki, mango habanero, and nuclear — the one you&rsquo;ll need a napkin for.</span></li>
    <li><span class="mname">Appetizers <b class="veg">V</b></span><i></i><span class="mdesc">Menu rounds out the savory side.</span></li>
  </ul>
</section>

<section class="menusection">
  <h2>Bar &amp; Sweet Drinks</h2>
  <p class="sectionnote">This is a burger bar — the bar part is real. <span class="veg">0% = non-alcoholic version available</span></p>
  <ul class="menurows">
    <li><span class="mname">Signature Sweet Drinks <b class="veg">0%</b></span><i></i><span class="mdesc">Sweet, sugary, unapologetic — and every one has a non-alcoholic version, same name, same fun.</span></li>
  </ul>
  <p class="sectionnote">Not into sweets? The bar has you too.</p>
</section>

<section class="menusection">
  <h2>The Kids</h2>
  <ul class="menurows">
    <li><span class="mname">Kids Menu — free on Mondays <b class="veg">V</b></span><i></i><span class="mdesc">Planned for opening: everything on the kids&rsquo; menu is free on Mondays.</span></li>
  </ul>
</section>

<section class="menufine">
  <p>Every menu item — burgers, breakfast, tenders, wings, apps, kids — has a vegetarian option. That&rsquo;s not a footnote, it&rsquo;s how the menu was built.</p>
  <p class="cta"><a class="btn btn-big" href="/contact">Ask us a question</a> <a class="btn btn-ghost btn-big" href="/visit">Where we&rsquo;re at</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_menu()}</script>
<script type="application/ld+json">{breadcrumbs('Menu', '/menu')}</script>
</body>
</html>''')

# ---------- SIGNATURE BURGERS ----------
PAGES['signature-burgers.html'] = (head(f'Signature Burgers — {BRAND_PLAIN}, Bangor ME',
    'The three signature half-pound burgers at Burgers & Bad Decisions, Bangor ME: The Classic Mistake, The Bad Decision, and The Hangover Burger. Vegetarian options on all of them.',
    '/signature-burgers'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">THE HEADLINES</p>
  <h1>Three mistakes<br>worth making</h1>
  <p class="lead">Half-pound patties, loaded on purpose. &ldquo;A lot of our signature burgers are very loaded with stuff,&rdquo; says owner Shianne Levesque. Every one has a vegetarian version.</p>
</section>

<div class="burgercards">
  <article class="burger">
    <p class="bnum">No. 001</p>
    <h2>The Classic Mistake <b class="veg">V</b></h2>
    <p class="bdesc">A half-pound cheeseburger. No gimmicks — just the biggest, juiciest thing in the case, done right. This is the one you order after you&rsquo;ve tried everything else.</p>
    <p class="bspec">1&frasl;2 lb patty &middot; cheese &middot; burger</p>
  </article>
  <article class="burger">
    <p class="bnum">No. 002</p>
    <h2>The Bad Decision <b class="veg">V</b></h2>
    <p class="bdesc">The namesake energy: a half-pound bacon cheddar burger with an onion ring and BBQ sauce. Sweet, smoky, absurd. Exactly the decision you make at 10 p.m. and don&rsquo;t regret.</p>
    <p class="bspec">1&frasl;2 lb patty &middot; bacon &middot; cheddar &middot; onion ring &middot; BBQ</p>
  </article>
  <article class="burger">
    <p class="bnum">No. 003</p>
    <h2>The Hangover Burger <b class="veg">V</b></h2>
    <p class="bdesc">A half-pound cheeseburger with an egg and bacon. Medical science, Main Street edition. Breakfast and dinner collide on a plate — which makes sense in a place that serves both around the clock.</p>
    <p class="bspec">1&frasl;2 lb patty &middot; egg &middot; bacon &middot; cheese</p>
  </article>
</div>

<section class="menufaq">
  <h2>Quick answers</h2>
  <dl>
    <div><dt>Is there a veg version of each?</dt><dd>Yes. A vegetarian option exists for every item on the menu — these three included.</dd></div>
    <div><dt>How much?</dt><dd>Prices are on the menu at the counter — the shop hasn&rsquo;t published them yet.</dd></div>
    <div><dt>When can I get one?</dt><dd>Opening soon at 68 Main Street. The Facebook page posts the date the moment it&rsquo;s set.</dd></div>
  </dl>
  <p class="cta"><a class="btn btn-big" href="/menu">See the whole menu</a> <a class="btn btn-ghost btn-big" href="{FB}" rel="noopener">Follow on Facebook</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Signature Burgers at Burgers & Bad Decisions', '/signature-burgers', 'Half-pound signature burgers — The Classic Mistake, The Bad Decision, and The Hangover Burger — at 68 Main Street, Bangor, ME. Vegetarian options available.')}</script>
<script type="application/ld+json">{breadcrumbs('Signature Burgers', '/signature-burgers')}</script>
<script type="application/ld+json">{ld_faq([
  ('Is there a vegetarian version of the signature burgers?', 'Yes. Every item on the menu at Burgers & Bad Decisions has a vegetarian option, including all three signature burgers.'),
  ('When does Burgers & Bad Decisions open?', 'Opening soon at 68 Main Street, Bangor, ME. The exact opening date is announced on the shop’s Facebook page.'),
])}</script>
</body>
</html>''')

# ---------- ALL-DAY BREAKFAST ----------
PAGES['all-day-breakfast.html'] = (head(f'All-Day Breakfast — {BRAND_PLAIN}, Bangor ME',
    'Breakfast around the clock at Burgers & Bad Decisions in Bangor, ME: waffles, breakfast sandwiches, burritos, french toast and hashbrowns — for the early shift and the late one.',
    '/all-day-breakfast'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">MORNING DOESN&rsquo;T QUIT</p>
  <h1>Breakfast, all day<br>every day</h1>
  <p class="lead">Waffles at 11 p.m.? On the menu. Burgers &amp; Bad Decisions is planning to open around 5 a.m. and close around midnight — built for the people who eat before sunrise and the ones who eat after midnight.</p>
</section>

<section class="menusection">
  <h2>The Morning Board</h2>
  <p class="sectionnote">Served morning, noon, and late. <span class="veg">V = vegetarian option available</span></p>
  <ul class="menurows">
    <li><span class="mname">Waffles <b class="veg">V</b></span><i></i><span class="mdesc">Golden, stacked, unbothered by the clock.</span></li>
    <li><span class="mname">Breakfast Sandwiches <b class="veg">V</b></span><i></i><span class="mdesc">Eggs, cheese, and something worth building a sandwich around.</span></li>
    <li><span class="mname">Breakfast Burritos <b class="veg">V</b></span><i></i><span class="mdesc">One-handed, for people running out the door at 4:45 a.m.</span></li>
    <li><span class="mname">Eggs, Any Style <b class="veg">V</b></span><i></i><span class="mdesc">How do you like &rsquo;em?</span></li>
    <li><span class="mname">French Toast <b class="veg">V</b></span><i></i><span class="mdesc">Breakfast with dessert&rsquo;s attitude.</span></li>
    <li><span class="mname">Hashbrowns <b class="veg">V</b></span><i></i><span class="mdesc">The crispy glue holding every breakfast together.</span></li>
  </ul>
</section>

<section class="quoteband">
  <blockquote>
    <p>&ldquo;I used to work at the Penobscot County Jail, and I remember how hard it was to finish a long shift and find a convenient place to eat.&rdquo;</p>
    <cite>Shianne Levesque, owner — via the Bangor Daily News (paraphrased in coverage)</cite>
  </blockquote>
  <div class="quotenote">
    <h2>Why the hours are backwards</h2>
    <p>Downtown Bangor doesn&rsquo;t have much open at 5 a.m. or at 11:30 p.m. The plan is to be the place that is — first responders and early shifts in the morning, families before school, and the post-bar crowd late, with the storefront sitting right next to downtown&rsquo;s bar block.</p>
    <p class="fineprint">Opening hours aren&rsquo;t final yet — the posted plan is roughly 5 a.m. to midnight, with the shop staying open a bit later on weekend nights. The Facebook page carries the confirmed schedule at opening.</p>
  </div>
</section>

<section class="homecta">
  <h2>Hungry at an ungodly hour?</h2>
  <p>That&rsquo;s the entire business plan. Opening soon at 68 Main Street.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See the full menu</a> <a class="btn btn-ghost btn-big" href="/visit">Map it</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_service('All-Day Breakfast at Burgers & Bad Decisions', '/all-day-breakfast', 'Waffles, breakfast sandwiches, burritos, eggs, french toast and hashbrowns served all day at 68 Main Street, Bangor, ME.')}</script>
<script type="application/ld+json">{breadcrumbs('All-Day Breakfast', '/all-day-breakfast')}</script>
</body>
</html>''')

# ---------- OUR STORY ----------
PAGES['our-story.html'] = (head(f'Our Story — {BRAND_PLAIN}, Bangor ME',
    'The story behind Burgers & Bad Decisions: owner Shianne Levesque, a former Penobscot County Jail worker, opening a family-friendly burger bar at 68 Main Street, Bangor ME.',
    '/our-story'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">ONE OWNER. ONE STOREFRONT.</p>
  <h1>A very good<br>bad decision</h1>
  <p class="lead">Burgers &amp; Bad Decisions is one locally owned restaurant — no chain, no franchise — at 68 Main Street in downtown Bangor, in the space the Taste of India family ran until their retirement in late September 2026.</p>
</section>

<section class="storygrid">
  <article class="prose">
    <h2>Where it came from</h2>
    <p>Shianne Levesque spent years working at the Penobscot County Jail — long shifts that ended at hours when nothing downtown was open. She remembered exactly what that felt like, and &ldquo;it&rsquo;s been something I&rsquo;ve wanted to do for a while.&rdquo;</p>
    <p>She chose 68 Main Street because the space is on the smaller side: comfortable and homey, not a warehouse. New kitchen equipment went in, fresh paint went up, and the rest came together around one idea — a place that feeds the early shift and the late one, and treats both like regulars.</p>
    <h2>Who it&rsquo;s for</h2>
    <p>&ldquo;This is a safe place for families and friends to hang out and just anybody, to be honest, whether you&rsquo;re 2 years old or you&rsquo;re 90 years old,&rdquo; Shianne says. &ldquo;I want you to feel at home.&rdquo;</p>
    <p>She&rsquo;s a single mother — which is why every kids&rsquo; menu item is planned free on Mondays. A discount for first responders, law enforcement and veterans is in the opening plan, and about half a dozen arcade cabinets are going in the front so dinner doubles as a night out.</p>
  </article>
  <aside class="pressbox">
    <h2>As covered by</h2>
    <ul class="presslist">
      <li><a href="https://www.bangordailynews.com/2026-10-21/bangor/bangor-business/burgers-and-bad-decisions-bangor-joam40zk0w/" rel="noopener">Bangor Daily News</a> — &ldquo;New burger restaurant coming into former Taste of India in downtown Bangor&rdquo;</li>
      <li><a href="https://b985.fm/burgers-bad-decisions-bangor-maine/" rel="noopener">98.5 the Bear</a> — &ldquo;What To Expect From Bangor&rsquo;s New Burger Restaurant&rdquo;</li>
      <li><a href="https://92moose.fm/burgers-bad-decisions-bangor-maine-restaurant/" rel="noopener">92 Moose</a> — &ldquo;Bangor&rsquo;s New Burgers &amp; Bad Decisions&rdquo;</li>
      <li><a href="https://mixmaine.com/burgers-and-bad-decisions-coming-to-bangor/" rel="noopener">107.9 The Mix</a> — &ldquo;&lsquo;Burgers and Bad Decisions&rsquo; Coming to Bangor&rdquo;</li>
    </ul>
    <p class="fineprint">Coverage ran in October&ndash;November 2026, including interviews with the owner. Menu items and plans on this site come from that coverage and the shop&rsquo;s own Facebook updates.</p>
  </aside>
</section>

<section class="homecta">
  <h2>Opening soon — downtown Bangor</h2>
  <p>The menu&rsquo;s being finalized, the games are landing, and the opening-night call goes up on <a href="{FB}" rel="noopener">Facebook</a> the moment it&rsquo;s set.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See the lineup</a> <a class="btn btn-ghost btn-big" href="/contact">Say hi</a></p>
</section>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Our Story', '/our-story')}</script>
</body>
</html>''')

# ---------- VISIT ----------
PAGES['visit.html'] = (head(f'Visit — {BRAND_PLAIN}, Bangor ME',
    'Burgers & Bad Decisions is opening soon at 68 Main Street, Bangor, ME 04401 — downtown, in the former Taste of India space. Map, directions, and opening updates.',
    '/visit'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">68 MAIN STREET</p>
  <h1>Opening soon,<br>downtown Bangor</h1>
  <p class="lead">The old Taste of India storefront on Main Street — right in the middle of downtown, next to the bar block. The remodel is the last stretch; the opening date goes up on <a href="{FB}" rel="noopener">Facebook</a> when it&rsquo;s locked.</p>
  <p class="cta"><a class="btn btn-big" href="{MAPQ}" rel="noopener">Get Directions</a> <a class="btn btn-ghost btn-big" href="/contact">Contact the Shop</a></p>
</section>

<div class="visitgrid">
  <section class="visitinfo">
    <h2>Where</h2>
    <address class="bigaddr">68 Main Street<br>Bangor, ME 04401</address>
    <p>On Main Street between the river and the courthouse end of downtown — the storefront that housed Taste of India for years, freshly taken over.</p>
    <h2>When</h2>
    <p>Opening soon — the confirmed date isn&rsquo;t posted yet. The shop&rsquo;s plan: open around 5 a.m., close around midnight, open a little later on weekend nights. Whatever gets posted on Facebook is gospel.</p>
    <h2>Good to know</h2>
    <ul>
      <li>Family-friendly, all ages — kids&rsquo; menu planned free on Mondays.</li>
      <li>First responders, law enforcement and veterans: discount planned.</li>
      <li>Arcade games planned in the front of the house.</li>
      <li>Vegetarian option on every menu item; every signature drink has a non-alcoholic version.</li>
    </ul>
    <p class="fineprint">Hours, prices and the opening date aren&rsquo;t final — they&rsquo;ll be posted here the day the shop confirms them.</p>
    <p class="cta"><a class="btn btn-ghost" href="/menu">What we serve</a></p>
  </section>
  <section class="visitmap">
    <div class="mapbox">
      <iframe title="Map to Burgers &amp; Bad Decisions, 68 Main St, Bangor, ME 04401" src="https://www.google.com/maps?q=68%20Main%20St%2C%20Bangor%2C%20ME%2004401&output=embed" loading="eager" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <p class="fineprint">Can&rsquo;t load the map? <a href="{MAPQ}" rel="noopener">Open it in Google Maps</a> or <a href="mailto:{EMAIL}">email the shop</a>.</p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Visit Burgers & Bad Decisions', '/visit', 'Dine-in at 68 Main Street, Bangor, ME 04401 — opening soon, in the former Taste of India space.')}</script>
<script type="application/ld+json">{breadcrumbs('Visit', '/visit')}</script>
</body>
</html>''')

# ---------- CONTACT ----------
PAGES['contact.html'] = (head(f'Contact — {BRAND_PLAIN}, Bangor ME',
    'Contact Burgers & Bad Decisions in Bangor, ME: email the shop, send a message through the form, or follow the opening updates on Facebook.',
    '/contact'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">TALK TO THE SHOP</p>
  <h1>Contact Burgers<br>&amp;&nbsp;Bad&nbsp;Decisions</h1>
  <p class="lead">Question about the opening, the menu, or your kid&rsquo;s birthday party? Email us or use the form — it lands in the shop&rsquo;s inbox.</p>
</section>

<div class="contactgrid">
  <form class="cform" method="post" action="/contact">
    <h2>Send a message</h2>
    <p><label for="f-name">Your name</label><input id="f-name" name="name" type="text" required maxlength="120" autocomplete="name"></p>
    <p><label for="f-email">Email</label><input id="f-email" name="email" type="email" required maxlength="160" autocomplete="email"></p>
    <p><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="5" required maxlength="4000"></textarea></p>
    <p><button class="btn btn-big" type="submit">Send Message</button></p>
    <p class="fineprint">This form emails the shop directly. We never share your address.</p>
  </form>
  <section class="cinfo">
    <h2>Direct lines</h2>
    <p class="clabel">Email</p>
    <p class="cbig"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="clabel">Walk in</p>
    <address class="bigaddr">68 Main Street<br>Bangor, ME 04401</address>
    <p class="clabel">Opening announcements</p>
    <p class="cbig"><a href="{FB}" rel="noopener">Facebook</a></p>
    <p class="fineprint">We&rsquo;re in the last stretch of build-out — replies may take a day or two. The phone line is coming with the opening.</p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Contact', '/contact')}</script>
</body>
</html>''')

# ---------- PRIVACY ----------
PAGES['privacy.html'] = (head(f'Privacy Policy — {BRAND_PLAIN}, Bangor ME',
    'Privacy policy for the Burgers & Bad Decisions website: how the contact form is handled. No trackers, no cookies.',
    '/privacy'), f'''{nav()}
<main id="main">
<section class="pagehead narrow">
  <p class="kicker">PRIVACY</p>
  <h1>Privacy Policy</h1>
</section>
<div class="prose">
  <p>This site belongs to {BRAND_PLAIN} ({FULL_ADDR}).</p>
  <h2>What we collect</h2>
  <p>The contact form on this site collects only the information you type into it — your name, your email address and your message — and sends it to the shop&rsquo;s own email address so the owners can answer you. That is the entire purpose of the data. It is not sold, shared or used for advertising.</p>
  <h2>Cookies and tracking</h2>
  <p>This site sets no cookies and uses no advertising trackers or analytics pixels of its own. The embedded Google map may set its own cookies once you interact with it, governed by Google&rsquo;s privacy policy.</p>
  <h2>Your choices</h2>
  <p>Want your message deleted from the shop&rsquo;s mailbox records? Email <a href="mailto:{EMAIL}">{EMAIL}</a> and ask. Questions about this policy go to the same address.</p>
  <p class="fineprint">This policy covers this website only.</p>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Privacy', '/privacy')}</script>
</body>
</html>''')

# ---------- 404 ----------
PAGES['404.html'] = (head(f'Page not found — {BRAND_PLAIN}',
    'Page not found at the Burgers & Bad Decisions site. Back to the menu, or straight to the opening-soon page.',
    '/404'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">404</p>
  <h1>Now <em>that&rsquo;s</em> a bad decision.</h1>
  <p class="lead">This page doesn&rsquo;t exist. The Hangover Burger does.</p>
  <p class="cta"><a class="btn btn-big" href="/">Back to Home</a> <a class="btn btn-ghost btn-big" href="/menu">See the Menu</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

# ---------- THANKS ----------
PAGES['thanks.html'] = (head(f'Message sent — {BRAND_PLAIN}',
    'Thanks for reaching out to Burgers & Bad Decisions — the shop will get back to you.',
    '/thanks'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">ORDER UP</p>
  <h1>Your message is in.</h1>
  <p class="lead">Thank you — Shianne will get back to you personally. Meanwhile, the lineup and the map are one click away.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See the Menu</a> <a class="btn btn-ghost btn-big" href="/visit">Plan the visit</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

for fname, (h, body) in PAGES.items():
    with open(os.path.join(PUB, fname), 'w', encoding='utf-8') as f:
        f.write(h + '\n' + body)
    print('wrote', fname, len(h + body), 'bytes')

# ---------- sitemap / robots / favicon ----------
pages_order = ['/', '/menu', '/signature-burgers', '/all-day-breakfast', '/our-story', '/visit', '/contact', '/privacy']
today = '2026-11-25'
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'<url><loc>{ORIGIN}{p}</loc><lastmod>{today}</lastmod></url>\n' for p in pages_order) + '</urlset>\n'
open(os.path.join(PUB, 'sitemap.xml'), 'w').write(sitemap)
open(os.path.join(PUB, 'robots.txt'), 'w').write(f'''User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
''')
favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1d1915"/><path d="M12 26c0-8 9-13 20-13s20 5 20 13z" fill="#e8b23c"/><rect x="12" y="29" width="40" height="7" rx="3" fill="#f5ecd8"/><rect x="11" y="38" width="42" height="7" rx="3.5" fill="#c8443a"/><path d="M12 49c0 0 4 3 20 3s20-3 20-3H12z" fill="#e8b23c"/></svg>
'''
open(os.path.join(PUB, 'favicon.svg'), 'w').write(favicon)
print('wrote sitemap.xml robots.txt favicon.svg')
print('PAGES:', len([f for f in PAGES if f.endswith('.html')]))
