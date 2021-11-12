import sys
import os
import random
from collections import Counter

class MetaPathGenerator:
    def __init__(self):
        self.lnclist = set()
        self.proteinlist = set()
        self.lnc_proteinlist = dict()
        self.protein_lnclist = dict()
        self.lnc_lncRNAlist = dict()
        self.pro_proteinlist = dict()

    def read_data(self, dirpath):
        with open(dirpath) as pid:
            data = pid.readlines()
        for index, line in enumerate(data):
            if index < 4121:
                lnc, pro = line.strip().split()
                lnc = 'v' + lnc
                pro = 'a' + pro
                self.lnclist.add(lnc)
                self.proteinlist.add(pro)
                if lnc not in self.lnc_proteinlist.keys():
                    self.lnc_proteinlist[lnc] = []
                self.lnc_proteinlist[lnc].append(pro)

                if pro not in self.protein_lnclist.keys():
                    self.protein_lnclist[pro] = []
                self.protein_lnclist[pro].append(lnc)

            else :
                if index >= 4121 and index < 264941:
                    lnc1, lnc2 = line.strip().split()
                    lnc1 = 'v' + lnc1
                    lnc2 = 'v' + lnc2
                    if lnc1 not in self.lnc_lncRNAlist.keys():
                        self.lnc_lncRNAlist[lnc1] = []
                    self.lnc_lncRNAlist[lnc1].append(lnc2)

                    if lnc2 not in self.lnc_lncRNAlist.keys():
                        self.lnc_lncRNAlist[lnc2] = []
                    self.lnc_lncRNAlist[lnc2].append(lnc1)

                else:
                    pro1, pro2 = line.strip().split()
                    pro1 = 'a' + pro1
                    pro2 = 'a' + pro2
                    if pro1 not in self.pro_proteinlist.keys():
                        self.pro_proteinlist[pro1] = []
                    self.pro_proteinlist[pro1].append(pro2)

                    if pro2 not in self.pro_proteinlist.keys():
                        self.pro_proteinlist[pro2] = []
                    self.pro_proteinlist[pro2].append(pro1)
        print("lnc:", len(self.lnclist))
        print("pro:", len(self.proteinlist))


    def generate_llppll_aca(self, outfile, numwalks, walklength):

        for index, lnc in enumerate(self.lnc_proteinlist):
            print(index)
            lnc0 = lnc
            for j in range(0, numwalks): #wnum walks
                outline = lnc0
                for i in range(0, walklength):
                    if lnc in self.lnc_lncRNAlist.keys():
                        lncs = self.lnc_lncRNAlist[lnc]
                        numc = len(lncs)
                        lncid = random.randrange(numc)
                        lnc = lncs[lncid]
                        outline += " " + lnc
                        if outline.count(' ') == 200:
                            break
                    pros = self.lnc_proteinlist[lnc]
                    numa = len(pros)
                    proid = random.randrange(numa)
                    pro = pros[proid]
                    outline += " " + pro
                    if outline.count(' ') == 200:
                        break
                    if pro in self.pro_proteinlist.keys():
                        pros = self.pro_proteinlist[pro]
                        numa = len(pros)
                        proid = random.randrange(numa)
                        pro = pros[proid]
                        outline += " " + pro
                        if outline.count(' ') == 200:
                            break
                    lncs = self.protein_lnclist[pro]
                    numc = len(lncs)
                    lncid = random.randrange(numc)
                    lnc = lncs[lncid]
                    outline += " " + lnc
                    if outline.count(' ') == 200:
                        break
                outfile.write(outline + "\n")
    def generate_lpl_aca(self, outfile, numwalks, walklength):

        for index, lnc in enumerate(self.lnc_proteinlist):
            print(index)
            lnc0 = lnc
            for j in range(0, numwalks): #wnum walks
                outline = lnc0
                for i in range(0, walklength):
                    pros = self.lnc_proteinlist[lnc]
                    numa = len(pros)
                    proid = random.randrange(numa)
                    pro = pros[proid]
                    outline += " " + pro
                    lncs = self.protein_lnclist[pro]
                    numc = len(lncs)
                    lncid = random.randrange(numc)
                    lnc = lncs[lncid]
                    outline += " " + lnc
                outfile.write(outline + "\n")
        outfile.close()

numwalks = int(sys.argv[1])
walklength = int(sys.argv[2])

dirpath = sys.argv[3]
outfilename = sys.argv[4]

def main():
    mpg = MetaPathGenerator()
    mpg.read_data(dirpath)
    outfile = open(outfilename, 'w')
    mpg.generate_llppll_aca(outfile, numwalks, walklength)
    mpg.generate_lpl_aca(outfile, numwalks, walklength)
if __name__ == "__main__":
	main()






























