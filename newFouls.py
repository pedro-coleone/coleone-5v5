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
                    lista_r_0 = SendRobotPosition(mray, 'penalty_kick', 'defensive', dp, None, 0)
                elif dp == "spin" or dp == "spin-v":
                    lista_r_0 = SendRobotPosition(mray, 'penalty_kick', 'defensive', 'spin_spin-v', None, 0)
                lista_r_1 = SendRobotPosition(mray, 'penalty_kick', 'defensive', 'spin_spin-v', None, 1) # Center back
                lista_r_2 = SendRobotPosition(mray, 'penalty_kick', 'defensive', 'spin_spin-v', None, 2) # Striker
            
            else:  # Ofensive
                #1 está indo a posição, falta verificação de posição correta
                lista_r_0 = SendRobotPosition(mray, 'penalty_kick', 'offensive', 'direct_switch', None, 0)
                if op == "direct" or op == "switch":
                    lista_r_1 = SendRobotPosition(mray, 'penalty_kick', 'offensive', 'direct_switch', None, 1)
                    lista_r_2 = SendRobotPosition(mray, 'penalty_kick', 'offensive', 'direct_switch', None, 2)
                elif op == "spin":
                    r = random.uniform(0, 1) # Generate random number between 0 and 1
                    if r < 0.001: # 0.5 is default value
                        lista_r_1 = SendRobotPosition(mray, 'penalty_kick', 'offensive', op, 'if', 1)
                        lista_r_2 = SendRobotPosition(mray, 'penalty_kick', 'offensive', op, 'if', 2)
                    else:
                        lista_r_1 = SendRobotPosition(mray, 'penalty_kick', 'offensive', op, 'else', 1)
                        lista_r_2 = SendRobotPosition(mray, 'penalty_kick', 'offensive', op, 'else', 2)
            #Replace each robot            
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0[0], lista_r_0[1], lista_r_0[2])
            Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_1[0], lista_r_1[1], lista_r_1[2])
            Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_2[0], lista_r_2[1], lista_r_2[2])

        # TODO FOULS: Revisar as posições futuramente do goalKick
        elif ref_data["foul"] == 2:
            if not ref_data["yellow"]:
                lista_r_0 = SendRobotPosition(mray, 'goal_kick', 'if', None, None, 0)
                lista_r_1 = SendRobotPosition(mray, 'goal_kick', 'if', None, None, 1)
                lista_r_2 = SendRobotPosition(mray, 'goal_kick', 'if', None, None, 2)
            else:
                lista_r_0 = SendRobotPosition(mray, 'goal_kick', 'else', None, None, 0)
                lista_r_1 = SendRobotPosition(mray, 'goal_kick', 'else', None, None, 1)
                if ball.yPos < 65:
                    lista_r_2 = SendRobotPosition(mray, 'goal_kick', 'else', 'ball_yPos', None, 2)
            #Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0[0], lista_r_0[1], lista_r_0[2])
            Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_1[0], lista_r_1[1], lista_r_1[2])
            Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_2[0], lista_r_2[1], lista_r_2[2])

        elif ref_data["foul"] == 3: # Freeball
            if ref_data["quad"] == 1: # First quadrant
                lista_r_0 = SendRobotPosition(mray, 'free_ball', 'quad1', None, None, 0)
                lista_r_1 = SendRobotPosition(mray, 'free_ball', 'quad1', None, None, 1)
                lista_r_2 = SendRobotPosition(mray, 'free_ball', 'quad1', None, None, 2)
            elif ref_data["quad"] == 2: # Second quadrant
                lista_r_0 = SendRobotPosition(mray, 'free_ball', 'quad2', None, None, 0)
                lista_r_1 = SendRobotPosition(mray, 'free_ball', 'quad2', None, None, 1)
                lista_r_2 = SendRobotPosition(mray, 'free_ball', 'quad2', None, None, 2)
            elif ref_data["quad"] == 3: # Third quadrant
                lista_r_0 = SendRobotPosition(mray, 'free_ball', 'quad3', None, None, 0)
                lista_r_1 = SendRobotPosition(mray, 'free_ball', 'quad3', None, None, 1)
                lista_r_2 = SendRobotPosition(mray, 'free_ball', 'quad3', None, None, 2)
            elif ref_data["quad"] == 4: # Fourth quadrant
                lista_r_0 = SendRobotPosition(mray, 'free_ball', 'quad4', None, None, 0)
                lista_r_1 = SendRobotPosition(mray, 'free_ball', 'quad4', None, None, 1)
                lista_r_2 = SendRobotPosition(mray, 'free_ball', 'quad4', None, None, 2)
            #Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0[0], lista_r_0[1], lista_r_0[2])
            Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_1[0], lista_r_1[1], lista_r_1[2])
            Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_2[0], lista_r_2[1], lista_r_2[2])

        if ref_data["foul"] == 4: #Kickoff
            #1 está indo a posição, falta verificação de posição correta
            if ref_data["yellow"]: # Defensive
                lista_r_0 = SendRobotPosition(mray, 'kickoff', 'defensive', None, None, 0)        
                lista_r_1 = SendRobotPosition(mray, 'kickoff', 'defensive', None, None, 1)        
                lista_r_2 = SendRobotPosition(mray, 'kickoff', 'defensive', None, None, 2)
                print(lista_r_0)
            #1 está indo a posição, falta verificação de posição correta
            else: # Ofensive
                lista_r_0 = SendRobotPosition(mray, 'kickoff', 'offensive', None, None, 0)        
                lista_r_1 = SendRobotPosition(mray, 'kickoff', 'offensive', None, None, 1)        
                lista_r_2 = SendRobotPosition(mray, 'kickoff', 'offensive', None, None, 2)
            # Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0[0], lista_r_0[1], lista_r_0[2])
            Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_1[0], lista_r_1[1], lista_r_1[2])
            Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_2[0], lista_r_2[1], lista_r_2[2])
    if mray:    
        if ref_data["foul"] == 4: #Kickoff
            #1 está indo a posição, falta verificação de posição correta
            if not ref_data["yellow"]: # Defensive
                lista_r_0 = SendRobotPosition(mray, 'kickoff', 'defensive', None, None, 0)
                lista_r_1 = SendRobotPosition(mray, 'kickoff', 'defensive', None, None, 1)
                lista_r_2 = SendRobotPosition(mray, 'kickoff', 'defensive', None, None, 2)
            else: # Ofensive
                # Kickoff normal - Transformar em estrategia selecionavel?
                #entidade0 = Entity(x=152, y=65, a=180, index=0)
                #entidade1 = Entity(x=93, y=88, a=210, index=1)
                #entidade2 = Entity(x=95, y=58, a=155, index=2)

                lista_r_0 = SendRobotPosition(mray, 'kickoff', 'offensive', None, 0)
                lista_r_1 = SendRobotPosition(mray, 'kickoff', 'offensive', None, 1)
                lista_r_2 = SendRobotPosition(mray, 'kickoff', 'offensive', None, 2)
            # Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0[0], lista_r_0[1], lista_r_0[2])
            Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_1[0], lista_r_1[1], lista_r_1[2])
            Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_2[0], lista_r_2[1], lista_r_2[2])

    return

