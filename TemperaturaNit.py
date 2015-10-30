import urllib.request

#requisitando e abrindo a conexão
pg = urllib.request.urlopen("http://www.climatempo.com.br/previsao-do-tempo/cidade/313/niteroi-rj")

#Lendo o conteúdo
txt = pg.read().decode("utf8")

#inserindo intervalo na string
c=txt[22537:22539]

#Exibindo requisição
print("Temperatura atual Niterói: " + c + "º")
