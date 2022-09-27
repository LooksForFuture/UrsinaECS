from ursina import Entity

class ECSWorld:
    pass

class ECStity(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.components = []
        self.ecs_world:ECSWorld = None
    
    def add_component(self, component):
        self.components.append(component)
    
    def add_components(self, *components):
        for component in components:
            self.components.append(component)
    
    def get_component(self, ComponentType):
        for component in self.components:
            if type(component) == ComponentType:
                return component
        
        return None
    
    def remove_component(self, ComponentType):
        for x in range(len(self.components)):
            if type(self.components[x]) == ComponentType:
                self.components.pop(x)
                return 1
        
        return 0

class System:
    def update(self, ecs_world:ECSWorld):
        pass

class ECSWorld:
    def __init__(self):
        self.entities = []
        self.systems = []
    
    def add_entity(self, *args, **kwargs) -> ECStity:
        e:ECStity = ECStity(*args, **kwargs)
        e.ecs_world = self
        self.entities.append(e)
        return e
    
    def remove_entity(self, e:ECStity):
        self.entities.remove(e)
    
    def add_system(self, system:System):
        self.systems.append(system)
    
    def update(self):
        for s in self.systems:
            s.update(self)
    
    def each(self, *ComponentTypes):
        for e in self.entities:
            validated = 1
            out = []
            for t in ComponentTypes:
                c = e.get_component(t)
                if c:
                    out.append(c)
                else:
                    validated = 0
                    break
            
            if validated:
                yield e, out
