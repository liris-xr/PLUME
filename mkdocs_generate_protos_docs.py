from shutil import which
import subprocess
from glob import glob
import platform
import os
import pathlib

last_proto_template_mtime = None

def generate_protos_docs(force_rebuild=False):
    global last_proto_template_mtime
    
    file_format_dir = "./docs/recorder/file-format/"

    protos_docs_template = os.path.join(file_format_dir, "proto_docs.tmpl")
    template_mtime = os.path.getmtime(protos_docs_template)

    if last_proto_template_mtime == None or template_mtime != last_proto_template_mtime:
        force_rebuild = True
        last_proto_template_mtime = template_mtime

    protos_dir = "./external/PLUME-Protos/"
    protos_docs_dir = os.path.join(file_format_dir, "proto-files/")

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

    print("Generating proto docs...")

    for proto in protos:
        proto_docs_path = protos_docs_dir / pathlib.Path(proto).relative_to(protos_dir).with_suffix(".md")
        pathlib.Path(proto_docs_path.parent).mkdir(parents=True, exist_ok=True)

        if os.path.exists(proto_docs_path) and not force_rebuild:
            continue
        
        args = [f"--proto_path={protos_dir}",
                f"--plugin=protoc-gen-doc={protoc_gen_doc_path}",
                f"--doc_out={protos_docs_dir}",
                f"--doc_opt={protos_docs_template},{str(proto_docs_path.relative_to(protos_docs_dir))}", proto]
        subprocess.run(["protoc", *args])
        print(f"Generated {proto_docs_path}")
    
    print("Done generating proto docs.")

def on_pre_build(**kwargs):
    generate_protos_docs(False)

if __name__ == "__main__":
    generate_protos_docs(True)