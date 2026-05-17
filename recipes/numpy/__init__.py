from pythonforandroid.recipes.numpy import NumpyRecipe

class CompatibleNumpyRecipe(NumpyRecipe):
    version = "1.26.4"
    url = "https://github.com/numpy/numpy/archive/refs/tags/v{version}.tar.gz"

recipe = CompatibleNumpyRecipe()
