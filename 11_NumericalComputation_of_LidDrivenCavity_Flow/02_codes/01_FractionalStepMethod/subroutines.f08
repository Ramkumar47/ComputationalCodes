!------------------------------------------------------------------------------
! Navier Stokes Solver using FDM
! Lid driven cavity flow problem
!
! Subroutines definition file
!------------------------------------------------------------------------------

! initializer
! subroutine-------------------------------------------------------------------
subroutine initializer()

    ! importing needed modules
    use modelVars

    implicit none

    ! initializing grid
    dx = Lx/float(Nx-1)
    dy = Ly/float(Ny-1)
    do i = 1,Nx
        do j = 1,Ny
            X(i,j) = float(i-1)*dx
            Y(i,j) = float(j-1)*dy
        end do
    end do

    ! initializing flow field
    U = 0; U(:,1) = Uplate; Us = U
    V = 0; Vs = V; P = 0

    ! computing number of timesteps
    N_timestep = int(endTime/dt)

    print *,"initialization done"


end subroutine initializer

! momentum equation solver
! subroutine-------------------------------------------------------------------
subroutine solve_mmtmEqn()

    ! importing needed modules
    use modelVars

    implicit none

    ! declaring some local variables
    real(kind = rkd) :: F_term, D_term, P_term

    ! solving momentum equations
    do i = 2,Nx-1
        do j = 2,Ny-1
            ! x-momentum equation
            ! convection term
            F_term = U(i,j)*(U(i+1,j)-U(i-1,j))/dx/2.0 + &
                            V(i,j)*(U(i,j+1)-U(i,j-1))/dy/2.0
            Us(i,j) = U(i,j) + dt*(-F_term)

            ! diffusion term
            D_term = nu*((Us(i+1,j) - 2.0*Us(i,j) + Us(i-1,j))/dx**2 + &
                        (Us(i,j+1) - 2.0*Us(i,j) + Us(i,j-1))/dy**2)

            U(i,j) = Us(i,j) + dt*(D_term)

            ! y-momentum equation
            ! convection term
            F_term = U(i,j)*(V(i+1,j)-V(i-1,j))/dx/2.0 + &
                            V(i,j)*(V(i,j+1)-V(i,j-1))/dy/2.0
            Vs(i,j) = V(i,j) + dt*(-F_term)

            ! diffusion term
            D_term = nu*((Vs(i+1,j) - 2.0*Vs(i,j) + Vs(i-1,j))/dx**2 + &
                        (Vs(i,j+1) - 2.0*Vs(i,j) + Vs(i,j-1))/dy**2)
            V(i,j) = Vs(i,j) + dt*(D_term)

        end do
    end do

    ! print *,"solved mmtm eqn"


end subroutine solve_mmtmEqn

! pressure equation solver
! subroutine-------------------------------------------------------------------
subroutine solve_pEqn()

    ! importing needed modules
    use modelVars

    implicit none

    ! declaring some local variables
    real(kind=rkd) :: dudx,dudy,dvdx,dvdy, coeff, err
    integer(kind=ikd) :: p_itr

    coeff = 2.0/dx**2 + 2.0/dy**2

    ! computing source term
    do i = 2,Nx-1
        do j = 2,Ny-1
            dudx = (U(i+1,j) - U(i-1,j))/dx/2.0
            dvdx = (V(i+1,j) - V(i-1,j))/dx/2.0
            dudy = (U(i,j+1) - U(i,j-1))/dy/2.0
            dvdy = (V(i,j+1) - V(i,j-1))/dy/2.0

            source(i,j) = rho*(dudx*dudx + 2.0*dudy*dvdx+ dvdy*dvdy)
        end do
    end do

    P = 0.0

    ! solving pressure poisson equation
    do p_itr = 1,10
        ! solving equation
        do i = 2,Nx-1
            do j = 2,Ny-1
                P(i,j) = 1.0/coeff*((P(i+1,j)+P(i-1,j))/dx**2 + &
                             (P(i,j+1)+P(i,j-1))/dy**2 + source(i,j))
            end do
        end do

        ! updating boundary pressure
        P(:,1) = 2.0*P(:,2) - P(:,3)
        P(Nx,:) = 2.0*P(Nx-1,:) - P(Nx-2,:)
        P(:,Ny) = 0.0 !2.0*P(:,Ny-1) - P(:,Ny-2)
        P(1,:) = 2.0*P(2,:) - P(3,:)
        ! P(Nx,:) = 2.0*P(Nx-1,:) - P(Nx-2,:)
        ! P(:,1) = 0.0
        ! P(:,Ny) = P(:,Ny-1)
        ! P(1,:) = P(2,:)
        ! P(Nx,:) = P(Nx-1,:)

        ! ! checking convergence
        err = maxval(abs(Ps - P))
        Ps = P
        ! if (err < 1e-4) then
        !     exit
        ! end if

    end do

    print *,"solved p eqn : iteration = ",p_itr, err


end subroutine solve_pEqn

! update velocity subroutine---------------------------------------------------
subroutine update_velocity()

    ! importing needed modules
    use modelVars

    implicit none

    do i = 2,Nx-1
        do j = 2,Ny-1
            U(i,j) = U(i,j) + (P(i+1,j) - P(i-1,j))/dx/2.0*dt/rho
            V(i,j) = V(i,j) + (P(i,j+1) - P(i,j-1))/dy/2.0*dt/rho
        end do
    end do

    print *,"updated velocity"

end subroutine update_velocity

! write csv subroutine
! definition-------------------------------------------------------------------
subroutine write_csv()

    ! importing needed modules
    use modelVars

    ! preparing filename to write solution data
    write(filename, "(A,ES8.2,A)") "solution_data_",time,".csv"

    ! opening file with filename
    open(unit = 1, file = "solution_data/"//filename)

    ! writing header
    write(unit = 1, fmt = "(A)") "X Y Z U V P Source"

    ! looping to write data to file
    do i = 1,Nx
        do j = 1,Ny
            write(unit = 1, fmt = *) X(i,j), Y(i,j), 0.0, U(i,j), V(i,j), P(i,j), Source(i,j)
        end do
    end do

    ! closing file
    close(unit = 1)

    print *,"solution data writen to csv file", filename

end subroutine write_csv
