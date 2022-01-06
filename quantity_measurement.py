from exception import ExceptionMeasurement
from length_conversion import Conversion


class QuantityMeasurement:

    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def __eq__(self, other):
        if other.length is None:
            raise ExceptionMeasurement("Null")
        if self.length != other.length:
            raise ExceptionMeasurement("Values are different")
        if type(self.length) != type(other.length):
            raise ExceptionMeasurement("Have different type")
        if self.unit == other.unit and other.length == self.length:
            return True
