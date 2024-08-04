from setuptools import setup, find_packages

setup(
    name='youtube_uploader_selenium',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List any dependencies here, e.g., 'selenium', 'requests', etc.
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here if needed
        ],
    },
    author='Multiple Contributors',
    author_email='your.email@example.com',
    description='A tool to upload videos to YouTube using Selenium',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AroSwift/youtube-uploader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
