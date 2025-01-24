with six_months_delivered_data as (
select distinct
    transportrequestid,
    destinationaddressid,
    trobjectreason,
    trobjectstate,
    externalaccountid,
    redshift_last_updated
from 
    PTRS_TRANSPORT_REQUESTS_NA 
WHERE 
    cast(redshift_last_updated as timestamp) BETWEEN cast('${date}' as timestamp) - INTERVAL 180 days and cast('${date}' as timestamp)
    and trobjectstate = 'DELIVERED'
),

remove_duplicates as (
select
    1 as region_id,
    transportrequestid, 
	destinationaddressid,
	trobjectreason,
	trobjectstate,
	externalaccountid,
	max(redshift_last_updated) as redshift_last_updated
from
    six_months_delivered_data
GROUP BY 
    transportrequestid,region_id, destinationaddressid,trobjectreason,trobjectstate,externalaccountid
)

select distinct 
    region_id, 
	transportrequestid, 
	destinationaddressid, 
	trobjectreason,
	trobjectstate,
	externalaccountid,
	redshift_last_updated
FROM remove_duplicates;