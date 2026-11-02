from search.sql import pretty


def test_keywords_are_upper_case():
    assert pretty("select id from docs where id = 1").startswith("SELECT id")
