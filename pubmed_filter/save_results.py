import csv
from pubmed_filter.filter_papers import is_non_academic

def save_to_csv(papers, filename="results.csv"):
    """Save filtered papers to CSV format."""
    print(f"📌 DEBUG: Saving {len(papers)} papers to {filename}")  # print

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["PubMed ID", "Title", "Publication Date", "Non-Academic Authors", "Company Affiliation"])

        for paper in papers:
            pubmed_id = paper.get("paper_id", "N/A")
            title = paper.get("title", "N/A")
            pub_date = paper.get("pub_date", "N/A")

            # Extract non-academic authors
            non_academic_authors = []
            company_affiliations = []

            for author in paper.get("authors", []):
                affiliation = author.get("affiliation", "").strip()
                if is_non_academic(affiliation):
                    non_academic_authors.append(author.get("name", "Unknown"))
                    company_affiliations.append(affiliation)

            # Debugging Print
            print(f"📌 SAVING TO CSV: {pubmed_id}, {title}, {pub_date}, {non_academic_authors}, {company_affiliations}")

            writer.writerow([pubmed_id, title, pub_date, "; ".join(non_academic_authors), "; ".join(company_affiliations)])

    print(f" Results saved to {filename}")
    

