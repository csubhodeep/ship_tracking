#!/bin/bash

docker \
run --name some-postgres \
-p 5400:5432 \
-e POSTGRES_USER="abcd" \
-e POSTGRES_PASSWORD="abcd" \
-e POSTGRES_DB="ship_data" \
-v ${PWD}/postgres-data:/var/lib/postgresql/data \
-d postgres