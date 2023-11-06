!------------------------------------------------------------------------------
! Numerical solution of 2D Heat Conduction Equation using FDM
! file: parameters nodules definition
!------------------------------------------------------------------------------

! defining simulation parameters definition
! file-------------------------------------------------------------------------
module params

    implicit none

    ! defining datatype
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! defining domain length and width
    real(kind=rkd), parameter :: L = 1.0, H = 1.0
    ! defining Hot and cold temperatures
    real(kind=rkd), parameter :: theta_hot = 1.0, theta_cold = 0.0
    ! defining number of grid points
    integer(kind=ikd), parameter :: nx = 1001, ny = 1001
    ! defining max iteration
    integer(kind=ikd), parameter :: max_iteration = 10000000

end module params

! deifning model variables
! module-----------------------------------------------------------------------
module modelvars

    use params

    implicit none

    ! defining integer scalars
    integer(kind=ikd) :: i,j,itr

    ! defining real scalars
    real(kind=rkd) :: residual

    ! computing dx and dy
    real(kind=rkd),parameter :: dx = L/float(nx-1), dy = H/float(ny-1)

    ! defining arrays to store field values and grid data points
    real(kind=rkd), dimension(ny,nx) :: x,y,T_prev,T

end module modelvars

!------------------------------------------------------------------------------
