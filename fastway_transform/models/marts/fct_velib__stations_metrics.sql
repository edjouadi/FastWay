{{ config(materialized='table') }}

with base as (
    select * from {{ ref('int_velib__stations_combined') }}
)

select
    station_id,
    station_name,
    capacity,
    bikes_available,
    docks_available,
    -- Calcul du taux d'occupation (évite la division par zéro)
    safe_divide(bikes_available, capacity) as occupancy_rate,
    
    -- Ajout d'une catégorie simple pour savoir si la station est "vide", "pleine" ou "ok"
    case 
        when bikes_available = 0 then 'Vide'
        when bikes_available = capacity then 'Pleine'
        else 'Normal'
    end as station_status,
    
    last_reported_at
from base
where capacity > 0