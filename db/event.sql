create table event_v1(
    id bigserial,
    insert_date_sk int,
    insert_timestamp timestamp,
    name varchar(255) DEFAULT NULL,
    description varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
)