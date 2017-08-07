#!/bin/bash

#syntax ./getgoes.sh yyyymm yyyy mm
#ex. ./getgoes.sh 201106 2011 06

#================================================Download online
#================>=0.8 MeV
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g15_epead_e1ew_4s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes15/csv/

mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/g15_epead_e1ew_4s_*.csv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/

#================>=2.0 MeV
#===GOES 13
#wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g13_hepad_ap_32s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes13/csv/
#mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
#mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/g13_hepad_ap_32s_*.csv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
#mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Hepad
#===GOES 15
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g15_epead_e2ew_16s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes15/csv/

mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/g15_epead_e2ew_16s_*.csv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/




#================================================Conversion
#================>=0.8 MeV
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*01.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*01.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*02.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*02.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*03.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*03.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*04.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*04.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*05.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*05.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*06.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*06.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*07.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*07.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*08.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*08.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*09.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*09.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*10.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*10.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*11.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*11.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*12.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*12.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*13.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*13.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*14.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*14.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*15.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*15.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*16.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*16.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*17.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*17.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*18.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*18.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*19.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*19.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*20.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*20.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*21.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*21.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*22.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*22.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*23.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*23.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*24.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*24.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*25.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*25.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*26.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*26.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*27.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*27.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*28.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*28.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*29.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*29.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*30.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*30.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*31.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*epead_e1ew*31.csv > ${file/%.csv/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/low_0.8mev/${1}/*x.dat .

for file in *epead_e1ew*01x.dat; do cut -d, -f1,6,7 *epead_e1ew*01x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*02x.dat; do cut -d, -f1,6,7 *epead_e1ew*02x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*03x.dat; do cut -d, -f1,6,7 *epead_e1ew*03x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*04x.dat; do cut -d, -f1,6,7 *epead_e1ew*04x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*05x.dat; do cut -d, -f1,6,7 *epead_e1ew*05x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*06x.dat; do cut -d, -f1,6,7 *epead_e1ew*06x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*07x.dat; do cut -d, -f1,6,7 *epead_e1ew*07x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*08x.dat; do cut -d, -f1,6,7 *epead_e1ew*08x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*09x.dat; do cut -d, -f1,6,7 *epead_e1ew*09x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*10x.dat; do cut -d, -f1,6,7 *epead_e1ew*10x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*11x.dat; do cut -d, -f1,6,7 *epead_e1ew*11x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*12x.dat; do cut -d, -f1,6,7 *epead_e1ew*12x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*13x.dat; do cut -d, -f1,6,7 *epead_e1ew*13x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*14x.dat; do cut -d, -f1,6,7 *epead_e1ew*14x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*15x.dat; do cut -d, -f1,6,7 *epead_e1ew*15x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*16x.dat; do cut -d, -f1,6,7 *epead_e1ew*16x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*17x.dat; do cut -d, -f1,6,7 *epead_e1ew*17x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*18x.dat; do cut -d, -f1,6,7 *epead_e1ew*18x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*19x.dat; do cut -d, -f1,6,7 *epead_e1ew*19x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*20x.dat; do cut -d, -f1,6,7 *epead_e1ew*20x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*21x.dat; do cut -d, -f1,6,7 *epead_e1ew*21x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*22x.dat; do cut -d, -f1,6,7 *epead_e1ew*22x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*23x.dat; do cut -d, -f1,6,7 *epead_e1ew*23x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*24x.dat; do cut -d, -f1,6,7 *epead_e1ew*24x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*25x.dat; do cut -d, -f1,6,7 *epead_e1ew*25x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*26x.dat; do cut -d, -f1,6,7 *epead_e1ew*26x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*27x.dat; do cut -d, -f1,6,7 *epead_e1ew*27x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*28x.dat; do cut -d, -f1,6,7 *epead_e1ew*28x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*29x.dat; do cut -d, -f1,6,7 *epead_e1ew*29x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*30x.dat; do cut -d, -f1,6,7 *epead_e1ew*30x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e1ew*31x.dat; do cut -d, -f1,6,7 *epead_e1ew*31x.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in *epead_e1ew*01xy.txt; do sed 's/,/ /g' *epead_e1ew*01xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*02xy.txt; do sed 's/,/ /g' *epead_e1ew*02xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*03xy.txt; do sed 's/,/ /g' *epead_e1ew*03xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*04xy.txt; do sed 's/,/ /g' *epead_e1ew*04xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*05xy.txt; do sed 's/,/ /g' *epead_e1ew*05xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*06xy.txt; do sed 's/,/ /g' *epead_e1ew*06xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*07xy.txt; do sed 's/,/ /g' *epead_e1ew*07xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*08xy.txt; do sed 's/,/ /g' *epead_e1ew*08xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*09xy.txt; do sed 's/,/ /g' *epead_e1ew*09xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*10xy.txt; do sed 's/,/ /g' *epead_e1ew*10xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*11xy.txt; do sed 's/,/ /g' *epead_e1ew*11xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*12xy.txt; do sed 's/,/ /g' *epead_e1ew*12xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*13xy.txt; do sed 's/,/ /g' *epead_e1ew*13xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*14xy.txt; do sed 's/,/ /g' *epead_e1ew*14xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*15xy.txt; do sed 's/,/ /g' *epead_e1ew*15xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*16xy.txt; do sed 's/,/ /g' *epead_e1ew*16xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*17xy.txt; do sed 's/,/ /g' *epead_e1ew*17xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*18xy.txt; do sed 's/,/ /g' *epead_e1ew*18xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*19xy.txt; do sed 's/,/ /g' *epead_e1ew*19xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*20xy.txt; do sed 's/,/ /g' *epead_e1ew*20xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*21xy.txt; do sed 's/,/ /g' *epead_e1ew*21xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*22xy.txt; do sed 's/,/ /g' *epead_e1ew*22xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*23xy.txt; do sed 's/,/ /g' *epead_e1ew*23xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*24xy.txt; do sed 's/,/ /g' *epead_e1ew*24xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*25xy.txt; do sed 's/,/ /g' *epead_e1ew*25xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*26xy.txt; do sed 's/,/ /g' *epead_e1ew*26xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*27xy.txt; do sed 's/,/ /g' *epead_e1ew*27xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*28xy.txt; do sed 's/,/ /g' *epead_e1ew*28xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*29xy.txt; do sed 's/,/ /g' *epead_e1ew*29xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*30xy.txt; do sed 's/,/ /g' *epead_e1ew*30xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e1ew*31xy.txt; do sed 's/,/ /g' *epead_e1ew*31xy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_low_electronfluxgoesepead.dat
rm *z.dat

mv *_low_electronfluxgoesepead.dat /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/electron/low_0.8mev/

#================>=2.0 MeV
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*01.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*01.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*02.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*02.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*03.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*03.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*04.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*04.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*05.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*05.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*06.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*06.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*07.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*07.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*08.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*08.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*09.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*09.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*10.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*10.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*11.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*11.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*12.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*12.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*13.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*13.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*14.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*14.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*15.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*15.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*16.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*16.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*17.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*17.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*18.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*18.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*19.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*19.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*20.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*20.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*21.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*21.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*22.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*22.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*23.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*23.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*24.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*24.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*25.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*25.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*26.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*26.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*27.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*27.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*28.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*28.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*29.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*29.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*30.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*30.csv > ${file/%.csv/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*31.csv; do sed '1,139d' /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*epead_e2ew*31.csv > ${file/%.csv/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/electron/high_2.0mev/${1}/*x.dat .

for file in *epead_e2ew*01x.dat; do cut -d, -f1,6,7 *epead_e2ew*01x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*02x.dat; do cut -d, -f1,6,7 *epead_e2ew*02x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*03x.dat; do cut -d, -f1,6,7 *epead_e2ew*03x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*04x.dat; do cut -d, -f1,6,7 *epead_e2ew*04x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*05x.dat; do cut -d, -f1,6,7 *epead_e2ew*05x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*06x.dat; do cut -d, -f1,6,7 *epead_e2ew*06x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*07x.dat; do cut -d, -f1,6,7 *epead_e2ew*07x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*08x.dat; do cut -d, -f1,6,7 *epead_e2ew*08x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*09x.dat; do cut -d, -f1,6,7 *epead_e2ew*09x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*10x.dat; do cut -d, -f1,6,7 *epead_e2ew*10x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*11x.dat; do cut -d, -f1,6,7 *epead_e2ew*11x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*12x.dat; do cut -d, -f1,6,7 *epead_e2ew*12x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*13x.dat; do cut -d, -f1,6,7 *epead_e2ew*13x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*14x.dat; do cut -d, -f1,6,7 *epead_e2ew*14x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*15x.dat; do cut -d, -f1,6,7 *epead_e2ew*15x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*16x.dat; do cut -d, -f1,6,7 *epead_e2ew*16x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*17x.dat; do cut -d, -f1,6,7 *epead_e2ew*17x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*18x.dat; do cut -d, -f1,6,7 *epead_e2ew*18x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*19x.dat; do cut -d, -f1,6,7 *epead_e2ew*19x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*20x.dat; do cut -d, -f1,6,7 *epead_e2ew*20x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*21x.dat; do cut -d, -f1,6,7 *epead_e2ew*21x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*22x.dat; do cut -d, -f1,6,7 *epead_e2ew*22x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*23x.dat; do cut -d, -f1,6,7 *epead_e2ew*23x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*24x.dat; do cut -d, -f1,6,7 *epead_e2ew*24x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*25x.dat; do cut -d, -f1,6,7 *epead_e2ew*25x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*26x.dat; do cut -d, -f1,6,7 *epead_e2ew*26x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*27x.dat; do cut -d, -f1,6,7 *epead_e2ew*27x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*28x.dat; do cut -d, -f1,6,7 *epead_e2ew*28x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*29x.dat; do cut -d, -f1,6,7 *epead_e2ew*29x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*30x.dat; do cut -d, -f1,6,7 *epead_e2ew*30x.dat > ${file/%.dat/y.txt}; done
for file in *epead_e2ew*31x.dat; do cut -d, -f1,6,7 *epead_e2ew*31x.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in *epead_e2ew*01xy.txt; do sed 's/,/ /g' *epead_e2ew*01xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*02xy.txt; do sed 's/,/ /g' *epead_e2ew*02xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*03xy.txt; do sed 's/,/ /g' *epead_e2ew*03xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*04xy.txt; do sed 's/,/ /g' *epead_e2ew*04xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*05xy.txt; do sed 's/,/ /g' *epead_e2ew*05xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*06xy.txt; do sed 's/,/ /g' *epead_e2ew*06xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*07xy.txt; do sed 's/,/ /g' *epead_e2ew*07xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*08xy.txt; do sed 's/,/ /g' *epead_e2ew*08xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*09xy.txt; do sed 's/,/ /g' *epead_e2ew*09xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*10xy.txt; do sed 's/,/ /g' *epead_e2ew*10xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*11xy.txt; do sed 's/,/ /g' *epead_e2ew*11xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*12xy.txt; do sed 's/,/ /g' *epead_e2ew*12xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*13xy.txt; do sed 's/,/ /g' *epead_e2ew*13xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*14xy.txt; do sed 's/,/ /g' *epead_e2ew*14xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*15xy.txt; do sed 's/,/ /g' *epead_e2ew*15xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*16xy.txt; do sed 's/,/ /g' *epead_e2ew*16xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*17xy.txt; do sed 's/,/ /g' *epead_e2ew*17xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*18xy.txt; do sed 's/,/ /g' *epead_e2ew*18xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*19xy.txt; do sed 's/,/ /g' *epead_e2ew*19xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*20xy.txt; do sed 's/,/ /g' *epead_e2ew*20xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*21xy.txt; do sed 's/,/ /g' *epead_e2ew*21xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*22xy.txt; do sed 's/,/ /g' *epead_e2ew*22xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*23xy.txt; do sed 's/,/ /g' *epead_e2ew*23xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*24xy.txt; do sed 's/,/ /g' *epead_e2ew*24xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*25xy.txt; do sed 's/,/ /g' *epead_e2ew*25xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*26xy.txt; do sed 's/,/ /g' *epead_e2ew*26xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*27xy.txt; do sed 's/,/ /g' *epead_e2ew*27xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*28xy.txt; do sed 's/,/ /g' *epead_e2ew*28xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*29xy.txt; do sed 's/,/ /g' *epead_e2ew*29xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*30xy.txt; do sed 's/,/ /g' *epead_e2ew*30xy.txt > ${file/%.txt/z.dat}; done
for file in *epead_e2ew*31xy.txt; do sed 's/,/ /g' *epead_e2ew*31xy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_high_electronfluxgoesepead.dat
rm *z.dat

mv *_high_electronfluxgoesepead.dat /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/electron/high_2.0mev/