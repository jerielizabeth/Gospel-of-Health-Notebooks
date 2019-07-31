<!-- 
.. date: 2018-10-01
.. title: 2. Clean
.. slug: readme-2 
-->

While OCR provides an efficient way to generate text from the images of documents, the process is not fool-proof. Depending on the particulars of the original page, such as font size and layout, as well as the quality of the digitization, the text data generated through computational recognition can be prone to a number of errors. 

In order to evaluate the data from the SDA periodicals, I first created a list of words against which to evaluate the tokens in the text. This consisted of words from the SCOWL collection, place and people names from the SDA yearbooks, and the language of the King James Bible. To the base generic list, I added a collection of specialized words that occurred frequently within the denominational literature.

Using these words, I worked title by title through the periodical scans, addressing the frequently occurring errorrs. These included special characters, errors in words due to line endings, and tokens where the white space was not correctly identified, either through extra white space between letters of a lack of whitespace between words. The age and type face of the periodicals created unique error patterns for each title, which were easier to address when working with each title independently.

These notebooks enable the user to examine the corrections I made for each periodical title and to recreate them.


Notebook Files
==============

Create Base Wordlists
---------------------

+ :doc:`Create Base Word List <create_wordlist>`
+ :doc:`Create list of US Place names <create-list-of-us-place-names>`
+ :doc:`Create list from King James translation of Bible <create-scriptural-word-list>`
+ :doc:`Create list of people and places from SDA Yearbooks <create-sda-people-and-places-lists>`


Create SDA Vocabulary List
--------------------------

+ :doc:`Generate Report on OCR Errors per Title <inspect-frequent-spelling-errors-round4>`
+ :doc:`Top Errors per Title for SDA Vocabulary <report-on-spelling-inspection>`

Evaluate and Correct Corpus Titles
----------------------------------

+ :doc:`Example of OCR Correction <example_of_ocr_cleaning>`
+ :doc:`Advocate of Christian Education <adv-ocr-evaluation-and-correction>`
+ :doc:`American Sentinel <amsn-ocr-evaluation-and-correction>`
+ :doc:`Adventist Review Anniversary Issues <arai-ocr-evaluation-and-correction>`
+ :doc:`Christian Education <ce-ocr-evaluation-and-correction>`
+ :doc:`Columbia Union Visitor <cuv-ocr-evaluation-and-correction>`
+ :doc:`Christian Educator, The <edu-ocr-evaluation-and-correction>`
+ :doc:`GC Session Bulletins <gcb-ocr-evaluation-and-correction>`
+ :doc:`Gospel Herald, The <gh-ocr-evaluation-and-correction>`
+ :doc:`Gospel of Health, The <goh-ocr-evaluation-and-correction>`
+ :doc:`Gospel Sickle <gs-ocr-evaluation-and-correction>`
+ :doc:`Home Missionary, The <hm-ocr-evaluation-and-correction>`
+ :doc:`Health Reformer, The <hr-ocr-evaluation-and-correction>`
+ :doc:`Indiana Reporter <ir-ocr-evaluation-and-correction>`
+ :doc:`Life Boat, The <lb-ocr-evaluation-and-correction>`
+ :doc:`Life and Health <lh-ocr-evaluation-and-correction>`
+ :doc:`Liberty Magazine <libm-ocr-evaluation-and-correction>`
+ :doc:`Lake Union Herald <luh-ocr-evaluation-and-correction>`
+ :doc:`North Michigan News <nmn-ocr-evaluation-and-correction>`
+ :doc:`Pacific Health Journal and Temperance Advocate <phj-ocr-evaluation-and-correction>`
+ :doc:`Present Truth and Adventist Review, The <ptar-ocr-evaluation-and-correction>`
+ :doc:`Pacific Union Recorder <pur-ocr-evaluation-and-correction>`
+ :doc:`Review and Herald (1850-1889) <rh18501889-ocr-evaluation-and-correction>`
+ :doc:`Review and Herald (1890-1920) <rh18901920-ocr-evaluation-and-correction>`
+ :doc:`Sligonian <sligo-ocr-evaluation-and-correction>`
+ :doc:`Sentinel of Liberty, The <sol-ocr-evaluation-and-correction>`
+ :doc:`Signs of the Times <st-ocr-evaluation-and-correction>`
+ :doc:`Southern Tidings <suw-ocr-evaluation-and-correction>`
+ :doc:`Church Officers Gazette, The <tcog-ocr-evaluation-and-correction>`
+ :doc:`Missionary Magazine, The <tmm-ocr-evaluation-and-correction>`
+ :doc:`West Michigan Herald <whm-ocr-evaluation-and-correction>`
+ :doc:`Youth's Instructor, The <yi-ocr-evaluation-and-correction>`