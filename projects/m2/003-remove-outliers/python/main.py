unsorted_int = []

def sort_input(unsorted_int):
    sorted_int = sorted(unsorted_int)
    return sorted_int

def remove_smallest_largest(sorted_int):
    list_copy = sorted_int[1:-1]
    return list_copy

def double_remove(sorted_int):
    list_copy = remove_smallest_largest(sorted_int)
    return (remove_smallest_largest(list_copy))

def collect_input():
    user_int = int(input('Start to input your values (at least 4 values) (0 to end and sort): '))

    if user_int != 0:
        unsorted_int.append(user_int)
        collect_input()

    if user_int == 0:
        list_len = len(unsorted_int)

        if list_len < 4:
            print('You have to enter at least 4 value')
            return

        sorted_int = sort_input(unsorted_int)
        outliers_remove_X2 = double_remove(sorted_int)
        
        print(f'Your list after the outliers removed is: \n {outliers_remove_X2}')
        print(f'Your original list is: \n {sorted_int}')

if __name__ == '__main__':
    print('Hello USER this program read a list of number and remove the two largest and two smallest values from it' )
    collect_input()