!-----------------------------------------------------------------------------!
! Lorentz Attractor simulation code                                           !
! subroutines definition file                                                 !
!-----------------------------------------------------------------------------!

! initializer subroutine
! definition-------------------------------------------------------------------
subroutine initializer()

    ! importing needed modules
    use modelVars

    ! overriding implicit datatype definition
    implicit none

    ! inizializing computation variables
    x = x_init
    y = y_init
    z = z_init
    x_new = 0.0; y_new = 0.0; z_new = 0.0

    time = 0.0

    ! initializing the data file
    open(unit = 1, file = 'solution_data/data.csv')
    write(unit = 1, fmt = *) "X Y Z"
    close(unit = 1)

end subroutine initializer

! equations subroutine definition for
! RK4--------------------------------------------------------------------------
! x - equation
subroutine f_x(xin,xout)

    ! importing needed modules
    use modelVars

    implicit none

    real(kind=rkd), intent(in) :: xin
    real(kind=rkd), intent(out) :: xout

    ! equation definition
    xout = sigma*(y - xin)

end subroutine f_x

! y - equation
subroutine f_y(yin, yout)

    ! importing needed modules
    use modelVars

    implicit none

    real(kind=rkd), intent(in) :: yin
    real(kind=rkd), intent(out) :: yout

    ! equation definition
    yout = x*(rho - z) - yin

end subroutine f_y

! z - equation
subroutine f_z(zin, zout)

    ! importing needed modules
    use modelVars

    implicit none

    real(kind=rkd), intent(in) :: zin
    real(kind=rkd), intent(out) :: zout

    ! equation definition
    zout = x*y - beta*zin

end subroutine f_z

! main solver subroutine
! definition-------------------------------------------------------------------
subroutine solver()

    ! importing needed modules
    use modelVars

    ! overriding implicit datatype definition
    implicit none

    ! solving x equation with RK4
    call f_x(x,k1)              ! RK-step 1
    call f_x(x+k1/2*dt,k2)      ! RK-step 2
    call f_x(x+k2/2*dt,k3)      ! RK-step 3
    call f_x(x+k3*dt,k4)        ! RK-step 4
    x_new = x + dt/6.0*(k1 + 2.0*k2 + 2.0*k3 + k4)

    ! solving y equation with RK4
    call f_y(y,k1)              ! RK-step 1
    call f_y(y+k1/2*dt,k2)      ! RK-step 2
    call f_y(y+k2/2*dt,k3)      ! RK-step 3
    call f_y(y+k3*dt,k4)        ! RK-step 4
    y_new = y + dt/6.0*(k1 + 2.0*k2 + 2.0*k3 + k4)

    ! solving z equation with RK4
    call f_z(z,k1)              ! RK-step 1
    call f_z(z+k1/2*dt,k2)      ! RK-step 2
    call f_z(z+k2/2*dt,k3)      ! RK-step 3
    call f_z(z+k3*dt,k4)        ! RK-step 4
    z_new = z + dt/6.0*(k1 + 2.0*k2 + 2.0*k3 + k4)

    ! updating the variables
    x = x_new
    y = y_new
    z = z_new

end subroutine solver

! write_data subroutine
! definition-------------------------------------------------------------------
subroutine write_data

    ! importing needed modules
    use modelVars

    ! overriding implicit datatype definition
    implicit none

    ! opening file with append access
    open(unit = 1, file = 'solution_data/data.csv', Access = 'append', &
        status = 'old')
    write(unit = 1, fmt = *) x,y,z
    close(unit = 1)

    print *,"write data done"

end subroutine write_data
