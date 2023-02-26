import unittest
import tarifas


class TesteTarifas(unittest.TestCase):

    def teste_get_price(self):
        """Testa se a função `get_price` retorna o valor correto para o par de origem e destino '011' e '016'"""
        self.assertEqual(tarifas.get_price('011', '016'), 1.9)

    def teste_sem_plano(self):
        """Testa se a função `sem_plano` retorna o valor correto para uma chamada com tempo igual a 20 e preço igual a 1.9'"""
        self.assertEqual(tarifas.sem_plano(20, 1.9), 38)

    def teste_com_plano(self):
        """Testa se a função `com_plano` retorna o valor correto para uma chamada com tempo igual a 50, preço igual a 1.9 e minutos do plano igual a 30.'"""
        self.assertEqual(tarifas.com_plano(50, 1.9, 30), 41.8)

    def teste_calcula_tarifas(self):
        """Testa se a função `calcula_tarifas` retorna o dicionário correto de tarifas para uma chamada com origem igual a '011', destino igual a '017' e tempo igual a 80.'"""
        esperado = {
            'sem_plano': 136.0,
            'FaleMais30': 93.5,
            'FaleMais60': 37.400000000000006,
            'FaleMais120': 0
        }
        resultado = tarifas.calcula_tarifas('011', '017', 80)
        self.assertDictEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()


