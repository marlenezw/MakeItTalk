"""
 # Copyright 2020 Adobe
 # All Rights Reserved.
 
 # NOTICE: Adobe permits you to use, modify, and distribute this file in
 # accordance with the terms of the Adobe license agreement accompanying
 # it.
 
"""

import setuptools

setuptools.setup(
    name="makeitalk_animation",
    version="3.9.5",
    author="Marlene Mhangami",
    author_email="marlenemhangami@gmail.com",
    description="A library for single image and audio one shot talking head animations. A brnach of the makeittalk library",
    packages=setuptools.find_packages(),
    install_requires=[
        "ffmpeg-python",
        "opencv-python",
        "face_alignment",
        "scikit-learn",
        "pydub",
        "pynormalize",
        "soundfile",
        "librosa",
        "pysptk",
        "pyworld",
        "resemblyzer",
        "tensorboardX",
        "gradio"
    ],
)