# PUBMED PAPER FILTERING SYSTEM 


# Overview 

This project is designed to identify and filter non-academic papers from PubMed search results. It retrieves scientific articles based on a given query, extracts metadata, and classifies papers based on author affiliations. The goal is to separate research from academic institutions and industry-affiliated organizations (e.g., biotech and pharmaceutical companies).

# Features 

✔️ Fetches research papers from PubMed using the Entrez API

✔️ Extracts title, authors, publication date, and affiliations

✔️ Identifies non-academic papers based on company-related keywords

✔️ Saves the filtered results to a structured CSV file


# How It Works

Fetch Papers: The script queries PubMed for a given topic and retrieves relevant article IDs.

Extract Metadata: Detailed information (title, authors, affiliations) is fetched for each paper.

Filter Non-Academic Papers: Affiliations are analyzed to determine if they belong to a company, biotech, or industry.

Save Results: The filtered data is stored in results.csv with columns:

- PubMed ID

- Title

- Publication Date

- Non-Academic Authors

- Company Affiliation

# Future Improvements

Enhance filtering accuracy using machine learning

Add a web-based interface for easier use

Expand the non-academic keyword list


# License

📜 MIT License – Free to use and modify
