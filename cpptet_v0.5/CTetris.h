#pragma once
#include "Tetris.h"


class CTetris : public Tetris {

    private:
        static Matrix*** setOfCBlockObjects;
        Matrix* iCScreen;
        Matrix* currCBlk;
        Matrix* tempCBlk;

    public:
        void deleteFullLines();
        static void init(int* setofblock[],int type, int degree);
        TetrisState accept(char key);
        void CdeleteTetris();
        Matrix* oCScreen;
        CTetris(){};

        CTetris(int y, int x) : Tetris(y,x) {

            Matrix* arrayScreen = createArrayScreen();
            this->iCScreen = new Matrix(arrayScreen);
            delete arrayScreen;
            this->oCScreen = new Matrix(iCScreen);

        }
        ~CTetris(){
            CdeleteTetris();
        }

};



