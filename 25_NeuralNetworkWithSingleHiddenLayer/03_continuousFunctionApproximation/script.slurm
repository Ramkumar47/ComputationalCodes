#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=iist
#SBATCH -o runLog-%j

# runnig python script
python script_contFunc.py > log.pythonRun 2>&1

