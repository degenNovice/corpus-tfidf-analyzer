
# Corpus TF-IDF Analyzer

**TF-IDF** (Term Frequency-Inverse Document Frequency) es un modelo para análisis de texto. El objetivo es aplicar técnicas de procesamiento de lenguaje natural (NLP), como **eliminación de stopwords**, **lematización**, y generar una matriz **TF-IDF**.

## Descripción

Se realizará un análisis sobre un conjunto de documentos (corpus), y extrae información relevante como:
- Las palabras más frecuentes.
- La palabra menos utilizada.
- Las palabras más repetidas en cada oración.
- La distribución de frecuencia de palabras.
- La visualización de resultados.

## Características

- **Preprocesamiento de texto**: elimina las **stopwords** y aplica **lematización** para mejorar la calidad del análisis.
- **TF-IDF**: genera una **matriz TF-IDF** que representa la importancia de las palabras dentro del corpus.
- **Análisis de frecuencia**: encuentra las palabras más repetidas y la palabra menos frecuente.
- **Visualización**: ofrece gráficos sobre la distribución de la frecuencia de palabras.

## Ejemplo de salida

```
Matriz TF-IDF:
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

Vocabulario:
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

Jerarquía de 6 palabras más usadas:
╭─────┬────────────┬─────────╮
│  #  │  Palabra   │  Veces  │
├─────┼────────────┼─────────┤
│  1  │   python   │    7    │
│  2  │ javascript │    7    │
│  3  │   cplus    │    5    │
│  4  │    rust    │    5    │
│  5  │ interpret  │    3    │
│  6  │  language  │    3    │
╰─────┴────────────┴─────────╯

La palabra menos utilizada es 'programmer' con 1 aparición/es.

Palabra más repetida por cada oración:
╭────────────┬─────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  Palabra   │  Veces  │ Oración                                                                                                │
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

## Tecnologías utilizadas

- **Python**
- **NLTK**: Biblioteca para procesamiento de lenguaje natural.
- **Scikit-learn**: Para la generación de la matriz TF-IDF.
- **Matplotlib**: Para la visualización de los datos.

## Instalación

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/AbrSantiago/corpus-tfidf-analyzer.git
   ```

2. Crear un entorno virtual e instálarlo en él:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows usa .venv\Scriptsctivate
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el script principal:
```bash
python main.py
```
