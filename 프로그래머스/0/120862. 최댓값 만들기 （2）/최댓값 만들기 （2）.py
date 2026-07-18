def solution(numbers):
    numbers.sort()
    idx = len(numbers) - 1
    max1 = numbers[0] * numbers[1]
    max2 = numbers[idx] * numbers[idx - 1]
    return max1 if max1 > max2 else max2