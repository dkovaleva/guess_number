# -*- coding: utf-8 -*-

def check_answer(answer):
    return answer in ['y', 'n']

def get_answer(function_check):
    result_ok = False
    while not result_ok:
        answer = input()
        if function_check(answer):
            result_ok = True
        else:
            print('Oops! You put in invalid answer. Try once more:')
    return answer


def guess_number(point1, point2):
    start = point1
    end = point2
    while True:
        if (end - start) > 2:
            middle = round(start + (end-start)/2 + 0.5)
            print('Is your number bigger than %s? Print "y" if yes, else "n"' % middle)
            if get_answer(check_answer) == 'y':
                start = middle
            else:
                end = middle
        else:
            while True:
                middle = start + (end - start) - 1
                print('Is your number bigger than %s? Print "y" if yes, else "n"' % middle)
                if get_answer(check_answer) == 'y':
                    return end
                else:
                    if (end - start) < 2:
                        return start
                    else:
                        end = middle




def main():
    print('Hello! Please, choose the number from 1 to 1000000 (1 million) and I will guess, what number is it!')
    number = guess_number(0, 1000000)
    print('I know! Your number is %s!' % number)


if __name__ == "__main__":
    main()