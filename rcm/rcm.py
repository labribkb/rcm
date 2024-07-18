import os
import tempfile
import webbrowser

import numpy as np
from jinja2 import Environment, FileSystemLoader, select_autoescape

__author__ = "Romain Giot"
__copyright__ = "Copyright 2024, Univ. Bordeaux"
__credits__ = ["Romain Giot"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Romain Giot"
__email__ = "romain.giot@u-bordeaux.fr"
__status__ = "Prototype"


class Rcm(object):
    """Build the needed data for a confusion matrix"""
    def __init__(self, conf_a, conf_b, labels = None) -> None:
        """
        Build the RCM object.

        - conf_a: first confusion matrix
        - conf_b: second confusion matrix
        - labels: ordered labels
        """
        assert conf_a is not None
        assert conf_b is not None


        assert np.asarray(conf_a).shape == np.asarray(conf_b).shape
        assert len(conf_a) == len(conf_a[0])

        if labels is None:
            labels = ["%d"%i for i in range(len(conf_a))]

        self._conf_a = conf_a
        self._conf_b = conf_b
        self._labels = labels

    def show(self, **args) -> None:
        """Generates the HTML code, save it in a file and open it in a webrowser.
        Returns the generated file name. It is up to the caller to delete it.
        Accept all arguments of generate_html
        """
        content = self.generate_html(**args)
        (fd, name) = tempfile.mkstemp(".html", text=True) #never deleted
        with open(name, 'w') as fd:
            print(content, file=fd)
        webbrowser.open(name)
        return name

    def generate_html(self,
                      rcm_width=500,
                      rcm_height=500,
                      rcm_head_font_size="15px",
                      global_font_family="Verdana, sans-serif",
                      rcm_body_font_size="30px",
                      nb_max_char_per_class=7,
                      legend_w=300,
                      legend_bar_w=50,
                      with_sliders=True,
                      symbol_plus="+",
                      symbol_minus="-"
                      ):
        """Generates the HTML code that represents the current RCM"""
        env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
            autoescape=select_autoescape()
        )
        tpl = env.get_template("index.html")
        print("A="  , self._conf_a)
        return tpl.render(
            conf_a=self._conf_a,
            conf_b=self._conf_b,
            labels=self._labels,
            rcm_width=rcm_width,
            rcm_height=rcm_height,
            rcm_head_font_size=rcm_head_font_size,
            global_font_family=global_font_family,
            rcm_body_font_size=rcm_body_font_size,
            nb_max_char_per_class=nb_max_char_per_class,
            legend_w=legend_w,
            legend_bar_w=legend_bar_w,
            with_sliders=with_sliders,
            symbol_minus=symbol_minus,
            symbol_plus=symbol_plus
        )
