with six_months_delivered_data as (
select distinct
    trid,
    trsnapshot.destinationAddressId,
    trsnapshot.transportObjectReason,
    trsnapshot.transportObjectState,
    trsnapshot.clientMetaData.externalAccountId,
    trsnapshot.lastUpdatedDate as lastUpdatedDate
from 
    ptrs_transport_request_update_events_prod_na_andes_data 
WHERE 
    cast(trsnapshot.lastUpdatedDate as timestamp) BETWEEN cast('${date}' as timestamp) - INTERVAL 180 days and cast('${date}' as timestamp)
    and trsnapshot.transportObjectState = 'DELIVERED'
),

remove_duplicates as (
select
    1 as region_id,
    trid as transportrequestid, 
	destinationAddressId as destinationaddressid,
	transportObjectReason as trobjectreason,
    transportObjectState as trobjectstate,
    externalAccountId as externalaccountid,
	max(lastUpdatedDate) as redshift_last_updated
from
    six_months_delivered_data
GROUP BY 
    trid,region_id, destinationAddressId, transportObjectReason, transportObjectState, externalAccountId
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