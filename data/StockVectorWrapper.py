from data import HasStockIndicators
import numpy as np


class StockVectorWrapper(HasStockIndicators):
    def __init__(self, *args, **kwargs):
        super(StockVectorWrapper, self).__init__(*args, **kwargs)
        self.enhance_elements()

    def floatinate(self):
        for x in self.df.columns:
            if (x != 'date'):
                self.df[x] = self.df[x].astype('float64')

    @property
    def vector(self):
        eig_ndarr = np.ndarray((211, 1))
        self.floatinate()
        mat = self.df.loc[:, self.df.columns != 'date']
        s = mat.values.transpose().dot(mat.values)
        eigval, eigvec = np.linalg.eig(s)
        for x in eigvec[0]:
            np.append(eig_ndarr, x)
        return eig_ndarr

    @property
    def shape(self):
        return self.df.shape
