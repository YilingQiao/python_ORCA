# python_ORCA
python interface for Optimal Reciprocal Collision Avoidance (ORCA), implemented with pybind11. More details about the algorithm can be found in the original C++ project <http://gamma.cs.unc.edu/RVO2/>


## Usage

1. install python package pytorch:
    ```
    pip install torch
    ```
2. compile the original C++ code and setup the python lib
    ```
    make
    ```
3. simply import pyorca in python and you can play with it. A demo is in pyscripts/Blocks.py
    ```
    python pyscripts/Blocks.py
    ```
4. Definitions of interfaces are in pybind/bind.cpp . You can modify them as you want.
