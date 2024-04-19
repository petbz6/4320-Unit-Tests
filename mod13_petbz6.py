import unittest
from datetime import datetime

# Stock Symbol Testing
class StockSymbol:
    def capitalized(self, symbol):
        return symbol == symbol.upper()

    def char_length(self, symbol):
        return len(symbol) >= 1 and len(symbol) <= 7

    def char_alpha(self, symbol):
        return symbol.isalpha()

class Stock_Symbol_Test(unittest.TestCase):
    def setUp(self):
        self.sym = StockSymbol()
        self.symbol = "AAPL"

    # Test for capitalized symbol
    def test_capitalized(self):
        self.assertTrue(self.sym.capitalized(self.symbol))
    
    # Test for character length between 1 and 7
    def test_char_length(self):
        self.assertTrue(self.sym.char_length(self.symbol))

    # Test for alpha characters
    def test_char_alpha(self):
        self.assertTrue(self.sym.char_alpha(self.symbol))


# Chart Type Testing
class ChartType:
    def numeric_character(self, chart_type):
        return len(chart_type) == 1 and chart_type.isdigit()

    def length(self, chart_type):
        return chart_type in ["1", "2"]

class Chart_Type_Test(unittest.TestCase):
    def setUp(self):
        self.chart = ChartType()
        self.chart_type = "1"  

    # Test for 1 numeric character
    def test_numeric_character(self):
        self.assertTrue(self.chart.numeric_character(self.chart_type))

    # Test for chart type 1 or 2
    def test_chart_type_length(self):
        self.assertTrue(self.chart.length(self.chart_type))

## Time Series Testing
class TimeSeries:
    def numeric_char(self, time_series):
        return len(time_series) == 1 and time_series.isdigit()

    def valid_char(self, time_series):
        return time_series in ["1", "2", "3", "4"]

class TimeSeriesTest(unittest.TestCase):
    def setUp(self):
        self.ts = TimeSeries()
        self.time_series = "1"  

    # Test for 1 numeric character
    def test_numeric_char(self):
        self.assertTrue(self.ts.numeric_char(self.time_series))

    # Test for valid numeric character 1-4
    def test_valid_char(self):
        self.assertTrue(self.ts.valid_char(self.time_series))


# Start Date Testing
class StartDate:
    def valid_start_date(self, start_date):
        datetime.strptime(start_date, "%Y-%m-%d")
        return True
            

class StartDateTest(unittest.TestCase):
    def setUp(self):
        self.sd = StartDate()
        self.start_date = "2024-01-01"

    # Test for valid start date format (YYYY-MM-DD)
    def test_valid_start_date(self):
        self.assertTrue(self.sd.valid_start_date(self.start_date))

# End Date Testing
class EndDate:
    def valid_end_date(self, end_date):
        datetime.strptime(end_date, "%Y-%m-%d")
        return True
            

class EndDateTest(unittest.TestCase):
    def setUp(self):
        self.ed = EndDate()
        self.end_date = "2024-12-31"

    # Test for valid end date format (YYYY-MM-DD)
    def test_valid_start_date(self):
        self.assertTrue(self.ed.valid_end_date(self.end_date))



if __name__ == "__main__":
    unittest.main()








