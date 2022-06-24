li = []

n = int(input())
for i in range(n):
    line = [int(i) for i in input().split()]
    line = line + line + line
    li.append(line)

li = li+li+li

def prefix_sum(li, n): 
    pli = []
    sum = 0
    for i in li: 
        sum+=i
        pli+=[sum]

    max_sum = -99999999999999
    for i in range(len(li)-n):
        for j in range(i+1, i+1+n):
            max_sum = max(max_sum, pli[j]-pli[i])
    return max_sum

def find_max_sum(li, n): 
    max_sum = -99999999999999
    #horizontal max 
    for i in li: 
        max_sum = max(max_sum, prefix_sum(i, n))
    
    #vertical max
    for i in range(n*3):
        temp_li = []
        for j in range(n*3):
            temp_li.append(li[j][i])
        max_sum = max(max_sum, prefix_sum(temp_li, n))
        
    #diagonal left to right max 
    for i in range(n*3): 
        temp_li = []
        for j in range(n*3):
            if(j+i>=n*3): 
                break
            else:
                temp_li.append(li[j][j+i])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))
        
    for i in range(1, n*3):
        temp_li = []
        for j in range(n*3): 
            if(j+i>=n*3): 
                break
            else:
                temp_li.append(li[j+i][j])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))
        
    #diagonal right to left max
    for i in range(n*3-1, -1, -1): 
        temp_li = []
        for j in range(n*3):
            if(i-j<0): 
                break
            else:
                temp_li.append(li[j][i-j])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))
            
    for i in range(n*3-1, -1, -1): 
        temp_li = []
        for j in range(1, n*3):
            #print(j, i-j+1)
            if(i-j<0): 
                break
            else:
                temp_li.append(li[j][i-j+1])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))

    return max_sum
    
print(find_max_sum(li, n))