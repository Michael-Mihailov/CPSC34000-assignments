# Template from Juvenal Nava               

import time
from linearSearch import linearSearch 
from binarySearch import binarySearch


# Open Input Data File
infile = open('data.txt')

#Start Empty List
table = list()   

# Load the table of records from the file
for data in infile:
    table.append( tuple( data.split('\t') ))   # split all the different fields (tab delimiter) and make a tuple from each row


def time_search_algorithm(search_func: callable, arr: list, target: int) -> tuple[int, float]:
    start_time = time.time()
    result = search_func(arr, target)
    end_time = time.time()
    return result, (end_time - start_time)


while (input("End Program (Y/n): ") != "Y"):
    rec_num = int(input("Enter Rec Num: "))

    linearSearchResult = time_search_algorithm(linearSearch, table, rec_num)
    print()
    print("Linear Search:")
    print(f"Key: {linearSearchResult[0]}")
    print(f"Time: {linearSearchResult[1]}")
    print()

    binarySearchResult = time_search_algorithm(binarySearch, table, rec_num)
    print("Binary Search:")
    print(f"Key: {binarySearchResult[0]}")
    print(f"Time: {binarySearchResult[1]}")
    print()

print("Done!")
infile.close()

