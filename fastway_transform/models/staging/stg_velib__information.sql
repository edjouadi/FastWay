{{ config(materialized='table') }}

with source as (
    select * from {{ source('velib_raw', 'external_station_information') }}
),

final as (
    select
        cast(json_value(station, '$.station_id') as string) as station_id,
        cast(json_value(station, '$.name') as string) as station_name,
        cast(json_value(station, '$.capacity') as int64) as capacity,
        cast(json_value(station, '$.lat') as float64) as latitude,
        cast(json_value(station, '$.lon') as float64) as longitude
    from source,
    -- On fait le unnest directement sur la source pour éviter le bug de BigQuery
    unnest(json_extract_array(string_field_0, '$.data.stations')) as station
)

select * from final