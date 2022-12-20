!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: grid genration subroutines
! description:
!    it contains subroutines related to the grid genration process
!------------------------------------------------------------------------------

! rectangular grid generation subroutine
subroutine generateGrid()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring and initializing locally needed variables
    integer(kind=ikd) :: i,j

    ! initializing coordinate arrays
    X = 0.0; Y = 0.0

    ! constructing grid
    do i = 1,Nx
        do j = 1,Ny
            X(i,j) = float(i-1)*deltaX
            Y(i,j) = float(j-1)*deltaY
        end do
    end do

    print *,"grid generated"


end subroutine generateGrid
