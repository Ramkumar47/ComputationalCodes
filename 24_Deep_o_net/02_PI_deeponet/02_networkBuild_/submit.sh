#!/bin/bash -login
# Propogate environment variables to compute node
#SBATCH --export=ALL

# set the number of nodes and processes per node
#SBATCH --nodes=1

# set the number of tasks (processes) per node.
#SBATCH --ntasks-per-node=1

#SBATCH --cpus-per-task=1

# set name of job
#SBATCH --job-name=PI_DON

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=ramkumar.sc22m007@pg.iist.ac.in

time python script.py > log.pythonRun 2>&1
