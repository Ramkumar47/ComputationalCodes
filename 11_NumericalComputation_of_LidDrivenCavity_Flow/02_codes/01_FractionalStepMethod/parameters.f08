!------------------------------------------------------------------------------
! Navier Stokes Solver using FDM
! Lid driven cavity flow problem
!
! parameters definition file
!------------------------------------------------------------------------------

! parameters module
module parameters

    ! overriding pre-allocation of datatypes
    implicit none

    ! defining kind of variables
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! length of domain in x and y directions
    real(kind=rkd), parameter :: Lx = 0.01, Ly = 0.01

    ! fluid parameters
    real(kind=rkd), parameter :: rho = 1.225, nu = 1.4604e-5

    ! number of grid points in x and y direction
    integer(kind=ikd), parameter :: Nx = 101, Ny = 101

    ! plate velocity definition
    real(kind=rkd), parameter :: Uplate = 1.4604

    ! simulation time and timestep
    real(kind=rkd), parameter :: endTime = 1.0, dt = 1e-5


end module parameters

! model variables module
module modelVars

    ! importing needed modules
    use parameters

    ! scalar variables
    real(kind=rkd) :: time, dx, dy

    ! label variables
    integer(kind=ikd) :: itr, i,j, N_timestep = 0

    ! scalar arrays
    real(kind=rkd),dimension(Nx,Ny) :: U,Us,V,Vs,P,X,Y,Ps = 0, pp,source

    ! declaring character strings for filename
    character(len=50) :: filename


end module modelVars
