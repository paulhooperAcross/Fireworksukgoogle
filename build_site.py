import os
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = ROOT / "pages"
OUTPUT = ROOT / "public"

OUTPUT.mkdir(exist_ok=True)

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset=\"utf-8\">
  <title>{title}</title>
  <meta name=\"description\" content=\"Find {title} events, times and locations. Updated for 2026.\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
</head>
<body>
  <nav><a href=\"/index.html\">Home</a></nav>
  <h1>{title}</h1>
  <div>{content}</div>
  <hr>
  <h3>Other locations</h3>
  <ul>
    {links}
  </ul>
</body>
</html>
"""

pages = []

for md_file in PAGES.glob("*.md"):
    name = md_file.stem
    title = name.replace("-", " ").title()
    content = md_file.read_text()

    pages.append((name, title, content))

# build pages with internal linking
for name, title, content in pages:
    other_links = ""
    for n, t, _ in pages:
        if n != name:
            other_links += f'<li><a href="/{n}.html">{t}</a></li>'

    html = TEMPLATE.format(title=title, content=content, links=other_links)

    (OUTPUT / f"{name}.html").write_text(html)

# index page
index_html = "<h1>Find Fireworks Near You (UK 2026)</h1><ul>"
for name, title, _ in pages:
    index_html += f'<li><a href="/{name}.html">{title}</a></li>'
index_html += "</ul>"

(OUTPUT / "index.html").write_text(index_html)

# sitemap
sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
sitemap += "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"

for name, _, _ in pages:
    sitemap += f"  <url><loc>https://fireworksuk.co.uk/{name}.html</loc></url>\n"

sitemap += "</urlset>"

(OUTPUT / "sitemap.xml").write_text(sitemap)

print("Site built with SEO + internal linking → public/")

# commit hint:
# git add .
# git commit -m "SEO build system with internal linking"
# git push

# run:
# python3 build_site.py

# Cloudflare:
# build command: python3 build_site.py
# output: public

# End

