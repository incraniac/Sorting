def bubble_sort (array , order = True) :
    # length = len (array)
    if order == True :
        for i in range (len(array)) :
            for j in range (0,len(array)-i-1) :
                if array[j] > array [j+1] :
                    (array[j],array[j+1]) = (array[j+1],array[j])
        return array

    elif order == False :
        for i in range (len(array)) :
            for j in range (0,len(array)-i-1) :
                if array[j] < array [j+1] :
                    (array[j],array[j+1]) = (array[j+1],array[j])
        return array


data = [2,5,4,-1,-9,5,0,-7]
print (bubble_sort(data))
print (bubble_sort(data,order=False))
print("not changing your code dont worry")
