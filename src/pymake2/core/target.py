"""
Defines the Target class which represents a single make target.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake2.core import makeconf

#---------------------------------------
# CLASSES
#---------------------------------------

class Target(object):
    """
    Represents a make target that. A single target consists of a name and a make
    function.  However, a target can also have pre- and post- functions, which
    act as hooks, giving a user the ability to perform operations before or
    after targets they have no control over.
        Targets may also have dependencies, which are other targets, thare are
    requierd to be made before this target is made.
    """
    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self, name, func=None):
        """
        Initializes the target to default values.

        :param name: Name of the target.
        :param func: Target make function.
        """
        self.checked    = False
        self.def_conf   = makeconf.from_dict({})
        self.depends    = []
        self.desc       = None
        self.func       = func
        self.name       = name
        self.post_funcs = []
        self.pre_funcs  = []

    #---------------------------------------
    # METHODS
    #---------------------------------------

    def make(self, conf):
        """
        Makes the target by invoking its make function with the specified
        configuration.

        :param conf: Make configuration.
        """

        if isinstance(conf, dict):
            conf = makeconf.from_dict(conf)

        conf = makeconf.merge(self.def_conf, conf)

        for f in self.pre_funcs:
            f(conf)

        self.func(conf)

        for f in self.post_funcs:
            f(conf)
