seats = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
         [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],\
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],\
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],\
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],\
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 1]]


for i in range(len(seats)) :
    for j in range(len(seats[i])) :
        if seats[i][j] == 0 :
            print('%3s' % '□', end='')
        else :
            print('%3s' % '■', end='')
    print()
    
print('\n※ 예약 가능 : ■, 예약 불가 : □')    