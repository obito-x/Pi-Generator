# find_pi_to_the_nth_digit.py
# {obito}
"""
    -About-

    'This program is the generator of pi with nth decimal place.'

    advantage  : if user enter other input instead of number , no effect on this program.
    diadvantage: program output materials form is depend on the size of user terminal.
                 But don't worry. even the view is not clear , this program can work exactly
                 recommend: [ 81 x 24  ]
                 use this ratio on your terminal and run this program.
                 And view clearly.
    enjoy :)
"""


from colorama import Fore

# variables
pi = 22/7
ch = 'y'


while ch == 'y':
    print('\n'*10)  # Space

    print(Fore.RESET + '\n************************************************************\n')
    print(Fore.LIGHTGREEN_EX + '\n This program is the generator of pi with nth decimal place \n'
          + Fore.RESET)  # Title
    print('\n************************************************************\n')

    print('\n'*8)  # Space

    print(Fore.RED + '\nWarning:' + Fore.YELLOW + 'The Maximum: 50!!\n'
          + ' '*8 + 'Only whole numbers of decimal place can enter!\n' + ' '*8 + 'eg: 0,4,23,50\n'
          + Fore.RESET)  # Warning
    # maximum is 50 but allow to enter to 55!!!

    try:
        n = int(input(Fore.CYAN + "\nEnter the nth decimal place of pi: " + Fore.GREEN))
    except:
        continue
    # user input and error handling

    if n < 51:
        try:
            print(Fore.CYAN + '\nPi: ' + Fore.RESET + f'%1.{n}f' % pi)
        except:
            continue
        # if user enter negative values, this error handling can fix
        # Generate Less than 51
    if n > 50:
        print(Fore.CYAN + '\nPi: ' + Fore.RESET + '%1.51f' % pi)
        print(Fore.LIGHTRED_EX + "\nThis generator can't generate after 51th." + Fore.RESET)
        # Generate greater than 55

    ch = input(Fore.GREEN + '\nEnter {-y-} to do again: ' + Fore.RESET)  # ask do again

    print('\n'*4)  # Space


# ******************************************************************************************** #
