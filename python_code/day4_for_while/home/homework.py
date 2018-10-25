import random
import string


class Code:

    prompt = ['too small', 'Congratulate!, You are right!', 'too big']

    @staticmethod
    def generate(num):

        ran_code = ''

        words = ''.join((string.ascii_letters, string.digits))

        for i in range(num):
            ran_code += random.choice(words)

        return ran_code

    @staticmethod
    def sieve(res, num):
        return (num > res) - (num < res)

    @staticmethod
    def start_guess():
        try:

            ran_num = random.randint(0, 100)

            print('You guess num is %s' % ran_num)

            while True:

                r = int(input('Please input a num'))

                sieve_right = Code.sieve(ran_num, r) + 1

                print('The num you guess is', Code.prompt[sieve_right])

                if sieve_right is 1:
                    break

        except ValueError:
            print('Please input number: \t')


print('The generate code is %s' % Code.generate(6))
Code.start_guess()

