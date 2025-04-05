from pubmed_filter.filter_papers import is_non_academic_affiliation

def test_is_non_academic():
    assert is_non_academic_affiliation("Pfizer Inc.") == True
    assert is_non_academic_affiliation("MIT University") == False
