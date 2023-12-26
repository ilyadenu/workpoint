from approximation import Approximation, Uf_approx_sinus
from auxiliary_files.stat import Uf_approx_sinus_stat


class PhaseCalculation(Approximation):

    def __init__(self, first_file: int, last_file: int):
        super().__init__(first_file, last_file)
        self.phase = 0.

    def maximum_matching(self):

        """Функция для расчета сдвига фазы от изменения рабочей точки"""

        uf = Uf_approx_sinus[470:520]
        uf_stat = Uf_approx_sinus_stat[470:520]

        count = 0
        for i in range(len(uf)):
            count += 1
            if uf[i] == max(uf):
                time_dynamic = self.time[470+count]

        count_stat = 0
        for i in range(len(uf_stat)):
            count_stat += 1
            if uf_stat[i] == max(uf_stat):
                time_static = self.time[470+count_stat]

        self.phase = abs(time_dynamic - time_static)
        self.phase = self.phase/(1*10e-7)

        return self.phase


pc = PhaseCalculation(17, 18)
pc.maximum_matching()
