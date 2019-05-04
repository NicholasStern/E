import numpy as np

def loadGloveModel(gloveFile, shape=(1917494, 300), downweight_factor=1.):
    '''
    Load GloVe pre-trained word vectors
    
    INPUT
    =====
    gloveFile: file with GloVe word vectors
        .txt file
    shape: (vocabulary size, number of latent dimensions)
        tuple
    downweight_factor: rescaling factor for GloVe embeddings
        float
    
    OUTPUTS
    =======
    glove_index_dict: dictionary w/ keys=words and values=row index in glove_embedding_weights
        dict
    glove_embedding_weights: matrix w/ n_row = vocabulary size and n_col = latent dimension
        np.array
    '''
    glove_index_dict = {}
    glove_embedding_weights = np.empty(shape)
    with open(gloveFile, 'r', encoding="utf8") as fp:
        i = 0
        for l in fp:
            l = l.strip().split()
            w = l[0]
            glove_vector = [float(x) for x in l[1:]]
            glove_index_dict[w] = i        
            glove_embedding_weights[i,:] = glove_vector
            i += 1
    glove_embedding_weights *= downweight_factor
    
    return glove_index_dict, glove_embedding_weights