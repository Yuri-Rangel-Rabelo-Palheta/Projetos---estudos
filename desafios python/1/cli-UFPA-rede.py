#script para cadastrar automaticamente usuários no servidor DHCP UFPA
# Autor: Yuri Rangel Rabelo Palheta
import paramiko

servidor = "10.209.24.249"
usuario = "root"
psswd = ""

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

psswd = input("Digite a senha para acessar o DHCP::")



ssh.connect(hostname = servidor , username = usuario , password = psswd) #conecta-se com o servidor ssh

stdin , stdout , stderro = ssh.exec_command("ifconfig") #aqui ele envia o comando para o servidor ssh

stdin.close() #evita errors

#lembrar que tem que alterar o arquivo para inserir na rede

for line in stdout.readlines():
    print(line.replace("\n","")) #print(line.split("\n"))


