# Codeforces Problem
# Name: {{cookiecutter.problem_name}}
# Link: https://codeforces.com/problemset/problem/{{cookiecutter.problem_number}}/{{cookiecutter.problem_letter}}


def main():
    number_of_tests = int(input())
    for _ in range(number_of_tests):
        number = int(input())
        print(run(number))


def run(number):
    return 2 * number


if __name__ == "__main__":
    main()
