
from random import *
from matrix import *

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()



###
### initialize variables
###     
arrayBlk = [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]
arrayBoo = [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ] ]
arrayBjj = [ [ 0, 0, 0, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 1, 1, 0 ] ]
arrayBll = [ [ 0, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 1, 0 ] ]
arrayBss = [ [ 0, 0, 0, 0 ], [ 0, 0, 1, 1 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ] ]
arrayBtt = [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]
arrayBzz = [ [ 0, 0, 0, 0 ], [ 1, 1, 0, 0 ], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ] ]

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  

i = randint(1,7)


iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
if(i == 1):
    currBlk = Matrix(arrayBlk)
if(i == 2):
    currBlk = Matrix(arrayBoo)    
if(i == 3):
    currBlk = Matrix(arrayBjj)
if(i == 4):
    currBlk = Matrix(arrayBll)
if(i == 5):
    currBlk = Matrix(arrayBss)
if(i == 6):
    currBlk = Matrix(arrayBtt)
if(i == 7):
    currBlk = Matrix(arrayBzz)
    
    
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()


    
###
### execute the loop
###
while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        
        tru = currBlk.get_array()
        
        for x,y in zip(range(0,3),range(3,0,-1)):
            for i,j in zip(range(x,y),range(y,x,-1)):
                tmp = tru[i][y]
                tru[i][y] = tru[x][i]
                tru[x][i] = tru[j][x]
                tru[j][x] = tru[y][j]
                tru[y][j] = tmp
                #tmp = tru[x][i]
                #tru[x][i] = tru[i][y]
                #tru[i][y] = tru[y][j]
                #tru[y][j] = tru[j][x]
                #tru[j][x] = tmp
        
        
        currBlk = Matrix(tru)
        #print('Not implemented')
       # continue
    elif key == ' ': # drop the block     
        
       
        while top <= iScreenDy-5:
            top += 1;
        
        
            
            
            
            
        
        #newBlockNeeded = True

    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    
    if (not tempBlk.anyGreaterThan(1) and key == ' '):
        tru = currBlk.get_array()
        countx = 0
        county = 0
        for x,y in zip(tru[3],tru[2]):
            if(x == 1):
                countx += 1
            if(y == 1):
                county += 1
        if(countx == 0 and county != 0):
            top += 1
        elif(countx == 0 and county == 0):
            top += 2
            
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk     
    
    
    
    
    
    
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise

            tru = currBlk.get_array()
        
            for x,y in zip(range(0,3),range(3,0,-1)):
                for i,j in zip(range(x,y),range(y,x,-1)):
                    tmp = tru[x][i]
                    tru[x][i] = tru[i][y]
                    tru[i][y] = tru[y][j]
                    tru[y][j] = tru[j][x]
                    tru[j][x] = tmp
                
            currBlk = Matrix(tru)
                 

        elif key == ' ': # undo: move up
            
            while True: #do/ whiie 문으로 공백문자 입력시 중복처리 
            
                re = tempBlk.get_array()

                for x in range(3,-1,-1):   
                    count = 0
                    for y in re[x]:
                        if ( y > 1):
                            count += 1
                    if(count != 0):
                        top -= 1
                        break

                #print('count 값:')
                #print(count)
                
                tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
                tempBlk = tempBlk + currBlk
                
                
                if not tempBlk.anyGreaterThan(1):
                    break


            
            


        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        
        

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()
    
    
    
    if newBlockNeeded:
        print("need new block")
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        i = randint(1,7)
        if(i == 1):
            currBlk = Matrix(arrayBlk)
        if(i == 2):
            currBlk = Matrix(arrayBoo)    
        if(i == 3):
            currBlk = Matrix(arrayBjj)
        if(i == 4):
            currBlk = Matrix(arrayBll)
        if(i == 5):
            currBlk = Matrix(arrayBss)
        if(i == 6):
            currBlk = Matrix(arrayBtt)
        if(i == 7):
            currBlk = Matrix(arrayBzz)
    

            
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###


# In[ ]:




