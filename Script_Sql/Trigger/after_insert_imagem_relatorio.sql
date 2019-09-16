use bot;

CREATE TRIGGER after_insert_imagem_relatorio
AFTER INSERT ON bot.mybot_imagem_relatorio FOR EACH ROW
insert into bot.mybot_confirmacao_relatorio(usuario_id,flag_confirmacao,imagem_id)
select 	usuario.id as id_usuario,
		0 flag_confirmacao,
        relatorio.id as id_relatorio
		from 
        bot.mybot_usuario usuario,
        (select id from bot.mybot_imagem_relatorio where id not in (SELECT imagem_id FROM bot.mybot_confirmacao_relatorio))relatorio
        
        where 
        role_id = (select id from bot.mybot_role where role = 'ADMIN')
        and
        area_id = (select id from bot.mybot_area where setor = 'ANALYTICS');
