



from operator import itemgetter
main_list = []


def list_sort():
    global main_list
    main_list = sorted(main_list, key=itemgetter(1))
    print(main_list)

def slope_cal(a, b):
        y = a[1] - b[1]
        x = a[0] - b[0]
        return y/x

def


def bottom_part():
    slope = 0
    flag = 0
    last_index = 0
    bot_line = []
    bot_line.append(main_list[0])
    first_stage = main_list.copy()
    first_stage.remove(main_list[0])
    while True:

        bot_line.append(first_stage[0])
        last_index += 1
        slope = slope_cal(bot_line[last_index - 1], bot_line[last_index])
        second_stage = first_stage.copy()
        second_stage.remove(first_stage[0])
        for i in second_stage:
            if slope < slope_cal(bot_line[last_index], i):
                bot_line.remove(bot_line[last_index])
                bot_line.append(i)
                flag = 1
        first_stage.remove(bot_line[last_index])


print("Welcome\n ")
n_inputs = int(input("Please enter of inputs:"))

while True:
    list_X = int(input("Enter X"))
    list_Y = int(input("Enter Y"))
    leaf = list_X, list_Y
    main_list.append(leaf)
    n_inputs -= 1
    if n_inputs == 0:
        break
list_sort()
bottom_part()
