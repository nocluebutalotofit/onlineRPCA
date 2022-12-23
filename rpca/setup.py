from setuptools import setup, find_packages

setup(
    name='rpca',
    version='0.9.0',
    url='https://github.com/wxiao0421/onlineRPCA',
    author='wexiao',
    author_email='author@gmail.com',
    description='Batch and Online Robust PCA (Robust Principal Component Analysis) implementation and examples (Python). A translation to matlab is available at this github repository. Robust PCA based on Principal Component Pursuit (RPCA-PCP) is the most popular RPCA algorithm which decomposes the observed matrix M into a low-rank matrix L and a sparse matrix S by solving Principal Component Pursuit',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)