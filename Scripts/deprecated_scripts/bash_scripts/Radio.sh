#!/bin/bash

# ./Radio.sh 201106 15 100 17-05-2012
# WIND Frequencies from 20 kHz to 1000 kHz

rm 201*_*.txt #reset all of the txt files

#for file in /Users/bryanyamashiro/Desktop/Type3/original/${1}.txt; do sed '1,37d' /Users/bryanyamashiro/Desktop/Type3/original/stereo${1}.txt > ${1}_1.txt; done # delete all the top row crap #on computer
#==================WIND 36-44 kHz

#for file in /Users/bryanyamashiro/Desktop/Type3/original/wind${1}.txt; do sed '1,40d' /Users/bryanyamashiro/Desktop/Type3/original/wind${1}.txt > ${1}_1.txt; done #remove header rows on computer

for file in /Volumes/r2fisher4/type3originals/wind${1}.txt; do sed '1,40d' /Volumes/r2fisher4/type3originals/wind${1}.txt > ${1}_1.txt; done #remove header rows on hardrive

#grep -e '^report\|^-th\|^-to' filename
grep -e '^'${4}'' ${1}_1.txt > ${1}_1_1.txt

cat ${1}_1_1.txt | tr -s ' ' > ${1}_2.txt #delimit with space
cut -f1-2,3-248 -d ' ' ${1}_2.txt > ${1}_3.txt #remove columns that are not in the threshold

#======================================Over 100 intensity

