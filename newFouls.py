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
        if ref_data["foul"] == 4: #Kickoff
            if ref_data["yellow"]: # Defensive
                lista_r_0 = SendRobotPosition(mray, 'kickoff', 'defensive', 0)        
                lista_r_1 = SendRobotPosition(mray, 'kickoff', 'defensive', 1)        
                lista_r_2 = SendRobotPosition(mray, 'kickoff', 'defensive', 2)
                print(lista_r_0)
            else: # Ofensive
                lista_r_0 = SendRobotPosition(mray, 'kickoff', 'offensive', 0)        
                lista_r_1 = SendRobotPosition(mray, 'kickoff', 'offensive', 1)        
                lista_r_2 = SendRobotPosition(mray, 'kickoff', 'offensive', 2)
            # Replace each robot
            Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0[0], lista_r_0[1], lista_r_0[2])
            Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_1[0], lista_r_1[1], lista_r_1[2])
            Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_2[0], lista_r_2[1], lista_r_2[2])

    else:    
        if not ref_data["yellow"]: # Defensive
            lista_r_0 = SendRobotPosition(mray, 'kickoff', 'defensive', 0)
            lista_r_1 = SendRobotPosition(mray, 'kickoff', 'defensive', 1)
            lista_r_2 = SendRobotPosition(mray, 'kickoff', 'defensive', 2)
        else: # Ofensive
            # Kickoff normal - Transformar em estrategia selecionavel?
            #entidade0 = Entity(x=152, y=65, a=180, index=0)
            #entidade1 = Entity(x=93, y=88, a=210, index=1)
            #entidade2 = Entity(x=95, y=58, a=155, index=2)

            lista_r_0 = SendRobotPosition(mray, 'kickoff', 'offensive', 0)
            lista_r_1 = SendRobotPosition(mray, 'kickoff', 'offensive', 1)
            lista_r_2 = SendRobotPosition(mray, 'kickoff', 'offensive', 2)
        # Replace each robot
        Robot2Position(robot0, ball, robot1, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_0[0], lista_r_0[1], lista_r_0[2])
        Robot2Position(robot1, ball, robot0, robot2, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_1[0], lista_r_1[1], lista_r_1[2])
        Robot2Position(robot2, ball, robot0, robot1, robotEnemy0, robotEnemy1, robotEnemy2, lista_r_2[0], lista_r_2[1], lista_r_2[2])

    return

