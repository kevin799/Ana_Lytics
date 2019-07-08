SELECT * FROM bot.mybot_usuario_funcao;

delete from bot.mybot_usuario_funcao where id_usuario_id=100030196033467
insert into bot.mybot_usuario_funcao(permissao,status,id_funcionalidade_id,id_usuario_id) 
values(1,1,1,100030196033467)

select UNIX_TIMESTAMP(now())