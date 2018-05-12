from setuptools import setup, find_packages

setup(name='turtle_compiler_hexbug',
	version='0.1',
	description='Python written compiler to interpret turtle code in Arduino (i.e. C++) and utilize it for a hexbug',
	url='https://github.com/v2thegreat/turtle-compiler-for-hexbug',
	author='v2thegreat',
	author_email='v2thegreat@gmail.com',
	license='MIT',
	packages=['turtle_compiler_hexbug'],
	zip_safe=False,
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
	)
