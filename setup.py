from setuptools import setup, find_packages

setup(
    name='kashimaPy',
    version='1.0.6.1',
    author='Alejandro Verri Kozlowski',
    author_email='averri@fi.uba.ar',
    description='A package for processing and mapping seismic data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/averriK/kashimaPy',  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'folium',
        'geopandas',
        'pyproj',
        'requests',
        'branca',
        'geopy',
        'matplotlib',
        'dataclasses; python_version < "3.7"',
        # 'typing_extensions; python_version < "3.8"',  # Uncomment if needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
