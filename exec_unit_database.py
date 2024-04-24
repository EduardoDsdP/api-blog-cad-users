# processamento unitarios de pequenas execuções de codigo para teste.




import sqlite3

with sqlite3.connect('servicos.db') as conexao:

    sql = conexao.cursor()

    sql.execute('CREATE TABLE IF NOT EXISTS servico(nome TEXT, especificacao TEXT, membros INTEGER);')

  
    sql.execute('INSERT INTO servico(nome, especificacao, membros) VALUES ("Servico 1", "Coleta", 2)')

    nome = input('Digite o nome do serviço: ')
    especificacao = input('Digite a especificação: ')
    membros_da_espec = int(input('Digite a quantidade de membros da espec: '))

    sql.execute('INSERT INTO servico VALUES (?, ?, ?)', [nome, especificacao, membros_da_espec])

   
    conexao.commit()

    
    servs = sql.execute('SELECT * FROM servico')
    for servico in servs:
        print(servico)

















   










