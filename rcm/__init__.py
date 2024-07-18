from . import confmat
from . import rcm

"""
Dependencies:
 - jinja2
"""

__author__ = "Romain Giot"
__copyright__ = "Copyright 2024, Univ. Bordeaux"
__credits__ = ["Romain Giot"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Romain Giot"
__email__ = "romain.giot@u-bordeaux.fr"
__status__ = "Prototype"



def random_conf_mat(nb_classes=10, density=0.7, min_success=0.3):
    """Generate a random confusion matrix"""
    cm = confmat.ConfMat(nb_classes, density, min_success)
    cm.build()
    return cm.p(tolist=True)

def build_rcm(conf_a, conf_b, labels=None) -> rcm.Rcm:
    return rcm.Rcm(conf_a, conf_b, labels)

