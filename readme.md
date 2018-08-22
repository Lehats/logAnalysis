

create pathCount View:

I decided to create this view, because it can be used in the queries of the get_Top_Articles()- and get_Top_Authors()-functions. So it cleans up both queries a bit.

sql-query to create pathCount view:

 create or replace view pathCount as select path, count(*) as count from log where status = '200 OK' and path like '%/article%'group by path order by path;