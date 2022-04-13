def distancing(places):
    answer = []
    rooms = len(places)
    
    print(places[0])
    print(places[0][0])
    test = places[0][0]
    print(test[0])
    
    for i in range(rooms):
        cmap = places[i] #['POOOP', 'OXXOX', 'OPXPX', 'OOXOX', 'POXXP']
        
        for row in range(5):
            for col in range(5):
                line = cmap[row]
                chars = line[col].split()
                print(chars)
    
    return answer



'''
print(places[0][0][0])
'''
