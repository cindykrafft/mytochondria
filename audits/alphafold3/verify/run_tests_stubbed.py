# Runs folding_input_test.py (absltest) against a source tree with the compiled modules stubbed out.
# Usage: python run_tests_stubbed.py <tree>/src [-- absltest args]
import sys, types, runpy, os
class Stub(types.ModuleType):
    __path__ = []
    def __getattr__(self, name):
        if name.startswith("__"): raise AttributeError(name)
        return type(name, (), {})
for name in ["alphafold3.cpp", "alphafold3.cpp.cif_dict", "alphafold3.structure", "alphafold3.structure.mmcif",
             "alphafold3.constants.chemical_components"]:
    sys.modules[name] = Stub(name)
sys.modules["alphafold3.structure"].mmcif = sys.modules["alphafold3.structure.mmcif"]
tree = sys.argv[1]; sys.path.insert(0, tree)
sys.argv = [os.path.join(tree, "alphafold3/common/folding_input_test.py")] + sys.argv[2:]
runpy.run_path(sys.argv[0], run_name="__main__")
