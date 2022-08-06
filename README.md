![image](https://user-images.githubusercontent.com/19657817/183250300-0cd26336-b33e-4353-ba9d-31f6f36181da.png)


<h2 align="center"> OpCluster - Automatic extraction and clustering of fine-grained opinions. </h2>  

Fine-grained opinion extraction and clustering tool for opinion mining ans summarization. Opcluster-PT also allows the customization for other languages, being minimally necessary a lexical language resource as such as WordNet, deverbal, foreign, and superlative lexicons. OpCluster-PT is currently customized for the Portuguese language.

The Opcluster-PT is an algorithm for hierarchical clustering of implicit and explicit fine-grained opinions (also called aspects). This method provides the automatic organization of similar  implicit and explicit aspects (considering the context of use)  from web consumer reviews within a tree. For example, in the review passage “she considered the camera price very expensive”, the consumer employed the term “price” to evaluate an aspect of the camera; however, consumers might also use the terms “cost”, “value”, “investment”, etc. In addition, consumers may use implicit or explicit aspects to refer to the same aspect, e.g., the sentences “she got calls at the São Francisco river” and “working anywhere” have been employed in actual reviews to evaluate the (implicit) “signal” aspect of a smartphone. It is also interesting to notice that, in some domains, proper names may be employed to refer to the aspects. For instance, the proper names “Sony” and “Nikon” may be used to evaluate the “product brand” aspect of digital cameras.

HOW TO RUN THE ALGORITHM?

1. Get the download git file folder;
2. Open the file "OpClusterPT.py" (It's necessário any developement IDE and the Python (2 or 3)  installed);
3. Check if all the input files is in the same folder that the "OpClusterPT.py" file;
4. Unzip the folders: "OntoPT.tar.xz" and "corp_xml_reli.zip";
4. Run the algorithm.

-- It was available also a set of aspects and labeled reviews that have been used in this master's degree work. However, if you need to apply this algorithm on another data, you need: (1) Download the CORP system - desktop version - (available here: https://www.inf.pucrs.br/linatural/wordpress/recursos-e-ferramentas/) and run it on the new dataset reviews. It will generate a set of XML files with the labeled reviews. This files will be used as input in the OpCluster-PT. Will soon be availabe the Opcluster-PT 2.0 web version. 


-- Adicional information about aspect-based sentiment analysis for Portuguese, you can read this technical report: http://conteudo.icmc.usp.br/pessoas/taspardo/ or this full thesis http://www.teses.usp.br/teses/disponiveis/55/55134/tde-31072018-170236/en.php. Another resources for aspect-based sentiment analysis / opinion mining (Portuguese Language) have been developed and availabled here: https://sites.google.com/icmc.usp.br/opinando/ .


CITING

Vargas, F.A. and Pardo, T.A.S. (2018). Aspect clustering methods for sentiment analysis. In the Proceedings of the 13th International Conference on the Computational Processing of Portuguese (PROPOR) (LNAI 11122), pp. 365-374. September, 24-26. Canela-RS/Brazil. 

BIBTEX

@inproceedings{DBLP:conf/propor/VargasAndPardo18,
  author    = {Francielle A. Vargas and
               Thiago A. S. Pardo},
  title     = {Aspect Clustering Methods for Sentiment Analysis},
  booktitle = {Proceedings of the 13th International Conference on the Computational Processing of Portuguese, {PROPOR} },
  pages     = {365–374},
  year      = {2018},
  address   = {Canela, Brazil},
  crossref  = {DBLP:conf/propor/2018},
}


ACKNOWLEDGEMENT

The authors are grateful to CAPES, FAPESP and USP Research Office for supporting this work.
