# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




def loop_issue():

    fruit_list = ['banana', 'orange', 'apple', 'strawberry' ]

    print('list id is {}'.format(id(fruit_list)))

    favorite = input('What is your favorite fruits? : ')

    for fruit in fruit_list:

        print('fruit is {} '.format(fruit))

        if fruit == favorite:

            print('だいちゅき')
            print('fruit id is {}'.format(id(fruit)))
            print('favorite id is {}'.format(id(favorite)))

        else:
            print('きらい')

def others():

    #format 使い方
    print( "Hi, I\'m {}".format('Tom') )

    #is 演算子

    #数値が同じならidも同じ
    a = 1
    b = 1
    c = a
    print("id of a is {}".format(id(a)))
    print("id of a is {}".format(id(b)))
    print("id of a is {}".format(id(1)))

    print(a is b) #同じ値ならTrue
    print(a is c) #c = aであるため、True

    b = 2
    print(a is b)  #値が変わっているため、False

    d = None

    if d is None :
        print('d is {}'.format('None'))
    else :
        print('d is not {}').format('None')


    #input関数の戻り値は、string型
    age = int(input('How old are you? : '  ))

    if age >= 18 :
        print('You are adult')
    else:
        print('You are child17')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    loop_issue()
