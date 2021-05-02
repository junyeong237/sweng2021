#pragma once
#include "Matrix.h"
#include<math.h>


enum TetrisState { Running, NewBlock, Finished };

class Tetris {

    public:
        static void init(int* setofblock[],int type, int degree);
        Matrix* createArrayScreen();
        Tetris(){};
        Tetris(int y, int x){
            this->iScreenDy = y;
            this->iScreenDx = x;
            this->idxBlockDegree = 0;
            Matrix* arrayScreen = createArrayScreen();
            this->iScreen = new Matrix(arrayScreen);
            delete arrayScreen;
            this->oScreen = new Matrix(iScreen);
            this->justStarted = true;

        };
        virtual ~Tetris(){
            std::cout << "소멸자" <<std::endl;;
            deleteTetris();
        };

        TetrisState accept(char key);
        static int iScreenDw;
        //void deleteFullLines();
        void deleteTetris();
    protected:
        Matrix* oScreen;
        int iScreenDy;
        int iScreenDx;
        int idxBlockDegree;
        static int nBlockTypes;
        static int nBlockDegrees;
        //static Matrix* setOfBlockObjects[MAX_BLK_TYPES][MAX_BLK_DEGREES];
        static Matrix*** setOfBlockObjects;

        bool justStarted;
        Matrix* iScreen;
        int top;
        int left;
        Matrix* currBlk;
        Matrix* tempBlk;
        TetrisState state;
        int arrayScreenDx;
        int arrayScreenDy;
        int idxBlockType;

};

int len(int* arr);