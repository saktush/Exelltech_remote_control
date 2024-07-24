import unittest
from modules.matrix import Matrix


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.matrix = Matrix(input_channels=4, output_channels=4)

    def test_initialization(self):
        self.assertEqual(self.matrix.inputs, 4)
        self.assertEqual(self.matrix.outputs, 4)
        self.assertEqual(len(self.matrix.routes), 4)
        self.assertEqual(len(self.matrix.gains), 4)
        self.assertTrue(all(len(row) == 4 for row in self.matrix.routes))
        self.assertTrue(all(len(row) == 4 for row in self.matrix.gains))

    def test_set_routes(self):
        new_routes = [
            [True, False, False, True],
            [False, True, True, False],
            [True, True, False, False],
            [False, False, True, True]
        ]
        self.matrix.routes = new_routes
        self.assertEqual(self.matrix.routes, new_routes)

    def test_set_gains(self):
        new_gains = [
            [-10.0, -20.0, -30.0, -40.0],
            [-50.0, -60.0, -70.0, -80.0],
            [0.0, -10.0, -20.0, -30.0],
            [-40.0, -50.0, -60.0, -70.0]
        ]
        self.matrix.gains = new_gains
        self.assertEqual(self.matrix.gains, new_gains)

    def test_individual_route_methods(self):
        self.matrix.set_route(row=0, col=0, value=True)
        self.assertTrue(self.matrix.get_route(row=0, col=0))

        self.matrix.set_route(row=0, col=0, value=False)
        self.assertFalse(self.matrix.get_route(row=0, col=0))

    def test_individual_gain_methods(self):
        self.matrix.set_gain(row=0, col=0, value=-50)
        self.assertEqual(self.matrix.get_gain(row=0, col=0), -50)

        with self.assertRaises(ValueError):
            self.matrix.set_gain(row=0, col=0, value=10)  # Out of range gain

    def test_input_channels_property(self):
        self.assertEqual(self.matrix.inputs, 4)

    def test_output_channels_property(self):
        self.assertEqual(self.matrix.outputs, 4)

    def test_str_representation(self):
        result = str(self.matrix)
        self.assertIn("Matrix with 4 input channels and 4 output channels", result)

    def test_increase_all_gains(self):
        def increase_gains(matrix: Matrix, increment: float) -> None:
            new_gains = []
            for row in matrix.gains:
                new_row = []
                for gain in row:
                    new_gain = min(matrix.MAX_GAIN, gain + increment)
                    new_row.append(new_gain)
                new_gains.append(new_row)
            matrix.gains = new_gains

        new_gains = [
            [-10.0, -20.0, -30.0, -40.0],
            [-50.0, -60.0, -70.0, -80.0],
            [0.0, -10.0, -20.0, -30.0],
            [-40.0, -50.0, -60.0, -70.0]
        ]
        self.matrix.gains = new_gains

        increase_gains(self.matrix, 5.0)

        expected_gains = [
            [-5.0, -15.0, -25.0, -35.0],
            [-45.0, -55.0, -65.0, -75.0],
            [0.0, -5.0, -15.0, -25.0],
            [-35.0, -45.0, -55.0, -65.0]
        ]
        self.assertEqual(self.matrix.gains, expected_gains)


if __name__ == '__main__':
    unittest.main()
