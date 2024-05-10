# Titulo = Hashzap
# Botao de iniciar Chat
    # popup (janela na frente da tela)
    # Titulo: Bem vindo ao Hashzap 
    # Campo de texto - Escreva seu nome no chat 
    # Botao: Entrar no chat 
       # Sumir com o titulo Hashzap
       # Sumir com o botao "Iniciar Chat"
       # Fechar a janela (popup)
       # Carregar o chat 
           # As mensagens que ja foram enviadas (Chat) 
           # Campo: Digite sua mensagem 
           # Botao: Enviar 

# Todo sistema sendo construido com flet deve-se: 
# importar o flet
import flet as ft

# criar a funcao principal do seu aplicativo
def main(pagina):
    # criar todas as funcionalidades 
    
    # criar o elemento 
    titulo = ft.Text("Hashzap")
    
    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem]) 
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value}: entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    
    # adiciona o elemento na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
                                                                             
# rodar o seu aplicativo 
ft.app(main, view=ft.WEB_BROWSER)                              

