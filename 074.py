def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
        
def digit_factorial(x, factorials):
    return sum([factorials[int(i)] for i in str(x)])

factorials = [factorial(i) for i in range(10)]
limit = 10**6
DFC_dict = {}
count = 0

for i in range(1, limit+1):
    tmp = i
    tmp_list = []
    
    while (tmp not in DFC_dict) and (tmp not in tmp_list):
        tmp_list.append(tmp)
        tmp = digit_factorial(tmp, factorials)
        
    if tmp in DFC_dict:
        tmp_DFC_value = DFC_dict[tmp]
        
        if tmp_DFC_value[-1] in tmp_list:
            tmp_DFC_value = tmp_DFC_value[:-1]
            
        tmp_list += tmp_DFC_value
        
    DFC_dict[i] = tmp_list
    if len(tmp_list) == 60:
        count += 1
        
print(count)
