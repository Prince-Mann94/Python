print(60+(10 ** 2)/ 4 * 7)  
print(4 * (6 + 5))             
print(4 * 6 + 5)
print(4 + 6 * 5)
print(3 + 1.5 + 4)

s = 'hello'
print(s[::-1])   # command to reverse the string using slicing 
print(s[4])      # print last word
print(s[-1])     # also print last word but using different slicing

list3 = [1,2,[3,4,'hello']] 
print(list3)

list3[2][2] = 'goodbye'    # replace 'hello' with 'goodbye' in list3
print(list3)

list4 = [1,2,['hello',1],['good']]
print(list4)
list4[3][0] = 'bye'      # replace 'good' with 'bye' in list4
print(list4)

list5 = [1,3,4,2,5]
sorted(list5)     # Method 1 for sorting the list
print(list5)      # doesn't change . It is a function
print(sorted(list5))  # Now it changes

list5.sort()      # Method 2 for sorting the list
print(list5)      # Changes occurs permanently. It is a method

d = {'simple_key' : 'hello'}  
print(d['simple_key'])      # grab hello

H = {'k1' : {'k2' : 'hello'}} 
print(H['k1']['k2'])      # grab hello

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])            # prints 'hello'

print(d['k1'][0]['nest_key'][0])               # prints 'this is deep'

g = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(g['k1'][2]['k2'][1]['tough'][2])        # prints ['hello']

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]                      # Two nested lists
print(l_one[2][0] >= l_two[2]['k1'])        # True or False