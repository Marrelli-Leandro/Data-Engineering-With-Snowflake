import snowflake.snowpark


def sum_val(session: snowflake.snowpark.Session) -> int:
    op = session.sql("SELECT 5+10").to_pandas()
    return op.iat[0, 0]
