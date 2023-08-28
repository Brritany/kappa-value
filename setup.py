from setuptools import setup, find_packages

setup(
    name='calculate_kappa_value',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'sklearn',
        'statsmodels',
        'tqdm'
    ],
    python_requires='>=3.6, <4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
