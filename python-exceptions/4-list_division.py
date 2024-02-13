#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    newList = []
    for index in range(list_length):
        try:
            div = my_list_1[index] / my_list_2[index]
            newList.append(div)
        except ZeroDivisionError:
            div = 0
            newList.append(div)
            print("division by 0")
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            div = 0
            newList.append(div)
            print("wrong type")
        finally:
            pass
    return newList
