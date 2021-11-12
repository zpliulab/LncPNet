with open('train/4121_positive_pair.txt') as pid:
    positive_LPI1 = pid.readlines()
with open('train/4121_location_negative_pair.txt') as pid:
    negative_LPI1 = pid.readlines()
with open('test/457_positive_pair.txt') as pid:
    positive_LPI2 = pid.readlines()
with open('test/457_location_negative_pair.txt') as pid:
    negative_LPI2 = pid.readlines()
with open('data/one_lncRNA_embedding.txt') as pid:
    lncRNA_embedding = pid.readlines()
with open('data/one_protein_embedding.txt') as pid:
    protein_embedding = pid.readlines()
lncRNA_dict = {}
for item in lncRNA_embedding:
    item = item.strip()
    item = item.split(' ', 1)
    lncRNA_dict[item[0]] = item[1]
protein_dict = {}
for item in protein_embedding:
    item = item.strip()
    item = item.split(' ', 1)
    protein_dict[item[0]] = item[1]
all_train_simple = []
positive_LPI_train_vector = []
for item in positive_LPI1:
    item = item.strip('\n')
    item = item.split('\t')
    positive_LPI_train_vector.append(lncRNA_dict[item[0]]+' '+protein_dict[item[1]]+'\n')
    all_train_simple.append(lncRNA_dict[item[0]]+' '+protein_dict[item[1]]+'\n')
negative_LPI_train_vector = []
for item in negative_LPI1:
    item = item.strip('\n')
    item = item.split('\t')
    negative_LPI_train_vector.append(lncRNA_dict[item[0]]+' '+protein_dict[item[1]]+'\n')
    all_train_simple.append(lncRNA_dict[item[0]] + ' ' + protein_dict[item[1]] + '\n')
with open('train/location_all_train_sample.txt', 'w') as pid:
    pid.writelines(all_train_simple)
all_test_simple = []
positive_LPI_test_vector = []
for item in positive_LPI2:
    item = item.strip('\n')
    item = item.split('\t')
    positive_LPI_test_vector.append(lncRNA_dict[item[0]]+' '+protein_dict[item[1]]+'\n')
    all_test_simple.append(lncRNA_dict[item[0]]+' '+protein_dict[item[1]]+'\n')
negative_LPI_test_vector = []
for item in negative_LPI2:
    item = item.strip('\n')
    item = item.split('\t')
    negative_LPI_test_vector.append(lncRNA_dict[item[0]]+' '+protein_dict[item[1]]+'\n')
    all_test_simple.append(lncRNA_dict[item[0]] + ' ' + protein_dict[item[1]] + '\n')
with open('test/location_all_test_sample.txt', 'w') as pid:
    pid.writelines(all_test_simple)
train_label = []
for i in range(4121):
    train_label.append('1'+'\n')
for j in range(4121):
    train_label.append('0'+'\n')
with open('train/train_label.txt', 'w') as f:
    f.writelines(train_label)
test_label = []
for i in range(457):
    test_label.append('1'+'\n')
for j in range(457):
    test_label.append('0'+'\n')
with open('test/test_label.txt', 'w') as f:
    f.writelines(test_label)
pass

