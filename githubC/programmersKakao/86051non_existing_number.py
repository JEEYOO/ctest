def solution(numbers):
    answer = 0
    
    # print(len(numbers)) 完
    for number in range(10):
        # print(number) 完
        # print(numbers[number]) 完
        if not number in numbers:
            answer += number
            
    return answer


'''
for number in range(len(numbers)):
'''
