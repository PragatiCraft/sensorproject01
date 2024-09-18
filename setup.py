from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    # Remove any newline characters
    requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(
    name="fault_detection",
    version="0.01",
    author="Pragati",
    author_email="pragatibandal2003@gmail.com",
    install_requirements=get_requirements('requirements.txt'),  # Fixed the parameter name
    packages=find_packages()
)
