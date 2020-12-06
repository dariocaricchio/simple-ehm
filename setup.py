from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Simple Ehm Cutter'
LONG_DESCRIPTION = 'Python package to cut silences and ehm sounds from audio and video files'

# Setting up
setup(
       # the name must match the folder name
        name="simple-ehm",
        version=VERSION,
        author="Morrolinux",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['ffmpeg'], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'ehm', 'silence', 'cutter', 'audio', 'video', 'file'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Canonical :: Ubuntu",
            "Operating System :: Microsoft :: Windows",
        ]
)
