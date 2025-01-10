from fpdf import FPDF

# Replace non-ASCII characters with their ASCII equivalents
def clean_text(text):
    replacements = {
        "’": "'", "“": '"', "”": '"', "–": "-", "•": "-", "—": "-", "–": "-", "**":""
    }
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)
    return text


def competitorReport(content):
    cleaned_content = clean_text(content)

    # Create PDF instance
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    title = "Competitor Analysis Report"
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, title, ln=True, align="C")
    pdf.ln(10)

    # Write content with subtitles for sections starting with ###
    pdf.set_font("Arial", size=12)
    for line in cleaned_content.split('\n'):
        if line.startswith("###"):  # Treat lines starting with ### as subtitles
            pdf.set_font("Arial", style="B", size=12)
            temp = line[3:]
            if "Aggregate Trends" in temp:
                temp = "Aggregate Trends / Competitor Analysis"
            elif "Actionable Insights" in temp:
                temp = "Actionable Insights / Strategic Recommendations"
                
            pdf.cell(0, 10, temp, ln=True)
            pdf.ln(5)
            pdf.set_font("Arial", size=12)
        else:
            temp = line.strip(" **")
            pdf.multi_cell(0, 10, temp)

    # Save the PDF
    file_path = "CompetitorAnalysisReport.pdf"
    pdf.output(file_path)

    print(f"PDF generated successfully: {file_path}")

