#!/bin/bash

# Crear directorio para los datos
mkdir -p data/raw

# Descargar todos los tipos de datos de taxi
for type in yellow green fhv; do
    mkdir -p data/raw/$type
    for month in {01..12}; do
        wget -P data/raw/$type https://d37ci6vzurychx.cloudfront.net/trip-data/${type}_tripdata_2023-${month}.parquet
    done
done