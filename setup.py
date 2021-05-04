from setuptools import setup
import os

# EDIT this variable to point to your workflow subdir
workflow_name = "pip_3d_dna"

package_files = [
    os.path.relpath(os.path.join(d, f), workflow_name)
    for d, _, files in os.walk(workflow_name)
    for f in files
]

setup(
    name=workflow_name,
    version="0.1.0",
    packages=[workflow_name],
    entry_points={
        "console_scripts": [
            "run-asm-pipeline={wn}.__main__:run_asm_pipeline".format(wn=workflow_name),
            "run-asm-pipeline-post-review={wn}.__main__:run_asm_pipeline_post_review".format(wn=workflow_name)
        ]
    },
    package_data={
        workflow_name: package_files
    },
)
