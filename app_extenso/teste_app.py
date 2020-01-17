import pytest

from app import traduz_inteiro

# Parametros para alguns testes da função de conversão de inteiro para extenso
@pytest.mark.parametrize("entrada , resultado", [
    ("0", "zero"),
    ("9", "nove"),
    ("10", "dez"),
    ("20", "vinte"),
    ("99", "noventa e nove"),
    ("100", "cem"),
    ("101", "cento e um"),
    ("110", "cento e dez"),
    ("120", "cento e vinte"),
    ("199", "cento e noventa e nove"),
    ("200", "duzentos"),
    ("999", "novecentos e noventa e nove"),
    ("1000", "um mil"),
    ("1001", "um mil e um"),
    ("1010", "um mil e dez"),
    ("1099", "um mil e noventa e nove"),
    ("1100", "um mil e cem"),
    ("1200", "um mil e duzentos"),
    ("1999", "um mil e novecentos e noventa e nove"),
    ("5050", "cinco mil e cinquenta"),
    ("10000", "dez mil"),
    ("10001", "dez mil e um"),
    ("10100", "dez mil e cem"),
    ("50050", "cinquenta mil e cinquenta"),
    ("99999", "noventa e nove mil e novecentos e noventa e nove"),
    ("-1", "menos um"),
    ("-10", "menos dez"),
    ("-99", "menos noventa e nove"),
    ("-999", "menos novecentos e noventa e nove"),
    ("-9999", "menos nove mil e novecentos e noventa e nove"),
    ("-88888", "menos oitenta e oito mil e oitocentos e oitenta e oito"),
    ])

def teste_extenso(entrada, resultado):
    assert traduz_inteiro(entrada) == resultado
