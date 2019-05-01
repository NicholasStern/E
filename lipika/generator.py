import cv2

class MyDataGenerator(keras.utils.Sequence):
    def __init__(self, files, batch_size, mapping):
        self.files = files
        self.batch_size = batch_size
        self.mapping = mapping

    def on_epoch_end(self):
        '''Shuffle list of files after each epoch.'''
        if self.shuffle:
            np.random.shuffle(self.files)

    def __getitem__(self, index):
        cur_files = self.files[index*self.batch_size:(index+1)*self.batch_size]
        # Generate data
        X, y = self.__data_generation(cur_files)
        return X, y

    def __data_generation(self, cur_files):
        X_img = np.zeros(shape=(self.batch_size, 300, 300, 3))
        X_word = np.zeros(shape=(self.batch_size, 300))

        for i, f in enumerate(cur_files):
            img = cv2.imread(f)
            # preprocess
            img = img/255

            # store image
            X_img[i] = img

            # need to figure out what this would look like 
            X_word[i] = mapping[f] # {}: filepath -> word vector
        return [X_img, X_word], Y

    def __len__(self):
        return int(np.floor(len(self.files) / self.batch_size))
