from action import defenderSpin, follower, follower_2, leaderSelector
from math import sqrt

def attack_3_leaders(ball, robot0, robot1, robot2, mray, enemy_robots):
    """Input: Ball, 3 robot attackers, mray flag and list of enemy robots.
    Description: All 3 attackers act like leaders, trying to shoot ball to the goal.
    Output: None."""
    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])

def attack_2_leaders(ball, robot0, robot1, robot2, mray, enemy_robots):
    """Input: Ball, 3 robot attackers, mray flag and list of enemy robots.
    Description: 2 robots act like leaders and the other follow the leader that's closest to the ball.
    Output: None."""
    select_2_leaders(robot0, robot1, robot2, ball)

    # Leaders  -> robot 2 and robot 1
    # Follower -> robot 0
    if robot2.isLeader and robot1.isLeader:
        robots_leaders = [robot2, robot1]
        if not mray:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 0 is close enough to the tha ball, it starts to do the defender spin
            if robot0.dist(ball) < 40:
                if (robot2.xPos > 195 and 100 > robot2.yPos > 40) and (robot1.xPos > 195 and 100 > robot1.yPos > 40):
                    follower_2(robot0, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot0, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

        # Same idea but for the other side of de field
        else:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=mray, friend1=robot1, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot1, ball, left_side=mray, friend1=robot2, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])

            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot0.dist(ball) < 40:
                if (robot2.xPos < 35 and 100 > robot2.yPos > 40) and (robot1.xPos < 35 and 100 > robot1.yPos > 40):
                    follower_2(robot0, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot0, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                
    # Leaders  -> robot 2 and robot 0
    # Follower -> robot 1
    elif robot2.isLeader and robot0.isLeader:
        robots_leaders = [robot2, robot0]
        if not mray:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot2, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot1.dist(ball) < 40:
                if (robot2.xPos > 195 and 100 > robot2.yPos > 40) and (robot0.xPos > 195 and 100 > robot0.yPos > 40):
                    follower_2(robot1, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot1, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
        else:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot2, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot2, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot1.dist(ball) < 40:
                if (robot2.xPos < 35 and 100 > robot2.yPos > 40) and (robot0.xPos < 35 and 100 > robot0.yPos > 40):
                    follower_2(robot1, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot1, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                
    # Leaders  -> robot 1 and robot 0
    # Follower -> robot 2
    else:
        robots_leaders = [robot1, robot0]
        if not mray:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot1, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot2.dist(ball) < 40:
                if (robot1.xPos > 195 and 100 > robot1.yPos > 40) and (robot0.xPos > 195 and 100 > robot0.yPos > 40):
                    follower_2(robot2, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot2, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
        else:
            # The robots 2 and 1 do the defender spin, and the robot 0 follow one of them
            defenderSpin(robot1, ball, left_side=not robot1.teamYellow, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            defenderSpin(robot0, ball, left_side=not robot1.teamYellow, friend1=robot1, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            
            # If robot 1 is close enough to the tha ball, it starts to do the defender spin
            if robot2.dist(ball) < 40:
                if (robot1.xPos < 35 and 100 > robot1.yPos > 40) and (robot0.xPos < 35 and 100 > robot0.yPos > 40):
                    follower_2(robot2, robots_leaders, ball,
                               enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower_2(robot2, robots_leaders, ball,
                           enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

    return

def attack_1_leaders(ball, robot0, robot1, robot2, mray, enemy_robots):
    """Input: Ball, 3 robot attackers, mray flag and list of enemy robots.
    Description: 1 robot acts like leaders and the other 2 follows the leader.
    Output: None."""
    leaderSelector(robot1, robot2, ball)

    if robot2.isLeader:
        if not mray:
            defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot0,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            '''
            If is the robot 1 is close enough to the tha ball, starts to do the defender spin
            '''
            if robot1.dist(ball) < 40:
                if robot2.xPos > 195 and (100 > robot2.yPos > 40):
                    follower(robot1, robot2, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot2, ball, robot0,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
            
            if robot0.dist(ball) < 40:
                if robot2.xPos > 195 and (100 > robot2.yPos > 40):
                    follower(robot0, robot2, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot1, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot2, ball, robot0,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

        #Same Idea but for the other side of de field
        else:
            defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot1,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot1.dist(ball) < 40:
                if robot2.xPos < 35 and (100 > robot2.yPos > 40):
                    follower(robot1, robot2, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot2, ball, robot0,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

            if robot0.dist(ball) < 40:
                if robot2.xPos < 35 and (100 > robot2.yPos > 40):
                    follower(robot0, robot2, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot1, friend2=robot2,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot2, ball, robot0,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

    elif robot1.isLeader:
        if not mray:
            defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot0.dist(ball) < 40:
                if robot1.xPos > 195 and (100 > robot1.yPos > 40):
                    follower(robot0, robot1, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot1, ball, robot2,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

            if robot2.dist(ball) < 40:
                if robot1.xPos > 195 and (100 > robot1.yPos > 40):
                    follower(robot2, robot1, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot1, ball, robot0,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
            
        else:
            defenderSpin(robot1, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot0.dist(ball) < 40:
                if robot1.xPos < 35 and (100 > robot1.yPos > 40):
                    follower(robot0, robot1, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot0, robot1, ball, robot2,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
            
            if robot2.dist(ball) < 40:
                if robot1.xPos < 35 and (100 > robot1.yPos > 40):
                    follower(robot2, robot1, ball, robot0,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot0, friend2=robot1,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot1, ball, robot0,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
    
    else:
        if not mray:
            defenderSpin(robot0, ball, left_side=not mray, friend1=robot1, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot1.dist(ball) < 40:
                if robot0.xPos > 195 and (100 > robot0.yPos > 40):
                    follower(robot1, robot0, ball, robot2,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot1, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot0, ball, robot2,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

            if robot2.dist(ball) < 40:
                if robot0.xPos > 195 and (100 > robot0.yPos > 40):
                    follower(robot2, robot0, ball, robot1,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot0, ball, robot1,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
            
        else:
            defenderSpin(robot0, ball, left_side=not mray, friend1=robot0, friend2=robot2,
                         enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            if robot1.dist(ball) < 40:
                if robot0.xPos < 35 and (100 > robot0.yPos > 40):
                    follower(robot1, robot0, ball, robot2,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot0, ball, left_side=not mray, friend1=robot2, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot1, robot0, ball, robot2,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
            
            if robot2.dist(ball) < 40:
                if robot0.xPos < 35 and (100 > robot0.yPos > 40):
                    follower(robot2, robot0, ball, robot1,
                             enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])
                else:
                    defenderSpin(robot2, ball, left_side=not mray, friend1=robot1, friend2=robot0,
                                 enemy1=enemy_robots[0], enemy2=enemy_robots[1], enemy3=enemy_robots[2], enemy4=enemy_robots[3], enemy5=enemy_robots[4])
            else:
                follower(robot2, robot0, ball, robot1,
                         enemy_robots[0], enemy_robots[1], enemy_robots[2], enemy_robots[3], enemy_robots[4])

def select_1_leader(robot1, robot2, robot3, ball):

    '''
    Calculate the distan of both robots to the ball
    '''
    dist1 = sqrt((robot1.xPos - ball.xPos) ** 2 + (robot1.yPos - ball.yPos) ** 2)
    dist2 = sqrt((robot2.xPos - ball.xPos) ** 2 + (robot2.yPos - ball.yPos) ** 2)
    dist3 = sqrt((robot3.xPos - ball.xPos) ** 2 + (robot3.yPos - ball.yPos) ** 2)

    if dist3 < dist2 and dist3 < dist1: # Strategy if robot 3 is closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot3.isLeader = True
            robot1.isLeader = False
            robot2.isLeader = False
            robot3.holdLeader += 1

        elif robot3.isLeader:
            robot3.holdLeader += 1

        elif robot1.holdLeader > 60:
            robot3.isLeader = True
            robot1.isLeader = False
            robot1.holdLeader = 0
            robot3.holdLeader += 1
        
        elif robot2.holdLeader > 60:
            robot3.isLeader = True
            robot2.isLeader = False
            robot2.holdLeader = 0
            robot3.holdLeader += 1

        elif robot1.isLeader:
            robot1.holdLeader += 1

        else:
            robot2.holdLeader += 1

    # Same idea, but robot 2 is closer to the ball
    elif dist2 < dist1 and dist2 < dist3: # Strategy if robot 2 is closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot2.isLeader = True
            robot1.isLeader = False
            robot3.isLeader = False
            robot2.holdLeader += 1

        elif robot2.isLeader:
            robot2.holdLeader += 1

        elif robot1.holdLeader > 60:
            robot2.isLeader = True
            robot1.isLeader = False
            robot1.holdLeader = 0
            robot2.holdLeader += 1
        
        elif robot3.holdLeader > 60:
            robot2.isLeader = True
            robot3.isLeader = False
            robot3.holdLeader = 0
            robot2.holdLeader += 1

        elif robot1.isLeader:
            robot1.holdLeader += 1

        else:
            robot3.holdLeader += 1

    # Same idea, but robot 1 is closer to the ball
    else:
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot1.isLeader = True
            robot2.isLeader = False
            robot3.isLeader = False
            robot1.holdLeader += 1

        elif robot1.isLeader:
            robot1.holdLeader += 1

        elif robot2.holdLeader > 60:
            robot1.isLeader = True
            robot2.isLeader = False
            robot1.holdLeader += 1
            robot2.holdLeader = 0
        
        elif robot3.holdLeader > 60:
            robot1.isLeader = True
            robot3.isLeader = False
            robot1.holdLeader += 1
            robot2.holdLeader = 0

        elif robot2.isLeader:
            robot2.holdLeader += 1

        else:
            robot3.holdLeader += 1

def select_2_leaders(robot1, robot2, robot3, ball): # ok

    '''
    Calculate the distan of both robots to the ball
    '''
    dist1 = sqrt((robot1.xPos - ball.xPos) ** 2 + (robot1.yPos - ball.yPos) ** 2)
    dist2 = sqrt((robot2.xPos - ball.xPos) ** 2 + (robot2.yPos - ball.yPos) ** 2)
    dist3 = sqrt((robot3.xPos - ball.xPos) ** 2 + (robot3.yPos - ball.yPos) ** 2)

    if dist3 < dist1 and dist2 < dist1: # Strategy if robot 3 and 2 are closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot3.isLeader = True
            robot2.isLeader = True
            robot1.isLeader = False
            robot3.holdLeader += 1
            robot2.holdLeader += 1

        elif robot3.isLeader and robot2.isLeader:
            robot3.holdLeader += 1
            robot2.holdLeader += 1

        elif robot1.holdLeader > 60:
            robot3.isLeader = True
            robot2.isLeader = True
            robot1.isLeader = False
            robot1.holdLeader = 0
            robot3.holdLeader += 1
            robot2.holdLeader += 1

        else:
            robot1.holdLeader += 1

            if robot2.holdLeader > 60:                
                robot3.isLeader = True
                robot2.isLeader = False                
                robot2.holdLeader = 0
                robot3.holdLeader += 1

            elif robot3.holdLeader > 60:
                robot2.isLeader = True
                robot3.isLeader = False                
                robot3.holdLeader = 0
                robot2.holdLeader += 1

            elif robot2.isLeader:
                robot2.holdLeader += 1
            
            else:
                robot3.holdLeader += 1

    # Same idea, but robots 3 and 1 are closer to the ball
    elif dist3 < dist2 and dist1 < dist2: # Strategy if robots 3 and 1 are closer to the ball
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot3.isLeader = True
            robot1.isLeader = True
            robot2.isLeader = False
            robot3.holdLeader += 1
            robot1.holdLeader += 1

        elif robot3.isLeader and robot1.isLeader:
            robot3.holdLeader += 1
            robot1.holdLeader += 1

        elif robot2.holdLeader > 60:
            robot3.isLeader = True
            robot1.isLeader = True
            robot2.isLeader = False
            robot2.holdLeader = 0
            robot1.holdLeader += 1
            robot3.holdLeader += 1

        else:
            robot2.holdLeader += 1

            if robot1.holdLeader > 60:                
                robot3.isLeader = True
                robot1.isLeader = False
                robot1.holdLeader = 0
                robot3.holdLeader += 1

            elif robot3.holdLeader > 60:
                robot1.isLeader = True
                robot3.isLeader = False                
                robot3.holdLeader = 0
                robot1.holdLeader += 1

            elif robot1.isLeader:
                robot1.holdLeader += 1
            
            else:
                robot3.holdLeader += 1

    # Same idea, but robots 1 and 2 are closer to the ball
    else:
        if robot1.isLeader is None and robot2.isLeader is None and robot3.isLeader is None:
            robot1.isLeader = True
            robot2.isLeader = True
            robot3.isLeader = False
            robot1.holdLeader += 1
            robot2.holdLeader += 1

        elif robot1.isLeader and robot2.isLeader:
            robot1.holdLeader += 1
            robot2.holdLeader += 1

        elif robot3.holdLeader > 60:
            robot1.isLeader = True
            robot2.isLeader = True
            robot3.isLeader = False
            robot3.holdLeader = 0
            robot2.holdLeader += 1
            robot1.holdLeader += 1

        else:
            robot3.holdLeader += 1

            if robot1.holdLeader > 60:                
                robot2.isLeader = True
                robot1.isLeader = False
                robot1.holdLeader = 0
                robot2.holdLeader += 1

            elif robot2.holdLeader > 60:
                robot1.isLeader = True
                robot2.isLeader = False                
                robot2.holdLeader = 0
                robot1.holdLeader += 1

            elif robot1.isLeader:
                robot1.holdLeader += 1
            
            else:
                robot2.holdLeader += 1
    
    # print("------------------------------")
    # print(f"Robot 3 is {'' if robot3.isLeader else 'not '} a leader.")
    # print(f"Robot 3 hold for {robot3.holdLeader} seconds.")
    # print(f"Robot 2 is {'' if robot2.isLeader else 'not '} a leader.")
    # print(f"Robot 2 hold for {robot2.holdLeader} seconds.")
    # print(f"Robot 1 is {'' if robot1.isLeader else 'not '} a leader.")
    # print(f"Robot 1 hold for {robot1.holdLeader} seconds.")
    # print("------------------------------")

def select_3_leaders(robot1, robot2, robot3, ball):
    robot1.isLeader = True
    robot2.isLeader = True
    robot3.isLeader = True