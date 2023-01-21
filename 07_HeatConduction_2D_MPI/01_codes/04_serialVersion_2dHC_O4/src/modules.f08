!------------------------------------------------------------------------------!
! 2D Heat conduction solver using 4th order accurate Central diff. scheme      !
! Serial version code                                                          !
!                                                                              !
! modules definitions                                                          !
!------------------------------------------------------------------------------!

! simulation parameters module definition
module parameters

    implicit none

    ! defining variable precision types
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! defining number of nodes in the computation domain
    integer(kind=ikd), parameter :: Nx = 101, Ny = 101
    integer(kind=ikd), parameter :: Ng = 1 ! no. of ghost nodes @ boundary

    ! defining length and width of the domain
    real(kind=rkd), parameter :: Lx = 0.01, Ly = 0.01

    ! boundary temperatures definition
    real(kind=rkd), parameter :: T_east = 293.0
    real(kind=rkd), parameter :: T_west = 373.0
    real(kind=rkd), parameter :: T_north = 293.0
    real(kind=rkd), parameter :: T_south = 293.0

    ! defining max number of iterations and convergence criterion
    integer(kind=ikd), parameter :: N_iterations = 10000
    real(kind=rkd), parameter :: convergence_value = 1e-6

end module parameters

! model variables module definition
module modelVariables

    use parameters

    implicit none

    ! defining scalar variables
    integer(kind=ikd),parameter :: Nxg = Nx+2*Ng, Nyg = Ny+2*Ng
    integer(kind=ikd) :: i,j, iter
    real(kind=rkd) :: dx = Lx/float(Nx-1), dy = Ly/float(Ny-1)
    real(kind=rkd) :: convergence_residual
    real(kind=rkd) :: A,B,C

    ! defining multi-dimensional variables
    real(kind=rkd), dimension(Nyg,Nxg) :: T, T_old, X,Y

end module modelVariables
