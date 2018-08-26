#!/usr/bin/env python3


import psycopg2


dbName = 'dbname=news'


def get_Top_Articles():

    """Establish a connection to the db named news using the python module
    psycopg2. Creates a connection object which is good till it'll be closed"""
    conn = psycopg2.connect(dbName)

    """create a cursor which is needed to search and fetch data in tables"""
    cCursor = conn.cursor()

    """Define SQL-query and pass it over to the curser which execute the
        query and fetch the results"""
    sQuery = "select * from pathCount order by count desc limit 3;"
    """
    sQuery = "select path, count(*) as num from log where status = '200 OK'
        and path like '%/article%'group by path order by num desc limit 3;"
    """
    cCursor.execute(sQuery)
    results = cCursor.fetchall()

    """Print the results. Before they're printed strings are edited using
        basic python string functions."""
    print("\nBelow listed the 3 most viewed articles : \n")
    print((results[0][0]).replace('/article/', '').replace(
        '-', ' ').title() + ': ' + str(results[0][1]) + ' views.')
    print((results[1][0]).replace('/article/', '').replace(
        '-', ' ').title() + ': ' + str(results[1][1]) + ' views.')
    print((results[2][0]).replace('/article/', '').replace(
        '-', ' ').title() + ': ' + str(results[2][1]) + ' views. \n')
    """Close the connection to teh db. A way to save resources"""
    conn.close()


def get_Top_Authors():

    """Establish a connection to the db named news using the python module
    psycopg2. Creates a connection object which is good till it'll be closed"""
    conn = psycopg2.connect(dbName)

    """create a cursor which is needed to search and fetch data in tables"""
    cCursor = conn.cursor()

    """Define SQL-query and pass it over to the curser which execute the
             query and fetch the results"""
    sQuery = """select name ,sum from authors, ( select sum(count) as sum,
                author from (select slug, author, count from articles,
                pathCount where concat('/article/',cast(slug as varchar(20)))
                like concat('%', cast(path as varchar(20)) , '%')) as
                newtable group by author) as sumtable where
                authors.id = sumtable.author order by sum desc;"""

    cCursor.execute(sQuery)
    results = cCursor.fetchall()

    """Print the results. Before they're printed strings are edited using
        basic python string functions."""

    print("\nBelow listed the most popular authors : \n")

    print(str(results[0][0]) + ': ' + str(results[0][1]) + ' views.')
    print(str(results[1][0]) + ': ' + str(results[1][1]) + ' views.')
    print(str(results[2][0]) + ': ' + str(results[2][1]) + ' views.')
    print(str(results[3][0]) + ': ' + str(results[3][1]) + ' views.\n')

    """Close the connection to teh db. A way to save resources"""
    conn.close()


def count_Errors():

    """Establish a connection to the db named news using the python module
    psycopg2. Creates a connection object which is good till it'll be closed"""
    conn = psycopg2.connect(dbName)

    """create a cursor which is needed to search and fetch data in tables"""
    cCursor = conn.cursor()

    """Define SQL-query and pass it over to the curser which execute the query
    and fetch the results"""
    sQuery = """select date, (oneperc*errorCount) as errorPercent from
                (select date(time) as date2, 100/cast(count(*) as decimal) as
                onePerc from log group by date2 order by date2) as
                onePercTable, (select date(time) , count(*) as errorCount
                from log where status != '200 OK' group by date order by date)
                as errorCountTable
                where onePercTable.date2 = errorCountTable.date
                and onePercTable.oneperc*errorcounttable.errorCount > 1;"""

    cCursor.execute(sQuery)
    results = cCursor.fetchall()

    """Print the results. Before they're printed strings are edited
    using basic python string functions."""
    print("\nBelow listed all dates with more than 1% errors : \n")

    print(str(results[0][0]) + ': ' + str(round(
        results[0][1], 2)) + '% Errors.\n')

    """Close the connection to teh db. A way to save resources"""
    conn.close()


get_Top_Articles()

get_Top_Authors()

count_Errors()
