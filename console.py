import shlex
import subprocess as sp

cmd = "xdg-open https://www.kaggle.com/punzalan/melanoma-hello"
sp.run(shlex.split(cmd), stdout=sp.PIPE, stderr=sp.PIPE)
