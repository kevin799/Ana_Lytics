use bot;

CREATE TRIGGER after_update_ensino_dialogo
AFTER UPDATE ON bot.mybot_ensino_dialogo FOR EACH ROW
insert into bot.mybot_conversa_ml(conversa,resposta)
				values(new.pergunta,new.resposta)


		
