def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
#A = [0, 1, 3, 5, 7, 6, 10, 4, 9, 8, 11, 2, 12]
A = [0,0,100,1,2,4,5,3,6,10,7,9,8,12,11,14,13,20,16,15,13,19,18,17]
#talist = input("List: ")
#exec(f"A = {talist}")
B, C = split_list(A)

def sortlist(a_list, b_list):
    returnlist = []
    aorglen = len(a_list)
    borglen = len(b_list)
    while len(returnlist)+1 != aorglen + borglen:
        if a_list[0] > b_list[0]:
            if returnlist == []:
                returnlist.append(a_list[0])
                returnlist.append(b_list[0])
                a_list.pop(0)
                b_list.pop(0)
                print(returnlist)
            else:
                for i in range(len(returnlist)):
                    if returnlist[i] <= a_list[0]:
                        returnlist.insert(i, a_list[0])
                        print(returnlist)
                        a_list.pop(0)
                        break
        elif a_list[0] < b_list[0]:
            if returnlist == []:
                returnlist.append(b_list[0])
                returnlist.append(a_list[0])
                b_list.pop(0)
                a_list.pop(0)
                print(returnlist)
            else:
                for i in range(len(returnlist)):
                    if returnlist[i] <= b_list[0]:
                        returnlist.insert(i, b_list[0])
                        print(returnlist)
                        b_list.pop(0)
                        break
        if a_list == []:
            while b_list != []:
                for i in range(len(returnlist)):
                    if returnlist[i] <= b_list[0]:
                        returnlist.insert(i, b_list[0])
                        print(returnlist)
                        b_list.pop(0)
                        break
            else: return returnlist
        if b_list == []:
            while a_list != []:
                for i in range(len(returnlist)):
                    if returnlist[i] <= a_list[0]:
                        returnlist.insert(i, a_list[0])
                        print(returnlist)
                        a_list.pop(0)
                        break
            else: return returnlist

print(sortlist(B, C))
