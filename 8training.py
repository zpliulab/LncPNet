import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.metrics import matthews_corrcoef
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from  sklearn.metrics import confusion_matrix, classification_report
plt.figure()
X_train = np.loadtxt('train/location_all_train_sample.txt', dtype=float, delimiter=' ')
X_test = np.loadtxt('test/location_all_test_sample.txt', dtype=float, delimiter=' ')
y_train = np.loadtxt('train/train_label.txt', dtype=float)
y_test = np.loadtxt('test/test_label.txt', dtype=float)


clf = svm.SVC(C=5, kernel='rbf', probability=True)
clf.fit(X_train, y_train)
svm_label = clf.predict(X_test)
svm_target = clf.decision_function(X_test)
fpr_svm, tpr_svm, thersholds_svm = roc_curve(y_test, svm_target)
score_flag_svm = 0
thre_flag_svm = 0
for thre in thersholds_svm:
    score_svm = np.zeros(shape=svm_target.shape)
    score_svm[svm_target>=thre] = 1
    score_svm[svm_target < thre] = 0
    acc_svm = accuracy_score(y_test, score_svm)
    if acc_svm>score_flag_svm:
        score_flag_svm = acc_svm
        thre_flag_svm = thre
score_svm = np.zeros(shape=svm_target.shape)
score_svm[svm_target >= thre_flag_svm] = 1
score_svm[svm_target < thre_flag_svm] = 0
aa_svm = accuracy_score(y_test, score_svm)
pp_svm = precision_score(y_test, score_svm)
rr_svm = recall_score(y_test, score_svm)
ff1_svm = f1_score(y_test, score_svm)
sspe_svm = recall_score(1-y_test,1-score_svm)
mcc_svm = matthews_corrcoef(y_test, score_svm)
print( format(aa_svm,'.4f'),format(pp_svm,'.4f'),format(rr_svm,'.4f'),format(ff1_svm,'.4f'), format(sspe_svm,'.4f'), format(mcc_svm,'.4f'))
roc_auc_svm = auc(fpr_svm, tpr_svm)
plt.plot(fpr_svm, tpr_svm, color='red', linestyle='-', label='LncPNet (AUC = {0:.3f})'.format(roc_auc_svm), lw=2)

plt.xlim([-0.05, 1.05])  # 设置x、y轴的上下限，以免和边缘重合，更好的观察图像的整体
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')  # 可以使用中文，但需要导入一些库即字体
plt.title('ROC Curve')
plt.legend(loc="lower right")#设置图例位置
plt.show()

pass
