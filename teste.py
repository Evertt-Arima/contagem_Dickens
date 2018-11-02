import collections


#arquivo = open('98-0.txt', encoding='utf-8')
#texto = arquivo.read()
#arquivo.close()

contador = {}

with open('98-0.txt', encoding='utf-8') as arquivo:
     # para ler linha a linha:
     for linha in arquivo:

         lista = linha.lower().split()

         for palavra in lista:

             palavra = palavra.replace(".", "")
             palavra = palavra.replace("\'", "")
             palavra = palavra.replace('\"', "")
             palavra = palavra.replace(",", "")
             palavra = palavra.replace(".", "")


             if palavra not in contador:
                 contador[palavra] = 1
             else:
                 contador[palavra] += 1

#for k, v in contador.items():
#    print(f'{k} : {v}')


d = collections.Counter(contador)

for palavra, contagem in d.most_common(10):
    print(palavra, " : ", contagem)





    # economizando memória lendo 'x' caracteres por vez:
    #tam_a_ler = 100 #definição da quantidade a ser lida

    #conteudo_arquivo = arquivo.read(tam_a_ler)

    #while len(conteudo_arquivo) > 0:
    #    print(conteudo_arquivo, end='')
    #    conteudo_arquivo = arquivo.read(tam_a_ler) #condição de parada do loop (retorna 0)
