##########################################################################
# Python Challenge Level 2 Solution
# Wilson Woods
# 10/17/19
# This program accepts a string and converts all characters of the string
# into ASCII codes
# QuickSort algorithm is then employed to sort the list of integer values
##########################################################################

def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


#list(chars)
#n = len(list(chars))
#arr = [0] * n
#i = 0
#for c in chars:
#    arr[i] = ord(c)
#    i+=1
#quickSort(arr,0,n-1)
#print ("Sorted ASCII codes: ")
#for x in range(0, n):
#    print(arr[x]),
#######################################################################
#count = 0
#for j in range(0, n):
#    count+=1
#    if arr[j] != arr[j+1]:
#        print "ASCII code ", arr[j-1], " appears ", count , " times."
#        count = 0

######################################################################
# better solution:
for a in chars:
    l = chars.count(a)
    if l < 20:
        print a, ":", l