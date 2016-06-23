# Named Entity Recognition `NER`
Named Entity Recognition research project

### Requirements
Python 2.7 or above
Pip for dependencies `python get-pip.py`

### Installing

#### Installing dependencies
* install numpy using `easy install`, using `sudo apt-get install python-setuptools python-dev build-essential` in linux.

* Install dependencies using the following command:
`sudo pip install -r dependencies`

#### Downloading the Corpus `CONLL 2002`

Execute the file CorpusDownloader.py using `python CorpusDownloader.py`, this will launch a GUI to download the Corpus, select Corpus tab then download the CONLL 2002, then press Download button.
corpus_downloader
![alt text](/images/corpus_downloader.png "Corpus downloader")

#### Running the classificator
`python ner.py`
