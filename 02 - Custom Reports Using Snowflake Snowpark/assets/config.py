from snowflake.snowpark import Session

session_config = {
    "account": "XXXXXXXXXXXXXXXX",
    "user": "XXXXXXXXXXXXXXXX",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "UDEMY",
    "schema": "PUBLIC",
    "password": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
}


def connection_builder():
    session = Session.builder.configs(session_config).create()
    return session
