
<!-- .. date: 2018-10-01
.. title: 5. Model
.. slug: readme-5 
-->

This Notebook documents the bash script I used to generate the topic models using MALLET from the command line. The script generates and records the random seed used in each execution of the software, so that the results can be reproduced. The process involves two steps run on the training data - a conversion of the corpus and the processing of the model. Additionally, the resulting model is used to classify the documents in the holdout data, which as noted in previous collection of notebooks, consists of documents with low word counts and high error rates. 

Due to memory issues with a corpus of this size, I ran this script on a remote server, using the `Digital Ocean <https://www.digitalocean.com/>`_ computing service. This greatly reduced the amount of time required to generate a model and removed the need to purchase larger dedicated hardware. By moving this work to the cloud, I was able to work with the larger sized corpus while still loading all of the corpus data into memory, rather than rely on a streaming solution such as that employed by the Python library Gensim. 

Notebook Files
==============

+ :doc:`Topic Model with MALLET <topic-modeling-with-mallet>`
