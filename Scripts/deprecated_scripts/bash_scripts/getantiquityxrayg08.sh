#!/bin/bash

#syntax ./getgoes.sh yyyymm yyyy mm
#ex. ./getgoes.sh 201106 2011 06

#================================================Download online
#================XRS
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g08_xrs_1m_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/${2}/${3}/goes08/csv/

mkdir /Users/bryanyamashiro/Desktop/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GOES/g08_xrs_1m_*.csv /Users/bryanyamashiro/Desktop/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GOES/${1} /Users/bryanyamashiro/Desktop/GOES/original/xray

#example g15_xrs_2s_20110101_20110101.csv
#================================================Conversion
#================EPEAD
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/g08_xrs_1m_*.csv; do sed '1,118d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/g08_xrs_1m_*.csv > ${file/%.csv/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*x.dat .

for file in g08_xrs_1m_*x.dat; do cut -d, -f1,2,3 g08_xrs_1m_*x.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in g08_xrs_1m_*xy.txt; do sed 's/,/ /g' g08_xrs_1m_*xy.txt > ${file/%.txt/z.dat}; done


rm *y.txt

cat *z.dat > ${1}_xrayfluxgoesxrs.dat
rm *z.dat

mv *_xrayfluxgoesxrs.dat /Users/bryanyamashiro/Desktop/GOES/converted/xray
