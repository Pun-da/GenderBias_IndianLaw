import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-c', '--clusters', type=str, help="File containing clusters")
    parser.add_argument('-o', '--output', type=str, help="Output file to save logs")
    return parser.parse_args()


def main(args):
    clusters = {}
    with open(args.clusters, 'r') as fc:
        for line in fc:
            fields = line.strip().split('\t')
            if len(fields) == 1:
                cluster = int(fields[0])
            else:
                cluster = int(fields[1])
            clusters[cluster] = clusters.get(cluster, 0) + 1

    sum_sizes = 0
    with open(args.output, 'a') as log_file:
        count = 0
        for cluster in sorted(clusters.keys()):
            cluster_size = clusters[cluster]
            sum_sizes += cluster_size
            log_file.write("{}\t{}\n".format(cluster, cluster_size))
            count+=1
        log_file.write("\nMean cluster size {} for {} clusters\n".format((sum_sizes / len(clusters)), count))
        log_file.write("-----------------------\n\n\n")


if __name__ == '__main__':
    args = parse_args()
    sys.stdout = open(args.output, 'a')  # Redirect stdout to the output file
    main(args)
