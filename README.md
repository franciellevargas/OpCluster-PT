![SSC-logo-300x171](https://user-images.githubusercontent.com/19657817/63529693-77e6b100-c4db-11e9-9385-7d9b109427a2.png) ![Screenshot from 2019-08-22 12-36-57](https://user-images.githubusercontent.com/19657817/63529275-ccd5f780-c4da-11e9-9d2c-dce592d855e7.png) 

<h2># Opcluster-PT <h2>
 An automatic opinion implicit and explicit aspect clustering tool (in Python) for aspect-based opinion mining / sentiment analysis applications. 

The Opcluster-PT is an algorithm for clustering of implicit and explicit aspects. In this method, our particular interest lies on clustering of implicit and explicit similar aspects in consumer reviews. For example, in the review passage “she considered the camera price very expensive”, the consumer employed the term “price” to evaluate an aspect of the camera; however, consumers might also use the terms “cost”, “value”, “investment”, etc. In addition, consumers may use implicit or explicit aspects to refer to the same aspect, e.g., the sentences “she got calls at the S˜ao Francisco river” and “working anywhere” have been employed in actual reviews to evaluate the (implicit) “signal” aspect of a smartphone. It is also interesting to notice that, in some domains, proper names may be employed to refer to the aspects. For instance, the proper names “Sony” and “Nikon” may be used to evaluate the “product brand” aspect of digital cameras.

HOW TO RUN THE ALGORITHM?

1. Get the download git file folder;
2. Open the file "OpClusterPT.py" (It's necessário some developement IDE and the Python (2 or 3)  installed);
3. Check if all the input files is in the same folder that the "OpClusterPT.py" file;
4. Unzip the folders: "OntoPT.tar.xz" and "corp_xml_reli.zip";
4. Run the algorithm.

Ops. Was available a set of aspects and reviews that was been used in this master's degree work. However, if you need to apply this algorithm on another data, you need: 1. Download the CORP system - desktop version - (available here: https://www.inf.pucrs.br/linatural/wordpress/recursos-e-ferramentas/) and run it on the new dataset reviews. It will generate a set of XML files with the annotaed reviews. This files will be used as input in the OpCluster-PT; 2. Extract of aspects this reviews (with implicit and explicit aspects) that you wish to cluster. For this second task, you can use this system available here: https://github.com/raulnhl8/Extracao-e-qualificacao-de-aspectos-de-opiniao-para-o-portugues.


HOW CAN I CITE THIS ALGORITHM?

Vargas, F.A. and Pardo, T.A.S. (2018). Aspect clustering methods for sentiment analysis. In the Proceedings of the 13th International Conference on the Computational Processing of Portuguese (PROPOR) (LNAI 11122), pp. 365-374. September, 24-26. Canela-RS/Brazil. 



