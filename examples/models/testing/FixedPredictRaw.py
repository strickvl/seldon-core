import numpy as np
import logging
from FixedBase import FixedBase
from seldon_core.proto import prediction_pb2 
import tensorflow as tf

class FixedPredictRaw(FixedBase):

    def __init__(self, iterations=1):
        super().__init__(iterations)
        
    def predict_raw(self, X):
        is_proto = isinstance(X, prediction_pb2.SeldonMessage)
        if not is_proto:
            return self.work()
        self.work()
        Y = np.array(self.work())
        datadef = prediction_pb2.DefaultData(
            tftensor = tf.make_tensor_proto(Y)
        )
        return prediction_pb2.SeldonMessage(data = datadef)



