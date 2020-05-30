from gerenciador import Gerenciador
from vetorizador import CountVectorizer, TFIDFVectorizer
from classificador import NaiveBayes, SVM

#Se o arquivo ainda não existe, usa código abaixo
'''
gerenciador = Gerenciador()
revisoes = gerenciador.revisoes
recomendacoes = gerenciador.recomendacoes

vetorizador1 = CountVectorizer(revisoes)
vetorizador2 = CountVectorizer(revisoes, (1,4))
vetorizador3 = TFIDFVectorizer(revisoes)
vetorizador4 = TFIDFVectorizer(revisoes, (1,4))

classificador1 = NaiveBayes("naive_bayes_1_1.pickle", vetorizador1, recomendacoes)
classificador2 = NaiveBayes("naive_bayes_1_4.pickle", vetorizador2, recomendacoes)
classificador3 = SVM("svm_1_1.pickle", vetorizador3, recomendacoes)
classificador4 = SVM("svm_1_4.pickle", vetorizador4, recomendacoes)
'''

#Se o Arquivo já existe, usa os códigos abaixo

classificador1 = NaiveBayes("naive_bayes_1_1.pickle")
classificador2 = NaiveBayes("naive_bayes_1_4.pickle")
classificador3 = SVM("svm_1_1.pickle")
classificador4 = SVM("svm_1_4.pickle")

#Avaliação dos classificadores

print(classificador1.marcador())
print(classificador2.marcador())
print(classificador3.marcador())
print(classificador4.marcador())
