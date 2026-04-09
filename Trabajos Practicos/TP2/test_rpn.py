import unittest
from rpn import evaluate, RPNError


class TestRPN(unittest.TestCase):

    # -----------------------
    # OPERACIONES BÁSICAS
    # -----------------------

    def test_add(self):
        self.assertEqual(evaluate("3 4 +".split()), 7)

    def test_complex_expression(self):
        self.assertEqual(
            evaluate("5 1 2 + 4 * + 3 -".split()),
            14
        )

    def test_multiplication_chain(self):
        self.assertEqual(
            evaluate("2 3 4 * +".split()),
            14
        )

    def test_float_operations(self):
        self.assertAlmostEqual(
            evaluate("2.5 2 *".split()),
            5.0
        )

    def test_negative_numbers(self):
        self.assertEqual(
            evaluate("-4 2 *".split()),
            -8
        )

    # -----------------------
    # ERRORES
    # -----------------------

    def test_division_by_zero(self):
        try:
            evaluate("3 0 /".split())
        except RPNError:
            pass
        else:
            self.fail("No detectó división por cero")

    def test_invalid_token(self):
        try:
            evaluate("3 x +".split())
        except RPNError:
            pass
        else:
            self.fail("No detectó token inválido")

    def test_insufficient_stack(self):
        try:
            evaluate("3 +".split())
        except RPNError:
            pass
        else:
            self.fail("No detectó pila insuficiente")

    def test_final_stack_error(self):
        try:
            evaluate("3 4".split())
        except RPNError:
            pass
        else:
            self.fail("No detectó pila final inválida")

    # -----------------------
    # COMANDOS DE PILA
    # -----------------------

    def test_dup(self):
        self.assertEqual(
            evaluate("5 dup +".split()),
            10
        )

    def test_swap(self):
        self.assertEqual(
            evaluate("3 4 swap -".split()),
            1
        )

    def test_drop(self):
        self.assertEqual(
            evaluate("3 4 drop".split()),
            3
        )

    def test_clear(self):
        try:
            evaluate("3 4 clear".split())
        except RPNError:
            pass
        else:
            self.fail("Clear no vació correctamente")

    # -----------------------
    # CONSTANTES
    # -----------------------

    def test_pi(self):
        self.assertAlmostEqual(
            evaluate("p".split()),
            3.1415926535,
            places=5
        )

    def test_e(self):
        self.assertAlmostEqual(
            evaluate("e".split()),
            2.71828,
            places=4
        )

    def test_phi(self):
        self.assertAlmostEqual(
            evaluate("j".split()),
            1.61803,
            places=4
        )

    # -----------------------
    # FUNCIONES
    # -----------------------

    def test_sqrt(self):
        self.assertEqual(
            evaluate("9 sqrt".split()),
            3
        )

    def test_log(self):
        self.assertEqual(
            evaluate("100 log".split()),
            2
        )

    def test_ln(self):
        result = evaluate("2.718281828 ln".split())
        self.assertAlmostEqual(result, 1, places=4)

    def test_exp(self):
        self.assertEqual(
            round(evaluate("1 ex".split())),
            3
        )

    def test_pow10(self):
        self.assertEqual(
            evaluate("2 10x".split()),
            100
        )

    def test_inverse(self):
        self.assertEqual(
            evaluate("2 1/x".split()),
            0.5
        )

    def test_power_yx(self):
        self.assertEqual(
            evaluate("2 3 yx".split()),
            8
        )

    def test_chs(self):
        self.assertEqual(
            evaluate("5 CHS".split()),
            -5
        )

    # -----------------------
    # TRIGONOMÉTRICAS
    # -----------------------

    def test_sin(self):
        result = evaluate("90 sin".split())
        self.assertAlmostEqual(result, 1, places=4)

    def test_cos(self):
        result = evaluate("0 cos".split())
        self.assertAlmostEqual(result, 1, places=4)

    def test_tan(self):
        result = evaluate("45 tg".split())
        self.assertAlmostEqual(result, 1, places=4)

    # -----------------------
    # MEMORIAS
    # -----------------------

    def test_store_and_recall(self):
        self.assertEqual(
            evaluate("5 0 STO 0 RCL".split()),
            5
        )

    def test_invalid_memory(self):
        try:
            evaluate("5 10 STO".split())
        except RPNError:
            pass
        else:
            self.fail("No detectó memoria inválida")


if __name__ == "__main__":
    unittest.main()