# Utility function to swap elements `A[i]` and `A[j]` in the list
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Function to rearrange the list such that every second element
# of the list is greater than its left and right elements
def rearrange_array(array):
    # start from the second element and increment index
    # by 2 for each iteration of the loop
    for i in range(1, len(array), 2):

        # if the previous element is greater than the current element,
        # swap the elements
        if array[i - 1] > array[i]:
            swap(array, i - 1, i)

        # if the next element is greater than the current element,
        # swap the elements
        if i + 1 < len(array) and array[i + 1] > array[i]:
            swap(array, i + 1, i)
