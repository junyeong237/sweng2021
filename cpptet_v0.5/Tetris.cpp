#include "Tetris.h"
#include <math.h>



int Tetris::nBlockTypes;
int Tetris::nBlockDegrees;

Matrix*** Tetris::setOfBlockObjects;
int Tetris::iScreenDw;


int len(int* arr) {

    int k = 0;
    while(1){
        if(arr[k] == -1){
            break;
        }
        k++;
    }
    if(k == 0)
        return k;
    else
        return k+1;

}





void Tetris::deleteTetris(){

    for(int i=0; i < Tetris::nBlockTypes; i++){
        for(int j=0; j <Tetris::nBlockDegrees;j++ )

            delete setOfBlockObjects[i][j];
    }

    for(int i=0; i < nBlockTypes; i++){
        delete [] setOfBlockObjects[i];
    }
    delete[] setOfBlockObjects;



    delete oScreen;
    delete iScreen;
    delete tempBlk;




}

void Tetris::init(int* setofblock[],int type, int degree)
{
    Tetris::nBlockTypes = type;
    Tetris::nBlockDegrees = degree;
    int array_maxsize = 0;


    for(int i=0; i < nBlockTypes; i++){
        if( array_maxsize <= sqrt(len(setofblock[i*nBlockDegrees])-1)){//수정
            array_maxsize = sqrt(len(setofblock[i*nBlockDegrees])-1);
        }
    }
    Tetris::iScreenDw = array_maxsize;

   	setOfBlockObjects = new Matrix**[nBlockTypes];
	for (int i = 0; i < nBlockTypes; i++)
		setOfBlockObjects[i] = new Matrix* [nBlockDegrees];
	for (int i = 0; i < nBlockTypes; i++)
	{
		for (int j = 0; j < nBlockDegrees; j++)
		{
			setOfBlockObjects[i][j] = new Matrix(setofblock[i*nBlockDegrees + j],sqrt(len(setofblock[i*nBlockDegrees])-1),sqrt(len(setofblock[i*nBlockDegrees])-1));
		}
	}





   
}


Matrix* Tetris::createArrayScreen(){

    this->arrayScreenDx = iScreenDw*2 + this->iScreenDx;
    this->arrayScreenDy = iScreenDw + this->iScreenDy;


   
    Matrix* selfarrayscreen = new Matrix(this->arrayScreenDy,this->arrayScreenDx);
    

    for(int y=0; y < this->arrayScreenDy; y++){
        for(int x=0; x < iScreenDw; x++){
            selfarrayscreen->get_array()[y][x] = 1;

        }

        for(int x=0; x < this->iScreenDx; x++ ){
            selfarrayscreen->get_array()[y][x+iScreenDw] = 0;
        }

        for(int x=0; x < iScreenDw; x++){
            selfarrayscreen->get_array()[y][iScreenDw + this->iScreenDx + x] = 1;

        }
    }

    for (int y=0; y < iScreenDw; y++){
        for (int x=0; x < this->arrayScreenDx; x++){
            selfarrayscreen->get_array()[this->iScreenDy + y][x] = 1;
        }
    }


    return selfarrayscreen;

}






TetrisState Tetris::accept(char key){

    this->state = Running;

    if (key >= '0' and key <= '6'){
        if (this->justStarted == false){
            //deleteFullLines();
        }
        delete this->iScreen;
        this->iScreen = new Matrix(this->oScreen);
        delete this->oScreen;
        this->idxBlockType = int(key-'0');
        this->idxBlockDegree = 0;
        this->currBlk = setOfBlockObjects[idxBlockType][idxBlockDegree];
        this->top = 0;
        this->left = iScreenDw + this->iScreenDx/2 - this->currBlk->get_dx()/2;
        this->tempBlk = this->iScreen->clip(this->top, this->left, this->top+this->currBlk->get_dy(), this->left+this->currBlk->get_dx());
        this->tempBlk = this->tempBlk->add(this->currBlk);
        this->justStarted = false;
        std::cout << std::endl;
    
        if (this->tempBlk->anyGreaterThan(1)){
            this->state = Finished;
        }
        this->oScreen = new Matrix(this->iScreen);
        this->oScreen->paste((this->tempBlk), this->top, this->left);

        return this->state;
    }
    else if (key == 'q'){

    }
    else if(key == 'a'){
        this->left -= 1;
    }
    else if (key == 'd'){
        this->left += 1;
    }
    else if (key == 's'){
        this->top += 1;
    }
    else if (key == 'w'){
        this->idxBlockDegree = (this->idxBlockDegree + 1) % Tetris::nBlockDegrees;
        this->currBlk = Tetris::setOfBlockObjects[this->idxBlockType][this->idxBlockDegree];
    }
    else if (key == ' '){
        while (!(this->tempBlk->anyGreaterThan(1))){
                this->top += 1;
                delete this->tempBlk;  
                this->tempBlk = this->iScreen->clip(this->top, this->left, this->top+this->currBlk->get_dy(), this->left+this->currBlk->get_dx());
                this->tempBlk = this->tempBlk->add(this->currBlk);
        }
    }
    else{
        std::cout << "wrong key" << std::endl;
    }

    delete this->tempBlk;        
    this->tempBlk = this->iScreen->clip(this->top, this->left, this->top+this->currBlk->get_dy(), this->left+this->currBlk->get_dx());
    this->tempBlk = this->tempBlk->add(this->currBlk);

    if (this->tempBlk->anyGreaterThan(1)) {
        if (key == 'a'){
            this->left += 1;
        }
        else if(key == 'd'){
            this->left -= 1;
        }
        else if(key == 's'){
            this->top -= 1;
            this->state = NewBlock;
        }
        else if(key == 'w'){
            this->idxBlockDegree = (this->idxBlockDegree - 1) % Tetris::nBlockDegrees;
            this->currBlk = Tetris::setOfBlockObjects[this->idxBlockType][this->idxBlockDegree];
        }
        else if(key == ' '){
            this->top -= 1;
            this->state = NewBlock;
        }
        delete this->tempBlk;      
        this->tempBlk = this->iScreen->clip(this->top, this->left, this->top+this->currBlk->get_dy(), this->left+this->currBlk->get_dx());
        this->tempBlk = this->tempBlk->add(this->currBlk);
    }

    this->oScreen = new Matrix(this->iScreen);
    this->oScreen->paste(this->tempBlk, this->top, this->left);

    return this->state;


}
