import math

#calcu


prob_list = [[[1/3,2/3],[2/3,1/3],[1/2,1/2]],
             [[2/5,3/5],[2/3,1/3]],
             [[1/5,4/5],[3/3,0]]]

proportion_list = [[3,3,2],[5,3],[5,3]]

original_T = [4/8,4/8]



def entropy(prob):
    if 0 in prob:
        return 0
    return -sum([x * math.log2(x) for x in prob])



def information_gain(prob_list,proportion_list,original_T):


    for m in range(0,len(prob_list)):
        entropy_list = []
        for prob in prob_list[m]:
                entropy_list.append(entropy(prob))
        s = 0
        for i in range(0,len(entropy_list)):
            s += proportion_list[m][i]/sum(proportion_list[m]) * entropy_list[i]
        print("for the attributes to which the proportions", proportion_list[m], " belong")
        print(" S is")
        print(s)
        print("the information gain ")
        print(entropy(original_T) - s)
information_gain(prob_list,proportion_list,original_T)

