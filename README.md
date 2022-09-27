# UrsinaECS
UrsinaECS is a simple and easy to use ECS for ursina engine. It has been designed to be flexible and as fast as possible.<br />
An ECS is an alternative to the traditional OOP programming structure. Entities are the game objects and Components are classes which contain data and each entity can contain unlimitted components. Systems are classes which retreive entities with specific components from the ECS world.<br />

Here is a simple example:
```python
from dataclasses import dataclass
from UrsinaECS import *
from ursina import Ursina, curve, time

@dataclass
class Rotatable:
    duration:float = 1.0

class Movable:
    pass

class RotateSystem:
    def __init__(self):
        self.d = 1.0
        self.sleep = 1.0
    def update(self, world:ECSWorld):
        if self.d >= self.sleep:
            self.d = 0.0

            for e, components in world.each(Rotatable):
                e.animate('rotation_y', e.rotation_y+365, duration=components[0].duration, curve=curve.in_out_expo)
        
        else:
            self.d += time.dt

app = Ursina()
ecs_world = ECSWorld()

cube1 = ecs_world.add_entity(model='cube', texture = 'white_cube', position=(-2, 0, 0))
cube1.add_component(Rotatable(0.5))

cube2 = ecs_world.add_entity(model='cube', texture = 'white_cube', position=(+2, 0, 0))
cube2.add_components(Rotatable(1.0), Movable())

ecs_world.add_system(RotateSystem())

def update():
    ecs_world.update()

app.run()
```
ECS entity is a child class of Ursina Entity class which has a list of it's components. The class is called "ECStity". Each ECStity should be created using the world and not by the user. And the systems are independant classes which must inherit from System class of UrsinaECS and have an update function. whenever you call the update function of the ECSWorld, the world calls update function of all the systems which have been attached to it.<br />

<h3>Future plans</h3>
<ul>
  <li>Adding a scene class for scene management</li>
  <li>A 3D physics library with support of ECS</li>
</ul>
