import sys, types, runpy
class Stub(types.ModuleType):
    __path__ = []
    def __getattr__(self, name):
        if name.startswith("__"): raise AttributeError(name)
        return type(name, (), {})
for name in ["alphafold3.cpp", "alphafold3.cpp.json_serialize", "alphafold3.model.model"]:
    sys.modules[name] = Stub(name)
sys.path.insert(0, sys.argv[1])
runpy.run_path("mcve_summary_confidences_chain_ids.py", run_name="__main__")
