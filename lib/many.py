class Parent:

    all = []

    def __init__(self, name, children=None):
        self.name = name
        self._children = []
        if children:
            for child in children:
                self.add_child(child)
        Parent.all.append(self)

    def children(self):
        return self._children

    def add_child(self, child):
        if isinstance(child, Child):
            self._children.append(child)
        else:
            raise ValueError("Child must be an instance of the Child class.")

class Child:

    def __init__(self, name):
        self.name = name

    def parents(self):
        return [parent for parent in Parent.all if self in parent.children()]

    def add_parent(self, parent):
        if isinstance(parent, Parent):
            parent.add_child(self)
        else:
            raise ValueError("Parent must be an instance of the Parent class.")


parent1 = Parent('Nick')
parent2 = Parent('Megan')
child1 = Child('Steve')
child2 = Child('Liz')

parent1.add_child(child1)
parent2.add_child(child1)
child2.add_parent(parent1)
child2.add_parent(parent2)
[ print(c.name) for c in parent1.children()]
[ print(p.name) for p in child1.parents()]
