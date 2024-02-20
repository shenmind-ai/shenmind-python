from setuptools import setup, find_packages

setup(
    name='shenmind',  # 包的名称
    version='0.1.1',  # 版本号
    author='shenmind',  # 作者姓名
    author_email='sdruc0611@gmail.com',  # 作者邮箱
    description='A Python package for shenmind',  # 包的描述信息
    packages=find_packages(),  # 包含的包
    install_requires=[  # 依赖的其他包
        'requests',
        'numpy',
    ],
    classifiers=[  # 软件分类标签
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
