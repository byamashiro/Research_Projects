#!/bin/bash

#syntax ./getgoes.sh yyyymm yyyy mm
#ex. ./getgoes.sh 201106 2011 06

#================================================Download online
#================EPEAD
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g08_eps_1m_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/${2}/${3}/goes08/csv/

mkdir /Users/bryanyamashiro/Desktop/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GOES/g08_eps_1m_*.csv /Users/bryanyamashiro/Desktop/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GOES/${1} /Users/bryanyamashiro/Desktop/GOES/original/eps


#================================================Conversion
#================EPEAD
for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/g08_eps_1m_*.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/g08_eps_1m_*.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*02.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*02.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*03.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*03.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*04.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*04.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*05.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*05.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*06.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*06.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*07.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*07.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*08.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*08.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*09.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*09.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*10.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*10.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*11.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*11.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*12.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*12.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*13.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*13.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*14.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*14.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*15.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*15.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*16.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*16.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*17.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*17.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*18.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*18.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*19.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*19.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*20.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*20.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*21.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*21.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*22.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*22.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*23.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*23.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*24.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*24.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*25.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*25.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*26.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*26.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*27.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*27.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*28.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*28.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*29.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*29.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*30.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*30.csv > ${file/%.csv/x.dat}; done
#for file in /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*31.csv; do sed '1,214d' /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*eps*31.csv > ${file/%.csv/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GOES/original/eps/${1}/*x.dat .

for file in g08_eps_1m_*x.dat; do cut -d, -f1,9,10,11 g08_eps_1m_*x.dat > ${file/%.dat/y.txt}; done
#-f1,5,6,7,8,9,10,11
#for file in *eps*02x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*02x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*03x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*03x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*04x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*04x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*05x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*05x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*06x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*06x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*07x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*07x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*08x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*08x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*09x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*09x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*10x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*10x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*11x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*11x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*12x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*12x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*13x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*13x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*14x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*14x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*15x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*15x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*16x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*16x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*17x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*17x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*18x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*18x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*19x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*19x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*20x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*20x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*21x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*21x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*22x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*22x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*23x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*23x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*24x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*24x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*25x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*25x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*26x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*26x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*27x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*27x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*28x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*28x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*29x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*29x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*30x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*30x.dat > ${file/%.dat/y.txt}; done
#for file in *eps*31x.dat; do cut -d, -f1,5,6,7,8,9,10,11 *eps*31x.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in g08_eps_1m_*xy.txt; do sed 's/,/ /g' g08_eps_1m_*xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*02xy.txt; do sed 's/,/ /g' *eps*02xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*03xy.txt; do sed 's/,/ /g' *eps*03xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*04xy.txt; do sed 's/,/ /g' *eps*04xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*05xy.txt; do sed 's/,/ /g' *eps*05xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*06xy.txt; do sed 's/,/ /g' *eps*06xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*07xy.txt; do sed 's/,/ /g' *eps*07xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*08xy.txt; do sed 's/,/ /g' *eps*08xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*09xy.txt; do sed 's/,/ /g' *eps*09xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*10xy.txt; do sed 's/,/ /g' *eps*10xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*11xy.txt; do sed 's/,/ /g' *eps*11xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*12xy.txt; do sed 's/,/ /g' *eps*12xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*13xy.txt; do sed 's/,/ /g' *eps*13xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*14xy.txt; do sed 's/,/ /g' *eps*14xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*15xy.txt; do sed 's/,/ /g' *eps*15xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*16xy.txt; do sed 's/,/ /g' *eps*16xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*17xy.txt; do sed 's/,/ /g' *eps*17xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*18xy.txt; do sed 's/,/ /g' *eps*18xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*19xy.txt; do sed 's/,/ /g' *eps*19xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*20xy.txt; do sed 's/,/ /g' *eps*20xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*21xy.txt; do sed 's/,/ /g' *eps*21xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*22xy.txt; do sed 's/,/ /g' *eps*22xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*23xy.txt; do sed 's/,/ /g' *eps*23xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*24xy.txt; do sed 's/,/ /g' *eps*24xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*25xy.txt; do sed 's/,/ /g' *eps*25xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*26xy.txt; do sed 's/,/ /g' *eps*26xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*27xy.txt; do sed 's/,/ /g' *eps*27xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*28xy.txt; do sed 's/,/ /g' *eps*28xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*29xy.txt; do sed 's/,/ /g' *eps*29xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*30xy.txt; do sed 's/,/ /g' *eps*30xy.txt > ${file/%.txt/z.dat}; done
#for file in *eps*31xy.txt; do sed 's/,/ /g' *eps*31xy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_protonfluxgoesepead.dat
rm *z.dat

mv *_protonfluxgoesepead.dat /Users/bryanyamashiro/Desktop/GOES/converted/eps
