import simple_choices


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="simple-choices",
    version=simple_choices.__version__,
    packages=('simple_choices',),


    author="Vadim Ryazanov",
    author_email="vadimvoronezh@ya.ru",
    description="Classes which make working with django choices simpler",
    license="PSF",
    keywords="simple django choices",
    url="http://github.com/HelloWorld/",
)
