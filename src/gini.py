# gini in python
# by fariz darari
# inspired by http://www.fao.org/docs/up/easypol/329/gini_index_040en.pdf
def compute_gini(lst):

    c = len(lst)
    s = sum(lst)
    s_g_prev = 0
    s_res = 0
    
    for i in lst:
        s_g = s_g_prev + (i/s)
        s_res += (s_g + s_g_prev) * (1/c)
        s_g_prev = s_g

    return 1-s_res

# example data, already sorted
lst = [1,2,3,4,5]
print(compute_gini(lst)) # https://shlegeris.com/gini gives 0.267

lst = [1,1,1,1,1]
print(compute_gini(lst)) # must be 0 (or close to 0)

lst = [20,20,20,20,50]
print(compute_gini(lst)) # https://shlegeris.com/gini gives 0.185

# must be sorted first
lst = [13,7,6,5,5,4,2,2,2] + [1]*13
lst.sort()
print(compute_gini(lst)) # https://prowd.id/dashboards/d734e97c1f66/profile gives 0.475 (as of Feb 1, 2021)
