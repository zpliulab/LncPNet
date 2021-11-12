with open('train/4121_positive_pair.txt') as pid:
    LPI = pid.readlines()
#lncRNA
with open('data/final_lncRNA_ID.txt') as pid:
    lncRNA_ID = pid.readlines()
each_lncRNA_correctioned_proteions = {}
for item in lncRNA_ID:
    value = set()
    item = item.strip('\n')
    for interaction in LPI:
        interaction = interaction.strip('\n')
        interaction = interaction.split('\t')
        if item == interaction[0]:
            value.add(interaction[1])
    each_lncRNA_correctioned_proteions[item] = list(value)
Jaccard_similar_RNA = []
for key1, value1 in each_lncRNA_correctioned_proteions.items():
    for key2, value2 in each_lncRNA_correctioned_proteions.items():
        #if key1 == key2:
            #continue
        tem = []
        for item in value1:
            if item in value2:
                tem.append(item)
        jiao_ji = len(tem)
        bing_ji = len(value1)+len(value2)-jiao_ji
        score = jiao_ji/bing_ji
        if score > 0.5:
            s = score
        else:
            continue
        Jaccard_similar_RNA.append(key1+'\t'+key2+'\t'+str(s)+'\n')
with open('data/Jaccard_similar_RNA.txt', 'w') as f:
    f.writelines(Jaccard_similar_RNA)
# protein
with open('data/final_protein_ID.txt') as pid:
    protein_ID = pid.readlines()
each_proytein_correctioned_lncRNAs = {}
for item in protein_ID:
    value = set()
    item = item.strip('\n')
    for interaction in LPI:
        interaction = interaction.strip('\n')
        interaction = interaction.split('\t')
        if item == interaction[1]:
            value.add(interaction[0])
    each_proytein_correctioned_lncRNAs[item] = list(value)
Jaccard_similar_protein = []
for key1, value1 in each_proytein_correctioned_lncRNAs.items():
    for key2, value2 in each_proytein_correctioned_lncRNAs.items():
        #if key1 == key2:
            #continue
        tem = []
        for item in value1:
            if item in value2:
                tem.append(item)
        jiao_ji = len(tem)
        bing_ji = len(value1) + len(value2) - jiao_ji
        score = jiao_ji / bing_ji
        if score != 0:
            s = score
        else:
            continue
        Jaccard_similar_protein.append(key1 + '\t' + key2 +'\t'+str(s)+ '\n')
with open('data/Jaccard_similar_protein.txt', 'w') as f:
    f.writelines(Jaccard_similar_protein)
pass
