import maya.cmds as mc

class JointCreator(object):
    def __init__(self, name):
        self.name = name

    def create(self):
        raise NotImplementedError("Subclasses must implement create()")


class WorldJointCreator(JointCreator):
    def create(self):
        new_joint = mc.joint(n=self.name)
        return new_joint


class MatchSelectionJointCreator(JointCreator):
    def create(self):
        mc.select(self.name)
        sel = mc.ls(sl=True)

        if sel:
            new_joint = mc.joint(n=(self.name + "_Jnt"))
        else:
            new_joint = mc.joint(n=(self.name + "_Jnt"))

        return new_joint


class MatchTransformJointCreator(JointCreator):
    def __init__(self, name, match_joint=None):
        super(MatchTransformJointCreator, self).__init__(name)
        self.match_joint = match_joint

    def create(self):
        new_joint = mc.joint(n=(self.name + "_Jnt"))

        if self.match_joint:
            match_translation = mc.getAttr("{}.translate".format(self.match_joint))[0]
            match_rotation = mc.getAttr("{}.rotate".format(self.match_joint))[0]
            mc.setAttr("{}.translate".format(new_joint), *match_translation)
            mc.setAttr("{}.rotate".format(new_joint), *match_rotation)

        return new_joint


class JointHierarchyBuilder(object):
    def __init__(self, root_locator_name):
        self.root_locator_name = root_locator_name

    def is_transform_node(self, node):
        return mc.nodeType(node) == 'transform'

    def traverse_locator_hierarchy(self, locator_name, indent=0):
        parent_locator = mc.listRelatives(locator_name, parent=True)

        if parent_locator:
            parent_locator_name = parent_locator[0]
            try:
                joint_creator = WorldJointCreator(locator_name + "_joint")
                new_joint = joint_creator.create()
                mc.matchTransform(new_joint, locator_name)
                mc.select(cl=1)
                mc.parent(new_joint, parent_locator_name + "_joint")
            except Exception as e:
                print("Skipped: Error creating joint for {}. Error: {}".format(locator_name, e))

        child_locators = mc.listRelatives(locator_name, children=True) or []
        child_locators = [child for child in child_locators if self.is_transform_node(child)]

        for child_locator in child_locators:
            self.traverse_locator_hierarchy(child_locator, indent + 1)

    def build_joint_hierarchy(self):
        self.traverse_locator_hierarchy(self.root_locator_name)
        group_name = mc.group(empty=True, name="skeleton_Grp")
        mc.parent("root_joint", group_name)
        mc.joint("root_joint", edit=True, orientJoint='xyz', secondaryAxisOrient='yup', children=True, zeroScaleOrient=True)


# Example usage:
builder = JointHierarchyBuilder("root")
builder.build_joint_hierarchy()
