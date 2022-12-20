!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: main program file
! description:
!    it contains the main program snippet
!------------------------------------------------------------------------------

! main program begin
program main

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring local variables
    integer(kind=ikd) :: icount = 0

    ! calling initializer subroutine
    call initializer()

    ! solver main loop
    mainloop: do while ((time .LE. maxSimTime) .AND. (icount .LE. maxTSCount))

        ! calculating timestep
        call compute_deltaT()

        ! calling solver

        ! updating boundary conditions
        call apply_bc()

        ! updating screen and checking convergence
        call check_convergence()
        print *, "time : ",time,"; icount : ",icount,"; residual : ", &
                convergenceResidual
        if (convergenceResidual < convergenceValue) then
            print *,"Solution converged!"
            exit mainloop
        end if

        ! updating simulation time and icount
        time = time + deltaT
        icount = icount + 1

    end do mainloop

    ! writing data to file
    call write_data()


    print *,"End"

end program main
