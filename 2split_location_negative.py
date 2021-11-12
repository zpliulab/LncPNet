with open('data/location_negative_sample.txt') as pid:
    NOLPI = pid.readlines()
TRAIN = []
TEST = []
for index, item in enumerate(NOLPI):
    if index < 4121:
        TRAIN.append(item)
    else:
        TEST.append(item)
with open('train/4121_location_negative_pair.txt', 'w') as pid:
    pid.writelines(TRAIN)
with open('test/457_location_negative_pair.txt', 'w') as pid:
    pid.writelines(TEST)