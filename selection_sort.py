from random import randint

def initialize_list():
    '''
    A function which creates a random list of twenty (20) random numbers
    to sort.
    '''
    num_list = list()

    for i in range(0,20):
        num_list.append(randint(0,100))

    return num_list

def selection_sort(num_list):
    '''
    This function is the core sorting algorithm. It takes the list made in
    initialize_list() as an input, and returns the same list, sorted from least
    to greatest.
    '''
    length_of_list = len(num_list)

    for i in range(0, length_of_list):
        number_of_iterations = i
        swap_value = 100

        for j in range (number_of_iterations, length_of_list):
            if num_list[j] < swap_value:
                swap_value = num_list[j]
                swap_index = j

                num_list[swap_index] = num_list[number_of_iterations]
                num_list[number_of_iterations] = swap_value

    return num_list

def main():
    '''
    a test bed to demonstrate the program's functionality
    it displays a randomized list, followed by the sorted list, ten (10) times
    '''
    for i in range(0, 50):
        list = initialize_list()
        print(list)
        selection_sort(list)
        print(list)
        print()

main()
