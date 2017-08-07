#!/bin/bash

#syntax ./getgoes.sh yyyymm yyyy mm
#ex. ./getgoes.sh 201106 2011 06

#================================================Download online
#================EPEAD
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g15_epead_p27w_32s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes15/csv/

mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/g15_epead_p27w_32s_*.csv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead

#================HEPAD
#===GOES 13
#wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g13_hepad_ap_32s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes13/csv/
#mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
#mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/g13_hepad_ap_32s_*.csv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
#mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad
#===GOES 15
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g15_hepad_ap_32s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes15/csv/

mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/g15_hepad_ap_32s_*.csv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad




#================================================Conversion
#================EPEAD
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*01.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*01.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*02.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*02.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*03.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*03.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*04.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*04.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*05.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*05.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*06.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*06.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*07.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*07.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*08.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*08.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*09.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*09.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*10.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*10.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*11.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*11.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*12.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*12.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*13.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*13.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*14.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*14.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*15.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*15.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*16.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*16.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*17.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*17.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*18.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*18.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*19.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*19.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*20.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*20.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*21.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*21.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*22.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*22.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*23.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*23.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*24.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*24.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*25.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*25.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*26.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*26.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*27.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*27.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*28.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*28.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*29.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*29.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*30.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*30.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*31.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*epead*31.csv > ${file/%.csv/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/${1}/*x.dat .

for file in *epead*01x.dat; do cut -d, -f1,10,13,16 *epead*01x.dat > ${file/%.dat/y.txt}; done
for file in *epead*02x.dat; do cut -d, -f1,10,13,16 *epead*02x.dat > ${file/%.dat/y.txt}; done
for file in *epead*03x.dat; do cut -d, -f1,10,13,16 *epead*03x.dat > ${file/%.dat/y.txt}; done
for file in *epead*04x.dat; do cut -d, -f1,10,13,16 *epead*04x.dat > ${file/%.dat/y.txt}; done
for file in *epead*05x.dat; do cut -d, -f1,10,13,16 *epead*05x.dat > ${file/%.dat/y.txt}; done
for file in *epead*06x.dat; do cut -d, -f1,10,13,16 *epead*06x.dat > ${file/%.dat/y.txt}; done
for file in *epead*07x.dat; do cut -d, -f1,10,13,16 *epead*07x.dat > ${file/%.dat/y.txt}; done
for file in *epead*08x.dat; do cut -d, -f1,10,13,16 *epead*08x.dat > ${file/%.dat/y.txt}; done
for file in *epead*09x.dat; do cut -d, -f1,10,13,16 *epead*09x.dat > ${file/%.dat/y.txt}; done
for file in *epead*10x.dat; do cut -d, -f1,10,13,16 *epead*10x.dat > ${file/%.dat/y.txt}; done
for file in *epead*11x.dat; do cut -d, -f1,10,13,16 *epead*11x.dat > ${file/%.dat/y.txt}; done
for file in *epead*12x.dat; do cut -d, -f1,10,13,16 *epead*12x.dat > ${file/%.dat/y.txt}; done
for file in *epead*13x.dat; do cut -d, -f1,10,13,16 *epead*13x.dat > ${file/%.dat/y.txt}; done
for file in *epead*14x.dat; do cut -d, -f1,10,13,16 *epead*14x.dat > ${file/%.dat/y.txt}; done
for file in *epead*15x.dat; do cut -d, -f1,10,13,16 *epead*15x.dat > ${file/%.dat/y.txt}; done
for file in *epead*16x.dat; do cut -d, -f1,10,13,16 *epead*16x.dat > ${file/%.dat/y.txt}; done
for file in *epead*17x.dat; do cut -d, -f1,10,13,16 *epead*17x.dat > ${file/%.dat/y.txt}; done
for file in *epead*18x.dat; do cut -d, -f1,10,13,16 *epead*18x.dat > ${file/%.dat/y.txt}; done
for file in *epead*19x.dat; do cut -d, -f1,10,13,16 *epead*19x.dat > ${file/%.dat/y.txt}; done
for file in *epead*20x.dat; do cut -d, -f1,10,13,16 *epead*20x.dat > ${file/%.dat/y.txt}; done
for file in *epead*21x.dat; do cut -d, -f1,10,13,16 *epead*21x.dat > ${file/%.dat/y.txt}; done
for file in *epead*22x.dat; do cut -d, -f1,10,13,16 *epead*22x.dat > ${file/%.dat/y.txt}; done
for file in *epead*23x.dat; do cut -d, -f1,10,13,16 *epead*23x.dat > ${file/%.dat/y.txt}; done
for file in *epead*24x.dat; do cut -d, -f1,10,13,16 *epead*24x.dat > ${file/%.dat/y.txt}; done
for file in *epead*25x.dat; do cut -d, -f1,10,13,16 *epead*25x.dat > ${file/%.dat/y.txt}; done
for file in *epead*26x.dat; do cut -d, -f1,10,13,16 *epead*26x.dat > ${file/%.dat/y.txt}; done
for file in *epead*27x.dat; do cut -d, -f1,10,13,16 *epead*27x.dat > ${file/%.dat/y.txt}; done
for file in *epead*28x.dat; do cut -d, -f1,10,13,16 *epead*28x.dat > ${file/%.dat/y.txt}; done
for file in *epead*29x.dat; do cut -d, -f1,10,13,16 *epead*29x.dat > ${file/%.dat/y.txt}; done
for file in *epead*30x.dat; do cut -d, -f1,10,13,16 *epead*30x.dat > ${file/%.dat/y.txt}; done
for file in *epead*31x.dat; do cut -d, -f1,10,13,16 *epead*31x.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in *epead*01xy.txt; do sed 's/,/ /g' *epead*01xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*02xy.txt; do sed 's/,/ /g' *epead*02xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*03xy.txt; do sed 's/,/ /g' *epead*03xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*04xy.txt; do sed 's/,/ /g' *epead*04xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*05xy.txt; do sed 's/,/ /g' *epead*05xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*06xy.txt; do sed 's/,/ /g' *epead*06xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*07xy.txt; do sed 's/,/ /g' *epead*07xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*08xy.txt; do sed 's/,/ /g' *epead*08xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*09xy.txt; do sed 's/,/ /g' *epead*09xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*10xy.txt; do sed 's/,/ /g' *epead*10xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*11xy.txt; do sed 's/,/ /g' *epead*11xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*12xy.txt; do sed 's/,/ /g' *epead*12xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*13xy.txt; do sed 's/,/ /g' *epead*13xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*14xy.txt; do sed 's/,/ /g' *epead*14xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*15xy.txt; do sed 's/,/ /g' *epead*15xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*16xy.txt; do sed 's/,/ /g' *epead*16xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*17xy.txt; do sed 's/,/ /g' *epead*17xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*18xy.txt; do sed 's/,/ /g' *epead*18xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*19xy.txt; do sed 's/,/ /g' *epead*19xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*20xy.txt; do sed 's/,/ /g' *epead*20xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*21xy.txt; do sed 's/,/ /g' *epead*21xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*22xy.txt; do sed 's/,/ /g' *epead*22xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*23xy.txt; do sed 's/,/ /g' *epead*23xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*24xy.txt; do sed 's/,/ /g' *epead*24xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*25xy.txt; do sed 's/,/ /g' *epead*25xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*26xy.txt; do sed 's/,/ /g' *epead*26xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*27xy.txt; do sed 's/,/ /g' *epead*27xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*28xy.txt; do sed 's/,/ /g' *epead*28xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*29xy.txt; do sed 's/,/ /g' *epead*29xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*30xy.txt; do sed 's/,/ /g' *epead*30xy.txt > ${file/%.txt/z.dat}; done
for file in *epead*31xy.txt; do sed 's/,/ /g' *epead*31xy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_protonfluxgoesepead.dat
rm *z.dat

mv *_protonfluxgoesepead.dat /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Epead

#================HEPAD
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*01.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*01.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*02.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*02.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*03.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*03.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*04.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*04.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*05.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*05.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*06.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*06.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*07.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*07.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*08.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*08.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*09.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*09.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*10.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*10.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*11.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*11.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*12.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*12.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*13.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*13.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*14.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*14.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*15.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*15.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*16.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*16.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*17.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*17.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*18.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*18.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*19.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*19.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*20.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*20.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*21.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*21.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*22.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*22.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*23.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*23.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*24.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*24.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*25.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*25.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*26.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*26.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*27.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*27.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*28.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*28.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*29.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*29.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*30.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*30.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*31.csv; do sed '1,283d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*hepad*31.csv > ${file/%.csv/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad/${1}/*x.dat .

for file in *hepad*01x.dat; do cut -d, -f1,10,13,16,19 *hepad*01x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*02x.dat; do cut -d, -f1,10,13,16,19 *hepad*02x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*03x.dat; do cut -d, -f1,10,13,16,19 *hepad*03x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*04x.dat; do cut -d, -f1,10,13,16,19 *hepad*04x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*05x.dat; do cut -d, -f1,10,13,16,19 *hepad*05x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*06x.dat; do cut -d, -f1,10,13,16,19 *hepad*06x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*07x.dat; do cut -d, -f1,10,13,16,19 *hepad*07x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*08x.dat; do cut -d, -f1,10,13,16,19 *hepad*08x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*09x.dat; do cut -d, -f1,10,13,16,19 *hepad*09x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*10x.dat; do cut -d, -f1,10,13,16,19 *hepad*10x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*11x.dat; do cut -d, -f1,10,13,16,19 *hepad*11x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*12x.dat; do cut -d, -f1,10,13,16,19 *hepad*12x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*13x.dat; do cut -d, -f1,10,13,16,19 *hepad*13x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*14x.dat; do cut -d, -f1,10,13,16,19 *hepad*14x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*15x.dat; do cut -d, -f1,10,13,16,19 *hepad*15x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*16x.dat; do cut -d, -f1,10,13,16,19 *hepad*16x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*17x.dat; do cut -d, -f1,10,13,16,19 *hepad*17x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*18x.dat; do cut -d, -f1,10,13,16,19 *hepad*18x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*19x.dat; do cut -d, -f1,10,13,16,19 *hepad*19x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*20x.dat; do cut -d, -f1,10,13,16,19 *hepad*20x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*21x.dat; do cut -d, -f1,10,13,16,19 *hepad*21x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*22x.dat; do cut -d, -f1,10,13,16,19 *hepad*22x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*23x.dat; do cut -d, -f1,10,13,16,19 *hepad*23x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*24x.dat; do cut -d, -f1,10,13,16,19 *hepad*24x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*25x.dat; do cut -d, -f1,10,13,16,19 *hepad*25x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*26x.dat; do cut -d, -f1,10,13,16,19 *hepad*26x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*27x.dat; do cut -d, -f1,10,13,16,19 *hepad*27x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*28x.dat; do cut -d, -f1,10,13,16,19 *hepad*28x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*29x.dat; do cut -d, -f1,10,13,16,19 *hepad*29x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*30x.dat; do cut -d, -f1,10,13,16,19 *hepad*30x.dat > ${file/%.dat/y.txt}; done
for file in *hepad*31x.dat; do cut -d, -f1,10,13,16,19 *hepad*31x.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in *hepad*01xy.txt; do sed 's/,/ /g' *hepad*01xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*02xy.txt; do sed 's/,/ /g' *hepad*02xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*03xy.txt; do sed 's/,/ /g' *hepad*03xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*04xy.txt; do sed 's/,/ /g' *hepad*04xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*05xy.txt; do sed 's/,/ /g' *hepad*05xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*06xy.txt; do sed 's/,/ /g' *hepad*06xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*07xy.txt; do sed 's/,/ /g' *hepad*07xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*08xy.txt; do sed 's/,/ /g' *hepad*08xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*09xy.txt; do sed 's/,/ /g' *hepad*09xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*10xy.txt; do sed 's/,/ /g' *hepad*10xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*11xy.txt; do sed 's/,/ /g' *hepad*11xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*12xy.txt; do sed 's/,/ /g' *hepad*12xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*13xy.txt; do sed 's/,/ /g' *hepad*13xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*14xy.txt; do sed 's/,/ /g' *hepad*14xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*15xy.txt; do sed 's/,/ /g' *hepad*15xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*16xy.txt; do sed 's/,/ /g' *hepad*16xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*17xy.txt; do sed 's/,/ /g' *hepad*17xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*18xy.txt; do sed 's/,/ /g' *hepad*18xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*19xy.txt; do sed 's/,/ /g' *hepad*19xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*20xy.txt; do sed 's/,/ /g' *hepad*20xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*21xy.txt; do sed 's/,/ /g' *hepad*21xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*22xy.txt; do sed 's/,/ /g' *hepad*22xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*23xy.txt; do sed 's/,/ /g' *hepad*23xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*24xy.txt; do sed 's/,/ /g' *hepad*24xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*25xy.txt; do sed 's/,/ /g' *hepad*25xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*26xy.txt; do sed 's/,/ /g' *hepad*26xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*27xy.txt; do sed 's/,/ /g' *hepad*27xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*28xy.txt; do sed 's/,/ /g' *hepad*28xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*29xy.txt; do sed 's/,/ /g' *hepad*29xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*30xy.txt; do sed 's/,/ /g' *hepad*30xy.txt > ${file/%.txt/z.dat}; done
for file in *hepad*31xy.txt; do sed 's/,/ /g' *hepad*31xy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_protonfluxgoeshepad.dat
rm *z.dat

mv *_protonfluxgoeshepad.dat /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Hepad