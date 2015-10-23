#!/usr/bin/env python
# import sys
import os
from setuptools import setup
from distutils.cmd import Command

try:
    import fontTools  # noqa
except:
    print("*** Warning: trufont requires FontTools, see:")
    print("    https://github.com/behdad/fonttools/")

try:
    import robofab  # noqa
except:
    print("*** Warning: trufont requires RoboFab (the python3-ufo3 branch), "
          "see:")
    print("    https://github.com/trufont/robofab")

try:
    import defcon  # noqa
except:
    print("*** Warning: trufont requires defcon (the python3-ufo3 branch), "
          "see:")
    print("    https://github.com/trufont/defcon")

# if "sdist" in sys.argv:
#    import os
#    import subprocess
#    import shutil
#    docFolder = os.path.join(os.getcwd(), "documentation")
#    # remove existing
#    doctrees = os.path.join(docFolder, "build", "doctrees")
#    if os.path.exists(doctrees):
#        shutil.rmtree(doctrees)
#    # compile
#    p = subprocess.Popen(["make", "html"], cwd=docFolder)
#    p.wait()
#    # remove doctrees
#    shutil.rmtree(doctrees)

CURR_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))


class TestCommand(Command):
    """ Run all *_test.py scripts in 'tests' folder with the same Python
    interpreter used to run setup.py.
    """

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        import glob

        test_dir = os.path.join(CURR_DIR, 'tests')
        os.chdir(test_dir)

        for test in glob.glob("**/*_test.py"):
            print(test)
            try:
                subprocess.check_call([sys.executable, test])
            except subprocess.CalledProcessError:
                raise SystemExit(1)

setup(
    name="defconQt",
    version="0.1.0",
    description="Trufont, a cross-platform font editor (a set of Qt interface "
                "objects for working with font data).",
    author="Adrien Tétar",
    author_email="adri-from-59@hotmail.fr",
    url="http://trufont.github.io",
    license="GNU LGPL 2.1/GNU GPL v3",
    packages=[
        "defconQt",
        "defconQt.objects",
        "defconQt.pens",
        "defconQt.representationFactories",
        "defconQt.util",
    ],
    entry_points={
        "gui_scripts": [
            "trufont =  defconQt.__main__:main"
        ]
    },
    package_dir={"": "Lib"},
    platforms=["Linux", "Win32", "Mac OS X"],
    classifiers=[
        "Environment :: GUI",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Fonts",
    ],
    cmdclass={
        'test': TestCommand
    }
)
