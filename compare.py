
def compare_list(lista,listb):

    point_a = 0
    point_b = 0
    for i in range(len(lista)):
        if lista[i] > listb[i]:
            point_a+=1
        elif lista[i] < listb[i]:
            point_b+=1
        else:
            continue

    print(point_a,point_b)

compare_list([17,28,30],[99,16,8])
