!------------------------------------------------------------------------------
! Numerical solution of 2D Heat Conduction Equation using FDM
! file: Main program
!------------------------------------------------------------------------------

! main program definition------------------------------------------------------
program main

    use params
    use modelvars

    implicit none

    ! initializing the variables
    call initializer()

    ! main solution loop
    main_loop: do itr = 1,max_iteration

        ! solving the equation
        call solve()

        ! checking convergence
        residual = maxval(abs(T_prev - T))
        T_prev = T
        if ( residual < 1e-6) then
            print *,"solution converged!"
            exit
        end if

        print *,"iteration = ",itr,"; residual = ",residual

    end do main_loop

    ! writing computed data to file
    call write_data()

    print *,"End"

end program main

!------------------------------------------------------------------------------
