!------------------------------------------------------------------------------
! Heat condution in 1D plane
!
! file description : parameters and model variables definition
!------------------------------------------------------------------------------

! parameters module definition
module parameters

    implicit none

    ! defining uniform variable kinds
    integer,parameter :: ikd = selected_int_kind(8)
    integer,parameter :: rkd = selected_real_kind(8,8)

    ! length of domain
    real(kind=rkd), parameter :: Lx = 1.0

    ! number of nodes in x
    integer(kind=ikd), parameter :: Nx = 99999

    ! number of processes
    integer(kind=ikd), parameter :: num_procs = 4

    ! maximum iteration count
    integer(kind=ikd), parameter :: maxIterCount = 100000

    ! convergence residual
    real(kind=rkd), parameter :: convergence_value = 1e-8

    ! boundary values
    real(kind=rkd), parameter :: T_east = 400.0
    real(kind=rkd), parameter :: T_west = 300.0

    ! thermal conductivity and heat source
    real(kind=rkd), parameter :: k = 1.0
    real(kind=rkd), parameter :: Q_source = 0.0

    ! spacial step size
    real(kind=rkd), parameter :: dx = Lx/float(Nx-1)

end module parameters

! model variables module
module modelVars

    use parameters

    implicit none

    ! computing chunk data size
    integer(kind=ikd), parameter :: N_chunk = Nx/num_procs

    ! defining multi-dimensional arrays
    real(kind=rkd), dimension(Nx) :: T, X
    real(kind=rkd), dimension(N_chunk) :: T_chunk
    real(kind=rkd), dimension(N_chunk+1) :: T_chunk_bc
    real(kind=rkd), dimension(N_chunk+2) :: T_chunk_bc2

    ! scalar variables definition
    real(kind=rkd) :: convergence_residual, conv_res_1,T_bc, T_bcl, T_bcr
    integer(kind=ikd) :: iter, i, ierror, proc_id, num_procs_input

end module modelVars
