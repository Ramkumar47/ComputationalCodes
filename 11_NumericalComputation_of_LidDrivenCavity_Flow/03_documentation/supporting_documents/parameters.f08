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
    real(kind=rkd), parameter :: Lx = 2.0, Ly = 2.0

    ! fluid parameters
    real(kind=rkd), parameter :: rho = 1.225, nu = 1.4604e-5

    ! number of grid points in x and y direction
    integer(kind=ikd), parameter :: Nx = 101, Ny = 101

    ! plate velocity definition
    real(kind=rkd), parameter :: Uplate = 1.0

    ! simulation time and timestep
    real(kind=rkd), parameter :: endTime = 300.0, dt = 1e-3

    ! initializing grid points
    integer(kind=rkd), parameter :: npx = nx + 1, npy = ny + 1
    integer(kind=rkd), parameter :: nux = npx - 1, nuy = npy
    integer(kind=rkd), parameter :: nvx = npx, nvy = npy - 1

end module parameters

! model variables module
module modelVars

    ! importing needed modules
    use parameters

    ! scalar variables
    real(kind=rkd) :: time, dx, dy

    ! label variables
    integer(kind=ikd) :: itr, i,j, N_timestep = 0, filecount = 1

    ! scalar arrays
    real(kind=rkd),dimension(Nx,Ny) :: X,Y,Ui,Vi,Pi
    real(kind=rkd), dimension(nuy,nux) :: U,Us
    real(kind=rkd), dimension(nvy,nvx) :: V,Vs
    real(kind=rkd), dimension(npy,npx) :: P,PP,d,PPs

    ! declaring character strings for filename
    character(len=50) :: filename


end module modelVars
