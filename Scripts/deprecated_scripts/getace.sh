#!/bin/bash

#syntax ./getace.sh yyyymm yyyy mm
#ex. ./getace.sh 201106 2011 06

#================================================Download online
#================swepam
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept ''${1}'*_ace_swepam_1m.txt' --directory-prefix=. ftp://sohoftp.nascom.nasa.gov/sdb/goes/ace/daily/

mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/*_ace_swepam_1m.txt /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam

#================mag
#===GOES 13
#wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'g13_hepad_ap_32s_*.csv' --directory-prefix=. http://satdat.ngdc.noaa.gov/sem/goes/data/new_full/${2}/${3}/goes13/csv/
#mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/GOES/${1}
#mv /Users/bryanyamashiro/Desktop/GoddardInternship2/GOES/g13_hepad_ap_32s_*.csv /Users/bryanyamashiro/Desktop/GoddardInternship2/GOES/${1}
#mv /Users/bryanyamashiro/Desktop/GoddardInternship2/GOES/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/GOES/original/Hepad
#===GOES 15
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept ''${1}'*_ace_mag_1m.txt' --directory-prefix=. ftp://sohoftp.nascom.nasa.gov/sdb/goes/ace/daily/
mkdir /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/*_ace_mag_1m.txt /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/${1}
mv /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/${1} /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag




#================================================Conversion
#================swepam

for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}01_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}01_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}02_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}02_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}03_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}03_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}04_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}04_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}05_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}05_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}06_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}06_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}07_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}07_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}08_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}08_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}09_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}09_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}10_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}10_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}11_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}11_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}12_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}12_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}13_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}13_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}14_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}14_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}15_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}15_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}16_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}16_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}17_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}17_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}18_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}18_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}19_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}19_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}20_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}20_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}21_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}21_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}22_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}22_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}23_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}23_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}24_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}24_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}25_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}25_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}26_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}26_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}27_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}27_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}28_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}28_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}29_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}29_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}30_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}30_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}31_ace_swepam_1m.txt; do sed '1,18d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/${1}31_ace_swepam_1m.txt > ${file/%.txt/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/swepam/${1}/*x.dat .

for file in *01_ace_swepam_1mx.dat; do sed 's/  */ /g' *01_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *02_ace_swepam_1mx.dat; do sed 's/  */ /g' *02_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *03_ace_swepam_1mx.dat; do sed 's/  */ /g' *03_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *04_ace_swepam_1mx.dat; do sed 's/  */ /g' *04_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *05_ace_swepam_1mx.dat; do sed 's/  */ /g' *05_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *06_ace_swepam_1mx.dat; do sed 's/  */ /g' *06_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *07_ace_swepam_1mx.dat; do sed 's/  */ /g' *07_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *08_ace_swepam_1mx.dat; do sed 's/  */ /g' *08_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *09_ace_swepam_1mx.dat; do sed 's/  */ /g' *09_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *10_ace_swepam_1mx.dat; do sed 's/  */ /g' *10_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *11_ace_swepam_1mx.dat; do sed 's/  */ /g' *11_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *12_ace_swepam_1mx.dat; do sed 's/  */ /g' *12_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *13_ace_swepam_1mx.dat; do sed 's/  */ /g' *13_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *14_ace_swepam_1mx.dat; do sed 's/  */ /g' *14_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *15_ace_swepam_1mx.dat; do sed 's/  */ /g' *15_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *16_ace_swepam_1mx.dat; do sed 's/  */ /g' *16_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *17_ace_swepam_1mx.dat; do sed 's/  */ /g' *17_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *18_ace_swepam_1mx.dat; do sed 's/  */ /g' *18_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *19_ace_swepam_1mx.dat; do sed 's/  */ /g' *19_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *20_ace_swepam_1mx.dat; do sed 's/  */ /g' *20_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *21_ace_swepam_1mx.dat; do sed 's/  */ /g' *21_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *22_ace_swepam_1mx.dat; do sed 's/  */ /g' *22_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *23_ace_swepam_1mx.dat; do sed 's/  */ /g' *23_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *24_ace_swepam_1mx.dat; do sed 's/  */ /g' *24_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *25_ace_swepam_1mx.dat; do sed 's/  */ /g' *25_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *26_ace_swepam_1mx.dat; do sed 's/  */ /g' *26_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *27_ace_swepam_1mx.dat; do sed 's/  */ /g' *27_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *28_ace_swepam_1mx.dat; do sed 's/  */ /g' *28_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *29_ace_swepam_1mx.dat; do sed 's/  */ /g' *29_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *30_ace_swepam_1mx.dat; do sed 's/  */ /g' *30_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done
for file in *31_ace_swepam_1mx.dat; do sed 's/  */ /g' *31_ace_swepam_1mx.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in *01_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *01_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *02_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *02_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *03_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *03_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *04_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *04_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *05_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *05_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *06_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *06_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *07_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *07_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *08_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *08_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *09_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *09_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *10_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *10_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *11_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *11_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *12_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *12_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *13_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *13_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *14_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *14_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *15_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *15_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *16_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *16_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *17_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *17_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *18_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *18_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *19_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *19_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *20_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *20_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *21_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *21_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *22_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *22_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *23_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *23_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *24_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *24_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *25_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *25_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *26_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *26_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *27_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *27_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *28_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *28_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *29_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *29_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *30_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *30_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *31_ace_swepam_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *31_ace_swepam_1mxy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_aceswepam.dat
rm *z.dat

