#!/bin/bash -login
# Propogate environment variables to compute node
#SBATCH --export=ALL

# job array
#SBATCH --array=1-50%2 # default 2 jobs per user restriction

# Set default partition to medium
#SBATCH --partition=medium

# set the number of nodes and processes per node
#SBATCH --nodes=1

# set the number of tasks (processes) per node.
#SBATCH --ntasks-per-node=1

#SBATCH --cpus-per-task=1

# set name of job
#SBATCH --job-name=ChaoticSystems

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=ramkumars.24@res.iist.ac.in

module load gnu14

make -C *_taskId_$SLURM_ARRAY_TASK_ID/cppCode/ refresh run

