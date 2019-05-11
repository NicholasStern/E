# Folder for Anthony's Scripts for AC209b Final Project

### Scripts and Notebooks

`meme_generator_scrape.py` - Script to scrape images, labels, and captions from Meme Generator. Adapted from a script in Dank Learning's [Github repo](https://github.com/alpv95/MemeProject).

`data_processing.ipynb` - Notebook to get GloVe embeddings, clean, and tokenize.

`pickle_utils.py` - A class and functions to handle serializing large files. Lifted from this [Stack Overflow response](https://stackoverflow.com/questions/31468117/python-3-can-pickle-handle-byte-objects-larger-than-4gb).

`loadGlove.py` - Function to read in GloVe embeddings .txt file and create mapping dictionary for words and embeddings.

### Data

**glove_objs.pkl** - Pickle file with [a, b] where 
- `a` is a dictionary w/ keys=words and values=row index in b
- `b` is a matrix where each row corresponds to a GloVe vector for a word in the entire GloVe vocabulary (roughly 1.9 million)
- **This file is included in our .gitignore.**

**full_clean_processed_data.pkl** - Pickle file with (embedding, idx2word, word2idx, captions) where
- `embedding` is a matrix where each row corresponds to the GloVe embedding for a word, with the words indexed by the `word2idx` dictionary
- `idx2word` and `word2idx` are mapping dictionaries
- `captions` is a .csv with padded and tokenized captions and image labels as well as file paths for base images
- **This file is included in our .gitignore, as are smaller, preliminary versions of this file.**

**memes** - Folder with all of scraped base images from Meme Generator.

**captions.csv** - Raw dataset from Meme Generator scrape with labels and captions from.

**google_twunter_lol.txt** - Offensive words from Google's "What Do You Love" project.

