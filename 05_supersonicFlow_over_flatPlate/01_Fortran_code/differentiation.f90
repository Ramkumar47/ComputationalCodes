!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: differentiation computation file
! description:
!    it contains the module and subroutines related to differentiation
!------------------------------------------------------------------------------

! differentiation module
! definition-------------------------------------------------------------------
module differentiation

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! differentiation matrix definitions

    ! x-derivative central-difference matrix
    real(kind=rkd), dimension(Nx,Nx) :: Mddx_central = 0

    ! x-derivative forward-difference matrix
    real(kind=rkd), dimension(Nx,Nx) :: Mddx_forward = 0

    ! x-derivative backward-difference matrix
    real(kind=rkd), dimension(Nx,Nx) :: Mddx_backward = 0

    ! y-derivative central-difference matrix
    real(kind=rkd), dimension(Ny,Ny) :: Mddy_central = 0

    ! y-derivative forward-difference matrix
    real(kind=rkd), dimension(Ny,Ny) :: Mddy_forward = 0

    ! y-derivative backward-difference matrix
    real(kind=rkd), dimension(Ny,Ny) :: Mddy_backward = 0

end module differentiation

! Note: executable staatements cannot be placed directly inside module,
! hence populating matrices is done on separate subroutines

! subroutine to initiate populating all diff.
! matrices---------------------------------------------------------------------
subroutine populate_diffMatrices()

    implicit none

    ! populating Mddx_central
    call populate_Mddx_central()

    ! populating Mddx_forward
    call populate_Mddx_forward()

    ! populating Mddx_backward
    call populate_Mddx_backward()

    ! populating Mddy_central
    call populate_Mddy_central()

    ! populating Mddy_forward
    call populate_Mddy_forward()

    ! populating Mddy_backward
    call populate_Mddy_backward()

end subroutine populate_diffMatrices

! populate Mddx_central matrix
subroutine populate_Mddx_central()

    ! using differentiation  and parameters module
    use differentiation
    use parameters

    ! populating values
    Mddx_central(1,1) = -1.0
    Mddx_central(2,1) = 1.0
    Mddx_central(Nx,Nx) = 1.0
    Mddx_central(Nx-1,Nx) = -1.0

    do i = 2,Nx-1
        Mddx_central(i-1,i) = -0.5
        Mddx_central(i+1,i) = 0.5
    end do

    Mddx_central = Mddx_central / deltaX

end subroutine populate_Mddx_central

! populate Mddx_forward matrix
subroutine populate_Mddx_forward()

    ! using differentiation  and parameters module
    use differentiation
    use parameters

    ! populating values
    Mddx_forward(Nx-1,Nx) = -1.0
    Mddx_forward(Nx,Nx) = 1.0

    do i = 1,Nx-1
        Mddx_forward(i,i) = -1.0
        Mddx_forward(i+1,i) = 1.0
    end do

    Mddx_forward = Mddx_forward / deltaX

end subroutine populate_Mddx_forward

! populate Mddx_backward matrix
subroutine populate_Mddx_backward()

    ! using differentiation  and parameters module
    use differentiation
    use parameters

    ! populating values
    Mddx_backward(1,1) = -1.0
    Mddx_backward(2,1) = 1.0

    do i = 2,Nx
        Mddx_backward(i,i) = 1.0
        Mddx_backward(i-1,i) = -1.0
    end do

    Mddx_backward = Mddx_backward / deltaX

end subroutine populate_Mddx_backward

! populate Mddy_central matrix
subroutine populate_Mddy_central()

    ! using differentiation  and parameters module
    use differentiation
    use parameters

    ! populating values
    Mddy_central(1,1) = -1.0
    Mddy_central(1,2) = 1.0
    Mddy_central(Ny,Ny) = 1.0
    Mddy_central(Ny,Ny-1) = -1.0

    do i = 2,Ny-1
        Mddy_central(i,i-1) = -0.5
        Mddy_central(i,i+1) = 0.5
    end do

    Mddy_central = Mddy_central / deltaY

end subroutine populate_Mddy_central

! populate Mddy_forward matrix
subroutine populate_Mddy_forward()

    ! using differentiation  and parameters module
    use differentiation
    use parameters

    ! populating values
    Mddy_forward(Ny,Ny-1) = -1.0
    Mddy_forward(Ny,Ny) = 1.0

    do i = 1,Ny-1
        Mddy_forward(i,i) = -1.0
        Mddy_forward(i,i+1) = 1.0
    end do

    Mddy_forward = Mddy_forward / deltaY

end subroutine populate_Mddy_forward

! populate Mddy_backward matrix
subroutine populate_Mddy_backward()

    ! using differentiation  and parameters module
    use differentiation
    use parameters

    ! populating values
    Mddy_backward(1,1) = -1.0
    Mddy_backward(1,2) = 1.0

    do i = 2,Ny
        Mddy_backward(i,i) = 1.0
        Mddy_backward(i,i-1) = -1.0
    end do

    Mddy_backward = Mddy_backward / deltaY

end subroutine populate_Mddy_backward

