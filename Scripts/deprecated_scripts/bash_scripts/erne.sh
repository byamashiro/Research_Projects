#!/bin/bash

for i in *.tgz; do
mkdir "$i-dir"
cd "$i-dir"
#unzip "../$i"
tar zxvf "../$i"

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
