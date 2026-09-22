# Runs the MCVE against the pure-Python folding_input module with AlphaFold 3's compiled modules stubbed out
# (no C++ build in this environment). Only to_json/from_json are exercised; nothing in the stubs is called.
import sys, types, runpy
class Stub(types.ModuleType):
    __path__ = []
    def __getattr__(self, name):
        if name.startswith("__"): raise AttributeError(name)
        return type(name, (), {})
for name in ["alphafold3.cpp", "alphafold3.cpp.cif_dict", "alphafold3.structure", "alphafold3.structure.mmcif",
             "alphafold3.constants.chemical_components"]:
    sys.modules[name] = Stub(name)
sys.modules["alphafold3.structure"].mmcif = sys.modules["alphafold3.structure.mmcif"]
sys.path.insert(0, sys.argv[1])
runpy.run_path("mcve_to_json_chain_order.py", run_name="__main__")
