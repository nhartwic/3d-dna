from pkg_resources import resource_filename
import subprocess
import sys

# gets name of this pip module so that you can access 3ddna scripts
workflow = __name__.split('.')[0]
mainsh = resource_filename(workflow, 'run-asm-pipeline-post-review.sh')
postsh = resource_filename(workflow, 'run-asm-pipeline.sh')

sys.stderr.write(str(sys.argv) + "\n")

def run_asm_pipeline():
    subprocess.call(["bash", mainsh] + sys.argv[1:])


def run_asm_pipeline_post_review():
    subprocess.call(["bash", postsh] + sys.argv[1:])