awk 'BEGIN { OFS = " "; }; { if ($3 > '${3}') $3 = NaN; else $3 = $3; }; 1' ${1}_3.txt > ${1}_4_2.txt #more inefficient threshold clipping !!! NEEDS TO BE MORE EFFICIENT
awk 'BEGIN { OFS = " "; }; { if ($4 > '${3}') $4 = NaN; else $4 = $4; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($5 > '${3}') $5 = NaN; else $5 = $5; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($6 > '${3}') $6 = NaN; else $6 = $6; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($7 > '${3}') $7 = NaN; else $7 = $7; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($8 > '${3}') $8 = NaN; else $8 = $8; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($9 > '${3}') $9 = NaN; else $9 = $9; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($10 > '${3}') $10 = NaN; else $10 = $10; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($11 > '${3}') $11 = NaN; else $11 = $11; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($12 > '${3}') $12 = NaN; else $12 = $12; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($13 > '${3}') $13 = NaN; else $13 = $13; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($14 > '${3}') $14 = NaN; else $14 = $14; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($15 > '${3}') $15 = NaN; else $15 = $15; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($16 > '${3}') $16 = NaN; else $16 = $16; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($17 > '${3}') $17 = NaN; else $17 = $17; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($18 > '${3}') $18 = NaN; else $18 = $18; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($19 > '${3}') $19 = NaN; else $19 = $19; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($20 > '${3}') $20 = NaN; else $20 = $20; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($21 > '${3}') $21 = NaN; else $21 = $21; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($22 > '${3}') $22 = NaN; else $22 = $22; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($23 > '${3}') $23 = NaN; else $23 = $23; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($24 > '${3}') $24 = NaN; else $24 = $24; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($25 > '${3}') $25 = NaN; else $25 = $25; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($26 > '${3}') $26 = NaN; else $26 = $26; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($27 > '${3}') $27 = NaN; else $27 = $27; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($28 > '${3}') $28 = NaN; else $28 = $28; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($29 > '${3}') $29 = NaN; else $29 = $29; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($30 > '${3}') $30 = NaN; else $30 = $30; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($31 > '${3}') $31 = NaN; else $31 = $31; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($32 > '${3}') $32 = NaN; else $32 = $32; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($33 > '${3}') $33 = NaN; else $33 = $33; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($34 > '${3}') $34 = NaN; else $34 = $34; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($35 > '${3}') $35 = NaN; else $35 = $35; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($36 > '${3}') $36 = NaN; else $36 = $36; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($37 > '${3}') $37 = NaN; else $37 = $37; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($38 > '${3}') $38 = NaN; else $38 = $38; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($39 > '${3}') $39 = NaN; else $39 = $39; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($40 > '${3}') $40 = NaN; else $40 = $40; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($41 > '${3}') $41 = NaN; else $41 = $41; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($42 > '${3}') $42 = NaN; else $42 = $42; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($43 > '${3}') $43 = NaN; else $43 = $43; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($44 > '${3}') $44 = NaN; else $44 = $44; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($45 > '${3}') $45 = NaN; else $45 = $45; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($46 > '${3}') $46 = NaN; else $46 = $46; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($47 > '${3}') $47 = NaN; else $47 = $47; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($48 > '${3}') $48 = NaN; else $48 = $48; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($49 > '${3}') $49 = NaN; else $49 = $49; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($50 > '${3}') $50 = NaN; else $50 = $50; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($51 > '${3}') $51 = NaN; else $51 = $51; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($52 > '${3}') $52 = NaN; else $52 = $52; }; 1' ${1}_4_2.txt > ${1}_4_1_extra_1.txt #rookie mistakes well covered up
awk 'BEGIN { OFS = " "; }; { if ($53 > '${3}') $53 = NaN; else $53 = $53; }; 1' ${1}_4_1_extra_1.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($54 > '${3}') $54 = NaN; else $54 = $54; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($55 > '${3}') $55 = NaN; else $55 = $55; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($56 > '${3}') $56 = NaN; else $56 = $56; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($57 > '${3}') $57 = NaN; else $57 = $57; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($58 > '${3}') $58 = NaN; else $58 = $58; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($59 > '${3}') $59 = NaN; else $59 = $59; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($60 > '${3}') $60 = NaN; else $60 = $60; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($61 > '${3}') $61 = NaN; else $61 = $61; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($62 > '${3}') $62 = NaN; else $62 = $62; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($63 > '${3}') $63 = NaN; else $63 = $63; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($64 > '${3}') $64 = NaN; else $64 = $64; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($65 > '${3}') $65 = NaN; else $65 = $65; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($66 > '${3}') $66 = NaN; else $66 = $66; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($67 > '${3}') $67 = NaN; else $67 = $67; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($68 > '${3}') $68 = NaN; else $68 = $68; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($69 > '${3}') $69 = NaN; else $69 = $69; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($70 > '${3}') $70 = NaN; else $70 = $70; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($71 > '${3}') $71 = NaN; else $71 = $71; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($72 > '${3}') $72 = NaN; else $72 = $72; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($73 > '${3}') $73 = NaN; else $73 = $73; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($74 > '${3}') $74 = NaN; else $74 = $74; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($75 > '${3}') $75 = NaN; else $75 = $75; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($76 > '${3}') $76 = NaN; else $76 = $76; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($77 > '${3}') $77 = NaN; else $77 = $77; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($78 > '${3}') $78 = NaN; else $78 = $78; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($79 > '${3}') $79 = NaN; else $79 = $79; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($80 > '${3}') $80 = NaN; else $80 = $80; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($81 > '${3}') $81 = NaN; else $81 = $81; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($82 > '${3}') $82 = NaN; else $82 = $82; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($83 > '${3}') $83 = NaN; else $83 = $83; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($84 > '${3}') $84 = NaN; else $84 = $84; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($85 > '${3}') $85 = NaN; else $85 = $85; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($86 > '${3}') $86 = NaN; else $86 = $86; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($87 > '${3}') $87 = NaN; else $87 = $87; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($88 > '${3}') $88 = NaN; else $88 = $88; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($89 > '${3}') $89 = NaN; else $89 = $89; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($90 > '${3}') $90 = NaN; else $90 = $90; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($91 > '${3}') $91 = NaN; else $91 = $91; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($92 > '${3}') $92 = NaN; else $92 = $92; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($93 > '${3}') $93 = NaN; else $93 = $93; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($94 > '${3}') $94 = NaN; else $94 = $94; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($95 > '${3}') $95 = NaN; else $95 = $95; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake 2-/->2
awk 'BEGIN { OFS = " "; }; { if ($96 > '${3}') $96 = NaN; else $96 = $96; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($97 > '${3}') $97 = NaN; else $97 = $97; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($98 > '${3}') $98 = NaN; else $98 = $98; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($99 > '${3}') $99 = NaN; else $99 = $99; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($100 > '${3}') $100 = NaN; else $100 = $100; }; 1' ${1}_4_2.txt > ${1}_4_1_extra_2.txt #more rookie mistakes, look the other way
awk 'BEGIN { OFS = " "; }; { if ($101 > '${3}') $101 = NaN; else $101 = $101; }; 1' ${1}_4_1_extra_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($102 > '${3}') $102 = NaN; else $102 = $102; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($103 > '${3}') $103 = NaN; else $103 = $103; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($104 > '${3}') $104 = NaN; else $104 = $104; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($105 > '${3}') $105 = NaN; else $105 = $105; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($106 > '${3}') $106 = NaN; else $106 = $106; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($107 > '${3}') $107 = NaN; else $107 = $107; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($108 > '${3}') $108 = NaN; else $108 = $108; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($109 > '${3}') $109 = NaN; else $109 = $109; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($110 > '${3}') $110 = NaN; else $110 = $110; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($111 > '${3}') $111 = NaN; else $111 = $111; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($112 > '${3}') $112 = NaN; else $112 = $112; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($113 > '${3}') $113 = NaN; else $113 = $113; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($114 > '${3}') $114 = NaN; else $114 = $114; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($115 > '${3}') $115 = NaN; else $115 = $115; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($116 > '${3}') $116 = NaN; else $116 = $116; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($117 > '${3}') $117 = NaN; else $117 = $117; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($118 > '${3}') $118 = NaN; else $118 = $118; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($119 > '${3}') $119 = NaN; else $119 = $119; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($120 > '${3}') $120 = NaN; else $120 = $120; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($121 > '${3}') $121 = NaN; else $121 = $121; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($122 > '${3}') $122 = NaN; else $122 = $122; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($123 > '${3}') $123 = NaN; else $123 = $123; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($124 > '${3}') $124 = NaN; else $124 = $124; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($125 > '${3}') $125 = NaN; else $125 = $125; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($126 > '${3}') $126 = NaN; else $126 = $126; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($127 > '${3}') $127 = NaN; else $127 = $127; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($128 > '${3}') $128 = NaN; else $128 = $128; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($129 > '${3}') $129 = NaN; else $129 = $129; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($130 > '${3}') $130 = NaN; else $130 = $130; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($131 > '${3}') $131 = NaN; else $131 = $131; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($132 > '${3}') $132 = NaN; else $132 = $132; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($133 > '${3}') $133 = NaN; else $133 = $133; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($134 > '${3}') $134 = NaN; else $134 = $134; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($135 > '${3}') $135 = NaN; else $135 = $135; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($136 > '${3}') $136 = NaN; else $136 = $136; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($137 > '${3}') $137 = NaN; else $137 = $137; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($138 > '${3}') $138 = NaN; else $138 = $138; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($139 > '${3}') $139 = NaN; else $139 = $139; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($140 > '${3}') $140 = NaN; else $140 = $140; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($141 > '${3}') $141 = NaN; else $141 = $141; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($142 > '${3}') $142 = NaN; else $142 = $142; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($143 > '${3}') $143 = NaN; else $143 = $143; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($144 > '${3}') $144 = NaN; else $144 = $144; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($145 > '${3}') $145 = NaN; else $145 = $145; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($146 > '${3}') $146 = NaN; else $146 = $146; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($147 > '${3}') $147 = NaN; else $147 = $147; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($148 > '${3}') $148 = NaN; else $148 = $148; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($149 > '${3}') $149 = NaN; else $149 = $149; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($150 > '${3}') $150 = NaN; else $150 = $150; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($151 > '${3}') $151 = NaN; else $151 = $151; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($152 > '${3}') $152 = NaN; else $152 = $152; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($153 > '${3}') $153 = NaN; else $153 = $153; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($154 > '${3}') $154 = NaN; else $154 = $154; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($155 > '${3}') $155 = NaN; else $155 = $155; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($156 > '${3}') $156 = NaN; else $156 = $156; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($157 > '${3}') $157 = NaN; else $157 = $157; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($158 > '${3}') $158 = NaN; else $158 = $158; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($159 > '${3}') $159 = NaN; else $159 = $159; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($160 > '${3}') $160 = NaN; else $160 = $160; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($161 > '${3}') $161 = NaN; else $161 = $161; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($162 > '${3}') $162 = NaN; else $162 = $162; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($163 > '${3}') $163 = NaN; else $163 = $163; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($164 > '${3}') $164 = NaN; else $164 = $164; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($165 > '${3}') $165 = NaN; else $165 = $165; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($166 > '${3}') $166 = NaN; else $166 = $166; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($167 > '${3}') $167 = NaN; else $167 = $167; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($168 > '${3}') $168 = NaN; else $168 = $168; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($169 > '${3}') $169 = NaN; else $169 = $169; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($170 > '${3}') $170 = NaN; else $170 = $170; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($171 > '${3}') $171 = NaN; else $171 = $171; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($172 > '${3}') $172 = NaN; else $172 = $172; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($173 > '${3}') $173 = NaN; else $173 = $173; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($174 > '${3}') $174 = NaN; else $174 = $174; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($175 > '${3}') $175 = NaN; else $175 = $175; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($176 > '${3}') $176 = NaN; else $176 = $176; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($177 > '${3}') $177 = NaN; else $177 = $177; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($178 > '${3}') $178 = NaN; else $178 = $178; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($179 > '${3}') $179 = NaN; else $179 = $179; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($180 > '${3}') $180 = NaN; else $180 = $180; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($181 > '${3}') $181 = NaN; else $181 = $181; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($182 > '${3}') $182 = NaN; else $182 = $182; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($183 > '${3}') $183 = NaN; else $183 = $183; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($184 > '${3}') $184 = NaN; else $184 = $184; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($185 > '${3}') $185 = NaN; else $185 = $185; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($186 > '${3}') $186 = NaN; else $186 = $186; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($187 > '${3}') $187 = NaN; else $187 = $187; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($188 > '${3}') $188 = NaN; else $188 = $188; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($189 > '${3}') $189 = NaN; else $189 = $189; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($190 > '${3}') $190 = NaN; else $190 = $190; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($191 > '${3}') $191 = NaN; else $191 = $191; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($192 > '${3}') $192 = NaN; else $192 = $192; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($193 > '${3}') $193 = NaN; else $193 = $193; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($194 > '${3}') $194 = NaN; else $194 = $194; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($195 > '${3}') $195 = NaN; else $195 = $195; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($196 > '${3}') $196 = NaN; else $196 = $196; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($197 > '${3}') $197 = NaN; else $197 = $197; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($198 > '${3}') $198 = NaN; else $198 = $198; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($199 > '${3}') $199 = NaN; else $199 = $199; }; 1' ${1}_4_2.txt > ${1}_4_1_extra_3.txt #another rookie mistake
awk 'BEGIN { OFS = " "; }; { if ($200 > '${3}') $200 = NaN; else $200 = $200; }; 1' ${1}_4_1_extra_3.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($201 > '${3}') $201 = NaN; else $201 = $201; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($202 > '${3}') $202 = NaN; else $202 = $202; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($203 > '${3}') $203 = NaN; else $203 = $203; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($204 > '${3}') $204 = NaN; else $204 = $204; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($205 > '${3}') $205 = NaN; else $205 = $205; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($206 > '${3}') $206 = NaN; else $206 = $206; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($207 > '${3}') $207 = NaN; else $207 = $207; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($208 > '${3}') $208 = NaN; else $208 = $208; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($209 > '${3}') $209 = NaN; else $209 = $209; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($210 > '${3}') $210 = NaN; else $210 = $210; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($211 > '${3}') $211 = NaN; else $211 = $211; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($212 > '${3}') $212 = NaN; else $212 = $212; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($213 > '${3}') $213 = NaN; else $213 = $213; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($214 > '${3}') $214 = NaN; else $214 = $214; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($215 > '${3}') $215 = NaN; else $215 = $215; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($216 > '${3}') $216 = NaN; else $216 = $216; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($217 > '${3}') $217 = NaN; else $217 = $217; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($218 > '${3}') $218 = NaN; else $218 = $218; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($219 > '${3}') $219 = NaN; else $219 = $219; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($220 > '${3}') $220 = NaN; else $220 = $220; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($221 > '${3}') $221 = NaN; else $221 = $221; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($222 > '${3}') $222 = NaN; else $222 = $222; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($223 > '${3}') $223 = NaN; else $223 = $223; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($224 > '${3}') $224 = NaN; else $224 = $224; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($225 > '${3}') $225 = NaN; else $225 = $225; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($226 > '${3}') $226 = NaN; else $226 = $226; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($227 > '${3}') $227 = NaN; else $227 = $227; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($228 > '${3}') $228 = NaN; else $228 = $228; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
#=========================================includes lower frequencies up to row 248
awk 'BEGIN { OFS = " "; }; { if ($229 > '${3}') $229 = NaN; else $229 = $229; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($230 > '${3}') $230 = NaN; else $230 = $230; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($231 > '${3}') $231 = NaN; else $231 = $231; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($232 > '${3}') $232 = NaN; else $232 = $232; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($233 > '${3}') $233 = NaN; else $233 = $233; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($234 > '${3}') $234 = NaN; else $234 = $234; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($235 > '${3}') $235 = NaN; else $235 = $235; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($236 > '${3}') $236 = NaN; else $236 = $236; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($237 > '${3}') $237 = NaN; else $237 = $237; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($238 > '${3}') $238 = NaN; else $238 = $238; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($239 > '${3}') $239 = NaN; else $239 = $239; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($240 > '${3}') $240 = NaN; else $240 = $240; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($241 > '${3}') $241 = NaN; else $241 = $241; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($242 > '${3}') $242 = NaN; else $242 = $242; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($243 > '${3}') $243 = NaN; else $243 = $243; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($244 > '${3}') $244 = NaN; else $244 = $244; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($245 > '${3}') $245 = NaN; else $245 = $245; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($246 > '${3}') $246 = NaN; else $246 = $246; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($247 > '${3}') $247 = NaN; else $247 = $247; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($248 > '${3}') $248 = NaN; else $248 = $248; }; 1' ${1}_4_2.txt > ${1}_4_1.txt

