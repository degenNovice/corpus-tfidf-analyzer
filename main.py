# TF-IDF (Term Frequency-Inverse Document Frequency):

# Realizar pipeline para analizar CorpusLenguajes.txt
#   - Aplicar stop_word ✅
#   - Lematización ✅
#   - Tf-Idf ✅
#   - Mostrar el corpus preparado ✅
#   - Mostrar la matriz TF-IDF generada ✅
#   - Mostrar el vocabulario generado ✅

# Analizar el mismo y redactar un informe con las conclusiones obtenidas.
#   - Obtener las jerarquía de 6 palabras mas usadas en el corpus ✅
#   - La palabra menos utilizada ✅
#   - Las palabras mas repetidas en la misma oración ✅
#   - Imprimir el gráfico de Distribución de Frecuencia ✅

import nltk
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import FreqDist
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from tabulate import tabulate, TableFormat, Line, DataRow
import pandas as pd


def run():
    corpus, corpus_lematizado = obtener_corpus('CorpusLenguajes.txt')
    mostrar_corpus(corpus)

    matriz, vocabulario = aplicar_tfidf(corpus)
    mostrar_matriz(matriz)
    mostrar_vocabulario_por_letra(vocabulario)

    frecuencia = obtener_frecuencia(corpus_lematizado)
    mostrar_6_palabras_mas_frecuentes(frecuencia)
    mostrar_palabra_menos_frecuente(frecuencia)
    mostrar_palabra_mas_repetida_por_cada_oracion(corpus_lematizado)
    graficar_distancia_de_frecuencia(frecuencia)


def obtener_corpus(file_name):
    contexto = globals().copy()
    with open(file_name, 'r', encoding='utf-8') as f:
        codigo = f.read()
    exec(codigo, contexto)
    corpus_lematizado = contexto['corpus']
    corpus = [" ".join(sublist) for sublist in corpus_lematizado]
    return corpus, corpus_lematizado


def mostrar_corpus(corpus):
    print("\nCorpus = [", )
    for sentence in corpus:
        print(f"\t'{sentence}'")
    print("]")


def quitarStopwords_eng(text):
    eng = stopwords.words("english")
    clean_text = [w.lower() for w in text if w.lower() not in eng
                  and w not in string.punctuation
                  and w not in ["'s", '|', '--', "''", "``", '.-']]
    return clean_text


def lematizar(text):
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in text]
    return lemmatized_text


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def aplicar_tfidf(corpus):
    vectorizer = TfidfVectorizer()
    matriz = vectorizer.fit_transform(corpus)  # Aplicar TF-IDF al corpus.
    vocabulario = vectorizer.vocabulary_
    return matriz, vocabulario


def mostrar_matriz(matriz, decimales=3):
    custom_format = TableFormat(
        lineabove=Line("╭─", "─", "─", "─╮"),
        linebelowheader=Line("├─", "─", "─", "─┤"),
        linebetweenrows=None,
        linebelow=Line("╰─", "─", "─", "─╯"),
        headerrow=DataRow("│ ", " ", " │"),
        datarow=DataRow("│ ", " ", " │"),
        padding=0,
        with_header_hide=None,
    )
    print("\nMatriz TF-IDF:")
    matriz_densa = matriz.toarray()
    df = pd.DataFrame(matriz_densa)
    df = df.map(lambda x: 0 if round(x, decimales) == 0 else round(x, decimales))
    tabla = tabulate(df, headers=(), tablefmt=custom_format, showindex=False)
    print(tabla)


def mostrar_vocabulario_por_letra(vocabulario):
    print("\nVocabulario:")
    agrupado = {}
    for palabra in vocabulario:
        letra = palabra[0].upper()
        agrupado.setdefault(letra, []).append(palabra)
    tabla = []
    for letra in sorted(agrupado.keys()):
        palabras = ", ".join(sorted(agrupado[letra]))
        tabla.append([letra, palabras])
    print(tabulate(tabla, headers=["Letra", "Palabras"], tablefmt="rounded_outline", colalign=("center", "left")))


def obtener_frecuencia(corpus_lematizado):
    corpus_tokenizado = [item for sublist in corpus_lematizado for item in sublist]
    frecuencia = FreqDist(corpus_tokenizado)
    return frecuencia


def mostrar_6_palabras_mas_frecuentes(frecuencia):
    top6 = frecuencia.most_common(6)
    tabla = [(i + 1, palabra, cantidad) for i, (palabra, cantidad) in enumerate(top6)]

    print("\nJerarquía de 6 palabras más usadas:")
    print(tabulate(tabla, headers=["#", "Palabra", "Veces"], tablefmt="rounded_outline", colalign=("center", "center", "center")))


def mostrar_palabra_menos_frecuente(frecuencia):
    menos_usada = frecuencia.most_common()[-1]
    print(f"\nLa palabra menos utilizada es '{menos_usada[0]}' con {menos_usada[1]} aparición/es.")


def mostrar_palabra_mas_repetida_en_una_misma_oracion(corpus_lematizado):
    mayor_repeticion = 0
    palabra_mas_repetida = ""
    oracion_mas_repetida = []
    for oracion in corpus_lematizado:
        freq = FreqDist(oracion)
        palabra, repeticiones = freq.most_common(1)[0]  # palabra más repetida en esa oración
        if repeticiones > mayor_repeticion:
            mayor_repeticion = repeticiones
            palabra_mas_repetida = palabra
            oracion_mas_repetida = oracion
    print(f"\nLa palabra más repetida en una misma oración es '{palabra_mas_repetida}' ({mayor_repeticion} veces)")
    print(f"en la oración: '{' '.join(oracion_mas_repetida)}'")


def mostrar_palabra_mas_repetida_por_cada_oracion(corpus_lematizado):
    print("\nPalabra más repetida por cada oración:")
    tabla = []
    for oracion in corpus_lematizado:
        freq = FreqDist(oracion)
        palabra, repeticiones = freq.most_common(1)[0]  # palabra más repetida en esa oración
        tabla.append((palabra, repeticiones, " ".join(oracion)))
    print(tabulate(tabla, headers=["Palabra", "Veces", "Oración"], tablefmt="rounded_outline", colalign=("center", "center", "left")))


def graficar_distancia_de_frecuencia(frecuencia):
    frecuencia.plot(20, show=True)


if __name__ == '__main__':
    run()
