from setuptools import find_packages,setup
from typing import List


def get_requirements():
    '''
    This is responsible for returning of list of requirements
    '''

    requirements_lst:List[str]=[]

    try:

        with open("requirements.txt") as file_obj:
            lines=file_obj.readlines()

            for line in file_obj:
                requirement=line.strip()
                if requirement and requirement!='e':
                    requirements_lst.append(requirement)


    except FileNotFoundError:
        print("requirements.txt file not error")


    return requirements_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="chandu",
    author_email="chandugodugu2006@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)