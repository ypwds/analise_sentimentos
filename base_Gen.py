from gerenciador import Gerenciador

gerenciador = Gerenciador()
revisoes = gerenciador.revisoes
recomendacoes = gerenciador.recomendacoes

#criar o arquivo revicoes_processadas.pickle
#print(len(revisoes))
#print(len(recomendacoes))

#testar o arquivo revisoes_processadas.pickle
print(revisoes[0])
print(recomendacoes[0])