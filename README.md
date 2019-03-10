# NamedEntityRecog
A mini project on Named Entity Recognition, that takes 4 inputs: first and last name, the location and organisation
and finds the various mentions of the entity in the web through a google search.

## Required Packages
* requests
* sys
* bs4
* nltk
* re
* word_tokenize
* pos_tag
* conlltags2tree
* tree2conlltags
* pprint

## Execute
* Before executing, uncomment the lines that download punkt, averaged_perceptron_tagger, maxent_ne_chunker, words.
* To run, type <code>python NER.py</code>

## How it works?
<p>
Each and every sentence is evaluated by tokenization and adding position tags to every word. The obtained array is converted into noun-phrase chunks with a regular expression. Our chunk pattern consists of one rule, that a noun phrase, NP, should be formed whenever the chunker finds an optional determiner, DT, followed by any number of adjectives, JJ, and then a noun, NN.
IOB tags are the standard way to represent chunk structures. After converting, we use nltk's ne_chunk() function to perform classification and addition of categories PERSON, ORGANISATION, LOCATION etc.
</p>
