count=1
rm -rf slurmArrayRun/
mkdir slurmArrayRun
for dir in *_*
do
    cp -r $dir slurmArrayRun/$dir"_taskId_"$count
    count=$(( count+1 ))
    echo $dir
done
cp submitArray.sh slurmArrayRun/
