#!/usr/bin/env python
# -*- coding: utf-8 -*-

#

from gnuradio import gr
import numpy as np

class blk (gr. sync_block ):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="Diferenciador",
            in_sig=[np.float32],
            out_sig=[np.float32])
        
        self.acum_anterior = 0.0
    def work(self, input_items, output_items):
        x = input_items[0]#señal de entrada
        y = output_items[0]#señal acumulada diferencial
        
        
        for i in range(len(x)):
            dif = x[i]
            y[i] = dif - self.acum_anterior
            self.acum_anterior  = dif

        return len(y)
        
        
        

