from shutil import which
import subprocess
from glob import glob
import platform
import os
import pathlib
from tqdm import tqdm

last_proto_template_mtime = 0

def generate_protos_docs(force_rebuild=False):
    global last_proto_template_mtime
    
    protos_docs_template = "./docs/PLUME-Protos/proto_docs.tmpl"
    template_mtime = os.path.getmtime(protos_docs_template)

    if template_mtime != last_proto_template_mtime:
        force_rebuild = True
        last_proto_template_mtime = template_mtime

    protos_dir = "./external/PLUME-Protos/"
    protos_docs_dir = "./docs/PLUME-Protos/protos/"

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

    for proto in tqdm(protos, desc="Generating docs"):
        proto_docs_path = protos_docs_dir / pathlib.Path(proto).relative_to(protos_dir).with_suffix(".md")
        pathlib.Path(proto_docs_path.parent).mkdir(parents=True, exist_ok=True)

        if os.path.exists(proto_docs_path) and not force_rebuild:
            continue
        
        args = [f"--proto_path={protos_dir}",
                f"--plugin=protoc-gen-doc={protoc_gen_doc_path}",
                f"--doc_out={protos_docs_dir}",
                f"--doc_opt={protos_docs_template},{str(proto_docs_path.relative_to(protos_docs_dir))}", proto]
        subprocess.run(["protoc", *args])

def on_pre_build(**kwargs):
    generate_protos_docs()