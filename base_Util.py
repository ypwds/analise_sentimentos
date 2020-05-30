from gerenciador import Gerenciador
from vetorizador import CountVectorizer, TFIDFVectorizer
from classificador import NaiveBayes, SVM
from util import analisar_sentimento

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

testar = True

while testar is True:
    texto = input("\n>>> ")

    if texto == "0":
        testar = False
    else:
        analisar_sentimento(classificador1, texto)
        analisar_sentimento(classificador2, texto)
        analisar_sentimento(classificador3, texto)
        analisar_sentimento(classificador4, texto)