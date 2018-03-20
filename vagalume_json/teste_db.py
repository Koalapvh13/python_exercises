

nomep = str(input('Digite qual seu nome: '))
print(nomep)
user = str(input('Digite qual seu nome: '))
print(user)
senha = str(input('Digite qual seu nome: '))
print(senha)

arquivo = open('letras.txt', 'w')
arquivo.write(nomep)
arquivo.write(user)
arquivo.write(senha)
arquivo.close()
