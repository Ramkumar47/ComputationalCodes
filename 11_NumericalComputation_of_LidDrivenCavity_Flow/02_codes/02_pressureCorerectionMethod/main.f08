!------------------------------------------------------------------------------
! Navier Stokes Solver using FDM
! Lid driven cavity flow problem
!
! Main solver code
!------------------------------------------------------------------------------

program main

    ! importing needed modules
    use modelVars

    ! initializing flow field variables
    call initializer()

    ! begin main loop computation
    mainloop: do itr = 1,N_timestep
    ! mainloop: do itr = 1,10

        ! solving momentum equation
        call solve_mmtmEqn()

        ! correcting pressure
        call solve_pEqn()

        ! update velocity
        call update_velocity()

        ! updating on screen
        print *,"iteration : ",itr,"/",N_timestep,"; time = ",time

        if (mod(itr,1000) == 0) then
            ! interpolate fields
            call interpolate_field()
            ! writing output to file
            call write_csv()
        endif

        ! updating timestep
        time = time + dt;

    end do mainloop

    ! ! interpolate fields
    ! call interpolate_field()
    !
    ! ! writing output to file
    ! call write_csv()

end program main
