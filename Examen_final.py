from math import cos, sin

def calcular_movimiento(degree:float, Fr:float, m1:float) -> list:
  """
  Genera una lista cuyos elementos contienen el valor de la masa m2 y el sentido del movimiento.
  El valor de m2 inicia en 0Kg y aumenta 0.5Kg hasta que m2 deje de subir.

  Parametros
  ----------
    degree (float): El angulo de inclinacion del plano inclinado
    Fr (float): El coeficiente de friccion de m1
    m1 (float) :La masa de m1
  
  Retorna
  -------
    (list): Retorna una lista de listas, donde el primer elemento contiene el valor de m2.
    El segundo valor es el sentido de m2 ('Subiendo', 'Equilibrio', 'Bajando')
  """
  sistema = dict()
  sistema['g'] = 9.81
  sistema['uk'] = Fr
  sistema['C1'] = {
    'm': m1,
    'mg': m1 * sistema['g'],
    'mgx': m1 * sistema['g'] * sin(degree),
    'mgy': m1 * sistema['g'] * cos(degree)
  }
  sistema['C2'] = {
    'm': 0
  }
  sistema['a'] = None

  while sistema['a'] == None or sistema['a'] <= 0:
    sistema['C2']['mg'] = sistema['C2']['m'] * sistema['g']
    print(-sin(degree), sistema['uk'] * cos(degree))
    sistema['a'] = sistema['C2']['mg'] - (sistema['C1']['mg'] * (-sin(degree) + sistema['uk'] * cos(degree)))
    sistema['a'] /= sistema['C2']['m'] + sistema['C1']['m']
    

    sistema['C2']['m'] += 0.5


print(calcular_movimiento(55,0.15,6))

def calcular_equilibrio(m1:float, m2:float, Fr:float) -> float:
  """
  Calcula el valor del angulo en el plano inclinado.
  Para el cual se cumpla que con la m1, m2 y el coeficiente de friccion el sistema este en un punto de equilibrio.
  Si los valores otorgados no permiten un estado de equilibrio en un angulo comprendido entre 10 y 85 el resultado será -1.

  Parametros
  ----------
    m1 (float): La masa de m1
    m2 (float) :La masa de m2
    Fr (float) :El coeficiente de friccion de m1
  
  Retorna
  -------
    (float) :El angulo de inclinacion para el cual hay un punto de equilibrio en el sistema o -1 si este no se cumple
  """
  pass

