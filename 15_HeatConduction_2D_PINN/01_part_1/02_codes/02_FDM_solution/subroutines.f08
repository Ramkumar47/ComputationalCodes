!------------------------------------------------------------------------------
! Numerical solution of 2D Heat Conduction Equation using FDM
! file: subroutines definition
!------------------------------------------------------------------------------

! defining initializer subroutine
subroutine initializer()

    use params
    use modelvars

    implicit none

    ! initializing grid points
    do i = 1,nx
        do j = 1,ny
            x(j,i) = dx*float(i-1)
            y(j,i) = dy*float(j-1)
        end do
    end do

    ! initializing temperature
    T = theta_cold
    T(:,1) = theta_hot

    print *,"initialization done!"

end subroutine initializer

! defining solver module-------------------------------------------------------
subroutine solve()

    use params
    use modelvars

    implicit none

    ! defining a constant to be used in the computation
    real(kind=rkd), parameter :: a = 2.0/dx**2 + 2.0/dy**2

    ! solving the equation
    do i = 2,nx-1
        do j = 2,ny-1
            T(j,i) = 1/a*((T(j,i+1)+T(j,i-1))/dx**2+(T(j+1,i)+T(j-1,i))/dy**2)
        end do
    end do

end subroutine solve

! defining data write module---------------------------------------------------
subroutine write_data()

    use params
    use modelvars

    implicit none

    ! opening new file
    open(unit =1, file="computed_data.csv")

    ! defining format to write the data
    50 format(f12.8,",",f12.8,",",f12.8)

    ! writing header
    write(unit=1,fmt = *) "X,Y,T"

    ! writing data to file
    do i = 1,nx
        do j = 1,ny
            write(unit = 1, fmt = 50) x(j,i), y(j,i), T(j,i)
        end do
    end do

    close(unit=1)

    print *,"computed data written to the file!"

end subroutine write_data

!------------------------------------------------------------------------------
