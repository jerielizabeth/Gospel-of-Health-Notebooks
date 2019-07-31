<!-- 
.. date: 2018-10-01
.. title: 7. Analyze
.. slug: readme-7 
-->

To use the topic model to analyze the language of the denomination, I used the data from the statefile to focus on particular aspects of the model, building from the document level data to looking at patterns by year and topic. By aggregating the model data, I suggest general patterns in the discourse of the denomination over time, patterns that open additional areas of inqury and that provide a wide-angle view of the denomination's literature and history. Because of the probabilistic nature of topic modeling, however, these patterns require additional verification (as demonstrated in `Chapter 3 <link://slug/chapter-3>`_) and are suggestive rather than deterministic.  

Additionally, I used the topic model as a type of index to retrieve documents on particular topics of interest. This use of topic modeling in document recovery is inline with the original functions of the algorithm, and is one of the most useful functions of the algorithm for historical analysis. Documents identified by the model as relating to different topics can then be used in other modes of analysis, from other forms of text mining to traditional close reading, as part of historical analysis.

Notebook Files
==============

+ :doc:`Explore Top Topics by Year <2018-10-17-yearly-top-topics>`
+ :doc:`Explore Top Documents per Topic by Year <2018-10-18-top-docs-by-topic-year>`

Investigate Cycles
------------------

+ :doc:`Aggregated End-times Topics <aggregated-end-times-topics>`
+ :doc:`Explore Top Yearly Topic Categories <2019-01-17-yearly-top-labels>`

AntConc
-------

To compute keyness scores in AntConc, I used log-likelihood and p < 0.05 (+ Bonferroni) to compute "Keyness" and %DIFF to compute "Effect", ranking the results by "Keyness" value. As part of the study, I compared the documents from year being examined to the documents from the five years prior and subsequent.