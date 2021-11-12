with open('data/one_Jaccard_vetor.txt') as pid:
    LPembedding_jaccard = pid.readlines()
lncRNA_embedding_jaccard = []
protein_embedding_jaccard = []
for item in LPembedding_jaccard[2:]:
    if item.startswith('v'):
        item = item.strip('v')
        lncRNA_embedding_jaccard.append(item)
    if item.startswith('a'):
        item = item.strip('a')
        protein_embedding_jaccard.append(item)
with open('data/one_blast_vetor.txt') as pid:
    LPembedding_blast = pid.readlines()
lncRNA_embedding_blast = []
protein_embedding_blast = []
for item in LPembedding_blast[2:]:
    if item.startswith('v'):
        item = item.strip('v')
        lncRNA_embedding_blast.append(item)
    if item.startswith('a'):
        item = item.strip('a')
        protein_embedding_blast.append(item)
lncRNA_homo = []
for i in lncRNA_embedding_jaccard:
    i = i.strip()
    i = i.split(' ', 1)
    for j in lncRNA_embedding_blast:
        j = j.strip()
        j = j.split(' ', 1)
        if i[0] == j[0]:
            lncRNA_homo.append(i[0]+' '+i[1]+' '+j[1]+'\n')
        else:
            continue
protein_homo = []
for i in protein_embedding_jaccard:
    i = i.strip()
    i = i.split(' ', 1)
    for j in protein_embedding_blast:
        j = j.strip()
        j = j.split(' ', 1)
        if i[0] == j[0]:
            protein_homo.append(i[0]+' '+i[1]+' '+j[1]+'\n')
        else:
            continue
with open('data/one_lncRNA_embedding.txt', 'w') as pid:
    pid.writelines(lncRNA_homo)
with open('data/one_protein_embedding.txt', 'w') as pid:
    pid.writelines(protein_homo)