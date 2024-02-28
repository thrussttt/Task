def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # Пока есть элементы в обеих половинках
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы, если есть
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)

def merge_sort_desc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_desc(left_half)
        merge_sort_desc(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:  # изменено условие сравнения
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_desc(arr)
print("Отсортированный массив по убыванию:", arr)