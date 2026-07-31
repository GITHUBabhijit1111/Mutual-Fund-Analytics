SELECT *
FROM aum_by_fund_house_clean
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
strftime('%Y-%m',date) AS Month,
AVG(nav) AS Avg_NAV

FROM nav_history_clean

GROUP BY Month

ORDER BY Month;

SELECT
state,
COUNT(*) AS Transactions

FROM investor_transactions_clean

GROUP BY state

ORDER BY Transactions DESC;

SELECT*FROM investor_transactions_clean;

SELECT
amfi_code,
expense_ratio_pct

FROM scheme_performance_clean

WHERE expense_ratio_pct<1;

SELECT
amfi_code,
return_5yr_pct

FROM scheme_performance_clean

ORDER BY return_5yr_pct DESC

LIMIT 5;

SELECT

AVG(amount_inr)

FROM investor_transactions_clean;

SELECT

fund_house,

SUM(aum_crore)

FROM aum_by_fund_house_clean

GROUP BY fund_house

ORDER BY SUM(aum_crore) DESC;

SELECT

strftime('%Y-%m',transaction_date) AS Month,

SUM(amount_inr)

FROM investor_transactions_clean

GROUP BY Month;

SELECT

category,

COUNT(*)

FROM fund_master_clean

GROUP BY category

ORDER BY COUNT(*) DESC;

SELECT

amfi_code,

MAX(nav)

FROM nav_history_clean

GROUP BY amfi_code

ORDER BY MAX(nav) DESC

LIMIT 10;