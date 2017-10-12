''' The function below consists logic to perform a insertion sort in
    acsending order on a list of numeric values passed in as a parameter'''

def insertionSort(arr):
    print('length of list:',len(arr))   #prints the length of the input list
    if len(arr) <= 1:                   #checks if the length is <= 1  
        return arr                      #and returns the array
    else:
        for i in range(0,len(arr)):     #insertion sort: picks an element and inserts
            j = i                       #it in the correct position.
            while j>=1 and arr[j] < arr[j-1]:
                (arr[j],arr[j-1]) = (arr[j-1],arr[j])
                j = j - 1
        return arr


