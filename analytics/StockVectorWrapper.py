from analytics.HasStockIndicators import HasStockIndicators
import numpy as np


class StockVectorWrapper(HasStockIndicators):
    def __init__(self, *args, **kwargs):
        super(StockVectorWrapper, self).__init__(*args, **kwargs)
        self.enhance_elements()

    def enhance_elements(self):
        print("Enhancing: " + self.name)
        for x in tqdm([x for x in self.__dict__.keys() if x != "df" and x != "name"]):
            ES = EnhancedSeries(x, self.__dict__[x])
            self.df = pd.concat([self.df, ES.df], axis=1)
            self.df.reset_index()
            self.df.fillna()
            self.df.to_csv(os.pardir + r'/' + self.name + r'.csv')

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
