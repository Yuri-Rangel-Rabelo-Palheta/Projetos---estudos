#escreve em um arquivo
#autor: Yuri Rangel Rabelo Palheta

arquivo = open("arq-test.txt", "r") # Abra o arquivo (leitura)
conteudo = arquivo.readlines()
conteudo.append("\nNova linha")   # insira seu conteúdo

arquivo = open("arq-test.txt", "w") # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()