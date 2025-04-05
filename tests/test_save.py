import os
from pubmed_filter.save_results import save_to_csv

def test_save_to_csv():
    sample_papers = [
        {"id": "12345", "title": "Cancer Study", "pubdate": "2024-01-01", 
        "non_academic_authors": [{"name": "John Doe", "affiliation": "Pfizer Inc."}]}
    ]
    
    save_to_csv(sample_papers, "test_output.csv")
    assert os.path.exists("test_output.csv")
    os.remove("test_output.csv")
