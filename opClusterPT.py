# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#---------------------------------------------------------------------------------------------------

#Bibliotecas----------------------------------------------------------------------------------------
import rdflib
import string
import os
import collections
import rdflib
import codecs
import unicodedata
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from rdflib import Graph, URIRef, Literal
#-----------------------------------------------------------------------------------------------------

#Declarações de vetor, dicionários e grafo------------------------------------------------------------
part = rdflib.term.URIRef('http://ontopt.dei.uc.pt/OntoPT.owl#parteDe')
temP = rdflib.term.URIRef('http://ontopt.dei.uc.pt/OntoPT.owl#temParte')
resA = rdflib.term.URIRef('http://ontopt.dei.uc.pt/OntoPT.owl#resultadoDaAccao')
serA = rdflib.term.URIRef('http://ontopt.dei.uc.pt/OntoPT.owl#serveParaAccao')
ref = rdflib.term.URIRef('http://ontopt.dei.uc.pt/OntoPT.owl#formaLexical')
hipe = rdflib.term.URIRef('http://ontopt.dei.uc.pt/OntoPT.owl#hiperonimoDe')
hipo = rdflib.term.URIRef('http://ontopt.dei.uc.pt/OntoPT.owl#hiponimoDe')
busca = []
busca_new = []
grupo = []
test = []
test2 = []
n_pos = 0
pos = ''
unitarios = []
#-----------------------------------------------------------------------------------------------------

#LÊ A LISTA DE ASPECTOS-------------------------------------------------------------------------------
with open('aspectos_reli.txt') as f:
    aspectos = f.read().lower().splitlines()
#------------------------------------------------------------------------------------------------------


#FUNÇÕES-----------------------------------------------------------------------------------------------
def busca_sinonimo(item_sinonimo):#--------------------------------------------------------------------
    #Relações do ONTO.pt que serão acessadas para busca do aspecto
    ontosim_busca = []
    g = rdflib.Graph()
    g.parse('/home/francielle/python/OntoPT.rdf')
    for s,p,o in g:
        entrada = rdflib.term.Literal(item_sinonimo)
        if entrada == o:
            temp1 = s
            #busca e guarda os sinônimos do aspecto
            for s1,p1,o1 in g:
                if s1 == temp1:
                    if p1 == ref:
                        sinonimo = o1.value
                        ontosim_busca.append(sinonimo)

    return ontosim_busca
#-----------------------------------------------------------------------------------------------------

def busca_onto(onto_all):#----------------------------------------------------------------------------
    #Relações do ONTO.pt que serão acessadas para busca do aspecto
    onto_busca = []
    g_new = rdflib.Graph()
    g_new.parse('/home/francielle/python/OntoPT.rdf')
    for s0,p0,o0 in g_new:
        entrada_new = rdflib.term.Literal(onto_all)
        if entrada_new == o0:
            temp10 = s0
            #busca e guarda os sinônimos do aspecto
            for s10,p10,o10 in g_new:
                if s10 == temp10:
                    if p10 == ref:
                        sinonimo_new = o10.value
                        onto_busca.append(sinonimo_new)
                        
                    #Merônimos/holônimos e Hiperônimo/Hipônimo e ResultadodaaçãoDe e ServeParaAccao
                    if (p10 in part) or (p10 in temP) or (p10 in resA) or p10 in serA: 
                        temp20 = o10                      
                        for s20,p20,o20 in g_new:
                            if (temp20 == s20) and (p20 == ref):
                                hierarquia = o20.value
                                onto_busca.append(hierarquia)

    return onto_busca
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

