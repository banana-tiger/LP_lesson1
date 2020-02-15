def get_summ(one, two, delimeter = '&'):
    #concat =f"{one.upper()}{delimeter}{two.upper()}" 
    concat ="{}{}{}".format(one.upper(), delimeter, two.upper())
    return concat

temp_var = get_summ('Learn', 'python')
print(temp_var)