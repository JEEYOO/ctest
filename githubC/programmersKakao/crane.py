def crane(board, moves):
    bucket = []
    answer = []
    for move in moves:
        for i in range(len(board)):
    
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]
                    bucket = bucket[:-2]
                break
    return len(answer)*2            
                    
"""       
    i = 1
    while i < len(bucket):
        if bucket[i-1] == bucket[i]:
            answer.append(bucket[i])
            bucket.remove(bucket[i])
            bucket.remove(bucket[i-1])
            i = 1
        else:
            i += 1
            
    return len(answer)*2
    
    answer = 0
    return answer
"""
