from setuptools import setup, find_packages
from typing import List


def get_requirments()-> List[str]:

    """
    This function returns a list of requirements for the package.
    """
    requirmenta_list:List[str] = []
    try:
        with open('requirements.txt') as f:
            lines = f.readlines()

            for line in lines:
                requirment = line.strip()
                if requirment and  requirment != '-e .':
                    requirmenta_list.append(requirment)

    except FileNotFoundError:
        print(f"requirements.txt not found. Please ensure it exists in the project directory.")

    return requirmenta_list

print(get_requirments())

setup(
    name='ai-trip-planner',  
    version='0.0.1',
    author='Vinay Kamma',
    author_email="kammavinay2760@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()
) 