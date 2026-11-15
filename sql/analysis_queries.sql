use uttarakhand;

-- count total proprties by appartment type

select apartment_type,count(*) as appartment
from property
group by apartment_type;


-- Average Price by City

SELECT City,
       AVG(Price) AS Avg_Price
FROM property
GROUP BY City
ORDER BY Avg_Price DESC;

-- Property Count by City

SELECT City,
       COUNT(*) AS Total_Properties
FROM property
GROUP BY City;

-- Top 10 Expensive Localities

SELECT Locality,
       AVG(Price) AS Avg_Price
FROM property
GROUP BY Locality
ORDER BY Avg_Price DESC
LIMIT 10;


-- categorize properties into price brackets

select
      case
      when price< 5000000 then 'BUDGET (=<50L)'
      when price between 5000000 and 15000000 then 'MID RANGE(50L- 1.5CR)'
      else 'LUXURY (>1.5CR)'
      end as price_segment,
      count(*) as total_listings
      from property
      group by price_segment
      order by total_listings desc;
      
      
      
      
      
      
      
      
      
      
      
      
      
      








