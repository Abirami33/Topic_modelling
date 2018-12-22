# Topic_modelling
Topic modelling analysis and learning [ SEMANTIC ANALYSIS ]

**news_analysis_manual folder:**

(contains the code file,output screenshot,output graph)

*PROCESS DONE:*

1) Manually collected headlines from 3 top newspapers dated DEC 21
2) Manually mapped those headlines to it's respective domains
3) Orgnized the collected corpus in python dictionaries
4) Seperated as keys and values
5) keys are sentences and values are domains/fields
6) From that domains list,frequency count of domians is collected
7) plotted a pie chart so that we can came to know the Top domains in news


**news_analysis_LDA folder:**

(contains input paragraph from news,code file,output screenshot)

*PROCESS DONE:*

1) Taken a paragraph from the TIMES OF INDIA Dated Dec 22
2) Split those as seperate sentences and compiled
3) Then We have to clean the document
4) cleaning means stemming,lemmatisation,stop_words removal (explained in comments)
5) Then cleaned document is converted as a dictionary by genism's corpora
6) Then Document matrix is calculated from that dictionary
7) Possible document-topic density and topic-word density is the result
   * Document-topic density means possible topics in a document
   * Topic-word density means possible words in that topic
