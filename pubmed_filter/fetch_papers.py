import requests # type: ignore
import time
import xml.etree.ElementTree as ET
import csv

def fetch_papers(query, max_results=10):
    """Fetches paper IDs from PubMed based on a search query."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch data from PubMed API")
    
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    
    print(f"🔹 Retrieved Paper IDs: {paper_ids}")  # Debugging line

    return paper_ids

def get_paper_details(paper_id):
    """Fetches full article details, including author affiliations, title, and publication date."""
    
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "xml"
    }
    
    response = requests.get(fetch_url, params=fetch_params)
    time.sleep(0.5)  # Prevent API rate limiting

    if response.status_code != 200:
        print(f"⚠️ Error fetching data for PubMed ID {paper_id}")
        return None
    
    root = ET.fromstring(response.text)
    paper_data = {"paper_id": paper_id, "title": "N/A", "pub_date": "N/A", "authors": []}

    # Extract Title
    title_element = root.find(".//ArticleTitle")
    if title_element is not None:
        paper_data["title"] = title_element.text

    # Extract Publication Date
    pub_year = root.find(".//PubDate/Year")
    pub_month = root.find(".//PubDate/Month")
    pub_day = root.find(".//PubDate/Day")

    if pub_year is not None:
        paper_data["pub_date"] = f"{pub_day.text if pub_day is not None else ''}-{pub_month.text if pub_month is not None else ''}-{pub_year.text}"

    # Extract Authors & Affiliations
    for author in root.findall(".//Author"):
        last_name = author.find("LastName")
        affiliation = author.find("AffiliationInfo/Affiliation")
        
        if last_name is not None and affiliation is not None:
            author_data = {"name": last_name.text, "affiliation": affiliation.text}
            paper_data["authors"].append(author_data)

    # 🔹 Debugging Output:
    print(f"📄 Extracted Data for {paper_id}: {paper_data}")
    
    return paper_data


def is_non_academic(affiliation):
    """Determines if an affiliation is non-academic."""
    non_academic_keywords = ["Inc.", "Ltd.", "LLC", "GmbH", "Corp.", "Pvt", "Company", "Biotech", "Pharmaceutical", "Therapeutics"]
    
    if any(keyword in affiliation for keyword in non_academic_keywords):
        return True
    return False



    
def extract_publication_date(xml_data):
    """Extracts publication date from XML response."""
    root = ET.fromstring(xml_data)
    
    # Look for different possible locations for publication date
    pub_date_paths = [
        ".//PubDate",
        ".//JournalIssue/PubDate",
        ".//MedlineCitation/Article/Journal/JournalIssue/PubDate"
    ]

    for path in pub_date_paths:
        pub_date_element = root.find(path)
        if pub_date_element is not None:
            year = pub_date_element.find("Year")
            month = pub_date_element.find("Month")
            day = pub_date_element.find("Day")

            # Constructing the final date
            date_parts = [year.text if year is not None else "N/A",
                        month.text if month is not None else "N/A",
                        day.text if day is not None else ""]

            extracted_date = "-".join([part for part in date_parts if part])  # Remove empty values
            
            # 🔹 Debugging Output:
            print(f"Extracted Date: {extracted_date}")
            return extracted_date

    return "N/A"
