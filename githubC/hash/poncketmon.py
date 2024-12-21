def solution2(nums):
    answer = 0
    newList = []
    # 중복제거
    for i in range(len(nums)):
        if nums[i] not in newList:
            newList.append(nums[i])
    # n/2 보다 크면 n/2 출력하고 작으면 nums 길이 출력
    if len(newList) > len(nums)/2:
        answer = len(nums)/2
    else: answer = len(newList)
    return answer


def solution(nums):
    answer = 0
    print(nums, type(nums))
    uniq = set(nums)       #
    print(uniq, type(uniq))
    
    if len(uniq) > len(nums)/2:
        answer = len(nums)/2
    else: answer = len(uniq)
    
    return answer
