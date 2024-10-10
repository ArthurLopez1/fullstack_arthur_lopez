CREATE TABLE IF NOT EXISTS marts.gender_distribution AS (
SELECT
	"Tittarnas kön",
	"Visningar (%)",
	"Genomsnittlig visningslängd",
	"Visningstid (timmar) (%)"
FROM
	tittare.tabelldata_alder);
	
SELECT * FROM marts.gender_distribution;

SELECT "Tittarnas kön", "Visningar (%)", "Visningstid (timmar) (%)"
FROM marts.gender_distribution;