!-----------------------------------------------------------------------------!
! Lorentz Attractor simulation code                                           !
! parameters definition file                                                  !
!-----------------------------------------------------------------------------!

! computation parameters definition
! module-----------------------------------------------------------------------
module parameters

    ! overriding default datatype allocation
    implicit none

    ! defining global data precision
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! solution end time and timestep
    real(kind=rkd), parameter :: end_time = 500.0, dt = 1e-4

    ! initial perturbation conditions
    real(kind=rkd), parameter :: x_init = 0.1
    real(kind=rkd), parameter :: y_init = 0.1
    real(kind=rkd), parameter :: z_init = 0.1

    ! values of coefficients
    real(kind=rkd), parameter :: rho = 28.0
    real(kind=rkd), parameter :: sigma = 10.0
    real(kind=rkd), parameter :: beta = 8.0/3.0

end module parameters

! model variables definition
! module-----------------------------------------------------------------------
module modelVars

    ! importing parameters module
    use parameters

    ! overriding default datatype definition
    implicit none

    ! defining scalar variables
    real(kind=rkd) :: x,x_new,y,y_new,z,z_new,time
    real(kind=rkd) :: k1,k2,k3,k4

    ! defining integer label variables
    integer(kind=rkd) :: i


end module modelVars
