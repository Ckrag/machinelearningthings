import numpy as np

#se slide 433
d = 2 # d is dimension
p = np.array([2.5,3]) # p is the pont
mean1 = np.array([2,2])
mean2 = np.array([5,3])
mean3 = np.array([1,4])

mean_list = [mean1,mean2,mean3]

cov_matrix1 = np.array([[3,0],[0,3]])
cov_matrix2 = np.array([[2,1],[1,4]])
cov_matrix3 = np.array([[16,0],[0,4]])
cov_matrixes = [cov_matrix1,cov_matrix2,cov_matrix3]


size_list = [0.3,0.2,0.5] #the relative share of each cluster

def em_clustering(d,p,mean_list,cov_matrixes,size_list):
    fcx_list = [] #list used to calculate pr(x) from slide 433
    for i in range (0,len(cov_matrixes)):
        mean = mean_list[i]
        size = size_list[i]
        cov_matrix = cov_matrixes[i]

        power = -0.5 * (((p-mean)@np.linalg.inv(cov_matrix))@np.transpose((p-mean)))
        fcx = 1/(np.sqrt((2*np.pi)**d*np.linalg.det(cov_matrix)))*np.e**power #fx(x) from slide 429
        fcx_list.append(fcx)

    pr_x = sum([a*b for a,b in zip(size_list,fcx_list)])  #pr(x) from slide 433
    print("the OVERALL probability of the data explained by k clusters is ", pr_x)
    for k in range (0,len(fcx_list)):
        print("th overall probability of the explained by the cluster with the mean ", mean_list[k], " is")
        print(fcx_list[k])
        print("the relative share of points in the cluster with the mean ", mean_list[k], " is")
        print(fcx_list[k] * size_list[k])
        print("the probability of some point belonging to the cluster with the mean ", mean_list[k], " is")
        print(size_list[k]*(fcx_list[k]/pr_x))

em_clustering(d,p,mean_list,cov_matrixes,size_list)
