import sqlparse


def pretty(sql):
    """A slow query, formatted for the logs."""
    return sqlparse.format(sql, reindent=True, keyword_case="upper")
