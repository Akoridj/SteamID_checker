import itertools
import time

symbols = "abcdefghijklmnopqrstuvwxyz0123456789-_"

def parse_input(input_str):
    if '-' in input_str:
        try:
            start, end = map(int, input_str.split('-'))
            if start <= 0 or end < start:
                raise ValueError("Неверный интервал.")
            return list(range(start, end + 1))
        except:
            raise ValueError("Введите корректный интервал в формате x-y")
    else:
        try:
            length = int(input_str)
            if length <= 0:
                raise ValueError("Длина должна быть положительным числом.")
            return [length]
        except:
            raise ValueError("Введите либо целое число, либо интервал вида x-y")

def format_duration(seconds):
    minutes, sec = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}ч {minutes}мин {sec}сек"

def generate_and_write(lengths, filename="list.txt"):
    with open(filename, "w") as file:
        for length in lengths:
            total = len(symbols) ** length
            print(f"Генерация длины: {length} ({total} записей)")

            start = time.time()
            buffer = ("".join(combo) + "\n" for combo in itertools.product(symbols, repeat=length))
            file.writelines(buffer)
            duration = time.time() - start

            print(f"Генерация длилась: {format_duration(duration)}\n")

def main():
    try:
        user_input = input("Введите длину ID или интервал (например: x или x-y): ").strip()
        lengths = parse_input(user_input)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    generate_and_write(lengths)

if __name__ == "__main__":
    main()
