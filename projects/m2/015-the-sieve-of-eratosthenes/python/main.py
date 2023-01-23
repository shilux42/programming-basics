def num_list_gen(limit):
    num_list = []
    num = -1

    while num < limit:
        num += 1
        num_list.append(num)

    return num_list

def list_cleaner(a_list):
    a_list_copy = a_list.copy()

    for num in a_list:
        if num == 0:
            a_list_copy.remove(num)

    return a_list_copy


def sieve_of_eratosthenes(limit):
    p = 2
    num_list = num_list_gen(limit)
    num_list[1] = 0
    num_list_copy = num_list.copy()

    while p != limit:

        for num in num_list:

            if num != 0:

                if (num >= p) and (p * num <= limit):
                    not_prime = p * num

                    if not_prime in num_list_copy:
                        index = num_list_copy.index(not_prime)
                        num_list_copy[index] = 0
            
        
        p += 1
    
    
    return num_list_copy

print (list_cleaner(sieve_of_eratosthenes(10000)))