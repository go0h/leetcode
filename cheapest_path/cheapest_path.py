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

    field = []
    for i in range(0, n):
        field.append(list(map(int, input().split())))

    print(f"rows = {n}, columns = {m}")
    print('\n'.join([' '.join([str(item) for item in row]) for row in field]))

    cheapest_path = [[0 for _ in range(0, m)] for _ in range(0, n)]

    # filling the first row
    cheapest_path[0][0] = field[0][0]
    for i in range(1, m):
        cheapest_path[0][i] = field[0][i] + cheapest_path[0][i - 1]

    # filling the first column
    for i in range(1, n):
        cheapest_path[i][0] = field[i][0] + cheapest_path[i - 1][0]

    # filling field
    for row in range(1, n):
        for col in range(1, m):
            cheapest_path[row][col] = min(
                cheapest_path[row - 1][col] + field[row][col],
                cheapest_path[row][col - 1] + field[row][col] 
            )
    
    print(cheapest_path[-1][-1])
    # print('\n'.join([' '.join([str(item) for item in row]) for row in cheapest_path]))
    

if __name__ == '__main__':
    main()