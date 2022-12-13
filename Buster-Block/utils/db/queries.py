import sys
sys.path.append('Buster-Block')
import utils.db.connect as db
import utils.log_control as log_control


def fetchTable(cols: str, table: str, filters: str, grouping: str):

    log_control.loggerDB.info('Starting query creation')

    try:
        query = 'SELECT '
        if len(cols) > 0:
            first_reg = 1
            for col in cols:
                if first_reg == 1:
                    query += col
                    first_reg = 0
                else:
                    query += ', ' 
                    query += col
        else:
            query += '* '

        query = addWhitespace(query)
        query += f'FROM {table}'

        if len(filters) > 0:
            query = addWhitespace(query)
            query += 'WHERE'
            for filter in filters:
                query = addWhitespace(query)
                query += filter

        if len(grouping) > 0:
            query = addWhitespace(query)
            query += 'GROUP BY'
            for group in grouping:
                query = addWhitespace(query)
                query += group

        log_control.loggerDB.info(f'Query: {query}')

    
        log_control.loggerDB.info('Executing query')
        results = db.conn.execute(query)
        for result in results.fetchall():
            print(result)
    except Exception as e:
        msj = 'Unsuccesful query execution, more info: '
        log_control.loggerDB.error(f"{msj}{e}")
        return msj


def addWhitespace(query):
    query += ' '
    return query
