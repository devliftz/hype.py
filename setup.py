from setuptools import setup

packages = [
    'hype',
    'hype.ext'
]

setup(
    name='hype.py',
    author='nap',
    url='https://github.com/devliftz/',
    version=1.3,
    packages=packages,
    license='MIT',
    description='Hypecord',
    include_package_data=True,
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
