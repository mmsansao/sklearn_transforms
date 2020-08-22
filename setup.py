from setuptools import setup


setup(
    name="my_custom_sklearn_transforms",
    version="1.0",
    description="""
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      """,
    url="https://github.com/mmsansao/sklearn_transforms/",
    author="Marcos Sansão",
    author_email="marcosmsansao@gmail.com",
    license="BSD",
    packages=["my_custom_sklearn_transforms"],
    zip_safe=False,
    install_requires=["imbalanced-learn==0.4.3"],
)
