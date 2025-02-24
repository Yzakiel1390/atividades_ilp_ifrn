from ast import literal_eval

print(f"{"\033[1;33mLista de Exercícios 4 - ILP\033[m":^51}")
print("\033[30m=\033[m"*51)
print(" 1 - Área do Quadrado \n 2 - Perímetro do Quadrado \n 3 - Área do Retângulo \n 4 - Perímetro do Retângulo \n 5 - c em [a, b] \n 6 - É Divisível \n 7 - É Par (2) \n 8 - Divisão Completa \n 9 - Quantidade de Bolos \n 10 - Lista 1 até n \n 11 - Pares de 2 até n \n 12 - n Primeiros Múltiplos de 3 \n 13 - n Primeiros Múltiplos de a \n 14 - Somar Lista de Inteiros \n 15 - Média Lista de Inteiros \n 16 - Soma Lista de Inteiros Pares e Ímpares \n 17 - Somas Diferentes \n 18 - Lista Pares e Ímpares \n 19 - Soma de Listas \n 20 - Elementos em ambos \n 21 - Todos os elementos em ambos \n 22 - Intercalação de Listas \n 23 - Saída 1 \n 24 - Saída 2 \n 25 - Saída 3 \n 26 - Saída 4 \n 27 - Saída 5 \n 28 - Saída 6 \n 29 - Saída 7 \n 30 - Saída 8")
option: str = input("\033[32m - Selecione uma das opções Acima: \033[31m\033[34m")

print("\033[30m-\033[m"*51)

match option:
    case "1":
        def square_area(n: float) -> float:
            return n ** 2

        print(f"Área: {square_area(float(input("Lado: ")))}")

    case "2":
        def square_perimeter(n: float) -> float:
            return 4 * n
        
        print(f"Perímetro: {square_perimeter(float(input("Lado: ")))}")

    case "3":
        def rectangle_area(base: float, height: float) -> float:
            return base * height
        
        base: float = float(input("Base: "))
        height: float = float(input("Altura: "))

        print(f"Área: {rectangle_area(base, height)}")

    case "4":
        def rectangle_perimeter(base: float, height: float) -> float:
            return 2 * base + 2 * height
        
        base: float = float(input("Base: "))
        height: float = float(input("Altura: "))

        print(f"Área: {rectangle_perimeter(base, height)}")
    
    case "5":
        def in_interval(start: int, end: int, search: int) -> bool:
            return start <= search <= end
        
        start: int = int(input("a: "))
        end: int = int(input("b: "))
        search: int = int(input("c: "))

        print(in_interval(start, end, search))

    case "6":
        def is_divisible(dividend: int, divisor: int) -> bool:
            return dividend % divisor == 0
        
        dividend: int = int(input("Dividendo: "))
        divisor: int = int(input("Divisor: "))

        print(is_divisible(dividend, divisor))

    case "7":
        def is_even_two(number1: int, number2: int) -> tuple[bool, bool]:
            return (number1 % 2 == 0, number2 % 2 == 0)
        
        number1: int = int(input("Número 1: "))
        number2: int = int(input("Número 2: "))

        print(*is_even_two(number1, number2), sep="\n")
        
    case "8":
        def complete_division(number1: int, number2: int) -> tuple[int, int]:
            return (number1 // number2, number1 % number2)
        
        number1: int = int(input("Número 1: "))
        number2: int = int(input("Número 2: "))

        print(*complete_division(number1, number2), sep="\n")
        
    case "9":
        def cake_amount(money: float, price: float) -> tuple[int, int]:
            return (money // price, money % price)
        
        money: float = float(input("Dinheiro: "))

        print(*cake_amount(money, 8.50), sep="\n")
        
    case "10":
        def list_1_n(n: int) -> list[int]:
            return list(range(1, n + 1))
        
        number: int = int(input("Número: "))

        print(list_1_n(number))
        
    case "11":
        def evens_2_n(n: int) -> list[int]:
            return list(range(2, n + 1, 2))
        
        number: int = int(input("Número: "))

        print(evens_2_n(number))
    
    case "12":
        def multiple_3(amount: int) -> list[int]:
            return list(range(3, 3 * amount + 1, 3))
        
        amount: int = int(input("Número: "))

        print(multiple_3(amount))
    
    case "13":
        def multiple_n_a(number: int, amount: int) -> list[int]:
            return list(range(number, number * amount + 1, number))
        
        number: int = int(input("Número: "))
        amount: int = int(input("Quantidade: "))

        print(multiple_n_a(number, amount))

    case "14":
        def sum_list(list_num: list[int]) -> int:
            return sum(list_num)
        
        list_num: list[int] = literal_eval(input("Lista de Inteiros: "))
        print(sum_list(list_num))

    case "15":
        def mean_list(list_num: list[int]) -> int:
            return sum(list_num) / len(list_num)
        
        list_num: list[int] = literal_eval(input("Lista de Inteiros: "))
        print(mean_list(list_num))

    case "16":
        def sum_even_odd_list(list_num: list[int]) -> tuple[int]:
            even_numbers: list[int] = [n for n in list_num if n % 2 == 0]
            odd_numbers: list[int] = [n for n in list_num if n % 2 != 0]
            return (sum(even_numbers), sum(odd_numbers))
        
        list_num: list[int] = literal_eval(input("Lista de Inteiros: "))
        print(*sum_even_odd_list(list_num), sep="\n")

    case "17":
        def different_sums(list_num: list[int], param: int) -> int:
            match param:
                case 0:
                    return sum(list_num)
                case param if param > 0:
                    return sum([n for n in list_num if n % 2 == 0])
                case param if param < 0:
                    return sum([n for n in list_num if n % 2 != 0])
        
        list_num: list[int] = literal_eval(input("Lista de Inteiros: "))
        param: int = int(input("- Parâmetro: "))
        print(different_sums(list_num, param))

    case "18":
        def even_and_pairs_list(list_num: list[int]) -> tuple[list[int]]:
            even_list: list[int] = [n for n in list_num if n % 2 == 0]
            odd_list: list[int] = [n for n in list_num if n % 2 != 0]
            return (even_list, odd_list)
        
        list_num: list[int] = literal_eval(input("Lista de Inteiros: "))
        print(*even_and_pairs_list(list_num), sep="\n")

    case "19":
        def sum_lists(list_num_1: list[int], list_num_2: list[int]) -> list[int]:
            return [list_num_1[i] + list_num_2[i] for i in range(len(list_num_1))]

        list_num_1: list[int] = literal_eval(input("Lista de Inteiros 1: "))
        list_num_2: list[int] = literal_eval(input("Lista de Inteiros 2: "))
        print(sum_lists(list_num_1, list_num_2))

    case "20":
        def same_elements(list_num_1: list[int], list_num_2: list[int]) -> list[int]:
            set_1: set[int] = set(list_num_1)
            set_2: set[int] = set(list_num_2)

            return list(set_1 & set_2)

        list_num_1: list[int] = literal_eval(input("Lista de Inteiros 1: "))
        list_num_2: list[int] = literal_eval(input("Lista de Inteiros 2: "))
        print(same_elements(list_num_1, list_num_2))
    
    case "21":
        def both_elements(list_num_1: list[int], list_num_2: list[int]) -> list[int]:
            set_1: set[int] = set(list_num_1)
            set_2: set[int] = set(list_num_2)

            return list(set_1 | set_2)

        list_num_1: list[int] = literal_eval(input("Lista de Inteiros 1: "))
        list_num_2: list[int] = literal_eval(input("Lista de Inteiros 2: "))
        print(both_elements(list_num_1, list_num_2))
    
    case "22":
        def intercalation_lists(list_num_1: list[int], list_num_2: list[int]) -> list[int]:
            new_list: list[int] = []

            for i in range(len(list_num_1)):
                new_list.append(list_num_1[i])
                new_list.append(list_num_2[i])

            return new_list

        list_num_1: list[int] = literal_eval(input("Lista de Inteiros 1: "))
        list_num_2: list[int] = literal_eval(input("Lista de Inteiros 2: "))
        print(intercalation_lists(list_num_1, list_num_2))

    case "23":
        def funcao(a, b):
            x = a + b
            return x

        print(funcao(2, 5)) # 7
        print(funcao(0, -3)) # -3

    case "24":
        def funcao(a, b):
            if a > 0:
                return b * 2
            return b * -1

        print(funcao(2, 5))  # 10
        print(funcao(-2, 3)) # -3
        print(funcao(0, -6)) # 6

    case "25":
        def funcao(a):
            x = 0
            i = 1
            while i <= 4:
                if i == a:
                    return x
                x = x + i
                i = i + 1
            return x

        print(funcao(10)) # 10
        print(funcao(3))  # 3
        print(funcao(1))  # 0

    case "26":
        def f1(x):
            return x ** 2 - 1

        def f2(x):
            return  x // 2 + 1

        print(f1(5)) # 24
        print(f2(7)) # 4
        print(f1(f2(15))) # 63

    case "27":
        def f1(x):
            return x % 2 == 0

        def f2(x):
            y = x
            while y % 2 != 0:
                y = y + 1
            return y

        def f3(x):
            if f1(x):
                return x
            return f2(x)

        print(f1(5))  # False
        print(f1(6))  # True
        print(f2(8))  # 8
        print(f2(11)) # 12
        print(f3(1))  # 2
        print(f3(4))  # 4

    case "28":
        def funcao(a, b):
            s = (b - a + 1) * (a + b) / 2
            return s

        print(funcao(1, 7)) # 28.0
        s = 5
        r = 9
        t = funcao(5, 9)
        print(t) # 35.0
        print(s) # 5

    case "29":
        def funcao(a1, n):
            an = a1 + (n - 1) * r
            s = n * (a1 + an) / 2
            return s

        r = 2
        i = 3
        q = 5
        s = 0
        funcao(i, q)
        print(s) # 0
        s = funcao(i, q)
        print(s) # 35.0

    case "30":
        import math

        def funcao(a, b, c):
            global erro
            erro = False
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                erro = True
                return None
            r = math.sqrt(delta)
            x1 = (- b + r) / (2 * a)
            x2 = (- b - r) / (2 * a)
            return x1, x2

        erro = None
        print(erro) # None
        funcao(1, -3, -10)
        print(erro) # False
        funcao(5, 3, 5)
        print(erro) # True
    
    case _: print("\033[31mOpção Inválida!\033[m")