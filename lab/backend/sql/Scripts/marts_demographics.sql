CREATE TABLE IF NOT EXISTS marts.gender_distribution AS (
    SELECT
        CASE 
            WHEN LOWER("Tittarnas kön") = 'kvinna' THEN 'Women'
            WHEN LOWER("Tittarnas kön") = 'man' THEN 'Men'
            ELSE "Tittarnas kön"  -- Retain the original name if it doesn't match
        END AS "Viewer's gender",
        "Visningar (%)" AS "Views (%)",
        "Genomsnittlig visningslängd" AS "Average view length",
        "Visningstid (timmar) (%)" AS "Display time (hours) (%)"
    FROM
        tittare.tabelldata_alder
);

--DROP TABLE IF EXISTS marts.gender_distribution;
	
SELECT * FROM marts.gender_distribution;


-- View Distribution by Country


-- Create table for country views summary
CREATE TABLE IF NOT EXISTS marts.country_views_summary AS 
(
    SELECT
        Geografi AS Country,
        Visningar AS Total_Views,
        "Visningstid (timmar)" AS Total_Watch_Time_Hours,
        "Genomsnittlig visningslängd" AS Average_View_Length
    FROM
        geografi.tabelldata
);


SELECT * FROM marts.country_views_summary;

--DROP TABLE IF EXISTS marts.country_views_summary;




