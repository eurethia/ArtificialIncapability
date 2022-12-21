
from distutils.core import setup
setup(
  name = 'ArtificialIncapability',         # How you named your package folder (MyLib)
  packages = ['ArtificialIncapability'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'World\'s SOTA AI',   # Give a short description about your library
  author = 'Eurethia Zhang',                   # Type in your name
  author_email = '3366841721@qq.com',      # Type in your E-Mail
  url = 'https://github.com/eurethia/ArtificialIncapability',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/eurethia/ArtificialIncapability/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['AI', 'True Intelligence', 'Stubidity'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)
