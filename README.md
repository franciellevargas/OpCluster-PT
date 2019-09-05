![SSC-logo-300x171](https://user-images.githubusercontent.com/19657817/63529693-77e6b100-c4db-11e9-9385-7d9b109427a2.png) ![Screenshot from 2019-08-22 12-36-57](https://user-images.githubusercontent.com/19657817/63529275-ccd5f780-c4da-11e9-9d2c-dce592d855e7.png) 

# Opcluster-PT
 An automatic opinion implicit and explicit aspect clustering tool (in Python) for aspect-based opinion mining / sentiment analysis applications. 

The Opcluster-PT is an algorithm for clustering of implicit and explicit aspects. In this method, our particular interest lies on clustering of implicit and explicit similar aspects in consumer reviews. For example, in the review passage “she considered the camera price very expensive”, the consumer employed the term “price” to evaluate an aspect of the camera; however, consumers might also use the terms “cost”, “value”, “investiment”, etc. In addition, consumers may use implicit or explicit aspects to refer to the same aspect, e.g., the sentences “she got calls at the São Francisco river” and “working anywhere” have been employed in actual reviews to evaluate the (implicit) “signal” aspect of a smartphone. It is also interesting to notice that, in some domains, proper names may be employed to refer to the aspects. For instance, the proper names “Sony” and “Nikon” may be used to evaluate the “product brand” aspect of digital cameras.

HOW TO RUN THE ALGORITHM?

1. Get the download git file folder;
2. Open the file "OpClusterPT.py" (It's necessário any developement IDE and the Python (2 or 3)  installed);
3. Check if all the input files is in the same folder that the "OpClusterPT.py" file;
4. Unzip the folders: "OntoPT.tar.xz" and "corp_xml_reli.zip";
4. Run the algorithm.

Ops. Was available also a set of aspects and labeled reviews that have been used in this master's degree work. However, if you need to apply this algorithm on another data, you need: 1. Download the CORP system - desktop version - (available here: https://www.inf.pucrs.br/linatural/wordpress/recursos-e-ferramentas/) and run it on the new dataset reviews. It will generate a set of XML files with the labeled reviews. This files will be used as input in the OpCluster-PT; 2. Extraction of aspects this reviews (with implicit and explicit aspects) that you wish to cluster. For this second task, you can use this system available here: https://github.com/raulnhl8/Extracao-e-qualificacao-de-aspectos-de-opiniao-para-o-portugues. With the OpCluster-PT you can extract the opinion too. So, To extract the opinion aspects you need first to undestand a litlle bit concepts of aspect-based opinion mining / sentiment analysis applications. If you domain is the products or book domain, you can use to extract the opinion aspects this aspects hierarchy in (OWL format) available here: http://conteudo.icmc.usp.br/pessoas/taspardo/sucinto/files/Ontologies-for-aspect-based-opinion-mining-master.zip. For to undestand a litlle bit more about aspect-based sentiment analysis for Portuguese, you can read this technical report: http://conteudo.icmc.usp.br/pessoas/taspardo/ or this full thesis http://www.teses.usp.br/teses/disponiveis/55/55134/tde-31072018-170236/en.php. Another resources for aspect-based sentiment analysis / opinion mining (Portuguese language) have been developed and availabled here: https://sites.google.com/icmc.usp.br/opinando/ .

CITING

Vargas, F.A. and Pardo, T.A.S. (2018). Aspect clustering methods for sentiment analysis. In the Proceedings of the 13th International Conference on the Computational Processing of Portuguese (PROPOR) (LNAI 11122), pp. 365-374. September, 24-26. Canela-RS/Brazil. 

BIBTEX

@inproceedings{DBLP:conf/propor/MonteiroSPARV18,
  author    = {Rafael A. Monteiro and
               Roney L. S. Santos and
               Thiago A. S. Pardo and
               Tiago A. de Almeida and
               Evandro E. S. Ruiz and
               Oto A. Vale},
  title     = {Aspect Clustering Methods for Sentiment Analysis},
  booktitle = {Proceedings of the 13th International Conference, {PROPOR} 2018, Canela, Brazil, September 24-26, 2018,
               Proceedings},
  pages     = {365–374},
  year      = {2018},
  crossref  = {DBLP:conf/propor/2018},
}


ACKNOWLEGMENT

Evandro Brasil Fonseca, author and developer of the CORP (resolução automática de correferências para o Português).




