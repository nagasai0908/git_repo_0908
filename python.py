def fibonacci(count: int) -> list[int]:
	numbers = []
	first, second = 0, 1

	for _ in range(count):
		numbers.append(first)
		first, second = second, first + second

	return numbers


def factorial(number: int) -> int:
	if number < 0:
		raise ValueError("Factorial is not defined for negative numbers")

	result = 1
	for value in range(2, number + 1):
		result *= value

	return result


print(fibonacci(10))
print(factorial(5))

