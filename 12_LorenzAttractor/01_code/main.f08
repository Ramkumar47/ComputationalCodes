!-----------------------------------------------------------------------------!
! Lorentz Attractor simulation code                                           !
! main program file                                                           !
!-----------------------------------------------------------------------------!

program main

    ! importing needed modules
    use modelVars

    implicit none

    ! initializing computation properties
    call initializer()

    ! begin main computation
    mainloop: do while (time <= end_time)

        ! computing field
        call solver()

        ! updating time and screen
        time = time + dt
        print *,"time = ",time," s"

        ! writing data to file
        call write_data()

    end do mainloop

    ! print solution end
    print *,"End"

end program main
