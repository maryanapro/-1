def read_int(prompt: str) -> int:
    """Считывает целое число с проверкой корректности ввода."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: необходимо ввести целое число.")

def read_float(prompt: str) -> float:
    """Считывает вещественное число с проверкой корректности ввода."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            return value
        except ValueError:
            print("Ошибка: необходимо ввести вещественное число.")

def read_matrix(n: int, m: int) -> list[list[float]]:
    """Считывает матрицу размером n x m построчно."""
    matrix = []

    for i in range(n):
        row = []
        print(f"\nВведите элементы {i + 1}-й строки:")
        for j in range(m):
            value = read_float(f"Введите элемент a[{i + 1}][{j + 1}]: ")
            row.append(value)
        matrix.append(row)

    return matrix

def print_matrix(matrix: list[list[float]]) -> None:
    """Выводит матрицу в обычном построчном виде."""
    print("\nВведённая матрица:")

    for row in matrix:
        print(" ".join(f"{value:g}" for value in row))


def main() -> None:
    print("Ввод вещественной матрицы построчно")
    print("и вывод её элементов по столбцам\n")

    while True:
        n = read_int("Введите количество строк n: ")
        if n > 0:
            break
        print("Ошибка: количество строк должно быть больше нуля.")

    while True:
        m = read_int("Введите количество столбцов m: ")
        if m > 0:
            break
        print("Ошибка: количество столбцов должно быть больше нуля.")

    matrix = read_matrix(n, m)

    print_matrix(matrix)

if __name__ == "__main__":
    main()
