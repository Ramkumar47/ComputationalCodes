!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: model variables module
! description:
!    it contains declarations & definitions of model variables
!------------------------------------------------------------------------------

! model variables module definition
module modelVars

    ! using parameters module
    use parameters

    ! overriding automatic variable type assignment
    implicit none

    ! defining multi-dimensional variables
    real(kind=rkd),dimension(Nx,Ny) :: rho, u, v, p, T, mu, k, Txx, Txy, Tyy
    real(kind=rkd),dimension(Nx,Ny) :: qx, qy, e, U1, U2, U3, U5, F1, F2, F3
    real(kind=rkd),dimension(Nx,Ny) :: F5, E1, E2, E3, E5, dTdx, dTdy, dudx
    real(kind=rkd),dimension(Nx,Ny) :: dudy, dvdx, dvdy, X, Y, rho_old = 0

    ! defining scalar variables
    real(kind=rkd) :: deltaT, time = 0, convergenceResidual = 1.0


end module modelVars

