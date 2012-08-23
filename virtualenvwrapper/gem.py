import logging
import os


log = logging.getLogger(__name__)

def post_activate_source(args):
    return """
#patch to wrap gems inside the virtual env
export _OLD_GEM_HOME="$GEM_HOME"
export _OLD_GEM_PATH="$GEM_PATH"
export GEM_HOME="$VIRTUAL_ENV/lib/gems"
export GEM_PATH=""
PATH="$GEM_HOME/bin:$PATH"
export PATH

"""



def pre_deactivate_source(args):
    return  """
#restore the value before entering the venv
export GEM_HOME="$_OLD_GEM_HOME"
export GEM_PATH="$GEM_PATH"

"""
