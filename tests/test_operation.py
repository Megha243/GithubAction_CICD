from src.math_operations import add, subtract

def test_add():
    assert add(2,3)==6
    assert add(-1,1)==0
    assert add(0,0)==0  

def teswt_subtract():
    assert subtract(5,2)==3
    assert subtract(0,1)==-1
    assert subtract(10,5)==5