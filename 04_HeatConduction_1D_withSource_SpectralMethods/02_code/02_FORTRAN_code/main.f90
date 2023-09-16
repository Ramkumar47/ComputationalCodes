!------------------------------------------------------------------------------
! Solutin of 1D heat conduction with source using spectral methods
!
! Main fortran file
!
! developed by Ramkumar S.
!------------------------------------------------------------------------------

! begin main program
program main

    ! using parameters and model_variables modules
    use parameters
    use model_vars

    ! explicit definition of variable types
    implicit none

    ! declaring needed variables
    integer(kind=ikd) :: i,n
    real(kind=rkd) :: sumVal = 0.0, an, A = 1.0/L*(Te-Tw + q*L**2/2.0/K)

    ! initializing the variables
    call initializer()

    print *, "Computing temperature at each node"

    ! main loop to compute temperature at each node point
    do i = 1,Nx
        ! initializing sum variable
        sumVal = 0.0
        ! sub loop running for summation of sine terms
        do n = 1,N_terms
           ! computing coefficient
           an = 2.0*Q/k*L**2/(n*pi)**3*(1.0-(-1.0)**n)

           ! adding to the sum variable
           sumVal = sumVal + an*sin(n*pi/L*X(i))

           ! computing the current temperature node value
           T(i) = Tw + (Te-Tw)*X(i)/L + sumVal

           ! computing analytical solution
           T_analytical(i) = -q*X(i)**2/2.0/k + A*X(i) + Tw
        end do
    end do

    ! writing data to the file
    call write()

end program main
