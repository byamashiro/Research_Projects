#!/bin/bash

#./gethet.sh 201106 11Aug
#========STEREO A
wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'AeH'${2}'*.1m' --directory-prefix=. http://www.srl.caltech.edu/STEREO/DATA/HET/Ahead/1minute/
#06Dec.1m
mv /Users/bryanyamashiro/Desktop/HET/AeH${2}.1m /Users/bryanyamashiro/Desktop/HET/originals


#========STEREO A

wget --recursive --level=1 --no-parent --no-directories -e robots=off  --accept 'BeH'${2}'.1m' --directory-prefix=. http://www.srl.caltech.edu/STEREO/DATA/HET/Behind/1minute/
#06Dec.1m
mv /Users/bryanyamashiro/Desktop/HET/BeH${2}.1m /Users/bryanyamashiro/Desktop/HET/originals



#=============================Loading files


rm /Users/bryanyamashiro/Desktop/HET/AeH*.1m
rm /Users/bryanyamashiro/Desktop/HET/BeH*.1m

cp -i /Users/bryanyamashiro/Desktop/HET/originals/AeH${2}.1m .
cp -i /Users/bryanyamashiro/Desktop/HET/originals/BeH${2}.1m .

echo loaded files for analysis

#=============================STEREO A


#=======conversion

sed '1,22d' AeH1*.1m > Aeam.1m #deletes unecessary headers above the data
cat Aeam.1m | tr -s ' ' > Aeamer.1m
cut -f2-5,12-33 -d ' ' Aeamer.1m > Aeamest.1m
awk ' { t = $1; $1 = $2; $2 = t; print; } ' Aeamest.1m > Aeamester.1m

cat Aeamester.1m | awk '{ if ($1 == "Jan") {$1 = "01"}
if ($1 == "Feb") {$1 = "02"}
if ($1 == "Mar") {$1 = "03"}
if ($1 == "Apr") {$1 = "04"}
if ($1 == "May") {$1 = "05"}
if ($1 == "Jun") {$1 = "06"}
if ($1 == "Jul") {$1 = "07"}
if ($1 == "Aug") {$1 = "08"}
if ($1 == "Sep") {$1 = "09"}
if ($1 == "Oct") {$1 = "10"}
if ($1 == "Nov") {$1 = "11"}
if ($1 == "Dec") {$1 = "12"}; print }' > Aeamestest.1m


awk 'BEGIN{OFS=FS=" "}$3<10{$3="0"$3}{print}' Aeamestest.1m > Ary.1m
sed -e "s/\(.............\)\(..\)/\1:\2/" <<< "$4" Ary.1m > Ary1.1m
awk ' { t = $1; $1 = $2; $2 = t; print; } ' Ary1.1m > Ary2.1m
sed 's/^\(.\{4\}\)/\1-/' Ary2.1m > Ary3.1m
sed 's/^\(.\{8\}\)/\1-/' Ary3.1m > Ary3_1.1m
gawk '{print $1 $2 $3" "$4" "$5" "$6" "$7" "$8" "$9" "$10" "$11" "$12" "$13" "$14" "$15" "$16" "$17" "$18" "$19" "$20" "$21" "$22" "$23" "$24" "$25" "$26}'  Ary3_1.1m > ${1}Ahead.1m

rm Aeam.1m
rm Aeamer.1m
rm Aeamest.1m
rm Aeamester.1m
rm Aeamestest.1m
rm Ary.1m
rm Ary1.1m
rm Ary2.1m
rm Ary3.1m
rm Ary3_1.1m

echo Ahead.1m files removed

#=============================STEREO B


#============conversion
sed '1,22d' BeH1*.1m > Beam.1m #deletes unecessary headers above the data
cat Beam.1m | tr -s ' ' > Beamer.1m
cut -f2-5,12-33 -d ' ' Beamer.1m > Beamest.1m
awk ' { t = $1; $1 = $2; $2 = t; print; } ' Beamest.1m > Beamester.1m

cat Beamester.1m | awk '{ if ($1 == "Jan") {$1 = "01"}
if ($1 == "Feb") {$1 = "02"}
if ($1 == "Mar") {$1 = "03"}
if ($1 == "Apr") {$1 = "04"}
if ($1 == "May") {$1 = "05"}
if ($1 == "Jun") {$1 = "06"}
if ($1 == "Jul") {$1 = "07"}
if ($1 == "Aug") {$1 = "08"}
if ($1 == "Sep") {$1 = "09"}
if ($1 == "Oct") {$1 = "10"}
if ($1 == "Nov") {$1 = "11"}
if ($1 == "Dec") {$1 = "12"}; print }' > Beamestest.1m


awk 'BEGIN{OFS=FS=" "}$3<10{$3="0"$3}{print}' Beamestest.1m > Bry.1m
sed -e "s/\(.............\)\(..\)/\1:\2/" <<< "$4" Bry.1m > Bry1.1m
awk ' { t = $1; $1 = $2; $2 = t; print; } ' Bry1.1m > Bry2.1m
sed 's/^\(.\{4\}\)/\1-/' Bry2.1m > Bry3.1m
sed 's/^\(.\{8\}\)/\1-/' Bry3.1m > Bry3_1.1m
gawk '{print $1 $2 $3" "$4" "$5" "$6" "$7" "$8" "$9" "$10" "$11" "$12" "$13" "$14" "$15" "$16" "$17" "$18" "$19" "$20" "$21" "$22" "$23" "$24" "$25" "$26}'  Bry3_1.1m > ${1}Behind.1m



rm Beam.1m
rm Beamer.1m
rm Beamest.1m
rm Beamester.1m
rm Beamestest.1m
rm Bry.1m
rm Bry1.1m
rm Bry2.1m
rm Bry3.1m
rm Bry3_1.1m


echo Behind.1m files removed
#=============================gnuplot
#cp /Users/bryanyamashiro/Desktop/HET/plt/${1}_protonflux.plt .
#gnuplot -e "call '${1}_protonflux.plt' ${1}"
#rm ${1}_protonflux.plt
#echo ${1}protonflux.plt generated

mv *Ahead.1m /Users/bryanyamashiro/Desktop/HET/converted
mv *Behind.1m /Users/bryanyamashiro/Desktop/HET/converted

#mv *.ps /Users/bryanyamashiro/Desktop/HET/loweplots
echo all files moved






