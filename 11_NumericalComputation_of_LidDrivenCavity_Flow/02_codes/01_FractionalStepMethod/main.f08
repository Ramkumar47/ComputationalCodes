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
    ! mainloop: do itr = 1,N_timestep
    mainloop: do itr = 1,1015

        ! solving momentum equation
        call solve_mmtmEqn()

        ! correcting pressure
        call solve_pEqn()

        ! updating velocity with corrected pressure
        call update_velocity()

        ! updating on screen
        print *,"iteration : ",itr,"; time = ",time

        ! updating timestep
        time = time + dt;

    end do mainloop

    ! writing output to file
    call write_csv()

end program main
