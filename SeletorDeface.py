import numpy as np


def define_circle(targetPos: tuple, frenteRobo: tuple, costasRobo: tuple):
    temp = frenteRobo[0] * frenteRobo[0] + frenteRobo[1] * frenteRobo[1]
    bc = (targetPos[0] * targetPos[0] + targetPos[1] * targetPos[1] - temp) / 2
    cd = (temp - costasRobo[0] * costasRobo[0] - costasRobo[1] * costasRobo[1]) / 2
    det = (targetPos[0] - frenteRobo[0]) * (frenteRobo[1] - costasRobo[1]) - (frenteRobo[0] - costasRobo[0]) * (
                targetPos[1] - frenteRobo[1])

    if abs(det) < 1.0e-6:
        return (None, np.inf)

    # Center of circle
    cx = (bc * (frenteRobo[1] - costasRobo[1]) - cd * (targetPos[1] - frenteRobo[1])) / det
    cy = ((targetPos[0] - frenteRobo[0]) * cd - (frenteRobo[0] - costasRobo[0]) * bc) / det

    radius = np.sqrt((cx - targetPos[0]) ** 2 + (cy - targetPos[1]) ** 2)
    return ((cx, cy), radius)


def PontosFrenteCosta(robotPosition, angle):
    frente = (robotPosition[0] + 5 * np.cos(angle), robotPosition[1] + 5 * np.sin(angle))
    costas = (robotPosition[0] - 5 * np.cos(angle), robotPosition[1] - 5 * np.sin(angle))
    return frente, costas


# TODO: VER INFLUENCIA DA VELOCIDADE NA DESACELERAÇAO, COMO IMPACTA LEVAR EM CONTA
def sideDecider(RobotPos, angle, targetPos, robotIndex):
    pontos = PontosFrenteCosta(RobotPos, angle)
    frente = pontos[0]
    costas = pontos[1]
    center, radius = define_circle(targetPos, frente, costas) 

    print(center)

    if center is not None:
        theta_frente = np.arctan2(frente[1] - center[1], frente[0] - center[0])
        theta_target = np.arctan2(targetPos[1] - center[1], targetPos[0] - center[0])
        theta_costas = np.arctan2(costas[1] - center[1], costas[0] - center[0])
        
        difFrente = np.abs( np.rad2deg(theta_frente - theta_target))
        difCostas = np.abs( np.rad2deg(theta_costas - theta_target))

        if difFrente < difCostas:
            univector = 1
        else:
            univector = -1

        #print("theta_frente: ",np.rad2deg( theta_frente))
        #print("theta_target: ", np.rad2deg(theta_target))
        #print("theta_costas: ", np.rad2deg(theta_costas))
        #print("theta_frente - theta_target: ", np.rad2deg(theta_frente - theta_target))
        #print("theta_costas - theta_target: ", np.rad2deg(theta_costas - theta_target))

    else:
        # ABORDAGEM DA RETA:
        df = (frente[0] - targetPos[0])**2 + (frente[1] - targetPos[1])**2
        dc = (costas[0] - targetPos[0])**2 + (costas[1] - targetPos[1])**2
        if df < dc:
            # ir de frente
            univector = 1
            print('Univerctor : ', univector)
        else:
            # ir de costas
            univector = -1
            print('Univerctor : ', univector)
    if robotIndex == 1:
        print("\nposição: ", RobotPos)
        print("univector: ", univector)
    
    return univector


# (30, -27)
#sideDecider((50, 50), np.deg2rad(135), (25, 70), 1)
#sideDecider((50, 50), np.deg2rad(135), (50, 25), 2)

