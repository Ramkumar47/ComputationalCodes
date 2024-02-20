!------------------------------------------------------------------------------
! Particle swarm optimization of temperature profile
!------------------------------------------------------------------------------
program main

    use parameters
    use modelVariables

    implicit none

    integer(kind=ikd) :: itr

    ! initializing the variables
    call initializer()

    ! performing optimization
    mainloop: do itr = 1,N_itr

        ! updating velocity
        call updateVelocity()

        ! updating position
        call updatePosition()

        ! computing pbest and gbest
        call computePbestGbest()

        ! writing computed data to file
        call writeData()

        print *,"iteration : ",itr,"; f_gbest : ",f_gbest,"; G_bestLoc : ",gbest

    end do mainloop

    print*,"done"

    ! closing the file
    close(unit=1)


end program main
