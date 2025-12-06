# for index , value in enumerate(['a' , 'b' , 'c']):
#     print(index , value)

# name = ["Ali", "Sara"]
# ages = [20,22]

# a = list(zip(name , ages))

# print(a)

# numbers = [1, 2, 3, 4, 5]

# def square(num):
#     return num * num

# result = map(square, numbers)
# print(list(result))



# -  Map() Function

# map() aik function hai jiska kaam hai Collection of Data (jaise list, tuple, set) ke har element par ek function apply karna — taake har element pe koi task perform ho jaye.

# numbers = [1, 2, 3, 4]
# 1. Element” ka matlab hota hai — list (ya koi collection) ke andar ka ek item jaise ka.
# is List me 4 elements hain


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for col in row:
        print(col , end=" ")
    print()


matrix = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []

for num in matrix:
    if num % 2 == 0:
        even_numbers.append(num)
    
print(even_numbers)
