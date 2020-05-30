from gerenciador import Gerenciador
from vetorizador import CountVectorizer, TFIDFVectorizer

gerenciador = Gerenciador()
revisoes = gerenciador.revisoes
recomendacoes = gerenciador.recomendacoes

vetorizador1 = CountVectorizer(revisoes)
vetorizador2 = CountVectorizer(revisoes, (1,4))
vetorizador3 = TFIDFVectorizer(revisoes)
vetorizador4 = TFIDFVectorizer(revisoes, (1,4))

print(len(vetorizador1.vetorizador.vocabulary_))
print(len(vetorizador2.vetorizador.vocabulary_))
print(len(vetorizador3.vetorizador.vocabulary_))
print(len(vetorizador4.vetorizador.vocabulary_))

