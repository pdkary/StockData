from utils.utils import *
from db.MongoConnector import MongoConnector
import pandas as pd

if __name__ == '__main__':
    symbols = save_sp500_tickers()
    client = MongoConnector()
    df = pd.DataFrame(columns=["a", "b", "c"])
    df.loc[len(df)] = [5, 1, 22]
    df.loc[len(df)] = [69, 404, 5]
    json = df.to_json()
    client.update_collection("test",df)
    df = client.get_collection_df("test")
    print('done')
    # start = getNow()
    # wrapper_list = WrapperFactory().setSymbols(symbols).as_list
    # if len(wrapper_list):
    #     vector_list = [x.vector for x in wrapper_list]
    #     vector_arr = np.ndarray((len(vector_list), vector_list[0].shape[0]))
    #     for x in vector_list:
    #         np.append(vector_arr, x)
    #
    #     nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(vector_arr)
    #     distances, indices = nbrs.kneighbors(vector_arr)
    #     end = getNow()
    #     print("Time Elapsed: ", (end - start).total_seconds(), "s")
    #     for x in range(len(indices)):
    #         print(symbols[indices[x][0]], symbols[indices[x][1]], distances[x][1])
