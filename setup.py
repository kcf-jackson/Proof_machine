from setuptools import setup

setup(name='proof_machine',
      version='0.27',
      description='A machine to do proof in statistics and probability',
      url='http://github.com/kcf-jackson/Proof_machine',
      author='Jackson Kwok',
      author_email='kcf.jackson@gmail.com',
      license='MIT',
      packages=['proof_machine', 'proof_machine.objClass', 'proof_machine.treeMap', 'proof_machine.others'],
      install_requires=['pythonds', 'orderedset'],
      zip_safe=False)
