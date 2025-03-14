# Задание №7 по варианту: `Снова сортировка`

Студент ИТМО, Юшков Андрей Михайлович  409941

## Вариант 23

## Задание 

Напишите программу пирамидальной сортировки на Python для последовательности в убывающем порядке. Проверьте ее, создав несколько рандомных
массивов, подходящих под параметры:

* Формат входного файла (input.txt). В первой строке входного файла содержится число n (1 ≤ n ≤ 10^5) — число элементов в массиве. Во второй
строке находятся n различных целых чисел, по модулю не превосходящих
10^9.


* Формат выходного файла (output.txt). Одна строка выходного файла с отсортированным по невозрастанию массивом. Между любыми двумя числами
должен стоять ровно один пробел.


* Для проверки можно выбрать случай, когда сортируется массив размера 10^3, 10^4, 10^5 чисел порядка 10^9, 
отсортированных в обратном порядке;
когда массив уже отсортирован в нужном порядке; когда много одинаковых
элементов, всего 4-5 уникальных; средний - случайный. Сравните на данных
сетах Randomized-QuickSort, MergeSort, HeapSort, InsertionSort.


* Есть ли случай, когда сортировка пирамидой выполнится за O(n)?


* Напишите процедуру Max-Heapify, в которой вместо рекурсивного вызова
использовалась бы итеративная конструкция (цикл).



## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.




## Запуск проекта

`git clone https://github.com/Andrey-Yushkov/Alhoritms.git`
`cd algoritm/lab5/`  
`python3 -m task6.src.task7` 

### Запуск теста:   
   
`git clone https://github.com/Andrey-Yushkov/Alhoritms.git`   
`cd algoritm/lab3/`  
`python -m task6.tests.TestTask7`
