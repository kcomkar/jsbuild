from distutils.core import setup
import jsbuild

files = ['templates/*']

setup(name='JSBuild',
    version=".".join( map(str, jsbuild.__version__) ),
    description='Javascript Build Utility With CommonJS Packages Support',
    license='MIT',
    author=jsbuild.__author__,
    author_email=jsbuild.__email__,
    url='http://github.com/jsbuild',
    packages=['jsbuild'],
    package_data = {'jsbuild' : files },
    scripts=['scripts/jsbuild'],
    classifiers=[
      'Development Status :: 1 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: MIT License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Programming Language :: Python',
      'Topic :: Software Development :: Building'
      ],
)