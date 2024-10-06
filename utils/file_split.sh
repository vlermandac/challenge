#!/bin/bash

# Verificar argumentos
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 filename N"
    exit 1
fi

filename="$1"
N="$2"

# Extraer el nombre del archivo y la extensión
base_name=$(basename "$filename" | sed 's/\(.*\)\..*/\1/')
extension="${filename##*.}"

# Calcula el número de líneas por archivo
total_lines=$(wc -l < "$filename")
lines_per_file=$(( (total_lines + N - 1) / N ))

# Divide el archivo en N archivos
split -d -l "$lines_per_file" "$filename" "${base_name}_"

# Renombra los archivos
counter=0
for file in ${base_name}_*; do
    mv "$file" "${base_name}_${counter}.$extension"
    counter=$((counter + 1))
done
