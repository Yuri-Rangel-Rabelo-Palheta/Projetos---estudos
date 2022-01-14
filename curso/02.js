function validaTriangulo (a,b,c){

    this.a = a
    this.b = b
    this.c = c

    if(((Math.abs(this.b - this.c)) < (this.a) <(this.b + this.c))||((Math.abs(this.a - this.c)) < (this.b) <(this.a + this.c))||((Math.abs(this.b - this.a)) < (this.c) <(this.b + this.a))){

        console.log("forma um triangulo")
        return true


    }
    else{

        return false

    }
        

}

function classificaTriangulo(a,b,c){

    this.a = a
    this.b = b
    this.c = c

    if(validaTriangulo(this.a,this.b,this.c)){
        if(this.a == this.b){


            if(this.b == this.c){
    
                return "triangulo equilatero"
    
            }
            else{
    
                return "triangulo isoceles"
    
            }
    
        }
        else{
    
            if(this.b == this.c){
    
                return "triangulo isoceles"
    
            }
            else{
    
                return "triangulo escaleno"
    
            }
    
        }
    }
    else{

        return "não forma triangulo"

    }


}


aV = 75//InputEvent("digite o vertice a: ")//3
bV = 3//InputEvent("digite o vertice b: ")
cV = 3//InputEvent("digite o vertice c: ")


console.log("tipo de triangulo: ",classificaTriangulo(aV,bV,cV))
