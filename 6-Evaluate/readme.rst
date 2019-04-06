<!-- 
.. date: 2018-10-01
.. title: 6. Evaluate
.. slug: readme-6 
-->

Topic models are notoriously difficult to evaluate. At the time of writing, methods for evaluating the quality and stability of topic models in general, and especially for humanities use, are an ongoing research with few standardized processes. Some of the more commonly used methods include automatically computed measures of topic coherence and interpretability of topics, though coherence and interpretability often do not align as neatly as would be desired. [1]_ 

Using topic models in historical analysis, and with a eye to development of language over time also changes the evaluation criteria for topic models in ways that are not well documented. Topic models are more typically used to categorize documents and can be evaluated on how well they succeed in assigning documents according to known categories. Used in historical research, topic models are deployed to categorized large collections of unknown content which was produced over extended periods of time. This introduces two complications: the lack of known categories to evaluate the model against, and the introduction of language changes that complicate topic information. 

The development and testing of a model in the face of these complications could constitute its own project. As I undertook the modeling as part of a historical analysis project, where the model is not the object of study but in service of the larger cultural and methodological analysis, this project opens morre questions regarding the creation and evaluation of topic models in historical research, rather than it answers. 



Notebook Files
==============

Visualizations
--------------

+ :doc:`PyLDAviz visualization <pyldavis_and_mallet>`
+ :doc:`Dendrogram of Topics <2018-10-16-cluster-topics>`

Stability of Topic Words
------------------------

+ :doc:`Measure Variation in Topic Keys <measure-variation-in-topic-keys>`

Interpretation
--------------

I managed the topic labels I developed for the model browser in a Google doc. The following notebook is used to take that spreadsheet data and format it into json for the browser `info.json` file. Currently, the results must be manually copied and pasted from the notebook to the browser file.

To create these labels, I drew on the words of the topics as well as read the top documents in which the topic appeared. This provided contextual information for distinguishing between similar topics.

+ :doc:`Export Topic Labels <export-topic-labels>`

.. [1] Cite Hannah Wallach Tea Leaves, 