import asyncio
from googletrans import Translator
from customtkinter import *
from PIL import Image


# Função para traduzir e atualizar o campo de destino
async def tradutor(texto: str):
    # Dicionário de idiomas
    idiomas = {
        'Auto': 'auto',
        'Inglês': 'en',
        'Espanhol': 'es',
        'Chinês': 'zh-cn',
        'Hindi': 'hi',
        'Árabe': 'ar',
        'Português': 'pt',
        'Bengali': 'bn',
        'Russo': 'ru',
        'Japonês': 'ja',
        'Alemão': 'de',
        'Francês': 'fr',
        'Coreano': 'ko',
        'Italiano': 'it',
        'Turco': 'tr',
        'Vietnamita': 'vi'
    }

    # Obter o idioma selecionado na ComboBox
    idioma_destino_selecionado = opcao_idioma_destino.get()
    codigo_idioma_destino = idiomas.get(idioma_destino_selecionado, 'pt')  # Padrão: 'pt'

    # Traduzir o texto
    async with Translator() as traduzir:
        resultado = await traduzir.translate(texto, dest=codigo_idioma_destino)
        input_idioma_destino.configure(state='normal')  # Habilitar o campo de destino
        input_idioma_destino.delete(0, 'end')  # Limpar o campo de destino
        input_idioma_destino.insert(0, resultado.text)  # Inserir o texto traduzido
        input_idioma_destino.configure(state='disabled')  # Desabilitar novamente o campo

    if opcao_idioma_destino.get() == 'Português' or opcao_idioma_destino.get() == 'Inglês':
        texto_para_voz(resultado.text)


def texto_para_voz(frase: str):
    if opcao_idioma_destino.get() == 'Português' or opcao_idioma_destino.get() == 'Inglês':

        import pyttsx3

        falar = pyttsx3.init('sapi5') 
        
        vozes = falar.getProperty('voices')
        if opcao_idioma_destino.get() == 'Português':
            idioma = 0
        else:
            idioma = 1

        falar.setProperty('voice', vozes[idioma].id)
        falar.say(frase)
        falar.runAndWait()


# iniciar customtk
janela = CTk()
janela.title('Gw Tradutor')
janela.iconbitmap('tradutor.ico')
janela.geometry('800x500')

# aparência
set_appearance_mode('dark')

# programa principal
imagem_tradutor = Image.open('tradutor_imagem.png')
titulo = CTkLabel(janela, text='Gw Tradutor', image=CTkImage(imagem_tradutor, size=(50, 50)), compound='bottom', font=('Segoe UI', 17))
titulo.place(relx=0.5, rely=0.1, anchor='center')

# primeira opção - Idioma de Origem
idioma_origem = CTkFrame(janela, fg_color='#00008B', border_color='#FFFFFF', border_width=2)
idioma_origem.place(relx=0.46, rely=0.4, anchor='e')

texto_idioma_origem = CTkLabel(idioma_origem, text='Idioma de Origem')
texto_idioma_origem.pack(anchor='s', expand=True, padx=30, pady=10)

# Aumentar o tamanho da largura da ComboBox
opcao_idioma_origem = CTkComboBox(
    idioma_origem,
    values=[
        'Auto', 'Inglês', 'Espanhol', 'Chinês', 'Hindi', 'Árabe', 
        'Português', 'Bengali', 'Russo', 'Japonês', 'Alemão', 
        'Francês', 'Coreano', 'Italiano', 'Turco', 'Vietnamita'
    ],
    fg_color='#FFFFFF',
    border_color='#1A1A1A',
    dropdown_fg_color='#FFFFFF',
    dropdown_text_color='#1A1A1A',
    state='readonly',
    text_color='#1A1A1A',
    width=200  # Aumentar a largura da ComboBox
)
opcao_idioma_origem.pack(anchor='s', expand=True, padx=30, pady=(15, 10))  # Ajustar espaçamento

# Aumentar o tamanho da largura da Entry
input_idioma_origem = CTkEntry(idioma_origem, placeholder_text='Digitar Texto', width=250)  # Aumentar a largura
input_idioma_origem.pack(padx=0.5, pady=10, anchor='n', expand=True)
input_idioma_origem.bind('<Return>', lambda event: asyncio.run(tradutor(input_idioma_origem.get())))

# segunda opção - Idioma de Destino
idioma_destino = CTkFrame(janela, fg_color='#00008B', border_color='#FFFFFF', border_width=2)
idioma_destino.place(relx=0.55, rely=0.4, anchor='w')

texto_idioma_destino = CTkLabel(idioma_destino, text='Idioma de Destino')
texto_idioma_destino.pack(anchor='s', expand=True, padx=30, pady=10)

# Aumentar o tamanho da largura da ComboBox
opcao_idioma_destino = CTkComboBox(
    idioma_destino,
    values=[
        'Inglês', 'Espanhol', 'Chinês', 'Hindi', 'Árabe', 
        'Português', 'Bengali', 'Russo', 'Japonês', 'Alemão', 
        'Francês', 'Coreano', 'Italiano', 'Turco', 'Vietnamita'
    ],
    fg_color='#FFFFFF',
    border_color='#1A1A1A',
    dropdown_fg_color='#FFFFFF',
    dropdown_text_color='#1A1A1A',
    state='readonly',
    text_color='#1A1A1A',
    width=200  # Aumentar a largura da ComboBox
)
opcao_idioma_destino.pack(anchor='s', expand=True, padx=30, pady=(15, 10))  # Ajustar espaçamento

# Aumentar o tamanho da largura da Entry
input_idioma_destino = CTkEntry(
    idioma_destino,
    placeholder_text='Tradução',
    width=250,  # Aumentar a largura
    state='disabled'  # Tornar o campo não editável
)
input_idioma_destino.pack(padx=0.5, pady=10, anchor='n', expand=True)

janela.mainloop()
