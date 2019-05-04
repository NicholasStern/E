# Folder for Anthony's Scripts for AC209b Final Project

### Scripts and Notebooks

`meme_generator_scrape.py` - Script to scrape images, labels, and captions from Meme Generator.

`tokenize.ipynb` - Notebook to clean, tokenize, and get GloVe embeddings.

`pickle_utils.py` - A class and functions to handle serializing large files. Lifted from this [Stack Overflow response](https://stackoverflow.com/questions/31468117/python-3-can-pickle-handle-byte-objects-larger-than-4gb).

### Data

**glove_objs.pkl** - Pickle file with [a, b] where 
- a is a dictionary w. keys=words and values=row index in b
- b is a matrix where each row corresponds to a GloVe vector for a word in the vocabulary

**memes** - Folder with all of scraped base images from Meme Generator.

**captions.csv** - Raw dataset from Meme Generator scrape with labels and captions from.

