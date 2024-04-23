# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3,3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.

def remove_duplicates(nums):
    new_list = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            new_list.append(nums[i])
    return new_list

print(remove_duplicates([1,2,3,3])) 


# 2- 
# Case1:
    # The length is even, the front and back halves are the same length.
# Case2:
    # The length is odd, we’ll say that the extra char goes in the front half.
    # E.g. ‘abced’, the front half is ‘abc’, the back half’de.
    # Given 2 strings, a and b, return a string of the form:
    # (a-front + b-front) + (a-back +b-back)


def split_strings (a,b):
    a_front = a[:len(a) // 2 + len(a) % 2]
    a_back = a[len(a) // 2 + len(a) % 2:]
    b_front = b[:len(b) // 2 + len(b) % 2]
    b_back = b[len(b) // 2 + len(b) % 2:]
    return a_front + b_front + a_back + b_back

print(split_strings('abcde', '12345')) 
print(split_strings('abc', '12345'))    



# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False


def check_diff(nums):
    return len(nums) == len(set(nums))

print(check_diff([1,5,7,9]))
print(check_diff([2,4,5,5,7,9]))


# 4- Given unordered list, sort it using algorithm bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

# 5- Gusses game

# ● Your game generates a random number and gives only 10 tries for the user to
# guess that number.
# ● Get a user input and compare it with the random number
# ● Display a hit message to the user in case the use number is smaller or bigger of
# the random number
# ● If the user type number is out of range(100), display a message that is not allowed
# and don’t count this as try.
# ● If user type a number that has been entered before, display a hint message and
# don’t count this as try
# ● In case the user entered a correct number within the 10 tries, display a
# congratulations message and let your application guess another random number
# with the remain number of tries
# ● If the user finishes all his tries, display a message to ask him if he wants to play
# again or not.


def guess_game():
    import random
    random_number = random.randint(1, 100)
    tries = 10
    guessed_numbers = []
    while tries > 0:
        user_input = int(input("Enter a number: "))
        if user_input < 1 or user_input > 100:
            print("Number is not allowed")
            continue
        if user_input in guessed_numbers:
            print("Number has been entered before")
            continue
        if user_input == random_number:
            print("Congratulations")
            random_number = random.randint(1, 100)
            tries = 10
            guessed_numbers = []
            continue
        if user_input < random_number:
            print("Number is smaller")
        else:
            print("Number is bigger")
        tries -= 1
        guessed_numbers.append(user_input)
    print("You lost\nDo you want to play again?")
    user_input = input("Enter 'yes' or 'no': ")
    if user_input == 'yes':
        guess_game()
    else:
        print("Ok, Goodbye")
        
        
guess_game();