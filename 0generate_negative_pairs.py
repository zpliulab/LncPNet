import pandas as pd
import random
lncRNA_location = []
with open('data/interactions_with_seq.txt') as pid:
    LPI = pid.readlines()
with open('data/lncRNA_location.fasta') as pid:
    lncRNA_data = pid.readlines()
for index, value in enumerate(lncRNA_data):
    if value.startswith('>'):
        value = value.strip('>')
        value = value.strip()
        lncRNA_data[index+1] = lncRNA_data[index+1].strip()
        lncRNA_location.append(value+'\t'+lncRNA_data[index+1]+'\n')
    else:
        continue
sheet = pd.read_excel('data/protein_location.xlsx', header=None)
a = sheet.values
protein_location = []
needed_negative_sample = set()
for i in range(61):
    protein_location.append(a[i][0]+'\t'+a[i][1]+'\n')
for i in lncRNA_location:
    i = i.strip().split('\t')
    for j in protein_location:
        j = j.strip().split('\t')
        if i[1] != j[1] and i[0]+'\t'+j[0]+'\n' not in LPI:
            needed_negative_sample.add(i[0]+'\t'+j[0]+'\n')
        else:
            continue
sheet1 = pd.read_excel('data/protein2.xlsx', header=None)
b = sheet1.values
protein1_location = []
for i in range(16):
    protein1_location.append(b[i][0]+'\t'+b[i][1]+'\t'+b[i][2]+'\n')
for i in lncRNA_location:
    i = i.strip().split('\t')
    for j in protein1_location:
        j = j.strip().split('\t')
        if i[1] != j[1] and i[1] != j[2] and i[0]+'\t'+j[0]+'\n' not in LPI:
            needed_negative_sample.add(i[0]+'\t'+j[0]+'\n')
        else:
            continue
needed_negative_sample = list(needed_negative_sample)
negative_sample = set()
while len(negative_sample) < 4578:
    index = random.randint(0,110224)
    negative_sample.add(needed_negative_sample[index])
negative_sample = list(negative_sample)
with open('data/location_negative_sample.txt', 'w') as pid:
    pid.writelines(negative_sample)
pass