import gcd
import pytest

tst_b = ((377, 610 ),(832040, 1346269), (9227465, 14930352) , (610,1), (1000,1)  )
tst_c= ( (1346269,1),(14930352,1))
tst_a= ((2,4) , (10, 1000), (27, 64), (105, 15), (81, 42))
# expected results (reference)

# basic exapmples
ref_a = [2,10, 1, 15, 3]

#fibonacci pairs
ref_b = [1,1,1,1,1]
ref_c = [1,1]

@pytest.mark.parametrize("inp, exp",[(tst_a, ref_a),(tst_b, ref_b), (tst_c, ref_c)])
def test_gcd_e(inp, exp ):
    res = [ gcd.gcd_e(a,b) for (a,b) in inp]    
    assert res == exp

