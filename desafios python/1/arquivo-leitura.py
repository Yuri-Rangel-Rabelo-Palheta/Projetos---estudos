#le um arquivo, cria se nao existir, insere dados no arquivo, retira dados do arquivo
#autor: Yuri Rangel Rabelo Palheta

import sys

arquivo = open("arq-test.txt" , "w") 
#cria o arquivo. r – leitura (padrão). w – gravação. a – adição. b – binário. 

arquivo.write("\nescreve uma linha")

arquivo.write("\n escreve uma segunda linha")

arquivo.close()



