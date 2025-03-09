import time
import tracemalloc

def measure(function, *args, **kwargs):
    start_time = time.perf_counter()
    tracemalloc.start()

    result = function(*args, **kwargs)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    res_time = end_time - start_time
    peak_memory = peak / 10 ** 6

    print(f"Execution time: {res_time:.6f} seconds")
    print(f"Peak memory usage: {peak_memory:.6f} MB")

    return result, res_time, peak_memory


def file_read(input_file_path='../txtf/input.txt'):
    with open(input_file_path, 'r') as file:
        lines = [list(map(int, line.split())) for line in file]
        print('Input:')
        for line in lines:
            print(*line)
    return tuple(lines)


def file_write(writing, output_file_path='../txtf/output.txt'):
    with open(output_file_path, 'w') as file:
        if isinstance(writing, list):
            for line in writing:
                if isinstance(line, list):
                    line = " ".join(map(str, line))
                file.write(f"{line}\n")
                print(f"Output: {line}")
        else:
            file.write(str(writing))
            print(f"Output: {writing}")