def is_non_academic(affiliation):
    """Check if an affiliation belongs to a company (non-academic)."""
    keywords = [
        "Inc", "Ltd", "LLC", "Corp", "Company", "Corporation",
        "Biotech", "Pharmaceutical", "Technology", "Therapeutics", 
        "Diagnostics", "Biomedical", "Healthcare", "Research Institute"
    ]

    if affiliation:
        affiliation_lower = affiliation.lower()
        return any(keyword.lower() in affiliation_lower for keyword in keywords)
    return False  # Return False if affiliation is empty


def filter_papers(papers):
    """Filters out non-academic papers based on affiliations."""
    non_academic_papers = []

    for paper in papers:
        print(f"\n🔍 Checking Paper ID: {paper.get('paper_id', 'Unknown')}")  # Debugging

        for author in paper.get("authors", []):
            affiliation = author.get("affiliation", "")

            print(f"   🔹 Checking Affiliation: {affiliation}")  # Debugging

            if is_non_academic(affiliation):
                print(f"   ✅ Non-Academic Affiliation Found: {affiliation}")  # Debugging
                non_academic_papers.append(paper)
                break  # Stop checking if we found at least one non-academic author

    return non_academic_papers
