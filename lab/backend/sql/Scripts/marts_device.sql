CREATE TABLE IF NOT EXISTS marts.device_views_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	datum) AS Datum,
	Enhetstyp,
	sum(Visningar) AS Visningar
FROM
	enhetstyp.diagramdata d
GROUP BY
	(datum,
	Enhetstyp )
ORDER BY 
	Datum ASC );


CREATE TABLE IF NOT EXISTS marts.device_summary AS (
    SELECT
        CASE 
            WHEN LOWER(Enhetstyp) = 'totalt' THEN 'Total'
            WHEN LOWER(Enhetstyp) = 'dator' THEN 'Desktop/Laptop'
            WHEN LOWER(Enhetstyp) = 'surfplatta' THEN 'Tablet'
            WHEN LOWER(Enhetstyp) = 'mobiltelefon' THEN 'Mobile'
            ELSE Enhetstyp
        END AS Enhetstyp,
        Visningar,
        "Visningstid (timmar)" AS Visningstid_timmar,
        "Genomsnittlig visningslängd" AS Visningslängd_genomsnitt
    FROM
        enhetstyp.tabelldata
);




SELECT * FROM marts.device_views_date;
SELECT * FROM marts.device_summary;