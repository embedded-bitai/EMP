import setuptools
# root directory 에서 pip install . -> python은 build가 수동
with open("README.md","r") as fh:
    long_description  = fh.read()
setuptools.setup(
    name='com_cheese_api', # 여기가 중요
    version='1.0',
    description='Python Distribution Utilities',
    long_description=long_description,
    author='youjeong2',
    author_email='progress.uj11@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)