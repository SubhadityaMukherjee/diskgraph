import os
import operator
import argparse
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Filestruc')
parser.add_argument('--p')
args = parser.parse_args()
filepath = args.p

finallist = []
tempdic = {}
finaldic = {}
# dict levels
def dictLevels():
    global finaldic
    for a in tempdic.keys():
        try:
            finaldic[tempdic[a]].append(a)
        except KeyError:
            pass
    temp = sorted(finaldic.items(), key=lambda kv: kv[0])
    for a in range(len(temp)):
        finaldic['Level '+str(a)]=finaldic[temp[a][0]]
        del finaldic[temp[a][0]]
#listing files
def list_files(startpath):

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        finallist.extend(['nd',root.split('/')[-1]])
        indent = ' ' * 4 * (level)
        tempdic[os.path.basename(root)]=4*level
        subindent = ' ' * 4 * (level + 1)
        templ = []
        for f in files:
            if 'Store' not in f:
                tempdic[f]=4 * (level + 1)
                templ.append(f)

        finallist.extend(['dd',templ])

#main function
def main():
    global finaldic
    list_files(filepath)
    finaldic = {k:[] for k in tempdic.values()}
    dictLevels()

    g = nx.DiGraph(finaldic)
    pos = nx.circular_layout(g)
    plt.figure(6,figsize=(20,20))
    nx.draw_circular(g,with_labels=True,node_color='r',font_size=8)
    plt.draw()
    plt.savefig('output.jpg')
    plt.show()



main()
