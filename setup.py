from setuptools import find_packages,setup
## Find packages -- checks for __init__ file inside packages

from typing import List

def get_requirements()->List[str]:
    ## This Function Will Return List Of Requirements
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and ignore -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Hey My requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Aditya Pandey",
    author_email="aditya3113pandey@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
