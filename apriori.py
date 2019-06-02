#get all combinations of classes of length l

import itertools
import  numpy as np

def get_comb(iter,l):
    return list(itertools.combinations(iter, l))

#get_comb(iter,3)


#get all candidates of length n+1 given freq itemsets of length n



#print(get_comb(input,1))

#print(get_comb(freq, 2)[0][0][0:2])

def get_1s(iter):
    c = [i for sub in iter for i in sub]
    c.sort()
    c = list(k for k, _ in itertools.groupby(c))
    return c

def join(iter):

    combs = get_comb(iter,2)
    #if len(combs[0]) == 2:
    #    return [list(a) for a in combs]

    candidates = []
    for i in combs:

        a = i[0]
        b = i[1]
        l = len(a)
        if all(a[0:l]) == all(b[0:l]) and a[l-1] != b[l-1]:
            t = list(a[0:l-1])
            t.append(a[l-1])
            t.append(b[l-1])
            t.sort()
            candidates.append(t)
    candidates.sort()
    candidates = list(k for k, _ in itertools.groupby(candidates))
    return candidates

def prune(iter):
    candidates = join(iter)
    print("The joined set with length ", len(candidates[0]), " are ", candidates)
    pruned = []
    for i in candidates:
        if len(i) == 2:
            pruned.append(i)
        else:
            t = list(itertools.combinations(i, len(i) - 1))
            t_iter = [tuple(p) for p in iter]
            if set(list(t)).issubset(set(t_iter)):
                pruned.append(i)
    print("The candidates/pruned with length ", len(candidates[0]), " are ", candidates)
    return pruned

def check_freq(iter,pruned,support):

    checked = []
    for i in pruned:
        n = 0
        for t in iter:
            if set(i).issubset(set(t)):
                n += 1


        #print(n)
        if n >= support:
            checked.append(i)
    return checked



def apriori(iter,support):

    #getting frequent of length one
    one = get_1s(iter)
    checked = check_freq(iter,one,support)

    freq_itemsets = []
    freq_itemsets.append(checked)

    while(len(checked) > 0):
        pruned = prune(checked)
        checked = check_freq(iter,pruned,support)
        freq_itemsets.append(checked)
        #if len(checked[0]) == 2:
        #    break
    print("the frequent itemsets are")
    for items in freq_itemsets:
        print(items)

    return freq_itemsets



transactions = [("A","B","E"),("B","D"),("C","D","F"),("A","B","D"),("A","C","E"),("B","C","E","F"),("A","C","E"),("A","B","C","E"),("A","B","C","D","F"),("B","C","D","E")]

support = 2

apriori(transactions,support)



#the script can also be used to get the candidates for next step:

#freq = [(1,2,3),(1,2,4),(1,2,5),(1,3,4),(1,3,5),(2,3,4),(2,3,5),(3,4,5)]
#print(prune(freq))