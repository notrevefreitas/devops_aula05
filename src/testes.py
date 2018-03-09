Importjogovelha
importsys
erroInicializar= False
jogo = jogovelha.inicializar()
iflen(jogo) != 3:
erroInicializar= True
else:
for linha in jogo:
iflen(linha) != 3:
erroInicializar= True
else:
for elemento in linha:
ifelemento != '.':
erroInicializar= True
iferroInicializar:
sys.exit(1)
else:
sys.exit(0)