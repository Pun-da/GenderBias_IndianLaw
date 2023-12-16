import subprocess

embeddings = "./trainingData/legalModel_noStem.bin"
fattr = "./paperImplementation/data/weat_lists/female_terms.txt"
mattr = "./paperImplementation/data/weat_lists/male_terms.txt"
iterns = "10000"
input_file = "./case_hypothesis_input.txt"
output_file = "./case_hypotest_output.txt"

command = [
    'python3',
    './paperImplementation/code/case_hypotest.py',
    '-v',
    embeddings,
    '-t',
    'w2v',
    '-f',
    fattr,
    '-m',
    mattr,
    '-i',
    iterns,
    '-c',
    input_file,
    '-o',
    output_file
]

try:
    output = subprocess.run(command, capture_output=True, text=True, check=True)
    print("Command output:")
    print(output.stdout)

except subprocess.CalledProcessError as e:
    print(f"Error executing command. Return code: {e.returncode}")
    print(e.output)
