{{ config(materialized='table') }}

with info as (
    select * from {{ ref('stg_velib__information') }}
),

status as (
    select * from {{ ref('stg_velib__status') }}
)

select
    info.station_id,
    info.station_name,
    info.capacity,
    info.latitude,
    info.longitude,
    status.bikes_available,
    status.docks_available,
    status.is_renting,
    status.last_reported_at
from info
left join status on info.station_id = status.station_id