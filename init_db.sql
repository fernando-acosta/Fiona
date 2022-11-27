
-- Store Power Regions in Puerto Rico. This table will likely have a fixed number of rows.
create table regions (
    region_id serial constraint regions_pk primary key,
    region_name varchar(20) not null
);

create unique index regions_region_id_uindex
    on regions (region_id);

-- Store different sources to get data from in the future.
create table data_sources (
    source_id serial constraint data_sources_pk primary key,
    source_name varchar(20) not null,
    source_url varchar(256) not null
);

create unique index data_sources_source_id_uindex
    on data_sources (source_id);

-- Mapping between regions, and sources. Helps keep track of ids necessary to fetch data for a region on a particular source.
create table source_region_mappings (
    source_id int not null
        constraint source_region_mapping_data_source_source_id_fk
            references data_sources
            on delete cascade,
    region_id int not null
        constraint source_region_mapping_region_region_id_fk
            references regions
            on delete cascade,
    source_specific_region_id varchar(20) not null,
    primary key (source_id, region_id)
);

-- How many people are without power, per region, identify source, when source was updated last, and when data was fetched.
create table outage_data (
    outage_data_id serial constraint outage_data_pk primary key,
    total_clients int not null,
    clients_without_power_service int not null,
    region_id int not null
        constraint outage_data_regions_region_id_fk
            references regions
            on delete cascade,
    source_id int not null
        constraint outage_data_data_source_source_id_fk
                references data_sources
                on delete cascade,
    source_last_updated_on timestamp not null,
    data_fetched_on timestamp not null
);

create unique index outage_data_outage_data_id_uindex
    on outage_data (outage_data_id);

-- Statistics done for all regions
create table general_statistics (
    statistics_id serial constraint general_statistics_pk primary key,
    statistics_name varchar(30) not null,
    statistics_description text not null,
    statistics_value decimal(9,6) not null,
    start_date timestamp not null,
    end_date timestamp not null,
    measured_on timestamp not null
);

create unique index general_statistics_statistics_id_uindex
    on general_statistics (statistics_id);


-- Statistics done per region
create table regional_statistics (
    regional_statistics_id serial constraint regional_statistics_pk primary key,
    statistics_name varchar(30) not null,
    statistics_description text not null,
    statistics_value decimal(9,6) not null,
    start_date timestamp not null,
    end_date timestamp not null,
    region_id int not null
        constraint regional_statistics_region_region_id_fk
            references regions
            on delete cascade,
    measured_on timestamp not null
);

create unique index regional_statistics_regional_statistics_id_uindex
    on regional_statistics (regional_statistics_id);
