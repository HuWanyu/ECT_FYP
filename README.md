# ECT_FYP
 
### Instructions

Clone or download the repo to your machine.

Use `conda` to create the virtual environment - currently environment creation via `pip3` is not supported. Navigate to the `SCDF_NER_FYP` directory and run the following in the command line:

`conda env create -f environment.yml`

You can verify that the required packages installed correctly by activating the environment (`conda activate m_ner`) and running `conda list`.

#### Dependencies

Major dependencies include `pytorch-transformers`, `spacy`, and `streamlit`. Take a look at the `environment.yml` file for a full list. (Note that at the moment, some of the packages in the environment are not strictly necessary, and a leaner environment file will be added down the line.)

## Usage

### Training a model

Use `python3 main.py` to train an English model and save per-epoch checkpoints.

**Before training a model:** run `python3 -m spacy download en_core_web_lg` before running the main script.

### Demo for monolingual NER

Once you have a usable model checkpoint, run `streamlit run demo.py en`, which opens a web app you can use to test the model's predictions interactively. Be sure to download `en_core_web_lg` before running the demo.

## Models

* The English model is a fine-tuned implementation of Google's `bert-base-cased` model, ensembled with spaCy's `en_core_web_lg`, which uses a CNN architecture.

## Data Sources

* The English BERT model was fine-tuned on [CONLL2003](http://aclweb.org/anthology/W03-0419) data and [Emerging Entities '17](https://noisy-text.github.io/2017/emerging-rare-entities.html) data. The Emerging Entities '17 data is composed of informal text (such as tweets), and includes more diverse entity types (such as creative works and products) than CONLL2003, providing the model with the ability to identify MISC entities in addition to the standard person, location, and organization tags.
* The English spaCy model was trained on [OntoNotes](https://catalog.ldc.upenn.edu/LDC2013T19) and uses GloVe word vectors trained on [Common Crawl](https://commoncrawl.org/); see the spaCy docs for more information.
