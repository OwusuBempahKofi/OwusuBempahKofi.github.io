import os
from jinja2 import Template
from weasyprint import HTML, CSS

# ----------------------------------------------------
# 1. SETUP STRUCTURE & CONFIGURATION
# ----------------------------------------------------
# Define output directories
BUILD_DIR = "dist"
STATIC_DIR = os.path.join(BUILD_DIR, "static")

os.makedirs(STATIC_DIR, exist_ok=True)

# Sample dynamic data for the static website
website_content = {
    "site_title": "Corporate Annual Report",
    "author": "Acme Corporation",
    "pages": [
        {
            "id": "home",
            "title": "Executive Summary",
            "body": "Welcome to the Acme Annual Report. This year we achieved milestone growths across all sectors, driven by our transition to fully automated workflows and sustainable infrastructure.",
        },
        {
            "id": "performance",
            "title": "Financial Performance",
            "body": "Our revenue grew by 24% year-over-year. Operating margins optimized by 12% following targeted architectural enhancements to our production systems.",
        },
    ],
}

# ----------------------------------------------------
# 2. DEFINE THE HTML & CSS TEMPLATES
# ----------------------------------------------------
# HTML layout using Jinja2 formatting
html_template_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ site_title }}</title>
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    {% for page in pages %}
    <div class="web-page" id="{{ page.id }}">
        <header>
            <span class="site-meta">{{ site_title }}</span>
            <span class="author-meta">{{ author }}</span>
        </header>

        <main>
            <h1>{{ page.title }}</h1>
            <p>{{ page.body }}</p>
        </main>

        <footer>
            <p>Confidential & Proprietary — Page {{ loop.index }}</p>
        </footer>
    </div>
    {% endfor %}
</body>
</html>
"""

# Global style rules that handle standard web view and PDF print layout
css_style_string = """
/* --- General Web Styling --- */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: #333333;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f6f9;
}

.web-page {
    background: #ffffff;
    max-width: 800px;
    margin: 30px auto;
    padding: 40px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border-radius: 8px;
}

header {
    display: flex;
    justify-content: space-between;
    border-bottom: 2px solid #0056b3;
    padding-bottom: 10px;
    margin-bottom: 30px;
    font-size: 0.85em;
    color: #666;
}

h1 {
    color: #0056b3;
    font-size: 2em;
}

footer {
    margin-top: 40px;
    border-top: 1px solid #e0e0e0;
    padding-top: 10px;
    font-size: 0.8em;
    color: #999;
    text-align: center;
}

/* --- PDF/Print Specific Media Rules --- */
@media print {
    body {
        background-color: #ffffff;
    }
    .web-page {
        margin: 0;
        padding: 0;
        box-shadow: none;
        page-break-after: always; /* Forces each website section onto a new PDF page */
    }

    /* Configures global PDF sheet specs via WeasyPrint */
    @page {
        size: A4;
        margin: 20mm;
    }
}
"""

# ----------------------------------------------------
# 3. BUILD THE STATIC WEBSITE
# ----------------------------------------------------
print("Building static website files...")

# Render HTML using Jinja2
template = Template(html_template_string)
rendered_html = template.render(website_content)

# Save the index.html and style.css target paths
html_file_path = os.path.join(BUILD_DIR, "index.html")
css_file_path = os.path.join(STATIC_DIR, "style.css")

with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(rendered_html)

with open(css_file_path, "w", encoding="utf-8") as f:
    f.write(css_style_string)

print(f"Static site successfully generated in the './{BUILD_DIR}' directory!")

# ----------------------------------------------------
# 4. EXPORT AND DOWNLOAD THE WEBSITE AS A PDF
# ----------------------------------------------------
print("Compiling website structure into PDF format...")
pdf_output_path = "website_export.pdf"

# Initialize Weasyprint to read the generated file infrastructure
html_doc = HTML(filename=html_file_path)

# Write the final compiled file to disk
html_doc.write_pdf(pdf_output_path)

print(f"Success! Download compiled and saved to: {os.path.abspath(pdf_output_path)}")
