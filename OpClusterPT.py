# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Libraries---------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------------

#Vector, Dictionaries and Graph
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


#Reading the list of aspects 
with open('aspectos_reli.txt') as f:
    aspectos = f.read().lower().splitlines()


#Set of functions
def busca_sinonimo(item_sinonimo):
    #Searching relatiosn into OntoPT graph = synonyms
    ontosim_busca = []
    g = rdflib.Graph()
   #Check if this file was unziped
    g.parse('OntoPT.rdf')
    for s,p,o in g:
        entrada = rdflib.term.Literal(item_sinonimo)
        if entrada == o:
            temp1 = s
            #Search and save the graph's match with the input item
            for s1,p1,o1 in g:
                if s1 == temp1:
                    if p1 == ref:
                        sinonimo = o1.value
                        ontosim_busca.append(sinonimo)

    return ontosim_busca

def busca_onto(onto_all):
    #Searching relatiosn into OntoPT graph = synonyms and hyperonym / hyponym and Meronyms / Holonyms and ResultadodaaçãoDe e ServeParaAccao
    onto_busca = []
    g_new = rdflib.Graph()
    g_new.parse('OntoPT.rdf')
    for s0,p0,o0 in g_new:
        entrada_new = rdflib.term.Literal(onto_all)
        if entrada_new == o0:
            temp10 = s0
            
            #synonyms
            for s10,p10,o10 in g_new:
                if s10 == temp10:
                    if p10 == ref:
                        sinonimo_new = o10.value
                        onto_busca.append(sinonimo_new)
                        
                    #Meronyms / Holonyms and hyperonym / hyponym and ResultadodaaçãoDe e ServeParaAccao
                    if (p10 in part) or (p10 in temP) or (p10 in resA) or p10 in serA: 
                        temp20 = o10                      
                        for s20,p20,o20 in g_new:
                            if (temp20 == s20) and (p20 == ref):
                                hierarquia = o20.value
                                onto_busca.append(hierarquia)

    return onto_busca

def busca_corp(item_corp):
    #Searching the itens into the files directory in XML that was processed and annotated by CORP
    bb = []
    aux0 = []
    item_corp_new = ''
    included_extenstions = []
    menU = 'Mencoes_Unicas'
    sn = 'sn'
    #I'ts necessary to set where are the files directory in XML that was processed and annotated by CORP
    relevant_path = 'corp_xml_reli'
    included_extenstions = ['xml']

    file_names = [fn for fn in os.listdir(relevant_path)
                if any(fn.endswith(ext) for ext in included_extenstions)]

    for fil in sorted(file_names):
        os.chdir(r'corp_xml_reli')
        fil2 = open(fil)
        corp = BeautifulSoup(fil2, 'xml')
                
        #Get the size of document clusters
        for item in corp:
            y = item.Cadeias.contents
            tam_lista = len(y)
            lista = range(tam_lista)

            #Get the number of groups from all directory files (XML)
            for j in lista:
                if item.Cadeias.contents[j].name is not None:
                            
                    #Checks if there ins't set of kind = "single mention" and "sn"
                    if item.Cadeias.contents[j].name != menU or item.Cadeias.contents[j].name != sn:
                        tam_lista1 = len(item.Cadeias.contents[j].contents)
                        lista2 = range(tam_lista1)
                                
                        
                        aux0[:] = []       
                        for jj in lista2:
                            if item.Cadeias.contents[j].contents[jj].name is not None:
                                aux0.append(item.Cadeias.contents[j].contents[jj].get('nucleo'))
                                        
                                item_corp_new = unicode(item_corp)
                                item_corp_new_new = unicodedata.normalize('NFKD', item_corp_new).encode('ascii','ignore')

                                for ixi in aux0[:]:
                                    if ixi is not None:
                                        ixi1 = unicodedata.normalize('NFKD', ixi).encode('ascii','ignore')

                                #Ensures unique mention chains will not be framed
                                if item.Cadeias.contents[j].name != menU:
                                    if item_corp_new_new == ixi1.lower(): 
                                        aux1 = item.Cadeias.contents[j].name
                                       
                                        #Find the set groups where the aspect is           
                                        for jj in lista2:
                                            if item.Cadeias.contents[j].contents[jj].name is not None:
                                                if item.Cadeias.contents[j].name == aux1:
                                                    temp01 = str(item.Cadeias.contents[j].contents[jj].get('nucleo'))
                                                    corref = temp01.lower()
                                                    bb.append(corref)
    return bb

def busca_deverbal(item_deverbal): 
    with open('deverbais1.txt') as d1:
        deverbais1 = d1.read().lower().splitlines()
    with open('deverbais2.txt') as d2:
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


def busca_estrangeirismo(item_estrangeiro):
    import string
    with open('estrangeirismo1.txt') as es1:
        estrangeirismo1 = es1.read().lower().splitlines()
    with open('estrangeirismo2.txt') as es2:
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


def busca_diminutivo_aumentativo(item_dimiaum):
    import string
    with open('diminutivo_aumentativo1.txt') as dimia1:
        diminuaumet1 = dimia1.read().lower().splitlines()
    with open('diminutivo_aumentativo2.txt') as dimia2:
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

def remove_repetidos(lista000):
    l = []
    for i1 in lista000:
        if i1 not in l:
            l.append(i1)
    l.sort()
    return l


def remove_valores_da_lista(the_list, val):
        while val in the_list:
            the_list.remove(val)

##Start--------------------------------------------------------------------------------------------------

for i in list(aspectos): 
    busca[:] = []
    busca_new[:] = []

    #ONTO-PT
    busca = busca_onto(i)

    #CORP
    test = busca_corp(i)
    for t111 in test[:]:
        busca.append(t111)

    #DEVERBAIS
    busca.append(busca_deverbal(i)) 

    #ESTRANGEIRISMO
    busca.append(busca_estrangeirismo(i))

    #DIMINUTIVOS & AUMENTATIVOS:
    busca.append(busca_diminutivo_aumentativo(i))

    #SUBSTRING
    for i2 in aspectos[:]:
        if (i in i2 and len(i) != len(i2)) or (i2 in i and len(i) != len(i2)):
            busca.append(i2)
        
    #Aspects not found in either base
    #busca.append(i)

    busca = remove_repetidos(busca)
    
    #Checks the intersection between search vector and aspect vector
    for jjj in busca[:]:
        for iii in aspectos[:]:
            if iii == jjj:
                grupo.append((i,iii))  
                remove_valores_da_lista(aspectos,iii)

                #Busca novamente os itens add no vetor "grupo" a partir do último aspecto adicionado
                #Porque se ele não pegar a última posição do vetor grupo, ele irá reclassficar os aspectos adicionado em "grupo"
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
                                    
                        #Remove the duplicates in "busca_new"
                        busca_new = remove_repetidos(busca_new) 

                        #Checks intersection between remnants and aspect vector
                        for bbb in busca_new[:]:
                            for aaa in aspectos[:]:
                                if aaa == bbb:
                                    grupo.append((i, aaa))
                                    remove_valores_da_lista(aspectos, aaa)
                                  
        
    #Retrieves the position of the last aspect added in the group vector.
    pos = grupo[-1]
    n_pos = grupo.index(pos)


    print(grupo)

