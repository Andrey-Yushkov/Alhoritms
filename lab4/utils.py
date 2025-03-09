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
        lines = file.read().splitlines()
        print("Input:")
        for line in lines:
            print(line)
    return lines


def file_write(writing, output_file_path='../txtf/output.txt'):

    with open(output_file_path, 'w') as file:
        for line in writing:
            file.write(f"{line}\n")
        print("Output:")
        for line in writing:
            print(line)


