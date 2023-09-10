from panda3d.core import Point3, Vec3
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)

        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        self.camera.setPos(0, -30, 10)  
        self.camera.lookAt(Point3(0, 0, 0))

        self.weapon = self.loader.loadModel("models/misc/sphere")
        self.weapon.reparentTo(self.camera)  
        self.weapon.setScale(0.5)
        self.weapon.setPos(0, 2, -2) 

        self.accept("space", self.shoot)

    def shoot(self):
        # Create a bullet
        bullet = self.loader.loadModel("models/misc/sphere")
        bullet.reparentTo(self.render)
        bullet.setScale(0.2)
        bullet.setPos(self.weapon.getPos(self.render)) 

        def move_bullet(task):
            if bullet.getPos().getY() > 50:  
                bullet.removeNode()  
                return Task.done
            bullet.setPos(bullet.getPos() + Vec3(0, 1, 0))  
            return Task.cont

        self.taskMgr.add(move_bullet, "move_bullet_task")

app = MyApp()
app.run()
