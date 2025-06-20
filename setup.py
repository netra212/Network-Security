'''
The setup.py file is an essential part of packaging and distributing Python Projects. It is used by setuptools (or distutils in Older python versions) to define the configuration of project, such as its metadata, dependencies, and more. 
'''
from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This functions will return list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            # Read Lines from the file. 
            lines = file.readlines()

            # Process each line. 
            for line in lines:
                requirement = line.strip()

                # Ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirement_lst

setup(
    name="NetworkSecurity", 
    version = "0.0.1",
    author = "Netra Bdr. Khatri", 
    author_email = "netra200021kcbdr@gmail.com", 
    packages = find_packages(),
    install_requires = get_requirements()
)