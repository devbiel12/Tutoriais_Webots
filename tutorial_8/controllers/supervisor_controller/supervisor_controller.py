from controller import Supervisor

TIME_STEP = 32

robot = Supervisor()  # cria a instância do Supervisor

# Referências do BB-8
bb8_node = robot.getFromDef('BB-8')
translation_field = bb8_node.getField('translation')

# Referência do campo children da raiz (para inserir nós)
root_node = robot.getRoot()
children_field = root_node.getField('children')

# Cria a bola e pega as referências dela
children_field.importMFNodeFromString(-1, 'DEF BALL Ball { translation 0 1 1 }')
ball_node = robot.getFromDef('BALL')
color_field = ball_node.getField('color')

i = 0
while robot.step(TIME_STEP) != -1:
  if i == 0:
    new_value = [2.5, 0, 0]
    translation_field.setSFVec3f(new_value)

  if i == 10:
    bb8_node.remove()

  if i == 20:
    children_field.importMFNodeFromString(-1, 'Nao { translation 2.5 0 0.334 }')

  # Acompanha a posição da bola
  position = ball_node.getPosition()
  print('Ball position: %f %f %f' % (position[0], position[1], position[2]))

  # Muda a cor quando a bola chega perto do chão
  if position[2] < 0.2:
    red_color = [1, 0, 0]
    color_field.setSFColor(red_color)

  i += 1