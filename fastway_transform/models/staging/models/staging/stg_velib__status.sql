with source as (
    select * from {{ source('velib_raw', 'external_station_status') }}
),

final as (
    select
        cast(json_value(station, '$.station_id') as string) as station_id,
        cast(json_value(station, '$.num_bikes_available') as int64) as bikes_available,
        cast(json_value(station, '$.num_docks_available') as int64) as docks_available,
        cast(json_value(station, '$.is_installed') as int64) as is_installed,
        cast(json_value(station, '$.is_returning') as int64) as is_returning,
        cast(json_value(station, '$.is_renting') as int64) as is_renting,
        timestamp_seconds(cast(json_value(station, '$.last_reported') as int64)) as last_reported_at
    from source,
    -- On extrait et on unnest en une seule opération propre
    unnest(json_extract_array(string_field_0, '$.data.stations')) as station
)

select * from final