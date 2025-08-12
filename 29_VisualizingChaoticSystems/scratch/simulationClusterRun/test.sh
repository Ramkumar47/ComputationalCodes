#!/bin/bash
#SBATCH --job-name=my_array_job  # Name of the job array
#SBATCH --array=1-10%4            # Defines 10 array tasks (from 1 to 10)
#SBATCH --time=00:10:00         # Maximum wall-clock time for each task
#SBATCH --mem=1G                # Memory requested for each task
#SBATCH --output=output_%A_%a.out # Output file pattern: %A=Job ID, %a=Array Task ID
#SBATCH --error=error_%A_%a.err   # Error file pattern
#SBATCH --partition=medium


# Load any necessary modules (e.g., software environments)
# module load my_software_package

# The core command to be executed by each array task
# The SLURM_ARRAY_TASK_ID environment variable provides the current task's index
echo "Running task with ID: $SLURM_ARRAY_TASK_ID"

# Example: Process a different input file for each task
# Assuming you have input files named input_1.txt, input_2.txt, etc.
# my_program --input-file input_${SLURM_ARRAY_TASK_ID}.txt --output-file results_${SLURM_ARRAY_TASK_ID}.csv

# Example: Perform a calculation based on the task ID
# result=$((SLURM_ARRAY_TASK_ID * 2))
# echo "Result for task $SLURM_ARRAY_TASK_ID: $result"

sleep 5 # Simulate some work
