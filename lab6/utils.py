import time
import tracemalloc
from typing import Tuple, Generator, Type
from inspect import stack
from pathlib import Path




def get_calling_file_path() -> Path:

    file_path = stack()[2].filename
    return Path(file_path).resolve()


def read(filename: str = '../txtf/input.txt', type_convert: Type = int) -> Generator[list, None, None]:

    file_path = Path(get_calling_file_path()).parent / filename

    try:
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue
                if type_convert is not str:
                    try:
                        parts = [type_convert(part) for part in parts]
                    except ValueError as e:
                        print(f"Ошибка конвертации строки: {e}")
                        continue
                yield parts
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")


def write(*values, sep: str = " ", end: str = "\n", filename: str = '../txtf/output.txt',
          to_end: bool = False) -> None:
    file_path = Path(get_calling_file_path()).parent / filename
    mode = 'a' if to_end else 'w'

    try:
        with file_path.open(mode, encoding='utf-8') as file:
            print(*values, sep=sep, end=end, file=file)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл {file_path}: {e}")


def time_data(func) -> float:

    time_start = time.perf_counter()
    func()
    elapsed = time.perf_counter() - time_start
    print(f"Время выполнения {func.__name__}: {elapsed:.6f} секунд")
    return elapsed


def memory_data(func) -> Tuple[float, float]:

    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    current_mb = current / (1024 ** 2)
    peak_mb = peak / (1024 ** 2)
    print(f"Потребление памяти {func.__name__}: текущее {current_mb:.2f} МБ, пиковое {peak_mb:.2f} МБ")
    return current_mb, peak_mb





