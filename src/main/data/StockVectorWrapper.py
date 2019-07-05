from src.main.data.HasStockIndicators import HasStockIndicators
import numpy as np


class StockVectorWrapper(HasStockIndicators):
    def __init__(self, *args, **kwargs):
        super(StockVectorWrapper, self).__init__(*args, **kwargs)
        self.enhance_elements()

    def vectorize(self):
        self.mean_vector = np.ndarray((1, self.df.shape[1]))
        self.std_vector = np.ndarray((1, self.df.shape[1]))
        for column_label in self.df.columns:
            if column_label != 'date':
                mean = self.df[column_label].mean()
                std = self.df[column_label].std()
                np.append(self.mean_vector, mean)
                np.append(self.std_vector, std)