mv *_aceswepam.dat /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam
sed -e "s/\(.............\)\(..\)/\1:\2/" <<< "$4" /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam1.dat
sed 's/^\(.\{4\}\)/\1-/' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam1.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam2.dat
sed 's/^\(.\{8\}\)/\1-/' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam2.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam1.dat
gawk '{print $1 $2 $3" "$4" "$5" "$6" "$7}'  /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam1.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam.dat
rm /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam1.dat
rm /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/swepam/${1}_aceswepam2.dat


#================mag

for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}01_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}01_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}02_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}02_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}03_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}03_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}04_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}04_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}05_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}05_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}06_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}06_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}07_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}07_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}08_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}08_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}09_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}09_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}10_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}10_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}11_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}11_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}12_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}12_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}13_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}13_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}14_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}14_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}15_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}15_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}16_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}16_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}17_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}17_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}18_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}18_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}19_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}19_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}20_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}20_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}21_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}21_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}22_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}22_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}23_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}23_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}24_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}24_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}25_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}25_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}26_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}26_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}27_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}27_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}28_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}28_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}29_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}29_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}30_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}30_ace_mag_1m.txt > ${file/%.txt/x.dat}; done
for file in /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}31_ace_mag_1m.txt; do sed '1,20d' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/${1}31_ace_mag_1m.txt > ${file/%.txt/x.dat}; done

mv /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/original/mag/${1}/*x.dat .

for file in *01_ace_mag_1mx.dat; do sed 's/  */ /g' *01_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *02_ace_mag_1mx.dat; do sed 's/  */ /g' *02_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *03_ace_mag_1mx.dat; do sed 's/  */ /g' *03_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *04_ace_mag_1mx.dat; do sed 's/  */ /g' *04_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *05_ace_mag_1mx.dat; do sed 's/  */ /g' *05_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *06_ace_mag_1mx.dat; do sed 's/  */ /g' *06_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *07_ace_mag_1mx.dat; do sed 's/  */ /g' *07_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *08_ace_mag_1mx.dat; do sed 's/  */ /g' *08_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *09_ace_mag_1mx.dat; do sed 's/  */ /g' *09_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *10_ace_mag_1mx.dat; do sed 's/  */ /g' *10_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *11_ace_mag_1mx.dat; do sed 's/  */ /g' *11_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *12_ace_mag_1mx.dat; do sed 's/  */ /g' *12_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *13_ace_mag_1mx.dat; do sed 's/  */ /g' *13_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *14_ace_mag_1mx.dat; do sed 's/  */ /g' *14_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *15_ace_mag_1mx.dat; do sed 's/  */ /g' *15_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *16_ace_mag_1mx.dat; do sed 's/  */ /g' *16_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *17_ace_mag_1mx.dat; do sed 's/  */ /g' *17_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *18_ace_mag_1mx.dat; do sed 's/  */ /g' *18_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *19_ace_mag_1mx.dat; do sed 's/  */ /g' *19_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *20_ace_mag_1mx.dat; do sed 's/  */ /g' *20_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *21_ace_mag_1mx.dat; do sed 's/  */ /g' *21_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *22_ace_mag_1mx.dat; do sed 's/  */ /g' *22_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *23_ace_mag_1mx.dat; do sed 's/  */ /g' *23_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *24_ace_mag_1mx.dat; do sed 's/  */ /g' *24_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *25_ace_mag_1mx.dat; do sed 's/  */ /g' *25_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *26_ace_mag_1mx.dat; do sed 's/  */ /g' *26_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *27_ace_mag_1mx.dat; do sed 's/  */ /g' *27_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *28_ace_mag_1mx.dat; do sed 's/  */ /g' *28_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *29_ace_mag_1mx.dat; do sed 's/  */ /g' *29_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *30_ace_mag_1mx.dat; do sed 's/  */ /g' *30_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done
for file in *31_ace_mag_1mx.dat; do sed 's/  */ /g' *31_ace_mag_1mx.dat > ${file/%.dat/y.txt}; done


rm *x.dat

for file in *01_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *01_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *02_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *02_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *03_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *03_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *04_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *04_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *05_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *05_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *06_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *06_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *07_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *07_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *08_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *08_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *09_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *09_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *10_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *10_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *11_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *11_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *12_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *12_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *13_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *13_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *14_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *14_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *15_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *15_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *16_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *16_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *17_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *17_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *18_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *18_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *19_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *19_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *20_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *20_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *21_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *21_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *22_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *22_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *23_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *23_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *24_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *24_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *25_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *25_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *26_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *26_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *27_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *27_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *28_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *28_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *29_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *29_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *30_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *30_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done
for file in *31_ace_mag_1mxy.txt; do cut -d' ' -f1,2,3,4,8,9,10 *31_ace_mag_1mxy.txt > ${file/%.txt/z.dat}; done

rm *y.txt

cat *z.dat > ${1}_acemag.dat
rm *z.dat

mv *_acemag.dat /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag
sed -e "s/\(.............\)\(..\)/\1:\2/" <<< "$4" /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag1.dat
sed 's/^\(.\{4\}\)/\1-/' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag1.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag2.dat
sed 's/^\(.\{8\}\)/\1-/' /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag2.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag1.dat
gawk '{print $1 $2 $3" "$4" "$5" "$6" "$7}'  /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag1.dat > /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag.dat
rm /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag1.dat
rm /Users/bryanyamashiro/Desktop/GoddardInternship2/ACEWIND/converted/mag/${1}_acemag2.dat