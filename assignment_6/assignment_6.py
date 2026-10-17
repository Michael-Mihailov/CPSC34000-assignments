# NOTE: You need to add the appropriate .txt file yourself!!!

import time


def read_file(filename: str, numLines: int = -1) -> list:
    data = []

    lineNum = 0
    with open(filename, "r") as file:
        for line in file:
            if numLines >= 0 and lineNum >= numLines:
                break
            row = tuple(line.split())
            data.append(row)
            lineNum += 1

    return data

def bubble_sort(data: list) -> list:
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j + 1] = data[j + 1], data[j]
        
    return data

def merge_sort(data: list) -> list:
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    merged = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i][0] <= right_half[j][0]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
    merged.extend(left_half[i:])
    merged.extend(right_half[j:])

    return merged

def time_sorting_algorithm(sort_func: callable, data: list) -> tuple[list, float]:
    start_time = time.time()
    result = sort_func(data)
    end_time = time.time()
    return result, (end_time - start_time)


def main():
    print("Assignment 6: Sorting Algorithms Performance Comparison")
    print()

    crime_data_filename = "Crime_Data_from_2020_to_2024(2).txt"
    ev_data_filename = "Electric_Vehicle_Population_Data(2).txt"

    # Test Crime Data File
    crime_data = read_file(crime_data_filename, 10000)
    print(f"Using the first {len(crime_data)} lines from the {crime_data_filename} file")
    sorted_crime_data_bubble, bubble_time = time_sorting_algorithm(bubble_sort, crime_data.copy())
    print(f"Bubble Sort Time for Crime Data: {bubble_time:.6f} seconds")
    sorted_crime_data_merge, merge_time = time_sorting_algorithm(merge_sort, crime_data.copy())
    print(f"Merge Sort Time for Crime Data: {merge_time:.6f} seconds")

    print("Results match:", sorted_crime_data_bubble == sorted_crime_data_merge)
    print(f"Bubble Sort / Merge Sort time ratio: {bubble_time / merge_time:.2f}")


    print()


    # Test EV Data File
    ev_data = read_file(ev_data_filename, 10000)
    print(f"Using the first {len(ev_data)} lines from the {ev_data_filename} file")
    sorted_ev_data_bubble, bubble_time = time_sorting_algorithm(bubble_sort, ev_data.copy())
    print(f"Bubble Sort Time for EV Data: {bubble_time:.6f} seconds")
    sorted_ev_data_merge, merge_time = time_sorting_algorithm(merge_sort, ev_data.copy())
    print(f"Merge Sort Time for EV Data: {merge_time:.6f} seconds")

    print("Results match:", sorted_ev_data_bubble == sorted_ev_data_merge)
    print(f"Bubble Sort / Merge Sort time ratio: {bubble_time / merge_time:.2f}")

    print()
    print("END OF PROGRAM")



if __name__ == "__main__":
    main()