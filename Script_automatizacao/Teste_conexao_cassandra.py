from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('bot')
session.execute("insert into bot.teste2 (teste_id,description) values(now(),'insert agendado realizado com sucesso!!!');")
cluster.shutdown()


'''
Video para configurar crontab(agendador de tarefa)
https://www.youtube.com/watch?v=GGTbXq1FUI0

Execução de um script sh.
https://www.youtube.com/watch?v=6Uq3L9fj36Q

'''