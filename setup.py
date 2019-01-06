import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='gym-tictactoe',
     version='0.30',
     scripts=[] ,
     author="Reza Sherafat",
     author_email="sherafat.us@gmail.com",
     description="Tic-Tac-Toe environment in OpenAI gym",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/shkreza/gym-tictactoe",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=['gym','matplotlib','numpy'],
 )