"""Never Gonna Give You Up"""


def convert_string():
    """Never Gonna Give You Up"""
    gusfring = input()
    mat = []
    gus = string_to_list(gusfring)
    ###convert first char###
    mat.append(float(string_replace(gus[0],0)))
    for i in range(1,len(gus)-1):
        mat.append(float(gus[i]))
    mat.append(float(string_replace(gus[len(gus)-1],len(gus))))
    
    print (mat)
        
def string_replace(string,gusfring):
    '''Shutup Walter'''
    if(gusfring == 0):
        return string[1::]
    else:
        return string[:-1:]

def string_to_list(string):
    '''Goodbye Walter'''
    listRes = list(string.split(", "))
    return listRes


convert_string()
