for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                if(i !=k) and (i != j) and (j != k) and (i != l) and (j != l) and (k != l):
                    print( i,j,k,l)