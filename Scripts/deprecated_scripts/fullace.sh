#!/bin/bash

#syntax ./getgoes.sh yyyymm yyyy mm
#ex. ./getgoes.sh 201106 2011 06
#WARNING COLUMNS NEED TO BE +1 DUE TO EXTRA ADDED INITIAL COLUMN $3

#================================================Conversion
#================mag magnetic field (ace)
rm -f *.txt
cp /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/original/fulldatal2/mag${1}.txt .
sed '1,60d' mag${1}.txt > mag1.txt #deletes unecessary shit above the data
cat mag1.txt | tr -s ' ' > mag2.txt

sed 's|\([0-9]*\)-\([0-9]*\)-\([0-9]*\).*|\3-\2-\1|' mag2.txt > mag3.txt
paste -d' ' mag3.txt mag2.txt > mag4.txt
cut -d' ' -f1,3,4,5,6 mag4.txt > magfinal${1}.txt
mv magfinal${1}.txt /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full
echo ''${1}' Magnetic field data reduced'

#================absolute mag magnetic field (ace)
rm -f *.txt
cp /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/original/fulldatal2/absmag${1}.txt .
sed '1,59d' absmag${1}.txt > absmag1.txt #deletes unecessary shit above the data
cat absmag1.txt | tr -s ' ' > absmag2.txt

sed 's|\([0-9]*\)-\([0-9]*\)-\([0-9]*\).*|\3-\2-\1|' absmag2.txt > absmag3.txt
paste -d' ' absmag3.txt absmag2.txt > absmag4.txt
cut -d' ' -f1,3,4 absmag4.txt > absmagfinal${1}.txt
mv absmagfinal${1}.txt /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full
echo ''${1}' Absolute Magnetic field data reduced'

#================swepam solar wind (ace) particle energies 0.26-36 KeV (ions)
rm -f *.txt
cp /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/original/fulldatal2/swepam${1}.txt .
sed '1,62d' swepam${1}.txt > swepam1.txt #deletes unecessary shit above the data
cat swepam1.txt | tr -s ' ' > swepam2.txt

sed 's|\([0-9]*\)-\([0-9]*\)-\([0-9]*\).*|\3-\2-\1|' swepam2.txt > swepam3.txt
paste -d' ' swepam3.txt swepam2.txt > swepam4.txt
cut -d' ' -f1,3,4 swepam4.txt > swepamfinal${1}.txt
mv swepamfinal${1}.txt /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full
echo ''${1}' ACE solar wind data reduced'

#================wind solar wind (wind) 7-24.8 kV (ions)
rm -f *.txt
cp /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/original/fulldatal2/windswe${1}.txt .
sed '1,68d' windswe${1}.txt > windswe1.txt #deletes unecessary shit above the data
cat windswe1.txt | tr -s ' ' > windswe2.txt

sed 's|\([0-9]*\)-\([0-9]*\)-\([0-9]*\).*|\3-\2-\1|' windswe2.txt > windswe3.txt
paste -d' ' windswe3.txt windswe2.txt > windswe4.txt
cut -d' ' -f1,3,5 windswe4.txt > windswefinal${1}.txt
mv windswefinal${1}.txt /Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full
echo ''${1}' WIND solar wind data reduced'

rm *.txt