from shutil import which
import subprocess
from glob import glob
import platform
import os

def generate_protos_docs():
    
    protos_docs_template = "./docs/PLUME-Protos/protos.tmpl"
    protos_generated_docs = "./docs/PLUME-Protos/protos.g.md"
    protos_generated_docs_dir = os.path.dirname(protos_generated_docs)
    protos_dir = "./external/PLUME-Protos/"

    if os.path.exists(protos_generated_docs):
        return

    if which('protoc') is None:
        print("protoc not found. Ensure that you installed and added it to your PATH.")
        exit()

    protos = glob(f"{protos_dir}/**/*.proto", recursive=True)

    system_name = platform.system().lower()

    if system_name == "windows":
        protoc_gen_doc_path = "./plugins/protoc-gen-doc-1.5.1/windows/protoc-gen-doc.exe"
    elif system_name == "linux":
        protoc_gen_doc_path = "./plugins/protoc-gen-doc-1.5.1/linux/protoc-gen-doc"
    elif system_name == "darwin":
        protoc_gen_doc_path = "./plugins/protoc-gen-doc-1.5.1/darwin/protoc-gen-doc"
    else:
        raise Exception(f"Unsupported system: {system_name}")

    os.makedirs(protos_generated_docs_dir, exist_ok=True)
    args = [f"--proto_path={protos_dir}",
            f"--plugin=protoc-gen-doc={protoc_gen_doc_path}",
            f"--doc_out={protos_generated_docs_dir}",
            f"--doc_opt={protos_docs_template},{os.path.basename(protos_generated_docs)}", *protos]
    subprocess.run(["protoc", *args])

def on_pre_build(**kwargs):
    generate_protos_docs()