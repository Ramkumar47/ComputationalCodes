!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: grid genration subroutines
! description:
!    it contains subroutines related to the grid genration process
!------------------------------------------------------------------------------

! physical grid generation
! subroutine-------------------------------------------------------------------
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

    ! checking if to read the grid from file
    if (read_grid_from_file) then
        call read_grid()
    else
        ! constructing grid
        do i = 1,Nx
            do j = 1,Ny
                X(j,i) = float(i-1)*deltaX
                Y(j,i) = float(j-1)*deltaY
            end do
        end do
        print *,"grid generated"
    endif

    ! writing grid coordinates to file
    call write_grid()

    ! generating computational grid
    call generate_computationGrid()

end subroutine generateGrid

! computational grid generation
! subroutine-------------------------------------------------------------------
subroutine generate_computationGrid()

    ! importing needed modules
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring and initializing locally needed variables
    integer(kind=ikd) :: i,j

    ! initializing computation plane grid basis
    Eta = 0.0; Eps = 0.0

    ! computing grid
    do i = 1,Nx
        do j = 1,Ny
            Eps(j,i) = float(i-1)
            Eta(j,i) = float(j-1)
        end do
    end do

    ! fixing step values
    dEta = 1.0
    dEps = 1.0

    ! computing inverse metrics
    do i = 2,Nx-1
        dXdEps(:,i) = (X(:,i+1) - X(:,i-1))/dEps/2.0
        dYdEps(:,i) = (Y(:,i+1) - Y(:,i-1))/dEps/2.0
    end do
    dXdEps(:,1) = (X(:,2) - X(:,1))/dEps
    dYdEps(:,1) = (Y(:,2) - Y(:,1))/dEps
    dXdEps(:,Nx) = (X(:,Nx) - X(:,Nx-1))/dEps
    dYdEps(:,Nx) = (Y(:,Nx) - Y(:,Nx-1))/dEps

    do j = 2,Ny-1
        dXdEta(j,:) = (X(j+1,:) - X(j-1,:))/dEta/2.0
        dYdEta(j,:) = (Y(j+1,:) - Y(j-1,:))/dEta/2.0
    end do
    dXdEta(1,:) = (X(2,:) - X(1,:))/dEta
    dYdEta(1,:) = (Y(2,:) - Y(1,:))/dEta
    dXdEta(Ny,:) = (X(Ny,:) - X(Ny-1,:))/dEta
    dYdEta(Ny,:) = (Y(Ny,:) - Y(Ny-1,:))/dEta

    ! computing jacobian matrix
    Jac = dXdEps*dYdEta - dXdEta*dYdEps

    print *,"computed grid transformation variables"

end subroutine generate_computationGrid

! subroutine to write the grid to
! file-------------------------------------------------------------------------
subroutine write_grid()

    ! importing needed modules
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring and initializing locally needed variables
    integer(kind=ikd) :: i,j

    ! opening new file
    open(unit = 1, file="grid.dat")

    ! writing number of nodes in the first line
    write(unit = 1, fmt='(I5 I5)') Nx,Ny

    ! writing coordinates in column wise order
    do i = 1,Nx
        do j = 1,Ny
            write(unit = 1, fmt='(es16.8 es16.8)') X(j,i), Y(j,i)
        end do
    end do

    ! closing file
    close(unit = 1)

    print *,"grid written to file : grid.dat"

end subroutine write_grid

! subroutine to read the grid from
! file-------------------------------------------------------------------------
subroutine read_grid()

    ! importing needed modules
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! NOTE: the values of Nx and Ny have to be manually specified
    ! in the parameters file, due to its constant nature

    ! declaring and initializing locally needed variables
    integer(kind=ikd) :: i,j

    ! opening input grid file
    open(unit = 1, file = "input_grid.dat", status="old")

    ! reading first line containing Nx and Ny, and dumping them
    read(unit = 1, fmt=*)

    ! reading coordinates from the file
    do i = 1,Nx
        do j = 1,Ny
            read(unit = 1, fmt='(es16.8 es16.8)') X(j,i), Y(j,i)
        end do
    end do

    ! closing the file
    close(unit = 1)

    print *,"grid read from the file : input_grid.dat"


end subroutine read_grid
