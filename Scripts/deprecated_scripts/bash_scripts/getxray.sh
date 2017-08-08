#!/bin/bash

#syntax ./getgoes.sh yyyymm yyyy mm
#ex. ./getgoes.sh 201106 2011 06

#================================================Download online
#================XRS
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g15_xrs_2s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes15/csv/

mkdir /Users/bryanyamashiro/Desktop/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GOES/g15_xrs_2s_*.csv /Users/bryanyamashiro/Desktop/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GOES/${1} /Users/bryanyamashiro/Desktop/GOES/original/xray

#example g15_xrs_2s_20110101_20110101.csv
#================================================Conversion
#================EPEAD
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*01.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*01.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*02.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*02.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*03.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*03.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*04.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*04.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*05.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*05.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*06.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*06.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*07.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*07.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*08.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*08.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*09.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*09.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*10.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*10.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*11.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*11.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*12.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*12.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*13.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*13.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*14.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*14.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*15.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*15.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*16.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*16.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*17.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*17.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*18.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*18.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*19.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*19.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*20.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*20.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*21.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*21.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*22.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*22.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*23.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*23.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*24.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*24.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*25.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*25.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*26.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*26.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*27.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*27.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*28.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*28.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*29.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*29.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*30.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*30.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*31.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*xrs*31.csv > ${file/%.csv/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GOES/original/xray/${1}/*x.dat .

for file in *xrs*01x.dat; do cut -d, -f1,4,7 *xrs*01x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*02x.dat; do cut -d, -f1,4,7 *xrs*02x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*03x.dat; do cut -d, -f1,4,7 *xrs*03x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*04x.dat; do cut -d, -f1,4,7 *xrs*04x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*05x.dat; do cut -d, -f1,4,7 *xrs*05x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*06x.dat; do cut -d, -f1,4,7 *xrs*06x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*07x.dat; do cut -d, -f1,4,7 *xrs*07x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*08x.dat; do cut -d, -f1,4,7 *xrs*08x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*09x.dat; do cut -d, -f1,4,7 *xrs*09x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*10x.dat; do cut -d, -f1,4,7 *xrs*10x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*11x.dat; do cut -d, -f1,4,7 *xrs*11x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*12x.dat; do cut -d, -f1,4,7 *xrs*12x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*13x.dat; do cut -d, -f1,4,7 *xrs*13x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*14x.dat; do cut -d, -f1,4,7 *xrs*14x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*15x.dat; do cut -d, -f1,4,7 *xrs*15x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*16x.dat; do cut -d, -f1,4,7 *xrs*16x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*17x.dat; do cut -d, -f1,4,7 *xrs*17x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*18x.dat; do cut -d, -f1,4,7 *xrs*18x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*19x.dat; do cut -d, -f1,4,7 *xrs*19x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*20x.dat; do cut -d, -f1,4,7 *xrs*20x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*21x.dat; do cut -d, -f1,4,7 *xrs*21x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*22x.dat; do cut -d, -f1,4,7 *xrs*22x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*23x.dat; do cut -d, -f1,4,7 *xrs*23x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*24x.dat; do cut -d, -f1,4,7 *xrs*24x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*25x.dat; do cut -d, -f1,4,7 *xrs*25x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*26x.dat; do cut -d, -f1,4,7 *xrs*26x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*27x.dat; do cut -d, -f1,4,7 *xrs*27x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*28x.dat; do cut -d, -f1,4,7 *xrs*28x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*29x.dat; do cut -d, -f1,4,7 *xrs*29x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*30x.dat; do cut -d, -f1,4,7 *xrs*30x.dat > ${file/%.dat/y.txt}; done
for file in *xrs*31x.dat; do cut -d, -f1,4,7 *xrs*31x.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in *xrs*01xy.txt; do sed 's/,/ /g' *xrs*01xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*02xy.txt; do sed 's/,/ /g' *xrs*02xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*03xy.txt; do sed 's/,/ /g' *xrs*03xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*04xy.txt; do sed 's/,/ /g' *xrs*04xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*05xy.txt; do sed 's/,/ /g' *xrs*05xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*06xy.txt; do sed 's/,/ /g' *xrs*06xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*07xy.txt; do sed 's/,/ /g' *xrs*07xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*08xy.txt; do sed 's/,/ /g' *xrs*08xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*09xy.txt; do sed 's/,/ /g' *xrs*09xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*10xy.txt; do sed 's/,/ /g' *xrs*10xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*11xy.txt; do sed 's/,/ /g' *xrs*11xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*12xy.txt; do sed 's/,/ /g' *xrs*12xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*13xy.txt; do sed 's/,/ /g' *xrs*13xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*14xy.txt; do sed 's/,/ /g' *xrs*14xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*15xy.txt; do sed 's/,/ /g' *xrs*15xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*16xy.txt; do sed 's/,/ /g' *xrs*16xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*17xy.txt; do sed 's/,/ /g' *xrs*17xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*18xy.txt; do sed 's/,/ /g' *xrs*18xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*19xy.txt; do sed 's/,/ /g' *xrs*19xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*20xy.txt; do sed 's/,/ /g' *xrs*20xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*21xy.txt; do sed 's/,/ /g' *xrs*21xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*22xy.txt; do sed 's/,/ /g' *xrs*22xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*23xy.txt; do sed 's/,/ /g' *xrs*23xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*24xy.txt; do sed 's/,/ /g' *xrs*24xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*25xy.txt; do sed 's/,/ /g' *xrs*25xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*26xy.txt; do sed 's/,/ /g' *xrs*26xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*27xy.txt; do sed 's/,/ /g' *xrs*27xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*28xy.txt; do sed 's/,/ /g' *xrs*28xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*29xy.txt; do sed 's/,/ /g' *xrs*29xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*30xy.txt; do sed 's/,/ /g' *xrs*30xy.txt > ${file/%.txt/z.dat}; done
for file in *xrs*31xy.txt; do sed 's/,/ /g' *xrs*31xy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_xrayfluxgoesxrs.dat
rm *z.dat

mv *_xrayfluxgoesxrs.dat /Users/bryanyamashiro/Desktop/GOES/converted/xray
