use bot;

CREATE TRIGGER after_insert_user
AFTER INSERT ON bot.mybot_usuario FOR EACH ROW
insert into bot.mybot_usuario_funcao(id_usuario_id,id_funcionalidade_id,permissao,status)
select distinct A.id,
				B.id,
                A.status_acesso,
                null status
                from
                bot.mybot_usuario A,
                bot.mybot_funcionalidades_bot B
				where
                A.id not in (select id_usuario_id from bot.mybot_usuario_funcao)
