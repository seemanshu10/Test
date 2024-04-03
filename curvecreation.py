import maya.cmds as cmds
import maya.mel as mm

class Ribbon(object):
    def __init__(self, name, mesh_name):
        self.name = name
        self.mesh_name = mesh_name

    def create(self):
        raise NotImplementedError("Subclasses must implement create()")

    def duplicate_mesh(self):
        return cmds.duplicate(self.mesh_name, n=self.name + '_dup')

    def blend_deformer(self, mesh):
        cmds.blendShape((mesh[0], self.mesh_name), foc=1, n='deform_BS')


class TwistRibbon(Ribbon):
    def create(self):
        dup = self.duplicate_mesh()
        self.blend_deformer(dup)
        cmds.select(dup)
        cmds.nonLinear(type='Twist', ap=1)
        return dup


class SineRibbon(Ribbon):
    def create(self):
        dup = self.duplicate_mesh()
        self.blend_deformer(dup)
        cmds.select(dup)
        cmds.nonLinear(type='Sine', ap=1)
        return dup


class BendRibbon(Ribbon):
    def create(self):
        dup = self.duplicate_mesh()
        self.blend_deformer(dup)
        cmds.select(dup)
        cmds.nonLinear(type='Bend', ap=1)
        return dup


class WaveRibbon(Ribbon):
    def create(self):
        dup = self.duplicate_mesh()
        self.blend_deformer(dup)
        cmds.select(dup)
        cmds.nonLinear(type='Wave', ap=1)
        return dup


class RibbonGuiTools(object):
    def __init__(self):
        self.new_window = "ToolsRibbon"
        self.size = (100, 100)

    def create_window(self):
        if cmds.window(self.new_window, q=True, exists=True):
            cmds.deleteUI(self.new_window)
        if cmds.windowPref(self.new_window, q=True, exists=True):
            cmds.windowPref(self.new_window, r=True)
        cmds.window(self.new_window, resizeToFitChildren=1, t='ToolsRibbon', widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True)
        cmds.separator(height=20)
        cmds.text(l="Generate ribbonMeshes")
        cmds.separator(height=20)
        cmds.rowLayout(numberOfColumns=2, adjustableColumn=True)
        cmds.button(l="outerEdgesLoop", bgc=(1, 0, 0), c=outer_edges_loop)
        cmds.button(l="innerEdgesLoop", bgc=(1, 0, 0), c=inner_out_loop)
        cmds.setParent("..")
        cmds.columnLayout(adjustableColumn=True)
        cmds.button(l="BuildRibbonStrip", bgc=(0, 0, 0), command=build_ribbon_plane)
        cmds.separator(height=10)
        cmds.setParent("..")
        cmds.columnLayout(adjustableColumn=True)
        cmds.radioButtonGrp('ribbons', labelArray2=['TwistRibbon', 'SineRibbon'], numberOfRadioButtons=2)
        cmds.radioButtonGrp('ribbons1', labelArray2=['BendRibbon', 'WaveRibbon'], numberOfRadioButtons=2)
        cmds.intFieldGrp('list_length', l='numberOfTwistJoints', value1=5)
        cmds.button(label="creatingRig", c=press)
        cmds.showWindow()


def outer_edges_loop(*args):
    cmds.select(add=1)
    curve = cmds.polyToCurve(form=2, degree=1, conformToSmoothMeshPreview=1)[0]
    cmds.rename(curve, "curveOuter")


def inner_out_loop(*args):
    cmds.select(add=1)
    curve = cmds.polyToCurve(form=2, degree=1, conformToSmoothMeshPreview=1)[0]
    cmds.rename(curve, "curveInner")


def build_ribbon_plane(*args):
    cmds.loft("curveInner", "curveOuter", n="RibbonMesh")


def press(*args):
    deformer_T = cmds.radioButtonGrp('ribbons', q=True, select=True)
    theList = [None, TwistRibbon, SineRibbon, BendRibbon, WaveRibbon]
    selects = theList[deformer_T]
    ribbon_instance = selects("ribbon_instance", "RibbonMesh")
    ribbon_instance.create()


if __name__ == "__main__":
    ribbon_gui = RibbonGuiTools()
    ribbon_gui.create_window()
