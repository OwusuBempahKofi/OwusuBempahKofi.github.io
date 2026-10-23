import os
import json
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader




# Load JSON data
with Path("portfolio.json").open(encoding="utf-8") as f:
    data = json.load(f)



    # Add any extra context if needed
    data["current_year"] = datetime.now(tz=UTC).year



    if "social_links" in data:
        for link in data["social_links"]:
            if link.get("svg_path"):
                with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
                    link["svg_data"] = svg_file.read()

    # Set up Jinja environment
    env = Environment(loader=FileSystemLoader("."), autoescape=True)
    index_template = env.get_template("index_template.html")
    resume_template = env.get_template("resume_template.html")

    # Render the template with the data
    html_output = index_template.render(**data)
    resume_output = resume_template.render(**data)


    # Write the output to an HTML file
    with Path("index.html").open("w", encoding="utf-8") as w:
        w.write(html_output)

    with Path("resume.html").open("w", encoding="utf-8") as ww:
        ww.write(resume_output)

    print("HTML file generated successfully!")

    #print(f"Static site successfully generated in the './{BUILD_DIR}' directory!")

    # ----------------------------------------------------
    # 4. EXPORT AND DOWNLOAD THE WEBSITE AS A PDF
    # ----------------------------------------------------
    print("Compiling website structure into PDF format...")
    pdf_output_path = "website_export.pdf"

    # Initialize Weasyprint to read the generated file infrastructure
    #html_doc = HTML(filename=html_output)

    # Write the final compiled file to disk
    #html_doc.write_pdf(pdf_output_path)

    #print(f"Success! Download compiled and saved to: {os.path.abspath(pdf_output_path)}")