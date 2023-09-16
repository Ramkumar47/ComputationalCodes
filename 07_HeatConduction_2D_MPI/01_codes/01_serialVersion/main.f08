!------------------------------------------------------------------------------
! Heat condution in 2D plane, serial version
!
! file description : main program definition
!------------------------------------------------------------------------------

! main program
program main

    use mpi
    use modelVars

    print *, "initializing T field"
    T = 300.0
    T(:,Nx) = T_east
    T(:,1) = T_west
    T(1,:) = T_south
    T(Ny,:) = T_north
    Ts = T

    print *,"initializing grid"
    X = 0.0
    Y = 0.0
    do i = 1,Nx
        do j = 1,Ny
            X(j,i) = i*dx
            Y(j,i) = j*dy
        end do
    end do

    ! supporting variables definition
    A = 2.0/dx**2 + 2.0/dy**2

    ! begining iteration
    main_loop: do iter = 1,maxIterCount

        ! looping through grid points
        do i = 2,Nx-1
            do j = 2,Ny-1
                Ts(j,i) = 1.0/A*((T(j,i+1)+T(j,i-1))/dx**2+(T(j+1,i)+T(j-1,i))/dy**2)
            end do
        end do

        ! computing residual
        convergence_residual = maxval(abs(Ts - T))
        T = Ts

        ! printing status
        50 format("iteration : ",I10,"; residual : ",ES16.8)
        print 50, iter,convergence_residual

        ! ! checking convergence
        ! if (convergence_residual < convergence_value) then
        !     print *,"solution converged !"
        !     exit main_loop
        ! endif

    end do main_loop

    ! writing data to file
    call write_csv()

end program main
