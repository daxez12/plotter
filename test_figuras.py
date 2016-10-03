import unittest
from figura import Figuras

class TestFiguras(unittest.TestCase):
	
	def setUp(self):
		self.figura = Figuras()

	def test_area_cuadrado_lado_5(self):
		resultado = self.figura.cuadrado(5)
		self.assertEqual(25, resultado)

	def test_area_cuadrado_lado_6(self):
		resultado = self.figura.cuadrado(6)
		self.assertEqual(36, resultado)	

	def test_area_cuadrado_lado_g(self):
		resultado = self.figura.cuadrado('g')
		self.assertEqual('dato incorrecto', resultado)

	def test_area_cuadrado_lado_4_5(self):
		resultado = self.figura.cuadrado(4.5)
		self.assertEqual(20.25, resultado)

	def test_area_rectangulo_base_5_altura_6(self):
		resultado = self.figura.rectangulo(5,6)
		self.assertEqual(30, resultado)

	def test_area_rectangulo_base_6_altura_8(self):
		resultado = self.figura.rectangulo(6,8)
		self.assertEqual(48, resultado)
	
	def test_area_rectangulo_base_g_altura_4(self):
		resultado = self.figura.rectangulo('g',4)
		self.assertEqual('dato incorrecto', resultado)

	def test_area_rectangulo_base_5_altura_g(self):
		resultado = self.figura.rectangulo(5,'g')
		self.assertEqual('dato incorrecto', resultado)

	def test_area_rectangulo_base_4_punto_5_altura_5_punto_1(self):
		resultado = self.figura.rectangulo(4.5,5.1)
		self.assertEqual(22.95, resultado)

	def test_area_rectangulo_base_menos_5_altura_6(self):
		resultado = self.figura.rectangulo(-5,6)
		self.assertEqual('dato incorrecto', resultado)

	def test_area_triangulo_base_5_altura_6(self):
		resultado = self.figura.triangulo(5,6)
		self.assertEqual(15, resultado)

	def test_area_triangulo_base_6_altura_8(self):
		resultado = self.figura.triangulo(6,8)
		self.assertEqual(24, resultado)

	def test_area_triangulo_base_g_altura_4(self):
		resultado = self.figura.triangulo('g',4)
		self.assertEqual('dato incorrecto', resultado)

	def test_area_triangulo_base_menos_5_altura_6(self):
		resultado = self.figura.triangulo(-5,6)
		self.assertEqual('dato incorrecto', resultado)

	def test_area_triangulo_base_4_punto_5_altura_5_punto_1(self):
		resultado = self.figura.triangulo(4.5,5.1)
		self.assertEqual(11.475, resultado)

	def test_area_circunferencia_radio_5(self):
		resultado = self.figura.circunferencia(5)
		self.assertEqual(78.53981633974483,resultado)

	def test_area_circunferencia_radio_6(self):
		resultado = self.figura.circunferencia(6)
		self.assertEqual(113.09733552923255,resultado)

	def test_area_circunferencia_radio_g(self):
		resultado = self.figura.circunferencia('g')
		self.assertEqual('dato incorrecto',resultado)

	def test_area_circunferencia_radio_menos_8(self):
		resultado = self.figura.circunferencia(-8)
		self.assertEqual('dato incorrecto',resultado)

	def test_area_circunferencia_radio_7_punto_7(self):
		resultado = self.figura.circunferencia(7.7)
		self.assertEqual(186.26502843133886,resultado)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()