#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from gnuradio import gr
import numpy as np

class Acumulador(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="Acumulador",
            in_sig=[np.float32],
            out_sig=[np.float32])
        self.cum_sum = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]
        
        for i in range(len(x)):
            suma = x[i]
            self.cum_sum += suma
            y[i] = self.cum_sum

        return len(y)
