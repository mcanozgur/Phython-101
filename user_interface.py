#graphical user interface

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0]
]

for list_m in picture:
    for each_number in list_m:
        if each_number == 0:
            print(' ', end='')             # boşluklu siyah yapsın diye. 
        elif each_number == 1:
            print('*', end='')             # her seferinde yeni bir line'a yazıyordu zaten. yine öyle oldu.
    print('')   #ilk listeyi bitirince aşağıya geçicek.