from string import punctuation


class Robot:
    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year
        self.regex = punctuation

    def greet(self):
        print('Hello! My name is ' + self.bot_name + '.')
        print('I was created in ' + str(self.birth_year) + '.')

    def remind_name(self):
        print('Please, remind me your name.')
        wrong = True
        while wrong:
            name = input()
            if any(c in self.regex for c in name) or not name:
                print('Please enter a valid name.')
                continue
            elif any(x.isalpha() for x in name) and any(x.isnumeric() for x in name) or name.isnumeric():
                print('Please enter a valid name.')
                continue
            try:
                print('What a great name you have, ' + name + '!\n')
            except ValueError:
                print("Please enter a valid name.")
                continue

            wrong = False

    def guess_age(self):
        print('Let me guess your age.\n')
        print('Enter remainders of dividing your age by 3, 5 and 7.')
        new = True
        while new:
            rem3 = input()
            if any(c in self.regex for c in rem3) or not rem3 or rem3.isalpha():
                print('Please enter valid number.')
                continue
            elif any(x.isalpha() for x in rem3) and any(x.isnumeric() for x in rem3):
                print('Please enter a valid number.')
                continue
            elif int(rem3) not in range(1, 10):
                print('Please enter a valid number between 1 and 9.')
                continue
            rem5 = input()
            if any(c in self.regex for c in rem5) or not rem5 or rem5.isalpha():
                print('Please enter valid number.')
                continue
            elif any(x.isalpha() for x in rem5) and any(x.isnumeric() for x in rem5):
                print('Please enter a valid number.')
                continue
            elif int(rem5) not in range(1, 10):
                print('Please enter a valid number between 1 and 9.')
                continue
            rem7 = input()
            if any(c in self.regex for c in rem7) or not rem7 or rem7.isalpha():
                print('Please enter valid number.')
                continue
            elif any(x.isalpha() for x in rem7) and any(x.isnumeric() for x in rem7):
                print('Please enter a valid number.')
                continue
            elif int(rem7) not in range(1, 10):
                print('Please enter a valid number between 1 and 9.')
                continue
            try:
                rem3 = int(rem3)
                rem5 = int(rem5)
                rem7 = int(rem7)
                age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
                print("Your age is " + str(age) + "; that's a good time to start programming!\n")
            except ValueError:
                print("Please enter valid number.")
                continue

            new = False

    def count(self):
        print('Now I will prove to you that I can count to any number you want.')
        curr = 0
        elf = True
        while elf:
            count = input()
            if any(c in self.regex for c in count) or not count:
                print("Please enter a valid number for counting.")
                continue
            elif any(x.isalpha() for x in count) and any(x.isnumeric() for x in count):
                print("Please enter a valid number for counting.")
                continue
            try:
                count = int(count)
                while curr <= count:
                    print(str(curr) + '!')
                    curr = curr + 1
            except ValueError:
                print("Please enter valid number for counting.")
                continue

            elf = False

    def test(self):
        print('Let\'s test your programming knowledge.')
        print('Why do we use methods?')
        print('1. To repeat a statement multiple times.')
        print('2. To decompose a program into several small subroutines.')
        print('3. To determine the execution time of a program.')
        print('4. To interrupt the execution of a program.')
        fill = True
        while fill:
            number = input()
            if any(c in self.regex for c in number) or not number:
                print("Please enter a valid input.")
                continue
            elif any(x.isalpha() for x in number) and any(x.isnumeric() for x in number):
                print("Please enter a valid input.")
                continue
            try:
                number = int(number)
                while number != 2:
                    print('Please, try again.')
                    number = int(input())

                print("Completed, have a nice day!\n")

            except ValueError:
                print("Please enter valid input.")
                continue

            fill = False


def main():
    robot = Robot('Axis', 2021)
    robot.greet()
    robot.remind_name()
    robot.guess_age()
    robot.count()
    robot.test()
    print('Congratulations, have a nice day!')


if __name__ == '__main__':
    main()
