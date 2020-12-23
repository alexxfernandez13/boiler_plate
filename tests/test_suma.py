from boiler_plate.main import suma

def test_suma(a=1,b=2):
    result = suma(a,b)
    assert result == 3