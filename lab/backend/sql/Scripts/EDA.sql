WITH 
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
	STRFTIME('%Y-%m-%d', tot.datum), 
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total as tot
LEFT JOIN date_table as tab 
ON tot.datum = tab.datum;


SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
enhetstyp.diagramdata group by Enhetstyp ;

select * from enhetstyp.diagramdata d ;

SELECT * EXCLUDE (Innehåll) FROM  innehall.tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  innehall.diagramdata;-- ORDER BY "Visningstid (timmar)";

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM innehall.totalt;

-- Extra EDAs
-- Total views and Watch Time
WITH 
    date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
    date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
    SUM(tot.visningar) AS total_views, 
    SUM(tab."visningstid (timmar)") AS total_watch_time	
FROM date_total AS tot
LEFT JOIN date_table AS tab ON tot.datum = tab.datum;

-- Daily views and watch time per day
WITH 
    date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
    date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
    STRFTIME('%Y-%m-%d', tot.datum) AS date,
    SUM(tot.visningar) AS daily_views,
    SUM(tab."visningstid (timmar)") AS daily_watch_time
FROM date_total AS tot
LEFT JOIN date_table AS tab ON tot.datum = tab.datum
GROUP BY STRFTIME('%Y-%m-%d', tot.datum)
ORDER BY date;

-- Top 5 Videos
SELECT
	Videotitel,
	"Publiceringstid för video",
	Visningar,
	"Visningstid (timmar)"
FROM
	innehall.tabelldata
ORDER BY
	"Visningstid (timmar)" DESC 
OFFSET 1
LIMIT 5;

-- Total Views by Device
SELECT
	Enhetstyp,
	SUM(Visningar) AS total_visningar
FROM
	enhetstyp.diagramdata
GROUP BY
	Enhetstyp;

