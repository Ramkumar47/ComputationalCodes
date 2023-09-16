!------------------------------------------------------------------------------
! Solutin of 1D heat conduction with source using spectral methods
!
! subroutines definition file
!------------------------------------------------------------------------------

! defining initializer subroutine
subroutine initializer()

    ! using parameters and model variables modules
    use parameters
    use model_vars

    ! explicit declaration of variable types
    implicit none

    ! declaring needed variables
    integer(kind=ikd) :: i
    real(kind=rkd) :: dx = L/float(Nx-1)

    print *,"Initializing the variables"

    ! looping through to initialize the temperature and position variables
    do i = 1,Nx
        T(i) = Tw
        X(i) = float(i-1)*dx
    end do

end subroutine initializer

! defining solution writer subroutine
subroutine write()

    use parameters
    use model_vars

    implicit none

    ! declaring needed variables
    integer(kind=ikd) :: i

    ! declaring format to be followed in writing to the file
    50 format(f7.5,",",f9.5,",",f9.5)

    ! opening file to write the data
    open(unit=1, file="data.csv", status="replace")

    ! writing header line
    write(unit=1, fmt='(A)') "X,T,T_a"

    ! writing the data to file
    do i = 1,Nx
        write(unit=1, fmt=50) X(i),T(i),T_analytical(i)
    end do

    ! closing the file
    close(unit=1)

    print *,"data written to file"

end subroutine write
