import random
def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    flag1 = 0
    empty_list = []
    while flag1 < 3:
        flag1 += 1
        data = random.choice(cards)
        def add_to_list(num):
                empty_list.append(num)
                full_list = []
                full_list += empty_list
                print(full_list)
                return full_list
        def sum_of_list():
            sum_of_list = 0
            list1 = add_to_list(data)
            for nums in list1:
                sum_of_list += nums
            return sum_of_list
        
        print(sum_of_list()) 
black_jack()


