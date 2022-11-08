# try:
#     # for pip >= 10
#     from pip._internal.req import parse_requirements
# except ImportError:
#     # for pip <= 9.0.3
#     from pip.req import parse_requirements

# def load_requirements(fname):
#     reqs = parse_requirements(fname, session="test")
#     return [str(ir.req) for ir in reqs]

# setup(name="yourpackage", install_requires=load_requirements("requirements.txt"), name='Distutils',
#       version='1.0',
#       description='Python Distribution Utilities',
#       author='Greg Ward',
#       author_email='gward@python.net',
#       url='https://www.python.org/sigs/distutils-sig/',
#       packages=['distutils', 'distutils.command'],
#      )