def busca_corp(item_corp):#------------------------------------------------------------------------------
    bb = []
    aux0 = []
    item_corp_new = ''
    included_extenstions = []
    menU = 'Mencoes_Unicas'
    sn = 'sn'
    #############PRECISA APONTAR ONDE ESTÁ OS ARQUIVOS (xml) PROCESSADOS PELO CORP AQUI!!!!###############
    relevant_path = '/home/francielle/python/corp/corp_xml_reli'
    included_extenstions = ['xml']

    #Tratamento para importar apenas arquivos não ocultos e não temporários
    file_names = [fn for fn in os.listdir(relevant_path)
                if any(fn.endswith(ext) for ext in included_extenstions)]

    for fil in sorted(file_names):
        os.chdir(r'/home/francielle/python/corp/corp_xml_reli')
        fil2 = open(fil)
        corp = BeautifulSoup(fil2, 'xml')
                
        #Pega o nÃºmero de clusters de cada arquivo, portanto o tamanho de clusters do documento
        for item in corp:
            y = item.Cadeias.contents
            tam_lista = len(y)
            lista = range(tam_lista)

            #Pego a quantidade de grupos de cadeias de todos os arquivos do diretÃ³rio
            for j in lista:
                if item.Cadeias.contents[j].name is not None:
                            
                    #Verifica se nenhuma cadeia Ã© "menÃ§Ã£o Ãºnica" e "sn" 
                    if item.Cadeias.contents[j].name != menU or item.Cadeias.contents[j].name != sn:
                        tam_lista1 = len(item.Cadeias.contents[j].contents)
                        lista2 = range(tam_lista1)
                                
                        #Limpa o vetor aux0

                        aux0[:] = []       
                        #Pega o nÃºcleo de todos as cadeias formadas pelo corp de todos os arquivos do diretÃ³rio
                        for jj in lista2:
                            if item.Cadeias.contents[j].contents[jj].name is not None:
                                aux0.append(item.Cadeias.contents[j].contents[jj].get('nucleo'))
                                        
                                item_corp_new = unicode(item_corp)
                                item_corp_new_new = unicodedata.normalize('NFKD', item_corp_new).encode('ascii','ignore')

                                for ixi in aux0[:]:
                                    if ixi is not None:
                                        ixi1 = unicodedata.normalize('NFKD', ixi).encode('ascii','ignore')

                                #Garante que cadeias de menções únicas não serão enquadradas
                                if item.Cadeias.contents[j].name != menU:
                                    if item_corp_new_new == ixi1.lower(): 
                                        aux1 = item.Cadeias.contents[j].name
                                       
                                        #Encontra os grupos de cadeias em que o aspecto está            
                                        for jj in lista2:
                                            if item.Cadeias.contents[j].contents[jj].name is not None:
                                                if item.Cadeias.contents[j].name == aux1:
                                                    temp01 = str(item.Cadeias.contents[j].contents[jj].get('nucleo'))
                                                    corref = temp01.lower()
                                                    bb.append(corref)
    return bb
#--------------------------------------------------------------------------------------------------------

#Busca o item na base do Iltec de deverbais--------------------------------------------------------------
def busca_deverbal(item_deverbal):
    #Cria o dicionário de deverbais
    with open('/home/francielle/python/deverbais1.txt') as d1:
        deverbais1 = d1.read().lower().splitlines()
    with open('/home/francielle/python/deverbais2.txt') as d2:
        deverbais2 = d2.read().lower().splitlines()
    dic1 = dict(zip(deverbais1, deverbais2))
    deb = collections.OrderedDict(sorted(dic1.items()))
    
    for chave, valor in sorted(deb.items()):
        if str(chave) == str(item_deverbal):
            deverbal = str(valor)
            return deverbal
        else:
            if valor == str(item_deverbal):
                deverbal = str(chave)
                return deverbal
#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------
def busca_estrangeirismo(item_estrangeiro):
    import string
    with open('/home/francielle/python/estrangeirismo1.txt') as es1:
        estrangeirismo1 = es1.read().lower().splitlines()
    with open('/home/francielle/python/estrangeirismo2.txt') as es2:
        estrangeirismo2 = es2.read().lower().splitlines()
    dic2 = dict(zip(estrangeirismo1, estrangeirismo2))
    est = collections.OrderedDict(sorted(dic2.items()))
    
    for chave1, valor1 in sorted(est.items()):
        if str(chave1) == str(item_estrangeiro):
            estrangeirismo = str(valor1)
            return estrangeirismo
        else:
            if valor1 == str(item_estrangeiro):
                estrangeirismo = str(chave1)
                return estrangeirismo
