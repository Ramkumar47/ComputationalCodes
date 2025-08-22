#!/bin/bash

for dir in ../../*_System
do
    echo $dir

    # sed -i '/An animation showing /c\An animation of the pre-computed solution trajectory for the given chaotic' $dir/index.qmd
    #
    # sed -i '/colored with the local lyapunov/c\system is presented below. The trajectory, spanning 10^3^ seconds, is colored' $dir/index.qmd
    #
    # sed -i '/be seen below./c\according to the calculated local Lyapunov exponents at each point in time.' $dir/index.qmd

    # sed '/^below./c\i dont know' $dir/index.qmd

    # sed -i 's/Lyapunov exponents/[Lyapunov exponents](https:\/\/en.wikipedia.org\/wiki\/Lyapunov_exponent)\{target="blank"\}/' $dir/index.qmd


#     sed -i "26 a\
# The colormap selected for the aforementioned animation employs a blue-green-red \
# gradient. The blue to green range corresponds to negative Lyapunov exponents, \
# signifying regions where the system's predictability decreases. Conversely, the \
# green to red range corresponds to positive Lyapunov exponents, indicative of \
# regions where the system exhibits an increase in unpredictability.\n " $dir/index.qmd


    # sed -i '/Further, the real-time/c\Furthermore, the real-time simulation may be executed up to the designated end' $dir/index.qmd
    # sed -i '/below./c\time as indicated below. As the simulation progresses, the 3D view of trajectory' $dir/index.qmd

#     sed -i "30 a\
# evolution can be explored by click-drag & scroll options in the mouse\/touchpad." $dir/index.qmd

    # sed -i "32 a\
    # The visualization was made using \
    # [P5.js](https://p5js.org/){target=\"blank\"}.\n " $dir/index.qmd

    # sed -i '20d' $dir/index.qmd

#     sed -i "19 a\
# system is presented below. The trajectory, spanning 10^3^ seconds, is colored" $dir/index.qmd

    # sed -i "25 a\
    #     A left-to-right 360^o^ view of the chaotic system trajectory" $dir/index.qmd

    # sed -i "s/Simulation/System description/" $dir/index.qmd


    # sed -i "29 a\
    #     ## Real-time simulation \n" $dir/index.qmd

    sed -i "s/Furthermore, the/The/" $dir/index.qmd
    sed -i "s/may be executed/can be executed/" $dir/index.qmd

    # break

done
