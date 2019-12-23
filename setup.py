import os
from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

# Python interface
setup(
    name='pyorca',
    install_requires=['torch'],
    ext_modules=[
        CppExtension(
            name='pyorca',
            include_dirs=['./RVO/src/'],
            sources=[
                'pybind/bind.cpp',
            ],
            libraries=['make_pytorch',
    
            'png','z','lapack','blas','boost_system','boost_filesystem','boost_thread','gomp','glut','GLU','GL','glapi'],
            library_dirs=['objs'],
        )
    ],
    cmdclass={'build_ext': BuildExtension},
    url='https://github.com/chrischoy/MakePytorchPlusPlus',
    zip_safe=False,
)
