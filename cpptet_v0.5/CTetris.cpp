#include "CTetris.h"



bool isvalue(int *a, int val,int size){ //1차 배열일경우 
    
    for (int i = 0; i < size; i++){
        if(a[i] == val){
            return true;
        }
            
    }

    return false;


}


Matrix*** CTetris::setOfCBlockObjects;

void CTetris::CdeleteTetris(){


    
    for(int i=0; i < Tetris::nBlockTypes; i++){
        for(int j=0; j <Tetris::nBlockDegrees;j++ ){
            delete setOfCBlockObjects[i][j];
        }
    }

    for(int i=0; i < Tetris::nBlockTypes; i++){
        delete [] setOfCBlockObjects[i];
    }
    delete[] setOfCBlockObjects;

    //delete tempCBlk;
    delete iCScreen;
    delete oCScreen;



}




void CTetris::deleteFullLines(){
    int **array1;
    array1 = this->oCScreen->get_array();
    int xx = this->oCScreen->get_dx();
    int yy = this->oCScreen->get_dy();
    int temp = this->iScreenDy-1;
        
    while(temp >= 0){
        if(!(isvalue(array1[temp],0,xx))){//not(0 in array[temp]):
            int i = temp;
            while(i > 0){
                array1[i] = array1[i-1];
                i -= 1;
            }
            //delete[] array1[0];
            array1[0] = new int[xx];

            
            for(int x=0; x < iScreenDw; x++){
                array1[0][x] = 1;
            }

            for(int x=0; x < this->iScreenDx; x++){
                array1[0][x+iScreenDw] = 0;
            }

            for(int x=0; x < iScreenDw; x++){
                array1[0][x+iScreenDw+this->iScreenDx] = 1;
            }

            continue;
        }


        else{
            temp -= 1;
        }
    }

    


}



void CTetris::init(int* setofblock[],int type, int degree){

    Tetris::init(setofblock,type,degree);

    setOfCBlockObjects = new Matrix**[nBlockTypes];
	for (int i = 0; i < nBlockTypes; i++)
		setOfCBlockObjects[i] = new Matrix* [nBlockDegrees];
	for (int i = 0; i < nBlockTypes; i++)
	{
		for (int j = 0; j < nBlockDegrees; j++)
		{
			setOfCBlockObjects[i][j] = new Matrix(setofblock[i*nBlockDegrees + j],sqrt(len(setofblock[i*nBlockDegrees])-1),sqrt(len(setofblock[i*nBlockDegrees])-1));
            setOfCBlockObjects[i][j]->mulc(i+1);
		}
	}


    



}

TetrisState CTetris::accept(char key){

    if (key >= '0' and key <= '6'){
        if (this->justStarted == false){
            deleteFullLines();
        }
        delete this->iCScreen;
        this->iCScreen = new Matrix(this->oCScreen);
    }

    this->oScreen = this->oCScreen->binary();
    delete this->oCScreen;

    
    this->state = this->Tetris::accept(key);

    this->currCBlk = CTetris::setOfCBlockObjects[idxBlockType][idxBlockDegree];
    this->tempCBlk = this->iCScreen->clip(this->top, this->left, this->top+this->currCBlk->get_dy(), this->left+this->currCBlk->get_dx());
    this->tempCBlk = this->tempCBlk->add(this->currCBlk);

    this->oCScreen = new Matrix(this->iCScreen);
    this->oCScreen->paste((this->tempCBlk), this->top, this->left);
    delete this->tempCBlk;

    return this->state;

}


