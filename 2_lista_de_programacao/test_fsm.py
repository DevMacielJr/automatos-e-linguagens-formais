from fsm_numero import FSMNumero

def test_zero():
    assert FSMNumero(0, "pt").processar() == "zero"

def test_pt():
    assert FSMNumero(11, "pt").processar() == "onze"

def test_en():
    assert FSMNumero(11, "en").processar() == "eleven"

def test_milhar():
    assert FSMNumero(1000, "pt").processar() == "mil"

def test_grande():
    assert FSMNumero(204328, "pt").processar() == "duzentos e quatro mil , trezentos e vinte e oito"