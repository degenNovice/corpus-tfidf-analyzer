
# Corpus TF-IDF Analyzer

**TF-IDF** (Term Frequency-Inverse Document Frequency) is a model for text analysis. The goal is to apply natural language processing (NLP) techniques such as **stopword removal**, **lemmatization**, and generate a **TF-IDF matrix**.

## Description

A set of documents (corpus) will be analyzed and information will be extracted:
- Most frequent words.
- Least used word.
- Most repeated words in each sentence.
- Word frequency distribution.
- Results visualization.

## Features

- **Text preprocessing**: removes **stopwords** and applies **lemmatization** to improve the quality of the analysis.
- **TF-IDF**: generates a **TF-IDF matrix** that represents the importance of words within the corpus.
- **Frequency analysis**: finds the most repeated words and the least frequent word.
- **Visualization**: provides charts on the word frequency distribution.

## Example output:

```
TF-IDF matrix:
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ 0     0    0     0     0    0    0     0     0     0     0.301 0.179 0     0     0     0   0     0   0     0    0     0     0   0.301 0     0    0    0.224 0     0     0     0.512 0     0.602 0     0.301 0     0     0     0    0.147 0     0    0     0     0   0     0     0   0     0    0     0     0    0   0     0     │
│ 0.272 0.32 0     0     0    0.32 0     0     0     0     0     0     0.238 0     0     0   0     0   0     0    0     0     0   0     0     0.32 0.32 0     0     0.156 0     0     0     0     0     0     0     0     0     0    0.156 0     0.32 0     0.272 0   0     0     0   0     0    0     0.238 0.32 0   0.272 0     │
│ 0     0    0     0     0    0    0     0     0     0     0     0     0.223 0     0     0.3 0     0.3 0     0    0     0     0.3 0     0     0    0    0     0     0.146 0     0     0     0     0     0     0     0     0     0    0     0     0    0.178 0     0.3 0     0     0.3 0     0    0.599 0     0    0.3 0     0     │
│ 0     0    0     0     0    0    0     0     0     0.358 0     0.25  0     0     0     0   0     0   0.358 0    0     0     0   0     0     0    0    0.314 0.422 0.206 0     0.358 0     0     0     0     0     0     0     0    0.206 0.358 0    0.25  0     0   0     0     0   0     0    0     0     0    0   0     0     │
│ 0.312 0    0     0     0    0    0.368 0     0     0     0     0     0     0.312 0     0   0     0   0     0    0     0.368 0   0     0.312 0    0    0     0     0.179 0     0     0     0     0     0     0     0     0     0    0     0     0    0     0     0   0.368 0     0   0     0    0     0.273 0    0   0.312 0.312 │
│ 0     0    0     0     0    0    0     0     0     0     0     0.28  0     0     0.472 0   0     0   0     0    0     0     0   0     0     0    0    0.351 0     0     0     0     0     0     0     0     0.472 0     0     0    0.23  0     0    0.28  0     0   0     0.472 0   0     0    0     0     0    0   0     0     │
│ 0     0    0     0.338 0    0    0     0     0     0     0     0     0.251 0.287 0     0   0.338 0   0     0    0     0     0   0     0     0    0    0     0     0.165 0.338 0     0     0     0     0     0     0.338 0     0    0.165 0     0    0     0.287 0   0     0     0   0.338 0    0     0.251 0    0   0     0.287 │
│ 0     0    0     0     0    0    0     0.344 0     0.585 0     0.204 0     0     0     0   0     0   0.292 0    0     0     0   0     0     0    0    0     0     0.168 0     0     0     0     0     0     0     0     0     0    0     0.585 0    0.204 0     0   0     0     0   0     0    0     0     0    0   0     0     │
│ 0     0    0.393 0     0    0    0     0     0.393 0     0     0     0     0     0     0   0     0   0     0    0.393 0     0   0     0     0    0    0     0     0.192 0     0     0.393 0     0.393 0     0     0     0.393 0    0.192 0     0    0     0     0   0     0     0   0     0    0     0     0    0   0     0     │
│ 0     0    0     0     0.42 0    0     0     0     0     0     0.249 0     0     0     0   0     0   0     0.42 0     0     0   0     0.357 0    0    0     0     0     0     0     0     0     0     0     0     0     0     0.42 0.205 0     0    0.249 0     0   0     0     0   0     0.42 0     0     0    0   0     0     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Vocabulary:
╭─────────┬───────────────────────────────────────────────────────────────╮
│  Letra  │ Palabras                                                      │
├─────────┼───────────────────────────────────────────────────────────────┤
│    A    │ application, artificial, available                            │
│    B    │ backend, beginner, browser                                    │
│    C    │ cloud, code, community, compilation, compile, cplus           │
│    D    │ data, development, due, dynamically                           │
│    E    │ ecosystem, ensures, execution, experienced, extensive         │
│    G    │ go, great                                                     │
│    H    │ high                                                          │
│    I    │ ideal, include, intelligence, interpret                       │
│    J    │ java, javascript, js                                          │
│    L    │ language, large, level, library, low                          │
│    N    │ nature, node, number                                          │
│    P    │ programmer, python                                            │
│    R    │ require, run, rust                                            │
│    S    │ science, security, server, slow, statically, strong, suitable │
│    T    │ typed                                                         │
│    U    │ use                                                           │
│    V    │ various                                                       │
│    W    │ weakly, web, widely                                           │
╰─────────┴───────────────────────────────────────────────────────────────╯

Hierarchy of the 6 most used words:
╭─────┬────────────┬─────────╮
│  #  │    Word    │  Times  │
├─────┼────────────┼─────────┤
│  1  │   python   │    7    │
│  2  │ javascript │    7    │
│  3  │   cplus    │    5    │
│  4  │    rust    │    5    │
│  5  │ interpret  │    3    │
│  6  │  language  │    3    │
╰─────┴────────────┴─────────╯

The least used word is 'programmer' with 1 occurrence(s).

Most repeated word per sentence:
╭────────────┬─────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│    Word    │  Times  │ Sentence                                                                                               │
├────────────┼─────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  language  │    2    │ python interpret high-level language cplus compile low-level language                                  │
│ javascript │    1    │ javascript run web browser python use various application include data science artificial intelligence │
│   typed    │    2    │ javascript dynamically weakly typed rust statically typed ensures great data security                  │
│   python   │    1    │ python javascript interpret language java cplus rust require compilation execution                     │
│ javascript │    1    │ javascript widely use web development go ideal server cloud application                                │
│   python   │    1    │ python slow cplus rust due interpret nature                                                            │
│ javascript │    1    │ javascript strong ecosystem node.js backend development python widely use data science                 │
│  require   │    2    │ javascript require compilation cplus rust require code compilation execution                           │
│   python   │    1    │ python javascript large community extensive number available library                                   │
│   python   │    1    │ python ideal beginner rust cplus suitable experienced programmer                                       │
╰────────────┴─────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Technologies Used

- **Python**
- **NLTK**: Library for natural language processing.
- **Scikit-learn**: Used for generating the TF-IDF matrix.
- **Matplotlib**: Used for data visualization.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AbrSantiago/corpus-tfidf-analyzer.git
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## NLTK Data Preparation

This project uses the NLTK library, which requires downloading some datasets before running the scripts.

Run the following Python script once to ensure all necessary NLTK resources are downloaded:
````bash
python prepare_environment.py
````

### Resources included:
- punkt
- wordnet
- stopwords
- averaged_perceptron_tagger

Note: If you skip this step, the script will attempt to download them automatically during execution, 
which might trigger repeated download prompts even if the files are already present.


## Usage

Run the main script:
```bash
python main.py
```
