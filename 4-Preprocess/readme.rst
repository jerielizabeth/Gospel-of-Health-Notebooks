
<!-- .. date: 2018-10-01
.. title: 4. Preprocess
.. slug: readme-4 
-->

For the dissertation, I incorporated a number of techniques to preprocess the text for topic modeling. 

+ First, following the suggestion of David Mimno in a blog post from 2015, I identified and connected noun phrases in the documents, so as to better separate out some of the more complex language use patterns deployed by the denomination. [1]_
+ Second, rather than using a traditional stop word list, which would remove words frequently used in modern English publications, I used a technique more commonly deployed with the topic modeling software Gensim of filtering out both high and low frequency words from the full corpus dictionary. This had a duel benefit of address both high frequency but context specific words, such as "God," as well as providing an additional filter for the remaining OCR errors, which make up a sizeable percentage of the remaining OCR errors.
+ Finally, following a strategy for document categorization with messy OCR data, I filtered out documents with low token rates and those with high error rates for use in training the topic model. [2]_ Once trained, I then applied the model to the held out documents, so that they received a topic assignment. Because of their high error rates, or lack of content, such documents would not have contributed meaningful information to the model and would instead have created more noise in the model.

I used these techniques to improve the quality of final topic model, moving beyond the defaults of standard topic modeling tools. The documents were then processed into a single (large) text file where each line contained the necessary metadata and text from a single document. I fed this, in addition to the list of stopwords created from filtering out the high and low frequency words, into MALLET, as documented in the `next notebook <link://slug/readme-5>`_.

Notebook Files
==============

Identify Noun Phrases
---------------------

+ :doc:`Identify frequent noun phrases <generate-noun-phrases-list>`
+ :doc:`Save list of noun phrases to module <save-noun-phrases-to-module>`

Create Stopword List
--------------------

+ :doc:`Identify high and low frequency words as stop words <2018-02-createstopwordlist>`
+ :doc:`Create stopword list for use with MALLET <create_filterlist_for_mallet_preprocessing>`

Filter Docs and Create Corpus Text Files
----------------------------------------

+ :doc:`Create Zips of Corpus Configurations <2018-02-createzipsofcorpussubsets>`
+ :doc:`Preprocess Corpora for Mallet <preprocess_corpus_for_mallet>`

.. [1] Mimno, David. “Using Phrases in Mallet Topic Models.” (2015): http://www.mimno.org/articles/phrases/. It is important to note that, while useful, this work was limited by the quality of the data from OCR and the problem of misidentified columns prevalent in the data source. With cleaner textual data, this work would be even more reliable.
.. [2] Taghva, Kazem, Thomas Nartker, and Julie Borsack. “Information Access in the Presence of Ocr Errors.” *Proceedings of the 1st ACM workshop on Hardcopy document processing* (2004): 1--8.