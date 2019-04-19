from distutils.core import setup
import py2exe,sys,os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files':1}},
    console = [{'script': 'PUBG_damage_v1.py'}],
    zipfile = None
)
