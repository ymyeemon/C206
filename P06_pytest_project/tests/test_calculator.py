from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        # arrange
        a = 224
        b = 125
        cal = Calculator()

        # act
        result = cal.subtract(a,b)

        # assert 
        expected = 99
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 19
        b = 6
        cal = Calculator()

        # act
        result = cal.multiply(a,b)

        # assert 
        expected = 114
        assert result == expected
    
    def test_divide(self):
        # arrange
        a = 60
        b = 5
        cal = Calculator()

        # act
        result = cal.divide(a,b)

        # assert 
        expected = 12
        assert result == expected