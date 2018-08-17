from psycopg2 import ProgrammingError


def execute(connection, statement):
    cursor = connection.cursor()

    cursor.execute(statement)

    # Get response
    response = list()
    try:
        response = cursor.fetchall()
        if not response:
            # Empty response list
            return None
    except ProgrammingError as e:
        if e.args and e.args[0] == 'no results to fetch':
            # No response available (i.e. no response given)
            return None

        # Some other programming error; re-raise
        raise e

    return response
