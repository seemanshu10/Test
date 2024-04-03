import maya.cmds as mc

class CtrlShape(object):
    def __init__(self, name):
        self.name = name

    def create(self):
        raise NotImplementedError("Subclasses must implement create()")

class CircleCtrl(CtrlShape):
    def create(self):
        ctrl = mc.circle(n=self.name, d=1, nr=(0, 1, 0), r=1, sw=360, s=15, ch=1)[0]
        return ctrl

class Cones(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(0.5, -1, 0.866025), (-0.5, -1, 0.866025), (0, 1, 0), (0.5, -1, 0.866025), (1, -1, 0), (0, 1, 0), (0.5, -1, -0.866025), (1, -1, 0), (0, 1, 0), (-0.5, -1, -0.866026), (0.5, -1, -0.866025), (0, 1, 0), (-1, -1, -1.5885e-007), (-0.5, -1, -0.866026), (0, 1, 0), (-0.5, -1, 0.866025), (-1, -1, -1.5885e-007)])
        return ctrl

class Square(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(1, 0, -1), (-1, 0, -1), (-1, 0, 1), (1, 0, 1), (1, 0, -1)])
        return ctrl

class Box(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(1, 1, -1), (1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, 1)])
        return ctrl

class Arrows(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(-1, 0, -3), (-2, 0, -3), (0, 0, -5), (2, 0, -3), (1, 0, -3), (1, 0, -1), (3, 0, -1), (3, 0, -2), (5, 0, 0), (3, 0, 2), (3, 0, 1), (1, 0, 1), (1, 0, 3), (2, 0, 3), (0, 0, 5), (-2, 0, 3), (-1, 0, 3), (-1, 0, 1), (-3, 0, 1), (-3, 0, 2), (-5, 0, 0), (-3, 0, -2), (-3, 0, -1), (-1, 0, -1), (-1, 0, -3)])
        return ctrl

class Triangle(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(-1, 0, 0), (0, 0, 1), (0, 0, -1), (-1, 0, 0)])
        return ctrl

class Dumbell(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(-1.207536, 0, 0.0254483), (-1.123549, -0.202763, 0.0254483), (-0.920786, -0.28675, 0.0254483), (-0.718023, -0.202763, 0.0254483), (-0.718023, -0.202763, 0.0254483), (-0.63504, -0.00242492, 0.0254483), (0.634091, 0, 0.0254483), (0.718023, -0.202763, 0.0254483), (0.920786, -0.28675, 0.0254483), (1.123549, -0.202763, 0.0254483), (1.207536, 0, 0.0254483), (1.123549, 0.202763, 0.0254483), (0.920786, 0.28675, 0.0254483), (0.718023, 0.202763, 0.0254483), (0.634091, 0, 0.0254483), (-0.63504, -0.00242492, 0.0254483), (-0.718023, 0.202763, 0.0254483), (-0.920786, 0.28675, 0.0254483), (-1.123549, 0.202763, 0.0254483), (-1.207536, 0, 0.0254483)])
        return ctrl

class ArrowOnBall(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(0, 0.35, -1.001567), (-0.336638, 0.677886, -0.751175), (-0.0959835, 0.677886, -0.751175), (-0.0959835, 0.850458, -0.500783), (-0.0959835, 0.954001, -0.0987656), (-0.500783, 0.850458, -0.0987656), (-0.751175, 0.677886, -0.0987656), (-0.751175, 0.677886, -0.336638), (-1.001567, 0.35, 0), (-0.751175, 0.677886, 0.336638), (-0.751175, 0.677886, 0.0987656), (-0.500783, 0.850458, 0.0987656), (-0.0959835, 0.954001, 0.0987656), (-0.0959835, 0.850458, 0.500783), (-0.0959835, 0.677886, 0.751175), (-0.336638, 0.677886, 0.751175), (0, 0.35, 1.001567), (0.336638, 0.677886, 0.751175), (0.0959835, 0.677886, 0.751175), (0.0959835, 0.850458, 0.500783), (0.0959835, 0.954001, 0.0987656), (0.500783, 0.850458, 0.0987656), (0.751175, 0.677886, 0.0987656), (0.751175, 0.677886, 0.336638), (1.001567, 0.35, 0), (0.751175, 0.677886, -0.336638), (0.751175, 0.677886, -0.0987656), (0.500783, 0.850458, -0.0987656), (0.0959835, 0.954001, -0.0987656), (0.0959835, 0.850458, -0.500783), (0.0959835, 0.677886, -0.751175), (0.336638, 0.677886, -0.751175), (0, 0.35, -1.001567)])
        return ctrl

class Pyramid(CtrlShape):
    def create(self):
        ctrl = mc.curve(n=self.name, d=1, p=[(0, 2, 0), (1, 0, -1), (-1, 0, -1), (0, 2, 0), (-1, 0, 1), (1, 0, 1), (0, 2, 0), (1, 0, -1), (1, 0, 1), (-1, 0, 1), (-1, 0, -1)])
        return ctrl

class CtrlShapeUtils(object):
    def __init__(self):
        pass

    def create_ctrl(self, func_name, name=None):
        if name is None and mc.ls(selection=True):
            name = mc.ls(selection=True)[0] + "_Ctrl"

        shape_classes = {
            'circle': CircleCtrl,
            'cones': Cones,
            'square': Square,
            'box': Box,
            'arrows': Arrows,
            'triangle': Triangle,
            'dumbell': Dumbell,
            'arrowOnBall': ArrowOnBall,
            'pyramid': Pyramid
        }

        ctrl_class = shape_classes.get(func_name)
        if ctrl_class:
            ctrl_instance = ctrl_class(name)
            return ctrl_instance.create()
        else:
            print("Shape not recognized. Please add a correct shape from the list.")
            return None

# Example usage:
# ctrl_utils = CtrlShapeUtils()
# ctrl_utils.create_ctrl('circle')
