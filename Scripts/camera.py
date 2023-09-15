from PPlay.sprite import Sprite


class Camera:
    
    def __init__(self, bkGround, focus):
        self.bkGround = bkGround
        self.objects =[]
        self.focus = focus
        self.objects.append(self.focus)
        self.leftDaedZone = 350
        self.rightDaedZone = 450

    def updade(self):
        if self.focus.get_x() >= self.rightDaedZone:
            self.bkGround.move_x(self.rightDaedZone - self.focus.get_x()) 
            self.focus.set_x(self.rightDaedZone)
        if self.focus.get_x() <= self.leftDaedZone:
            self.bkGround.move_x(self.leftDaedZone - self.focus.get_x()) 
            self.focus.set_x(self.leftDaedZone)
    
    
    def draw(self):
        self.bkGround.draw()
        for i in self.objects:
            i.draw()





    


    