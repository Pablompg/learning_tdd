def fizzbuzz_method(i: int) -> str:
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)

for i in range(1, 16):
    print(fizzbuzz_method(i))



