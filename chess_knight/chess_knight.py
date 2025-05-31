import sys


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    n, m = list(map(int, input().split()))[:2]

    field = [[0 for _ in range(0, m)] for _ in range(0, n)]

    MOVES = [(2, 1), (1, 2)]

    field[0][0] = 1
    for row in range(0, n):
        for col in range(0, m):
            if field[row][col] > 0:
                if row + 2 < n and col + 1 < m:
                    field[row + 2][col + 1] = field[row][col] + field[row + 2][col + 1]
                if row + 1 < n and col + 2 < m:
                    field[row + 1][col + 2] = field[row][col] + field[row + 1][col + 2]
    
    print(field[-1][-1])

if __name__ == '__main__':
    main()