cp /Users/bryanyamashiro/Desktop/RadioBurst/${1}_4_1.txt /Users/bryanyamashiro/Desktop/RadioBurst/converted/ 


#=====================================Under 10 intensity supress

awk 'BEGIN { OFS = " "; }; { if ($3 < '${2}') $3 = 1.0; else $3 = $3; }; 1' ${1}_4_1.txt > ${1}_4_2.txt #more inefficient threshold clipping !!! NEEDS TO BE MORE EFFICIENT
awk 'BEGIN { OFS = " "; }; { if ($4 < '${2}') $4 = 1.0; else $4 = $4; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($5 < '${2}') $5 = 1.0; else $5 = $5; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($6 < '${2}') $6 = 1.0; else $6 = $6; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($7 < '${2}') $7 = 1.0; else $7 = $7; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($8 < '${2}') $8 = 1.0; else $8 = $8; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($9 < '${2}') $9 = 1.0; else $9 = $9; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($10 < '${2}') $10 = 1.0; else $10 = $10; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($11 < '${2}') $11 = 1.0; else $11 = $11; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($12 < '${2}') $12 = 1.0; else $12 = $12; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($13 < '${2}') $13 = 1.0; else $13 = $13; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($14 < '${2}') $14 = 1.0; else $14 = $14; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($15 < '${2}') $15 = 1.0; else $15 = $15; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($16 < '${2}') $16 = 1.0; else $16 = $16; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($17 < '${2}') $17 = 1.0; else $17 = $17; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($18 < '${2}') $18 = 1.0; else $18 = $18; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($19 < '${2}') $19 = 1.0; else $19 = $19; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($20 < '${2}') $20 = 1.0; else $20 = $20; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($21 < '${2}') $21 = 1.0; else $21 = $21; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($22 < '${2}') $22 = 1.0; else $22 = $22; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($23 < '${2}') $23 = 1.0; else $23 = $23; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($24 < '${2}') $24 = 1.0; else $24 = $24; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($25 < '${2}') $25 = 1.0; else $25 = $25; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($26 < '${2}') $26 = 1.0; else $26 = $26; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($27 < '${2}') $27 = 1.0; else $27 = $27; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($28 < '${2}') $28 = 1.0; else $28 = $28; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($29 < '${2}') $29 = 1.0; else $29 = $29; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($30 < '${2}') $30 = 1.0; else $30 = $30; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($31 < '${2}') $31 = 1.0; else $31 = $31; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($32 < '${2}') $32 = 1.0; else $32 = $32; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($33 < '${2}') $33 = 1.0; else $33 = $33; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($34 < '${2}') $34 = 1.0; else $34 = $34; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($35 < '${2}') $35 = 1.0; else $35 = $35; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($36 < '${2}') $36 = 1.0; else $36 = $36; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($37 < '${2}') $37 = 1.0; else $37 = $37; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($38 < '${2}') $38 = 1.0; else $38 = $38; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($39 < '${2}') $39 = 1.0; else $39 = $39; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($40 < '${2}') $40 = 1.0; else $40 = $40; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($41 < '${2}') $41 = 1.0; else $41 = $41; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($42 < '${2}') $42 = 1.0; else $42 = $42; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($43 < '${2}') $43 = 1.0; else $43 = $43; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($44 < '${2}') $44 = 1.0; else $44 = $44; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($45 < '${2}') $45 = 1.0; else $45 = $45; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($46 < '${2}') $46 = 1.0; else $46 = $46; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($47 < '${2}') $47 = 1.0; else $47 = $47; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($48 < '${2}') $48 = 1.0; else $48 = $48; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($49 < '${2}') $49 = 1.0; else $49 = $49; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($50 < '${2}') $50 = 1.0; else $50 = $50; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($51 < '${2}') $51 = 1.0; else $51 = $51; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($52 < '${2}') $52 = 1.0; else $52 = $52; }; 1' ${1}_4_2.txt > ${1}_4_1_extra_1.txt #rookie mistakes well covered up
awk 'BEGIN { OFS = " "; }; { if ($53 < '${2}') $53 = 1.0; else $53 = $53; }; 1' ${1}_4_1_extra_1.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($54 < '${2}') $54 = 1.0; else $54 = $54; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($55 < '${2}') $55 = 1.0; else $55 = $55; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($56 < '${2}') $56 = 1.0; else $56 = $56; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($57 < '${2}') $57 = 1.0; else $57 = $57; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($58 < '${2}') $58 = 1.0; else $58 = $58; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($59 < '${2}') $59 = 1.0; else $59 = $59; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($60 < '${2}') $60 = 1.0; else $60 = $60; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($61 < '${2}') $61 = 1.0; else $61 = $61; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($62 < '${2}') $62 = 1.0; else $62 = $62; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($63 < '${2}') $63 = 1.0; else $63 = $63; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($64 < '${2}') $64 = 1.0; else $64 = $64; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($65 < '${2}') $65 = 1.0; else $65 = $65; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($66 < '${2}') $66 = 1.0; else $66 = $66; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($67 < '${2}') $67 = 1.0; else $67 = $67; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($68 < '${2}') $68 = 1.0; else $68 = $68; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($69 < '${2}') $69 = 1.0; else $69 = $69; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($70 < '${2}') $70 = 1.0; else $70 = $70; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($71 < '${2}') $71 = 1.0; else $71 = $71; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($72 < '${2}') $72 = 1.0; else $72 = $72; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($73 < '${2}') $73 = 1.0; else $73 = $73; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($74 < '${2}') $74 = 1.0; else $74 = $74; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($75 < '${2}') $75 = 1.0; else $75 = $75; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($76 < '${2}') $76 = 1.0; else $76 = $76; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($77 < '${2}') $77 = 1.0; else $77 = $77; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($78 < '${2}') $78 = 1.0; else $78 = $78; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($79 < '${2}') $79 = 1.0; else $79 = $79; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($80 < '${2}') $80 = 1.0; else $80 = $80; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($81 < '${2}') $81 = 1.0; else $81 = $81; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($82 < '${2}') $82 = 1.0; else $82 = $82; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($83 < '${2}') $83 = 1.0; else $83 = $83; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($84 < '${2}') $84 = 1.0; else $84 = $84; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($85 < '${2}') $85 = 1.0; else $85 = $85; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($86 < '${2}') $86 = 1.0; else $86 = $86; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($87 < '${2}') $87 = 1.0; else $87 = $87; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($88 < '${2}') $88 = 1.0; else $88 = $88; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($89 < '${2}') $89 = 1.0; else $89 = $89; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($90 < '${2}') $90 = 1.0; else $90 = $90; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($91 < '${2}') $91 = 1.0; else $91 = $91; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($92 < '${2}') $92 = 1.0; else $92 = $92; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($93 < '${2}') $93 = 1.0; else $93 = $93; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($94 < '${2}') $94 = 1.0; else $94 = $94; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($95 < '${2}') $95 = 1.0; else $95 = $95; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake 2-/->2
awk 'BEGIN { OFS = " "; }; { if ($96 < '${2}') $96 = 1.0; else $96 = $96; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($97 < '${2}') $97 = 1.0; else $97 = $97; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($98 < '${2}') $98 = 1.0; else $98 = $98; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($99 < '${2}') $99 = 1.0; else $99 = $99; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($100 < '${2}') $100 = 1.0; else $100 = $100; }; 1' ${1}_4_2.txt > ${1}_4_1_extra_2.txt #more rookie mistakes, look the other way
awk 'BEGIN { OFS = " "; }; { if ($101 < '${2}') $101 = 1.0; else $101 = $101; }; 1' ${1}_4_1_extra_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($102 < '${2}') $102 = 1.0; else $102 = $102; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($103 < '${2}') $103 = 1.0; else $103 = $103; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($104 < '${2}') $104 = 1.0; else $104 = $104; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($105 < '${2}') $105 = 1.0; else $105 = $105; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($106 < '${2}') $106 = 1.0; else $106 = $106; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($107 < '${2}') $107 = 1.0; else $107 = $107; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($108 < '${2}') $108 = 1.0; else $108 = $108; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($109 < '${2}') $109 = 1.0; else $109 = $109; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($110 < '${2}') $110 = 1.0; else $110 = $110; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($111 < '${2}') $111 = 1.0; else $111 = $111; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($112 < '${2}') $112 = 1.0; else $112 = $112; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($113 < '${2}') $113 = 1.0; else $113 = $113; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($114 < '${2}') $114 = 1.0; else $114 = $114; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($115 < '${2}') $115 = 1.0; else $115 = $115; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($116 < '${2}') $116 = 1.0; else $116 = $116; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($117 < '${2}') $117 = 1.0; else $117 = $117; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($118 < '${2}') $118 = 1.0; else $118 = $118; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($119 < '${2}') $119 = 1.0; else $119 = $119; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($120 < '${2}') $120 = 1.0; else $120 = $120; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($121 < '${2}') $121 = 1.0; else $121 = $121; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($122 < '${2}') $122 = 1.0; else $122 = $122; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($123 < '${2}') $123 = 1.0; else $123 = $123; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($124 < '${2}') $124 = 1.0; else $124 = $124; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($125 < '${2}') $125 = 1.0; else $125 = $125; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($126 < '${2}') $126 = 1.0; else $126 = $126; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($127 < '${2}') $127 = 1.0; else $127 = $127; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($128 < '${2}') $128 = 1.0; else $128 = $128; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($129 < '${2}') $129 = 1.0; else $129 = $129; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($130 < '${2}') $130 = 1.0; else $130 = $130; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($131 < '${2}') $131 = 1.0; else $131 = $131; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($132 < '${2}') $132 = 1.0; else $132 = $132; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($133 < '${2}') $133 = 1.0; else $133 = $133; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($134 < '${2}') $134 = 1.0; else $134 = $134; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($135 < '${2}') $135 = 1.0; else $135 = $135; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($136 < '${2}') $136 = 1.0; else $136 = $136; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($137 < '${2}') $137 = 1.0; else $137 = $137; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($138 < '${2}') $138 = 1.0; else $138 = $138; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($139 < '${2}') $139 = 1.0; else $139 = $139; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($140 < '${2}') $140 = 1.0; else $140 = $140; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($141 < '${2}') $141 = 1.0; else $141 = $141; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($142 < '${2}') $142 = 1.0; else $142 = $142; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($143 < '${2}') $143 = 1.0; else $143 = $143; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($144 < '${2}') $144 = 1.0; else $144 = $144; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($145 < '${2}') $145 = 1.0; else $145 = $145; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($146 < '${2}') $146 = 1.0; else $146 = $146; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($147 < '${2}') $147 = 1.0; else $147 = $147; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($148 < '${2}') $148 = 1.0; else $148 = $148; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($149 < '${2}') $149 = 1.0; else $149 = $149; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($150 < '${2}') $150 = 1.0; else $150 = $150; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($151 < '${2}') $151 = 1.0; else $151 = $151; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($152 < '${2}') $152 = 1.0; else $152 = $152; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($153 < '${2}') $153 = 1.0; else $153 = $153; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($154 < '${2}') $154 = 1.0; else $154 = $154; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($155 < '${2}') $155 = 1.0; else $155 = $155; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($156 < '${2}') $156 = 1.0; else $156 = $156; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($157 < '${2}') $157 = 1.0; else $157 = $157; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($158 < '${2}') $158 = 1.0; else $158 = $158; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($159 < '${2}') $159 = 1.0; else $159 = $159; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($160 < '${2}') $160 = 1.0; else $160 = $160; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($161 < '${2}') $161 = 1.0; else $161 = $161; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($162 < '${2}') $162 = 1.0; else $162 = $162; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($163 < '${2}') $163 = 1.0; else $163 = $163; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($164 < '${2}') $164 = 1.0; else $164 = $164; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($165 < '${2}') $165 = 1.0; else $165 = $165; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($166 < '${2}') $166 = 1.0; else $166 = $166; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($167 < '${2}') $167 = 1.0; else $167 = $167; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($168 < '${2}') $168 = 1.0; else $168 = $168; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($169 < '${2}') $169 = 1.0; else $169 = $169; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($170 < '${2}') $170 = 1.0; else $170 = $170; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($171 < '${2}') $171 = 1.0; else $171 = $171; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($172 < '${2}') $172 = 1.0; else $172 = $172; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($173 < '${2}') $173 = 1.0; else $173 = $173; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($174 < '${2}') $174 = 1.0; else $174 = $174; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($175 < '${2}') $175 = 1.0; else $175 = $175; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($176 < '${2}') $176 = 1.0; else $176 = $176; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($177 < '${2}') $177 = 1.0; else $177 = $177; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($178 < '${2}') $178 = 1.0; else $178 = $178; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($179 < '${2}') $179 = 1.0; else $179 = $179; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($180 < '${2}') $180 = 1.0; else $180 = $180; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($181 < '${2}') $181 = 1.0; else $181 = $181; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($182 < '${2}') $182 = 1.0; else $182 = $182; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($183 < '${2}') $183 = 1.0; else $183 = $183; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($184 < '${2}') $184 = 1.0; else $184 = $184; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($185 < '${2}') $185 = 1.0; else $185 = $185; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($186 < '${2}') $186 = 1.0; else $186 = $186; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($187 < '${2}') $187 = 1.0; else $187 = $187; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($188 < '${2}') $188 = 1.0; else $188 = $188; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($189 < '${2}') $189 = 1.0; else $189 = $189; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($190 < '${2}') $190 = 1.0; else $190 = $190; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($191 < '${2}') $191 = 1.0; else $191 = $191; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($192 < '${2}') $192 = 1.0; else $192 = $192; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($193 < '${2}') $193 = 1.0; else $193 = $193; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($194 < '${2}') $194 = 1.0; else $194 = $194; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($195 < '${2}') $195 = 1.0; else $195 = $195; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($196 < '${2}') $196 = 1.0; else $196 = $196; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($197 < '${2}') $197 = 1.0; else $197 = $197; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($198 < '${2}') $198 = 1.0; else $198 = $198; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($199 < '${2}') $199 = 1.0; else $199 = $199; }; 1' ${1}_4_2.txt > ${1}_4_1_extra_3.txt #another rookie mistake
awk 'BEGIN { OFS = " "; }; { if ($200 < '${2}') $200 = 1.0; else $200 = $200; }; 1' ${1}_4_1_extra_3.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($201 < '${2}') $201 = 1.0; else $201 = $201; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($202 < '${2}') $202 = 1.0; else $202 = $202; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($203 < '${2}') $203 = 1.0; else $203 = $203; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($204 < '${2}') $204 = 1.0; else $204 = $204; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($205 < '${2}') $205 = 1.0; else $205 = $205; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($206 < '${2}') $206 = 1.0; else $206 = $206; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($207 < '${2}') $207 = 1.0; else $207 = $207; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($208 < '${2}') $208 = 1.0; else $208 = $208; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($209 < '${2}') $209 = 1.0; else $209 = $209; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($210 < '${2}') $210 = 1.0; else $210 = $210; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($211 < '${2}') $211 = 1.0; else $211 = $211; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($212 < '${2}') $212 = 1.0; else $212 = $212; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($213 < '${2}') $213 = 1.0; else $213 = $213; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($214 < '${2}') $214 = 1.0; else $214 = $214; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($215 < '${2}') $215 = 1.0; else $215 = $215; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($216 < '${2}') $216 = 1.0; else $216 = $216; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($217 < '${2}') $217 = 1.0; else $217 = $217; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($218 < '${2}') $218 = 1.0; else $218 = $218; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($219 < '${2}') $219 = 1.0; else $219 = $219; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($220 < '${2}') $220 = 1.0; else $220 = $220; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($221 < '${2}') $221 = 1.0; else $221 = $221; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($222 < '${2}') $222 = 1.0; else $222 = $222; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($223 < '${2}') $223 = 1.0; else $223 = $223; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($224 < '${2}') $224 = 1.0; else $224 = $224; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($225 < '${2}') $225 = 1.0; else $225 = $225; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($226 < '${2}') $226 = 1.0; else $226 = $226; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($227 < '${2}') $227 = 1.0; else $227 = $227; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($228 < '${2}') $228 = 1.0; else $228 = $228; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
#=========================================includes lower frequencies up to row 248
awk 'BEGIN { OFS = " "; }; { if ($229 < '${2}') $229 = 1.0; else $229 = $229; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($230 < '${2}') $230 = 1.0; else $230 = $230; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($231 < '${2}') $231 = 1.0; else $231 = $231; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($232 < '${2}') $232 = 1.0; else $232 = $232; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($233 < '${2}') $233 = 1.0; else $233 = $233; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($234 < '${2}') $234 = 1.0; else $234 = $234; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($235 < '${2}') $235 = 1.0; else $235 = $235; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($236 < '${2}') $236 = 1.0; else $236 = $236; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($237 < '${2}') $237 = 1.0; else $237 = $237; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($238 < '${2}') $238 = 1.0; else $238 = $238; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($239 < '${2}') $239 = 1.0; else $239 = $239; }; 1' ${1}_4_2.txt > ${1}_4_2_2.txt #wow such mistake
awk 'BEGIN { OFS = " "; }; { if ($240 < '${2}') $240 = 1.0; else $240 = $240; }; 1' ${1}_4_2_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($241 < '${2}') $241 = 1.0; else $241 = $241; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($242 < '${2}') $242 = 1.0; else $242 = $242; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($243 < '${2}') $243 = 1.0; else $243 = $243; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($244 < '${2}') $244 = 1.0; else $244 = $244; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($245 < '${2}') $245 = 1.0; else $245 = $245; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($246 < '${2}') $246 = 1.0; else $246 = $246; }; 1' ${1}_4_2.txt > ${1}_4_1.txt
awk 'BEGIN { OFS = " "; }; { if ($247 < '${2}') $247 = 1.0; else $247 = $247; }; 1' ${1}_4_1.txt > ${1}_4_2.txt
awk 'BEGIN { OFS = " "; }; { if ($248 < '${2}') $248 = 1.0; else $248 = $248; }; 1' ${1}_4_2.txt > ${1}_4_1.txt



