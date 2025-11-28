
"""
In this example:

Outer list  → [1, 2, [2, 3]]
Inner list  → [2, 3]

A shallow copy only creates a new OUTER list,
but the INNER list is still shared between 'a' and 'b'.

So if we change the inner list in 'b',
the same change will appear in 'a' because both point
to the same inner list.
"""
# a = [1,2,[2,3]]  
# b = a.copy()

# We change the inner list in 'b'
# Because shallow copy shares the inner list,
# this change will also appear in the original list 'a'.

# b[2][1] = 7 
# print(a)
# print(b)



# Deep Copy


from copy import deepcopy

# In this list:
# a = [1, 2, [2, 3]]
# Outer list  → [1, 2, [...]]
# Inner list  → [2, 3]
# 
# Deep copy creates a NEW outer list AND a NEW inner list.
# Nothing is shared between 'a' and 'c'.
# 
# So any change inside c's inner list will NOT affect a.

a = [1, 2, [2, 3]]
c = deepcopy(a)

c[2][1] = 7   # Changing the inner list in 'c' DOES NOT change 'a'

print(a)  
print(c)














