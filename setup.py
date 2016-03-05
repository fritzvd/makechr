from distutils.core import setup

long_description = """Makechr is a tool for generating NES graphics from pixel art images. It creates the NES graphical components as separate files, letting you easily include these are binaries into homebrew ROMs. There are many option for handling different types of input images, check the README for more information."""

setup(name='Makechr',
      version='1.0',
      description='Makechr tool for generating NES graphics',
      long_description=long_description,
      author='Dustin Long',
      author_email='me@dustmop.io',
      scripts=['bin/makechr'],
      url='http://dustmop.io/software/makechr',
      license='GPL3',
      packages=['makechr'],
      install_requires=[
          'argparse',
          'Pillow',
          'protobuf',
      ])
