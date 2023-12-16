import subprocess

embeddings = "./trainingData/legalModel_noStem.bin"
cluster_size = "500"
batch_size = "100"
fattrs = "./paperImplementation/data/weat_lists/female_terms.txt"
mattrs = "./paperImplementation/data/weat_lists/male_terms.txt"
output_file = "./clusterFlow_output.txt"
output_file2 = "./clusterSummary.txt"
output_file3 = "./genderAssociation_cluster.txt"

command = [
    'python3',
    './paperImplementation/code/cluster_embeddings.py',
    '-v',
    embeddings,
    '-t',
    'w2v',
    '-k',
    cluster_size,
    '-b',
    batch_size,
    '-o',
    output_file
]


command2 = [
    'python3',
    './paperImplementation/code/cluster_sizes.py',
    '-c',
    output_file,
    '-o',
    output_file2
]

command3 = [
    'python3',
    './paperImplementation/code/gender_associations.py',
    '-v',
    embeddings,
    '-t',
    'w2v',
    '-c',
    output_file,
    '-f',
    fattrs,
    '-m',
    mattrs,
    '-o',
    output_file3
]

try:
    output = subprocess.run(command, capture_output=True, text=True, check=True)
    print("Command output:")
    print(output.stdout)


except subprocess.CalledProcessError as e:
    print(f"Error executing command. Return code: {e.returncode}")
    print(e.output)

try : 
    print("Command output2 : ")
    final_output = subprocess.run(command2, capture_output=True, text=True, check=True)
    print(final_output.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error executing command. Return code: {e.returncode}")
    print(e.output)

def read_clusters(file_path):
    clusters = {}
    with open(file_path, 'r') as file:
        for line in file:
            word, cluster = line.strip().split('\t')
            cluster = int(cluster)
            if cluster not in clusters:
                clusters[cluster] = []
            clusters[cluster].append(word)
    return clusters

def save_clusters_to_file(clusters):
    with open('clusters_examples.txt', 'w') as output_file:
        for cluster, words in clusters.items():
            output_file.write(f"Cluster {cluster} : {words}\n")


clusters = read_clusters(output_file)
save_clusters_to_file(clusters)


try : 
    
    output = subprocess.run(command3, capture_output=True, text=True, check=True)
    print("Command output 3:")
    print(output.stdout)


except subprocess.CalledProcessError as e:
    print(f"Error executing command. Return code: {e.returncode}")
    print(e.output)

    
