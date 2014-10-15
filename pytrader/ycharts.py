from datetime import datetime

from numpy import array, vectorize
from pandas import DataFrame
from ychartspy.client import YChartsClient


class DataImplementation(object):
    def __init__(self):
        self.client = YChartsClient()

    def get_prices(self, ticker, time_length):
        raw_data = self.client.get_security_prices(ticker, time_length)
        return convert_to_pandas(raw_data)

    def get_eps(self, ticket, time_length):
        raw_data = self.client.get_security_metric(ticker, "eps_ttm", time_length)
        return convert_to_pandas(raw_data)


def convert_to_pandas(raw_data):
    numpy_data = array(raw_data)
    vectorized = vectorize(lambda x: datetime.fromtimestamp(x / 1000).strftime("%Y-%m-%d"))
    return DataFrame(numpy_data[:, 1], index=vectorized(numpy_data[:, 0]))