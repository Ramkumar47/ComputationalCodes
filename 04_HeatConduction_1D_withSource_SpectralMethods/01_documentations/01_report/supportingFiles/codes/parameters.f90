!------------------------------------------------------------------------------
! Solutin of 1D heat conduction with source using spectral methods
!
! parameters and model variables module definition file
!------------------------------------------------------------------------------

! computation parameter variables definition
module parameters

    ! explicit definition of variable types
    implicit none

    ! defining precision and type for real and integer kind variables
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! number of terms to be taken in the sine series and number of vertex
    ! points to be taken in the x direction
    integer(kind=ikd), parameter :: N_terms = 40, Nx = 101

    ! length in x direction
    real(kind=rkd), parameter :: L = 1.0

    ! defining pi value
    real(kind=rkd), parameter :: PI = 4.0*atan(1.0)

    ! defining thermal conductivity and heat source values
    real(kind=rkd), parameter :: k = 1.0, q = 1000.0

    ! defining temperature values at west and east end of the domain
    real(kind=rkd), parameter :: Tw = 300.0, Te = 500.0

end module parameters

! model variables definition
module model_vars

    ! using parameters module
    use parameters

    ! explicit definition of variable types
    implicit none

    ! defining temperature and position arrays
    real(kind=rkd), dimension(Nx) :: T, X, T_analytical

end module model_vars
