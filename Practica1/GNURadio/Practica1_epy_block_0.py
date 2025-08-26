import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Promedios_de_tiempos',
            in_sig=[np.float32],
            out_sig=[np.float32, np.float32, np.float32, np.float32, np.float32]
        )
        self.acum_sum = 0.0
        self.acum_sq_sum = 0.0
        self.acum_var_sum = 0.0
        self.N_total = 0

    def work(self, input_items, output_items):
        x = input_items[0]
        N = len(x)

        self.N_total += N

        # Promedio
        suma = np.sum(x)
        self.acum_sum += suma
        media = self.acum_sum / self.N_total

        # Media Cuadrática
        x2 = np.square(x)
        suma_x2 = np.sum(x2)
        self.acum_sq_sum += suma_x2
        media_cuad = self.acum_sq_sum / self.N_total

        # RMS
        rms = np.sqrt(media_cuad)

        # Potencia promedio (igual a media cuadrática)
        potencia = media_cuad

        # Desviación estándar
        suma_var = np.sum((x - media) ** 2)
        self.acum_var_sum += suma_var
        desviacion = np.sqrt(self.acum_var_sum / self.N_total)

        # Salidas: solo una muestra por salida
        output_items[0][0] = media
        output_items[1][0] = media_cuad
        output_items[2][0] = rms
        output_items[3][0] = potencia
        output_items[4][0] = desviacion

        return 1

