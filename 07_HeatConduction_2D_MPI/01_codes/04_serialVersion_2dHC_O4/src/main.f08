!------------------------------------------------------------------------------!
! 2D Heat conduction solver using 4th order accurate Central diff. scheme      !
! Serial version code                                                          !
!                                                                              !
! main program                                                                 !
!------------------------------------------------------------------------------!

program main

    ! importing needed modules
    use modelVariables

    ! over-riding default declaration of variable types
    implicit none

    ! initializing flow field variables
    call initializer()

    ! beginning computation
    mainloop: do iter = 1, N_iterations

        ! initializing ghost node values
        call update_ghostNodes()

        ! computing field values : guss seidel method
        do i = 2+Ng, Nxg-1-Ng
            do j = 2+Ng, Nyg-1-Ng
                ! computing parts of equation
                A = 1.0/dx**2*(-1.0/12.0*T(j,i+2)+4.0/3.0*T(j,i+1) &
                                + 4.0/3.0*T(j,i-1)-1.0/12.0*T(j,i-2))
                B = 1.0/dy**2*(-1.0/12.0*T(j+2,i)+4.0/3.0*T(j+1,i) &
                                + 4.0/3.0*T(j-1,i)-1.0/12.0*T(j-2,i))
                C = 5.0/2.0*(1.0/dx**2 + 1.0/dy**2)

                T(j,i) = 1.0/C*(A+B)
            end do
        end do

        ! computing residual
        convergence_residual = maxval(abs(T-T_old))
        T_old = T

        print *,"iteration = ", iter,"; residual = ",convergence_residual

        if (convergence_residual < convergence_value) then
            print *,"solution converged ! "
            exit mainloop
        endif

    end do mainloop

    ! writing data to csv file
    call write_csv()

    print *,"End"

end program main
