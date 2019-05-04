# Folder for Anthony's Scripts for AC209b Final Project

### Scripts and Notebooks

`meme_generator_scrape.py` - Script to scrape images, labels, and captions from Meme Generator. Adapted from a script in Dank Learning's [Github repo](https://github.com/alpv95/MemeProject).

`data_processing.ipynb` - Notebook to get GloVe embeddings, clean, and tokenize.

`pickle_utils.py` - A class and functions to handle serializing large files. Lifted from this [Stack Overflow response](https://stackoverflow.com/questions/31468117/python-3-can-pickle-handle-byte-objects-larger-than-4gb).

### Data

**glove_objs.pkl** - Pickle file with [a, b] where 
- a is a dictionary w/ keys=words and values=row index in b
- b is a matrix where each row corresponds to a GloVe vector for a word in the entire GloVe vocabulary (roughly 1.9 million)

**memes** - Folder with all of scraped base images from Meme Generator.

**captions.csv** - Raw dataset from Meme Generator scrape with labels and captions from.

