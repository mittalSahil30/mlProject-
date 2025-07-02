from setuptools import find_packages, setup
from typing import List

HypenEDot = '-e .'
def get_requirements(filePath:str) ->List[str]:
  '''
  this function return the list of requirements
  '''
  requirements = []
  with open(filePath) as fileObj:
    requirements = fileObj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]
    
    
    if HypenEDot in requirements:
      requirements.remove(HypenEDot)
      
  return requirements
  
setup(
name = 'mlProject',
versions = '0.0.1',
author = 'sahil',
author_email= 'sahilmittal3003@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