#-------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------
def busca_diminutivo_aumentativo(item_dimiaum):
    import string
    with open('/home/francielle/python/diminutivo&aumentativo1.txt') as dimia1:
        diminuaumet1 = dimia1.read().lower().splitlines()
    with open('/home/francielle/python/diminutivo&aumentativo2.txt') as dimia2:
        diminuaumet2 = dimia2.read().lower().splitlines()
    dic3 = dict(zip(diminuaumet1, diminuaumet2))
    dimutivo_aumentativo = collections.OrderedDict(sorted(dic3.items()))
    
    for chave2, valor2 in sorted(dimutivo_aumentativo.items()):
        if str(chave2) == str(item_dimiaum):
            diau = str(valor2)
            return diau
        else:
            if valor2 == str(item_dimiaum):
                diau = str(chave2)
                return diau
#-------------------------------------------------------------------------------------------------------

#Remove valores repetidos de uma lista------------------------------------------------------------------
def remove_repetidos(lista000):
    l = []
    for i1 in lista000:
        if i1 not in l:
            l.append(i1)
    l.sort()
    return l

#Remove valores de uma lista-----------------------------------------------------------------------------
def remove_valores_da_lista(the_list, val):
        while val in the_list:
            the_list.remove(val)

#Início--------------------------------------------------------------------------------------------------
#Percorrer a lista de aspecto ordenada de acordo com a maior frequência
#Utilizei a função 'reversed' porque há a necessidade de remover itens da lista estando iterando nela
#se não utilizarmos, misteriosamente ele 'pula' um item da lista
#---------------------------------------------------------------------------------------------------------
for i in list(aspectos): 
    #Limpa os valores das lista de "busca" e "busca_new" 
    busca[:] = []
    busca_new[:] = []

    #ONTO-pt: Sinônimos / parte-todo / resultado_da_ação
    busca = busca_onto(i)

    #CORP
    test = busca_corp(i)
    for t111 in test[:]:
        busca.append(t111)

    #DEVERBAIS-------------------------------------------------------------------------------------------
    busca.append(busca_deverbal(i)) 

    #ESTRANGEIRISMO: lista de alguns estrangeirismo-------------------------------------------------------
    busca.append(busca_estrangeirismo(i))

    #DIMINUTIVOS & AUMENTATIVOS: -------------------------------------------------------------------------
    busca.append(busca_diminutivo_aumentativo(i))

    #SUBSTRING--------------------------------------------------------------------------------------------
    for i2 in aspectos[:]:
        if (i in i2 and len(i) != len(i2)) or (i2 in i and len(i) != len(i2)):
            busca.append(i2)
        
    #Itens que não foram encontrados em nenhuma das bases
    #busca.append(i)

    #Remove repetidos-------------------------------------------------------------------------------------
    busca = remove_repetidos(busca)
    
    #Verifica a intersecção entre o vetor de busca e o vetor de aspectos----------------------------------
    for jjj in busca[:]:
        for iii in aspectos[:]:
            if iii == jjj:
                grupo.append((i,iii))  
                remove_valores_da_lista(aspectos,iii)

                #Busca novamente os itens add no vetor "grupo" a partir do último aspecto adicionado
                #Porque se ele não pegar a última posição do vetor grupo, ele irá reclassficar dos os aspectos adicionado em "grupo"

                for idd, (gr1, gr2) in enumerate(grupo):

                    #Aqui que ele pega a última posição do vetor, para que a reclassificação seja realizada sobre os aspectos de G(i) e não de G(full)
                    #Pega o último item adicionado no vetor "grupo"
                    if idd > n_pos: 
                        
                        #CORP
                        test2 = busca_corp(gr2)
                        for tt in test2[:]:
                            busca_new.append(tt)
                      
                        #DIMINUTIVOS & AUMENTATIVOS:
                        busca_new.append(busca_diminutivo_aumentativo(gr2))
         
                        #ESTRANGEIRISMO
                        busca_new.append(busca_estrangeirismo(gr2))        
                                    
                        #Remove repetidos de busca_new
                        busca_new = remove_repetidos(busca_new) 

                        #Verifica a intersecção entre os remanscentes e a lista de aspectos
                        for bbb in busca_new[:]:
                            for aaa in aspectos[:]:
                                if aaa == bbb:
                                    grupo.append((i, aaa))
                                    remove_valores_da_lista(aspectos, aaa)

    #------------------------------------------------------------------------------------------------                                     
        
    #Recupera a posição do último aspecto adicionado no vetor grupo
    pos = grupo[-1]
    n_pos = grupo.index(pos)


    print(grupo)

