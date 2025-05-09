def omp(y0,A0):
    import math as mt
    import numpy as np
    from numpy import linalg as LA
    s=mt.ceil(len(y0))
    # print(s)
    a=np.zeros((A0.shape[0],0))
    pos=np.zeros((1,s))
    r_n=y0
#     print(np.sum(r_n))
    if np.sum(r_n)==0:
        hat_x=np.zeros((1,A0.shape[1]))
        return hat_x
    # s=2
    for k in range(0,s,1):
        pr=abs(np.dot(A0.T,r_n))
    #     print(pr)
        posx=np.argmax(pr)
#         A.shape
#         y.shape
        a=np.column_stack((a,A0[:,posx]))
        A0[:,posx]=np.zeros((1,y0.shape[0]))
        aa=np.dot(a.T,a)
    #     print(aa)
#         print(y)
#         y.shape
        pangkat=LA.matrix_power(aa,-1)
        aug_x=np.dot(np.dot(pangkat,a.T),y0)    
        r_n=y0-np.dot(a,aug_x)
    #     print(k)
        pos[0,k]=posx

    hat_x=np.zeros((1,A0.shape[1]))
    for k in range(0,len(aug_x),1):
    #     print(pos[0,k])
        hat_x[0,round(pos[0,k])]=aug_x[k]
#     print(A)
#     print("Ukuran A ="+str(A.shape))
    return hat_x






# def omp(y,A):
#     import math as mt
#     import numpy as np
#     from numpy import linalg as LA
#     s=mt.ceil(len(y))
#     # print(s)
#     a=np.zeros((A.shape[0],0))
#     pos=np.zeros((1,s))
#     r_n=y
# #     print(np.sum(r_n))
#     if np.sum(r_n)==0:
#         hat_x=np.zeros((1,A.shape[1]))
#         return hat_x
#     # s=2
#     for k in range(0,s,1):
#         pr=abs(np.dot(A.T,r_n))
#     #     print(pr)
#         posx=np.argmax(pr)
# #         A.shape
# #         y.shape
#         a=np.column_stack((a,A[:,posx]))
#         A[:,posx]=np.zeros((1,y.shape[0]))
#         aa=np.dot(a.T,a)
#     #     print(aa)
# #         print(y)
# #         y.shape
#         pangkat=LA.matrix_power(aa,-1)
#         aug_x=np.dot(np.dot(pangkat,a.T),y)    
#         r_n=y-np.dot(a,aug_x)
#     #     print(k)
#         pos[0,k]=posx

#     hat_x=np.zeros((1,A.shape[1]))
#     for k in range(0,len(aug_x),1):
#     #     print(pos[0,k])
#         hat_x[0,round(pos[0,k])]=aug_x[k]
# #     print(A)
# #     print("Ukuran A ="+str(A.shape))
#     return hat_x
