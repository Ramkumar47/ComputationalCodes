!------------------------------------------------------------------------------
! Heat condution in 2D plane, serial version
!
! file description : parameters and model variables definition
!------------------------------------------------------------------------------

! parameters module definition
module parameters

    implicit none

    ! defining uniform variable kinds
    integer,parameter :: ikd = selected_int_kind(8)
    integer,parameter :: rkd = selected_real_kind(8)

    ! length and width of domain
    real(kind=rkd), parameter :: Lx = 1.0, Ly = 1.0

    ! number of nodes in x and y direction
    integer(kind=ikd), parameter :: Nx = 100000, Ny = 3

    ! maximum iteration count
    integer(kind=ikd), parameter :: maxIterCount = 100000

    ! convergence residual
    real(kind=rkd), parameter :: convergence_value = 1e-8

    ! boundary values
    real(kind=rkd), parameter :: T_east = 300.0
    real(kind=rkd), parameter :: T_west = 300.0
    real(kind=rkd), parameter :: T_north = 400.0
    real(kind=rkd), parameter :: T_south = 300.0

    ! spacial step size
    real(kind=rkd), parameter :: dx = Lx/float(Nx-1)
    real(kind=rkd), parameter :: dy = Ly/float(Ny-1)

end module parameters

! model variables module
module modelVars

    use parameters

    implicit none

    ! defining multi-dimensional arrays
    real(kind=rkd), dimension(Ny,Nx) :: Ts, T, X,Y

    ! scalar variables definition
    real(kind=rkd) :: convergence_residual, A
    integer(kind=ikd) :: iter, i, j

end module modelVars
