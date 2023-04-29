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
            X(j,i) = float(i-1)*dx
            Y(j,i) = float(j-1)*dy
        end do
    end do

    ! initializing flow field
    U = 0; U(nuy,:) = Uplate; Us = U
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
    real(kind = rkd) :: F_term, D_term, P_term, va,vb,uc,ud

    ! solving x-momentum equation
    do i = 2,nux-1
        do j = 2,nuy-1
            va = 0.5*(v(j,i) + v(j,i+1))
            vb = 0.5*(v(j-1,i) + v(j-1,i+1))

            ! convection term
            F_term = (u(j,i+1)**2 - u(j,i-1)**2)/dx/2.0 + &
                (u(j+1,i)*va - u(j-1,i)*vb)/dy/2.0

            ! diffusion term
            D_term = nu*(u(j,i+1) - 2.0*u(j,i) + u(j,i-1))/dx**2 + &
                nu*(u(j+1,i) - 2.0*u(j,i) + u(j-1,i))/dy**2

            ! pressure term
            P_term = 1.0/rho*(p(j,i+1) - p(j,i))/dx

            us(j,i) = u(j,i) + dt*(-F_term + D_term - P_term)
        end do
    end do

    ! solving y-momentum equation
    do i = 2,nvx-1
        do j = 2,nvy-1
            uc = 0.5*(u(j,i-1) + u(j+1,i-1))
            ud = 0.5*(u(j,i) + u(j+1,i))

            ! convection term
            F_term = (ud*v(j,i+1) - uc*v(j,i-1))/dx/2.0 + &
                    (v(j+1,i)**2 - v(j-1,i)**2)/dy/2.0

            ! diffusion term
            D_term = nu*(v(j,i+1) - 2.0*v(j,i) + v(j,i-1))/dx**2 + &
                nu*(v(j+1,i) - 2.0*v(j,i) + v(j-1,i))/dy**2

            ! pressure term
            P_term = 1.0/rho*(p(j+1,i) - p(j,i))/dy

            vs(j,i) = v(j,i) + dt*(-F_term + D_term - P_term)
        end do
    end do


end subroutine solve_mmtmEqn

! pressure equation solver
! subroutine-------------------------------------------------------------------
subroutine solve_pEqn()

    ! importing needed modules
    use modelVars

    implicit none

    ! ! declaring some local variables
    ! real(kind=rkd) :: dudx,dudy,dvdx,dvdy, coeff, err
    ! integer(kind=ikd) :: p_itr

    ! declaring some local variables
    real(kind=rkd) :: a,b,c,err
    integer(kind=ikd) :: p_itr

    ! computing coefficients
    a = 2.0*(dt/dx**2 + dt/dy**2)
    b = - dt/dx**2
    c = - dt/dy**2
    do i = 2,npx-1
        do j = 2,npy-1
            d(j,i) = rho/dx*(Us(j,i)-Us(j,i-1))+rho/dy*(Vs(j,i)-Vs(j-1,i))
        end do
    end do

    ! solving pressure correction equation
    pp = 0.0
    do p_itr = 1,100
        ! solving equation
        do i = 2,npx-1
            do j = 2,npy-1
                pp(j,i) = -1.0/a*(b*pp(j,i+1) + b*pp(j,i-1) + c*pp(j+1,i) + c*pp(j-1,i) + d(j,i))
            end do
        end do

        ! extrapolating pressure correction
        pp(:,1) = 2.0*pp(:,2) - pp(:,3)
        pp(:,npx) = 2.0*pp(:,npx-1) - pp(:,npx-2)
        pp(1,:) = 2.0*pp(2,:) - pp(3,:)
        pp(npy,:) = 2.0*pp(npy-1,:) - pp(npy-2,:)

        ! checking convergence
        err = maxval(abs(pp - pps))
        pps = pp

        if (err < 1e-4) then
            exit
        end if

    end do

    print *,"pressure converged in ",p_itr, err

    P = P + 0.1*pp

end subroutine solve_pEqn

! update velocity subroutine---------------------------------------------------
subroutine update_velocity()

    ! importing needed modules
    use modelVars

    implicit none

    ! updating x-velocity
    do i = 2,nux-1
        do j = 2,nuy-1
            U(j,i) = Us(j,i) - 0.1*dt/dx*(pp(j,i+1) - pp(j,i))
        end do
    end do

    do i = 2,nvx-1
        do j = 2,nvy-1
            V(j,i) = Vs(j,i) - 0.1*dt/dy*(pp(j+1,i) - pp(j,i))
        end do
    end do

    print *,"updated velocity"

end subroutine update_velocity

! interpolation subroutine
! definition-------------------------------------------------------------------
subroutine interpolate_field()

    ! importing needed modules
    use modelVars

    implicit none

    ! interpolating fields
    do i = 1,Nx
        do j = 1,Ny
            Ui(j,i) = 0.5*(u(j,i)+u(j+1,i))
            Vi(j,i) = 0.5*(v(j,i)+v(j,i+1))
            Pi(j,i) = 0.25*(p(j,i)+p(j,i+1)+p(j+1,i)+p(j+1,i+1))
        end do
    end do

    ! correcting boundary values
    Ui(:,1) = 0.0
    Ui(:,Nx) = 0.0
    Ui(1,:) = 0.0
    Ui(Ny,:) = Uplate

    Vi(:,1) = 0.0
    Vi(:,Nx) = 0.0
    Vi(1,:) = 0.0
    Vi(Ny,:) = 0.0

    ! print *,"interpolation done"

end subroutine interpolate_field

! write csv subroutine
! definition-------------------------------------------------------------------
subroutine write_csv()

    ! importing needed modules
    use modelVars

    implicit none

    ! preparing filename to write solution data
    write(filename, "(A,I0.10,A)") "solution_data_",filecount,".csv"

    ! opening file with filename
    open(unit = 1, file = "solution_data/"//filename)

    ! writing header
    write(unit = 1, fmt = "(A)") "X Y Z U V P Time"

    ! looping to write data to file
    do i = 1,Nx
        do j = 1,Ny
            write(unit = 1, fmt = *) X(j,i), Y(j,i), 0.0, Ui(j,i), Vi(j,i), Pi(j,i),time
        end do
    end do

    ! closing file
    close(unit = 1)

    ! print *,"solution data writen to csv file ", filename

    filecount = filecount + 1

end subroutine write_csv