cat ${1}_4_1.txt | tr -s ' ' > ${1}_5.txt #delimit...
cp /Users/bryanyamashiro/Desktop/RadioBurst/${1}_5.txt /Users/bryanyamashiro/Desktop/RadioBurst/converted/


#=======renaming

mv /Users/bryanyamashiro/Desktop/RadioBurst/converted/${1}_4_1.txt /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}parsebrybry.dat
mv /Users/bryanyamashiro/Desktop/RadioBurst/converted/${1}_5.txt /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}reducedparsebrybry.dat

#cp /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}parsebrybry.dat .
#cp /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}reducedparsebrybry.dat .
cut -f3-248 -d ' ' /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}parsebrybry.dat > /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}sequenced_nodate_parsebrybry.dat
cut -f3-248 -d ' ' /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}reducedparsebrybry.dat > /Users/bryanyamashiro/Desktop/RadioBurst/converted/${4}reducedsequenced_nodate_parsebrybry.dat




#=====================averaging
#awk '{c=0;for(i=3;i<=248;++i){c+=$i/246};print $0, " ", c}' ${1}_5.txt > ${1}_6.txt #average all the above
#cat ${1}_6.txt | tr -s ' ' > ${1}_7.txt #delimit new average columns
#cut -f1-2,249 -d ' ' ${1}_7.txt > ${1}_8.txt #remove all columns except averages
#awk '{split($1,a,"-");$1=a[3]"-"a[2]"-"a[1]}1' ${1}_8.txt > windt3_${1}.txt #remodel date to yyyy-mm-dd

rm 201*_*.txt #remove excess files
#rm *.dat
echo "WIND Type 3 Loaded"
