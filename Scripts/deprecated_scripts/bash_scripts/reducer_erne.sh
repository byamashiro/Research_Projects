#!/bin/bash

for i in *.SL2; do
#mkdir "$i-dir"
#cd "$i-dir"
#unzip "../$i"
#tar zxvf "../$i"
cut -d, -f1,2,3,9,10,13,14 "$i" > "../columns/test_$i.dat"
done

exit 0

for j in *; do
mv "$j" "$i.${j##*.}"
cd "$i.${j##*.}"
rm ESU*
rm LED*
rm *.PL2
cp HED* ../../../erne_converted

done
cd ../..
done

rm -rf *.tgz-dir
