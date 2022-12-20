!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: write data functions file
! description:
!    it contains subroutines related to writing computed data to file
!------------------------------------------------------------------------------

! master write data subroutine
! definition-------------------------------------------------------------------
subroutine write_data()

    ! importing needed modules
    use parameters

    ! overriding automatic variable type assignment
    implicit none

    ! checking file type to write
    if (fileType == "csv") then
        call write_csv()
    else
        print *,"Error!, unknown file type to write ! ",fileType
    end if

end subroutine write_data

! csv file writer subroutine
! definition-------------------------------------------------------------------
subroutine write_csv()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring local variables
    integer(kind=ikd) :: i,j

    ! creating new directory to store the computed data
    call system("rm -rf solution_files")
    call system("mkdir solution_files")

    ! opening file
    open(unit = 1, file = "solution_files/data.csv")

    ! writing header
    write(unit = 1, fmt = '(A)') "X,Y,Z,u,v,p,rho,T"

    ! format specifier
    50 format(f12.10","f12.10","f12.10","f12.5","f12.5","f12.5","f12.5","f12.5)

    ! looping through the nodes
    do i = 1,Nx
        do j = 1,Ny
            write(unit = 1, fmt = 50) X(i,j),Y(i,j),0.0,u(i,j),v(i,j),p(i,j), &
                                rho(i,j),T(i,j)
        end do
    end do

    ! closing file
    close(unit = 1)

    print *,"written data to file"

end subroutine write_csv
