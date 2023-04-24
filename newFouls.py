import random
from simClasses import Ball
from bridge import (Entity, Actuator)
from action import Robot2Position, SendRobotPosition

# % ID of each foul

"""
FREE_KICK = 0
PENALTY_KICK = 1
GOAL_KICK = 2
FREE_BALL = 3
KICKOFF = 4 (Testando para o kickoff)
STOP = 5
GAME_ON = 6
HALT = 7
"""

'''
Input: Replacer client, data from referee, team color (True = Yellow, False = Blue) and foul ID.
Description: Our robots are replaced in diferents places of the field according to the fouls
(using position on X, Y, angle and index of each robot).
Output: Entity objects.
'''

def automatic_replacement(ref_data, mray, op, dp, robot0, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2):
    ball = Ball()
    #Objetos já foram criados anteriormente enão basta passar os parametros do json
    #para esses objetos criados
    if not mray:
        if ref_data["foul"] == 1: # Penalty kick
            #1 está indo a posição, falta verificação de posição correta
            if ref_data["yellow"]:  # Defensive
                if dp == "direct":
                    lista_r_0 = SendRobotPosition(mray, ref_data, 0, dp)
                elif dp == "spin" or dp == "spin-v":
                    lista_r_0 = SendRobotPosition(mray, ref_data, 0, 'spin_spin-v')
                lista_r_1 = SendRobotPosition(mray, ref_data, 1, 'spin_spin-v') # Center back
                lista_r_2 = SendRobotPosition(mray, ref_data, 2, 'spin_spin-v') # Striker
            
            else:  # Ofensive
                #1 está indo a posição, falta verificação de posição correta
                lista_r_0 = SendRobotPosition(mray, ref_data, 0, 'direct_switch')
                if op == "direct" or op == "switch":
                    lista_r_1 = SendRobotPosition(mray, ref_data, 1, 'direct_switch')
                    lista_r_2 = SendRobotPosition(mray, ref_data, 2, 'direct_switch')
                elif op == "spin":
                    r = random.uniform(0, 1) # Generate random number between 0 and 1
                    if r < 0.001: # 0.5 is default value
                        lista_r_1 = SendRobotPosition(mray, ref_data, 1, op, 'if')
                        lista_r_2 = SendRobotPosition(mray, ref_data, 2, op, 'if')
                    else:
                        lista_r_1 = SendRobotPosition(mray, ref_data, 1, op, 'else')
                        lista_r_2 = SendRobotPosition(mray, ref_data, 2, op, 'else')
            #Replace each robot            
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0, lista_r_1, lista_r_2)

        # TODO FOULS: Revisar as posições futuramente do goalKick
        elif ref_data["foul"] == 2:
            if not ref_data["yellow"]:
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            else:
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                if ball.yPos < 65:
                    lista_r_2 = SendRobotPosition(mray, ref_data, 2, 'ball_yPos')
            #Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0, lista_r_1, lista_r_2)

        elif ref_data["foul"] == 3: # Freeball
            if ref_data["quad"] == 1: # First quadrant
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            elif ref_data["quad"] == 2: # Second quadrant
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            elif ref_data["quad"] == 3: # Third quadrant
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            elif ref_data["quad"] == 4: # Fourth quadrant
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            #Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0, lista_r_1, lista_r_2)
            
        if ref_data["foul"] == 4: #Kickoff
            #1 está indo a posição, falta verificação de posição correta
            if ref_data["yellow"]: # Defensive
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)        
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)        
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)

            #1 está indo a posição, falta verificação de posição correta
            else: # Ofensive
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)        
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)        
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            # Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0, lista_r_1, lista_r_2)
            
    if mray:    
        if ref_data["foul"] == 4: #Kickoff
            #1 está indo a posição, falta verificação de posição correta
            if not ref_data["yellow"]: # Defensive
                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            else: # Ofensive
                # Kickoff normal - Transformar em estrategia selecionavel?
                #entidade0 = Entity(x=152, y=65, a=180, index=0)
                #entidade1 = Entity(x=93, y=88, a=210, index=1)
                #entidade2 = Entity(x=95, y=58, a=155, index=2)

                lista_r_0 = SendRobotPosition(mray, ref_data, 0)
                lista_r_1 = SendRobotPosition(mray, ref_data, 1)
                lista_r_2 = SendRobotPosition(mray, ref_data, 2)
            # Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0, lista_r_1, lista_r_2)

    return

