from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path):
    with open(file_path) as file_obj:
        reqr = file_obj.readlines()
        requirements = [i.replace('/n','') for i in reqr]
        return requirements





setup(
    name = 'diamond_price_prediction',
    author = 'naveen',
    author_email = 'kattanaveen483@gmail.com',
    version = '0.0.1',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
)








