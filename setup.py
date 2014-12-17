from setuptools import setup

setup(name='gitography_dependencies',
      version='0.2',
      description='Dependency resolution for gitography builds',
      url='http://github.com/obowersa/gitography_dependencies',
      author='Owen Bower Adams',
      author_email='owen@obowersa.net',
      license='MIT',
      packages=['gitography_dependencies'],
      entry_points={
          'console_scripts':
          ['gitography-dependency=gitography_dependencies.command_line:main'],

      },
      install_requires=[
          'requests',
      ],
      zip_safe=False)
