from setuptools import setup
import os

# EDIT this variable to point to your workflow subdir
workflow_name = "3d-dna"

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
        "scripts": [
            "run-asm-pipeline-post-review.sh",
            "run-asm-pipeline.sh"
        ]
    },
    package_data={
        f"{workflow_name}": package_files
    },
)
