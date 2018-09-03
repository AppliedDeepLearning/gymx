from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

name = 'gymx'

setup(
    name=name,
    version='0.0.1',
    description=long_description.splitlines()[0],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ravindra Marella',
    author_email='mv.ravindra007@gmail.com',
    url='https://github.com/AppliedDeepLearning/{}'.format(name),
    license='MIT',
    packages=find_packages(),
    install_requires=['grpcio', 'protobuf', 'numpy'],
    extras_require={
        'dev': [
            'grpcio-tools',
            'googleapis-common-protos',
        ]
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='{} gym grpc reinforcement-learning'.format(name),
)
