#!/bin/bash

start_dir=$(pwd)

cd script
script_dir=$(pwd)

cd ${start_dir}

mkdir results
cd results
results=$(pwd)

cd ${start_dir}

cd Primer_db
primerDB=$(pwd)

cd ${start_dir}

cd Sequences
cd H1
H1_seq=$(pwd)
cd ../H3
H3_seq=$(pwd)

arr=(MP)

#H3

subtype_folder=$(basename $(pwd))

for i in "${arr[@]}"
do
    blastn -task blastn-short \
    -gapopen 3 \
    -penalty -1 \
    -outfmt 6 \
    -query ${primerDB}/primer_database_with_duplicate_names_v1.fasta \
    -subject ${i}.fa > blastn_H3_${i}.csv


python3 ${script_dir}/primer.py

Rscript ${script_dir}/Rscript2.R

mv *csv ${results}
mv *pdf ${results}


done


#H1

cd ${H1_seq}

for i in "${arr[@]}"
do
    blastn -task blastn-short \
    -gapopen 3 \
    -penalty -1 \
    -outfmt 6 \
    -query ${primerDB}/primer_database_with_duplicate_names_v1.fasta \
    -subject ${i}.fa > blastn_H1_${i}.csv


python3 ${script_dir}/primer.py

Rscript ${script_dir}/Rscript2.R

mv *csv ${results}
mv *pdf ${results}

done










