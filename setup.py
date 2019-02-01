from setuptools import setup
  
classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware',
               'Topic :: System :: Monitoring']

setup(name             = 'cayenne_energenie',
      version          = '0.1.0',
      author           = 'myDevices',
      author_email     = 'N/A',
      description      = 'myDevices Cayenne Energenie Pi-mote Control plugin',
      keywords         = 'myDevices IoT Cayenne Energenie Pi-mote plugin',
      url              = 'https://www.mydevices.com/',
      classifiers      = classifiers,
      packages         = ['cayenne_energenie'],
      install_requires = ['gpiozero'])