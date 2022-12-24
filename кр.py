class Robot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, stroka):
        self.stroka = stroka
        for i in range(0, len(stroka)):
            if stroka[i] == 'n' and self.y <100:
                self.y +=1
            elif stroka[i] == 's' and self.y >0:
                self.y -= 1
            elif stroka[i] == 'e' and self.x <100:
                self.x += 1
            elif stroka[i] == 'w' and self.x >0:
                self.x -=1
            else:
                print('вышел за границу')
                break
        return self.x, self.y
robot = Robot(0,0)
print(robot.move('nene'))





