! csv file writer subroutine
! definition-------------------------------------------------------------------
subroutine write_csv()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! creating new directory to store the computed data
    call system("rm -rf solution_files_csv")
    call system("mkdir solution_files_csv")

    ! opening file
    open(unit = 1, file = "solution_files_csv/data.csv")

    ! writing header
    write(unit = 1, fmt = '(A)') "X,Y,Z,T"

    ! format specifier
    50 format(es16.8","es16.8","es16.8","es16.8","es16.8)

    ! looping through the nodes
    do i = 1,Nx
        do j = 1,Ny
            write(unit = 1, fmt = 50) X(j,i),Y(j,i),0.0,T(j,i)
        end do
    end do

    ! closing file
    close(unit = 1)

    print *,"written data to csv file"

end subroutine write_csv

