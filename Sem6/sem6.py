# Напишите программу вычесления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет оперций стандартный.

# пример:

# 2+2=>4;
# 1+2*3=>7;
# 1-2*3=>-5;

# добавьте возможность использования скобок, меняющих приоритет операций.

# пример:

# 1+2*3=>7;
# (1+2)*3=>
# РЕШЕНИЕ

my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
my_list_out = list(my_text)
print(my_list_out)
i = 1


def Calc(my_list):
    i = 1
    while '*' in my_list or '/' in my_list:
        if my_list[i] == '*':
            my_list[i-1] = int(my_list[i-1])*int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        elif my_list[i] == '/':
            my_list[i-1] = int(my_list[i-1])/int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        else:
            i += 1
    i = 1
    while '+' in my_list or '-' in my_list:
        if my_list[i] == '+':
            my_list[i-1] = int(my_list[i-1])+int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        elif my_list[i] == '-':
            my_list[i-1] = int(my_list[i-1])-int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        else:
            i += 1
    return my_list


while '(' in my_list_out:
    bracket_left = my_list_out.index('(')
    bracket_right = my_list_out.index(')')
    my_list_out = my_list_out[:bracket_left]+Calc(my_list_out[bracket_left+1:bracket_right])+my_list_out[bracket_right+1:]


print(Calc(my_list_out))
# Решение1:
# #my_text = input()
# #print(eval(my_text))
# exec(f'print({my_text})')
