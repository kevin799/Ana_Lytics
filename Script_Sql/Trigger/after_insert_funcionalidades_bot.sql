
use bot;

CREATE TRIGGER after_insert_funcionalidades_bot
AFTER INSERT ON bot.mybot_funcionalidades_bot FOR EACH ROW
insert into bot.mybot_usuario_funcao(id_usuario_id,id_funcionalidade_id,permissao,status) 
select distinct A.id,
				B.id,
                A.status_acesso,
                0 status 
                from 
                bot.mybot_usuario A,
                bot.mybot_funcionalidades_bot B
				where 
                B.id not in (select id_funcionalidade_id from bot.mybot_usuario_funcao)
