from saleae.range_measurements import AnalogMeasurer
import numpy as np
from numpy import trapz

class Current(AnalogMeasurer):
    supported_measurements = ["area"]

    """
    Class initialisation
    """
    def __init__(self, requested_measurements):
        super().__init__(requested_measurements)
        self.batches = []

    """
    Does not process data. Simply attaches
    samples to be processed later.
    """
    def process_data(self, data):
        self.batches.append(data.samples)

    """
    Calculates the voltage drop Max - Average Divide by 0.1 ohm R
    """  
    def measure(self):
        data = np.concatenate(self.batches)
        maxVoltage = np.amax(data)
        minVoltage = np.amin(data)
        averageVoltage = np.mean(data)
        voltageDrop = maxVoltage - minVoltage
        averageCurrent = voltageDrop / 0.1
        maxCurrent = (maxVoltage - minVoltage) / 0.1
        return {"Vdrop" : round(voltageDrop,6),
                "Iavg" : round(averageCurrent,6),
                "Vavg": round(averageVoltage,6),
                "Vmax" : round(maxVoltage,6),
                "Vmin: : round(minVoltage,6),
                "Imax" : round(maxCurrent,6)}
        
