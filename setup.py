# from distutils.core import setup
from setuptools import setup, find_packages
setup(
    # Name of the package
    name='SequaGUI',

    # Packages to include into the distribution
    packages=find_packages(), 
    version='0.0.4',
    license='',
    description='Advanced button continuation',
    long_description = open('README.md').read(),
    long_description_context_type = 'text/markdown',
    author='Sequa Inc', 
    author_email='soberonlineemail@gmail.com',     
    keywords=['python', 'Tkinter', 'GUI', 'package'],

    # List of packages to install with this one
    install_requires=["Babel==2.14.0",     
                        "matplotlib==3.8.2" ,
                        "numpy==1.26.2",
                        "opencv-python==4.8.1.78",       
                        "pandas==2.1.4",
                        "Pillow==10.1.0",      
                        "pyperclip==1.8.2",     
                        "pywin32==306",
                        "screeninfo==0.8.1",
                        "tkcalendar==1.6.1",     
                        "ttkthemes==3.2.2"],
)