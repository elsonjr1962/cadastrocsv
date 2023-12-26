print('Bem vindo a Ferramenta de Cadastro')

arquivo = open('cadastros.csv', 'a')

nome        = input('Digite o nome: ')
cadastro    = input('Digite o cadastro: ')
funcao      = input('Digite o funcao: ')

arquivo.write(nome+';'+cadastro+';'+funcao+'\n')
arquivo.close()


