def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >=6:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3]
        del list_to_remove_elements[3]
        return list_to_remove_elements
    elif len(list_to_remove_elements)==5:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3]
        return list_to_remove_elements
    elif len(list_to_remove_elements)==4:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements)>=1:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    else:
        return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    len1=len(list_to_compare1)
    len2=len(list_to_compare2)
    if len1>=3 and len2>=3:
        if list_to_compare1[2]==list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    lista1=list_of_lists_to_modify[0]
    lista2=list_of_lists_to_modify[1]
    lista3=list_of_lists_to_modify[2]
    lista1=lista1[0:2]
    lista2=lista2[1:4]
    lista3=lista3[-2::1]
    listafinal=lista1,lista2,lista3
    listafinal=list(listafinal)
    return listafinal
