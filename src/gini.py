# gini in python
# by fariz darari
# inspired by Page 9 of http://www.fao.org/docs/up/easypol/329/gini_index_040en.pdf
def compute_gini(lst):

    lst = sorted(lst) # gini formula assumes sorted data

    c = len(lst) # number of elements
    s = sum(lst) # total wealth
    s_g_prev = 0
    s_res = 0
    
    for i in lst:
        s_g = s_g_prev + (i/s)
        s_res += (s_g + s_g_prev) * (1/c)
        s_g_prev = s_g

    return 1-s_res

lst = [1,2,3,4,5]
print(compute_gini(lst)) # https://shlegeris.com/gini gives 0.267

lst = [1,1,1,1,1]
print(compute_gini(lst)) # must be 0 (or close to 0)

lst = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000000]
print(compute_gini(lst)) # must be close to 1, https://shlegeris.com/gini gives 0.968

lst = [20,20,20,20,50]
print(compute_gini(lst)) # https://shlegeris.com/gini gives 0.185

lst = [13,7,6,5,5,4,2,2,2] + [1]*13
print(compute_gini(lst)) # https://prowd.id/dashboards/d734e97c1f66/profile gives 0.475 (as of Feb 1, 2021)
