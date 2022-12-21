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

    ! Note: the matrix allocation in here is (Rows, columns) hence, it is
    ! (Ny,Nx) and the pointer goes first through all rows of 1st column,
    ! then next column, and so on. Hence the for-loop has to be set accordinly
    ! for speed and efficiency in computation

    ! defining multi-dimensional variables
    real(kind=rkd),dimension(Ny,Nx) :: rho, u, v, p, T, mu, k, Txx, Txy, Tyy
    real(kind=rkd),dimension(Ny,Nx) :: qx, qy, e, U1, U2, U3, U5, F1, F2, F3
    real(kind=rkd),dimension(Ny,Nx) :: F5, E1, E2, E3, E5, dTdx, dTdy, dudx
    real(kind=rkd),dimension(Ny,Nx) :: dudy, dvdx, dvdy, X, Y, rho_old = 0

    ! defining scalar variables
    real(kind=rkd) :: deltaT, time = 0, convergenceResidual = 1.0


end module modelVars

