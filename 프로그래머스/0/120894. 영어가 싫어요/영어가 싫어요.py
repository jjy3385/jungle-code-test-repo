def solution(numbers):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i,v in enumerate(num_list):
        numbers = numbers.replace(v,str(i))
    return int(numbers)