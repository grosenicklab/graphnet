"""
A package to solve separable convex optimization problems, based on 
"""

import os, sys
import string

from Cython.Compiler import Main

def cython_extension(srcfile):
    options = Main.CompilationOptions(include_path=[os.path.join(os.path.abspath(os.path.dirname(__file__)), 'include')])
    Main.compile(srcfile, options=options)

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None,parent_package,top_path)

    config.add_subpackage('cwpath')

    return config

if __name__ == '__main__':

    #cython_extension("cwpath/lasso.pyx")
    cython_extension("cwpath/graphnet.pyx")
    cython_extension("cwpath/regression.pyx")
    cython_extension("cwpath/cwpath.pyx")
    
    from numpy.distutils.core import setup

    c = configuration(top_path='',
                      ).todict()
    setup(**c)
