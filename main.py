from utils.utils import *
if __name__ == '__main__':
    symbols = save_sp500_tickers()
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
