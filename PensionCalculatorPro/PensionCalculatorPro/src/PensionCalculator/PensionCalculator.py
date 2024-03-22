import unittest

 """ Definición de excepciones hace posible control y manejar errores de manera estructurada y facil de entender """
class edad_negativa(Exception):
    """Excepción lanzada cuando la edad es negativa."""

class saldo_negativo(Exception):
    """Excepción lanzada cuando el saldo es negativo."""

class rentabilidad_negativa(Exception):
    """Excepción lanzada cuando la rentabilidad es negativa."""

class administracion_negativa(Exception):
    """Excepción lanzada cuando la administración es negativa."""

class semanas_insuficientes(Exception):
    """Excepción lanzada cuando las semanas laboradas son insuficientes."""

class edad_insuficiente(Exception):
    """Excepción lanzada cuando la edad es insuficiente para jubilarse."""

class rentabilidad_superior_cien(Exception):
    """Excepción lanzada cuando la rentabilidad supera el 100%."""

class semanas_negativas(Exception):
    """Excepción lanzada cuando las semanas laboradas son negativas."""

class sexo_invalido(Exception):
    """Excepción lanzada cuando el sexo no es 'mujer' o 'hombre'."""

def calcular_pension(edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion):
    """Calcula la pensión basada en diversos factores. """

    Argumentos:
        edad_actual (int): Edad actual de la persona.
        sexo (str): Sexo de la persona, debe ser 'mujer' o 'hombre'.
        salario_actual (float): Salario actual de la persona.
        semanas_laboradas (int): Número de semanas laboradas por la persona.
        ahorro_actual (float): Ahorro actual en el fondo de pensiones.
        rentabilidad_fondo (float): Rentabilidad anual del fondo de pensiones.
        tasa_administracion (float): Tasa de administración del fondo de pensiones.

    Retorna:
        tuple: Una tupla con el valor del ahorro pensional esperado, la pensión anual y la pensión mensual.
    """
    # Variables constantes
    semanas_minimas = 1150
    edad_jubilacion_mujer = 57
    edad_jubilacion_hombre = 62
    rentabilidad_maxima = 100
    cero = 0

    # Control de errores
    if edad_actual < cero:
        raise edad_negativa("La edad no puede ser negativa")

    if semanas_laboradas < cero:
        raise semanas_negativas("Las semanas laboradas no pueden ser negativas")

    if semanas_laboradas < semanas_minimas:
        raise semanas_insuficientes("Las semanas laboradas son insuficientes")

    if ahorro_actual < cero:
        raise saldo_negativo("El saldo no puede ser negativo")

    if rentabilidad_fondo < cero:
        raise rentabilidad_negativa("La rentabilidad del fondo no puede ser negativa")

    if rentabilidad_fondo > rentabilidad_maxima:
        raise rentabilidad_superior_cien("La rentabilidad del fondo no puede ser mayor al 100%")

    if tasa_administracion < cero:
        raise administracion_negativa("La tasa de administración del fondo no puede ser negativa")

    try:
        if edad_actual >= edad_jubilacion_mujer and sexo == "mujer":
            raise edad_insuficiente("La mujer ya debería haberse jubilado")

        if edad_actual > edad_jubilacion_hombre and sexo == "hombre":
            raise edad_insuficiente("El hombre ya debería haberse jubilado")
        
        if sexo not in {"mujer", "hombre"}:
            raise sexo_invalido("El sexo debe ser 'mujer' o 'hombre'")
    except edad_insuficiente as e:
        print("Advertencia:", e)

    """
Calculos para el valor de la pension
    """
    años_restantes = edad_jubilacion_mujer - edad_actual if sexo == "mujer" else edad_jubilacion_hombre - edad_actual

    valor_ahorro_pensional_esperado = ahorro_actual * ((1 + rentabilidad_fondo / rentabilidad_maxima) ** años_restantes)
    valor_pension_anual = valor_ahorro_pensional_esperado * ((rentabilidad_fondo - tasa_administracion) / rentabilidad_maxima)
    valor_pension_mensual = valor_pension_anual / 12

    return valor_ahorro_pensional_esperado, valor_pension_anual, valor_pension_mensual

if __name__ == '__main__':
    unittest.main()
