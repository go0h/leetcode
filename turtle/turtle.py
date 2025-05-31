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

    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    # Создание и заполнение DP таблицы
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = grid[0][0]

    # Заполнение первой строки
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Заполнение первого столбца
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Заполнение остальной части таблицы
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])

    # Восстановление пути
    path = []
    i, j = n-1, m-1
    while i > 0 or j > 0:
        if i == 0:
            path.append('R')
            j -= 1
        elif j == 0:
            path.append('D')
            i -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                path.append('D')
                i -= 1
            else:
                path.append('R')
                j -= 1

    # Переворачиваем путь, так как собирали его с конца
    path.reverse()

    print(dp[-1][-1])
    print(''.join(path))

if __name__ == '__main__':
    main() # type: ignore