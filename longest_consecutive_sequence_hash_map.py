def longest_consecutive_sequence(mylist1):
    k=sorted(set(mylist1))
    sum1=1
    max_value=0
    if len(mylist1)<=1:
        return len(mylist1)
    for i in range(1,len(k)):
        sum2=k[i]-k[i-1]
        if sum2==1:
            sum1=sum1+1
        else:
            if sum1>max_value:
                max_value=sum1
            sum1=1
    if sum1>max_value:
        max_value=sum1
    return max_value
                
            
        
        


print( def longest_consecutive_sequence(mylist1):
    k=sorted(set(mylist1))
    sum1=1
    max_value=0
    if len(mylist1)<=1:
        return len(mylist1)
    for i in range(1,len(k)):
        sum2=k[i]-k[i-1]
        if sum2==1:
            sum1=sum1+1
        else:
            if sum1>max_value:
                max_value=sum1
            sum1=1
    if sum1>max_value:
        max_value=sum1
    return max_value
                
            
        
        


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
