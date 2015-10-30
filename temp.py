#coding:utf-8
import urllib.request

pg=urllib.request.urlopen('http://www.climatempo.com.br/previsao-do-tempo/cidade/313/niteroi-rj')

txt=pg.read().decode('utf8')

c=txt.find('°')

print (txt[c-2:c])
