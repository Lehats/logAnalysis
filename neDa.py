import psycopg2

dbName = 'dbname=news'

def get_Top_Articles():
    
    """Establish a connection to the db named news using the python module psycopg2. Creates a connection object which is good till it'll be closed"""
    conn = psycopg2.connect(dbName)

    """create a cursor which is needed to search and fetch data in tables"""
    cCursor = conn.cursor()

    """Define SQL-query and pass it over to the curser which execute the query and fetch the results"""
    sQuery = "select path, count(*) as num from log where status = '200 OK' and path like '%/article%'group by path order by num desc limit 3;"
    cCursor.execute(sQuery)
    results = cCursor.fetchall()

    """Print the results. Before they're printed strings are edited using basic pythin string functions."""
    print ("\nBelow listed the 3 most viewed articles : \n")
    print ((results[0][0]).replace('/article/','').replace('-', ' ').title() + ': ' + str(results[0][1]) + ' views.')
    print ((results[1][0]).replace('/article/','').replace('-', ' ').title() + ': ' + str(results[1][1]) + ' views.')
    print ((results[2][0]).replace('/article/','').replace('-', ' ').title() + ': ' + str(results[2][1]) + ' views. \n')
    """Close the connection to teh db. A way to save resources"""     
    conn.close()


get_Top_Articles()




