from game import *
from matrix import *

##################################################
### ColorDecorator for Tetris Class
##################################################

class ColorDecorator(Game):
    

    def initCBlocks(self, setOfBlockObjects): # self.initCBlocks(game.setOfBlockObjects)

        self.setOfCBlockObjects = [[0]*self.game.nBlockDegrees for _ in range(self.game.nBlockTypes)]
                                                                         
        for i in range(self.game.nBlockTypes):
            for j in range(self.game.nBlockDegrees):
                obj = Matrix(setOfBlockObjects[i][j])
                obj.mulc(i+1)
                self.setOfCBlockObjects[i][j] = obj
        return


    def __init__(self, game): #ColorDecorator(Tetris(20, 15))
        self.game = game
        self.initCBlocks(game.setOfBlockObjects)
        arrayScreen = game.createArrayScreen()
        self.iCScreen = Matrix(arrayScreen)
        self.oCScreen = Matrix(self.iCScreen)
        return

    def accept(self, key):
        if key >= '0' and key <= '6':
            if self.game.justStarted == False:
                self.deleteFullLines()
            self.iCScreen = Matrix(self.oCScreen)
            
        state = self.game.accept(key)
        self.CurrCBlk = self.setOfCBlockObjects[self.game.idxBlockType][self.game.idxBlockDegree]

        self.tempCBlk = self.iCScreen.clip(self.game.top, self.game.left, self.game.top+self.CurrCBlk.get_dy(), self.game.left+self.CurrCBlk.get_dx())
        self.tempCBlk = self.tempCBlk + self.CurrCBlk
        
        self.oCScreen = Matrix(self.iCScreen)
        self.oCScreen.paste(self.tempCBlk,self.game.top,self.game.left)
                
                

        return state

    def getScreen(self):
        return self.oCScreen
    
    
    

    def deleteFullLines(self):
        nCScanned = self.game.deleteFullLines()
        nCDeleted = 0

        zeroc = Matrix([[ 0 for x in range(0, (self.game.iScreenDx - 2*self.game.iScreenDw))]])
        for y in range(nCScanned - 1, -1, -1):

            cy = self.game.top + y + nCDeleted

            linec = self.oCScreen.binary().clip(cy, 0, cy+1, self.game.oScreen.get_dx())
            if linec.sum() == self.oCScreen.binary().get_dx():

                tempc = self.oCScreen.clip(0, 0, cy, self.oCScreen.get_dx())
                self.oCScreen.paste(tempc, 1, 0)
                self.oCScreen.paste(zeroc, 0, self.game.iScreenDw)
                nCDeleted += 1
                self.game.oScreen = self.oCScreen.binary()


        return
