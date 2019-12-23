# python_ORCA
python interface for Optimal Reciprocal Collision Avoidance (ORCA), implemented with pybind11. More details about the algorithm can be found in the original C++ project <http://gamma.cs.unc.edu/RVO2/>


## Usage

1. install python package pytorch:
    ```
    pip install torch
    ```
2. compile the original C++ sode and setup the python lib
    ```
    make
    ```
3. import pyorca in python and you can use the orca algorithm in python. A demo is in pyscripts/Blocks.py
    ```
    python pyscripts/Blocks.py
    ```
