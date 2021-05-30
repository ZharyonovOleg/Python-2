c = (568, 100, 56, 89, 405, 78)

# 1
def min_num1(lst): # O(N**2)
    for a in lst: # O(N)
        min_n1 = True # O(1)
        for b in lst: # O(N)
            if a > b: # O(N)
                min_n1 = False # O(1)
        if min_n1: # O(N)
            return a # O(1)

print(c)
print(min_num1(c))

# 2
def min_num2(lst): # O(N**2)
    min_n2 = lst[0] # O(1)
    for d in lst: # O(N)
        if d < min_n2: # O(N)
            min_n2 = d # O(1)
    return min_n2 # O(1)

print(min_num2(c))