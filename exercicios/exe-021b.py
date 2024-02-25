#Faça um progrma em Pyhron que abra e reproduza o áudio de um arquivo mp3. 

import pygame

def reproduzir_audio(arquivo_mp3):
    # Inicializar o módulo mixer da pygame
    pygame.mixer.init()

    # Carregar o arquivo MP3
    pygame.mixer.music.load(arquivo_mp3)

    # Reproduzir o arquivo MP3
    pygame.mixer.music.play()

    # Aguardar o término da reprodução
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Parar a reprodução
    pygame.mixer.music.stop()

if __name__ == "__main__":
    # Substitua "caminho/do/arquivo.mp3" pelo caminho do seu arquivo MP3
    arquivo_mp3 = "c:/Users/raiss/OneDrive/Documentos/studypy/exercicios/exe-021.mp3"
    
    try:
        reproduzir_audio(arquivo_mp3)
    except pygame.error as e:
        print(f"Erro ao reproduzir o áudio: {e}")
