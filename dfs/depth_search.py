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

    edges = dict((k, []) for k in range(1, n + 1))
    visited = dict((k, False) for k in range(1, n + 1))

    for _ in range(0, m):
        s, e = list(map(int, input().split()))[:2]
        edges[s].append(e)
        edges[e].append(s)


    stack = [1]
    result = []
    visited[1] = True

    while stack:
        u = stack.pop()
        result.append(u)
        for v in edges[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    # def depth_search(vertice, edges):
    #     if visited[vertice]:
    #         return
    #     visited[vertice] = True
    #     for end in edges[vertice]:
    #         if vertice != end:
    #             depth_search(end, edges)

    # depth_search(1, edges)

    # result = [k for (k, v) in visited.items() if v == True]
    print(len(result))
    print(' '.join(str(i) for i in sorted(result)))

if __name__ == '__main__':
    main()