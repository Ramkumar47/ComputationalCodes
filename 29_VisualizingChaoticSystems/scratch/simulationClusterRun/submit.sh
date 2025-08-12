#!/bin/bash -login
# Propogate environment variables to compute node
#SBATCH --export=ALL

# Set default partition to medium
#SBATCH --partition=medium

# set the number of nodes and processes per node
#SBATCH --nodes=1

# set the number of tasks (processes) per node.
#SBATCH --ntasks-per-node=50

#SBATCH --cpus-per-task=1

# set name of job
#SBATCH --job-name=ChaoticSystems

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=ramkumars.24@res.iist.ac.in

module load gnu14

# for dir in *_*
# do
#     cd $dir/cppCode/
#     make refresh
#     make run
#     touch DONE.txt
#     cd ../../
# done


make -C 01_JCS-08-13-2022_System/cppCode/ refresh run&
make -C 02_Lorenz_System/cppCode/ refresh run&
make -C 03_Rossler_System/cppCode/ refresh run&
make -C 04_Nose-Hoover_System/cppCode/ refresh run&
make -C 05_Diffusionless_Lorenz_System/cppCode/ refresh run&
make -C 06_Sprott_C_System/cppCode/ refresh run&
make -C 07_Sprott_D_System/cppCode/ refresh run&
make -C 08_Sprott_E_System/cppCode/ refresh run&
make -C 09_Sprott_F_System/cppCode/ refresh run&
make -C 10_Sprott_G_System/cppCode/ refresh run&
make -C 11_Sprott_H_System/cppCode/ refresh run&
make -C 12_Sprott_I_System/cppCode/ refresh run&
make -C 13_Sprott_J_System/cppCode/ refresh run&
make -C 14_Sprott_K_System/cppCode/ refresh run&
make -C 15_Sprott_L_System/cppCode/ refresh run&
make -C 16_Sprott_M_System/cppCode/ refresh run&
make -C 17_Sprott_N_System/cppCode/ refresh run&
make -C 18_Sprott_O_System/cppCode/ refresh run&
make -C 19_Sprott_P_System/cppCode/ refresh run&
make -C 20_Sprott_Q_System/cppCode/ refresh run&
make -C 21_Sprott_R_System/cppCode/ refresh run&
make -C 22_Sprott_S_System/cppCode/ refresh run&
make -C 23_Rossler_Prototype-4_System/cppCode/ refresh run&
make -C 24_Simplest_Chaotic_System/cppCode/ refresh run&
make -C 25_Malasoma_System/cppCode/ refresh run&
make -C 26_Moore-Spiegel_System/cppCode/ refresh run&
make -C 27_Linz-Sprott_System/cppCode/ refresh run&
make -C 28_Elwakil-Kennedy_System/cppCode/ refresh run&
make -C 29_Chua_System/cppCode/ refresh run&
make -C 30_Chen_System/cppCode/ refresh run&
make -C 31_Halvorsen_System/cppCode/ refresh run&
make -C 32_Thomas_System/cppCode/ refresh run&
make -C 33_Rabinovich-Fabrikant_System/cppCode/ refresh run&
make -C 34_Leipnik-Newton_System/cppCode/ refresh run&
make -C 35_Arneodo-Coullet-Tresser_System/cppCode/ refresh run&
make -C 36_Lorenz-84_System/cppCode/ refresh run&
make -C 37_Wei_System/cppCode/ refresh run&
make -C 38_Wang-Chen_System/cppCode/ refresh run&
make -C 39_Reflection_Symmetric_System/cppCode/ refresh run&
make -C 40_Butterfly_System/cppCode/ refresh run&
make -C 41_Line_Equilibrium_System/cppCode/ refresh run&
make -C 42_Mostly_Quadratic_System/cppCode/ refresh run&
make -C 43_Dissipative-Conservative_System/cppCode/ refresh run&
make -C 44_Time-Reversible_Reflection-Invariant_System/cppCode/ refresh run&
make -C 45_Plane_Equilibrium_System/cppCode/ refresh run&
make -C 46_Forced_Ueda_System/cppCode/ refresh run&
make -C 47_Megastable_System/cppCode/ refresh run&
make -C 48_Attracting_Torus_System/cppCode/ refresh run&
make -C 49_Buncha_System/cppCode/ refresh run&
make -C 50_Signum_Thermostat_System/cppCode/ refresh run&

