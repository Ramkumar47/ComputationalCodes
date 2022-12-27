!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: initialization and calculation file
! description:
!    it contains subroutines related to computation fields initialization
!    and calculation
!------------------------------------------------------------------------------

! initializer subroutine
! definition-------------------------------------------------------------------
subroutine initializer()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    if (resume_simulation .eq. 0) then ! fresh start of simulation
        ! generating grid
        call generateGrid()

        ! initializing flow field primitive variables
        p = P_inf
        rho = P_inf/R/T_inf
        u = M_inf*sqrt(g*R*T_inf)
        ! u = 0.0
        v = 0
        T = T_inf
        e = Cv*T
    elseif (resume_simulation .eq. 1) then ! resume simulation
        call read_prevSolFile()
    else
        print *,"invalid value in variable : resume_simulation"
        ERROR stop
    endif

    print *,"initialization done"

end subroutine initializer

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
            X(j,i) = float(i-1)*deltaX
            Y(j,i) = float(j-1)*deltaY
        end do
    end do

    print *,"grid generated"


end subroutine generateGrid


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

    ! using derived datatype to write a csv file line
    Type :: csv_data
        real(kind=rkd) :: X
        real(kind=rkd) :: Y
        real(kind=rkd) :: Z
        real(kind=rkd) :: u
        real(kind=rkd) :: v
        real(kind=rkd) :: p
        real(kind=rkd) :: rho
        real(kind=rkd) :: T
        real(kind=rkd) :: Mach
    end type csv_data

    type(csv_data) :: CSVFile_line


    ! creating new directory to store the computed data
    call system("rm -rf solution_files")
    call system("mkdir solution_files")

    ! opening file
    open(unit = 1, file = "solution_files/data.csv")

    ! writing header
    write(unit = 1, fmt = '(A)') "X,Y,Z,u,v,p,rho,T,Mach"

    ! format specifier
    50 format(f16.10","f16.10","f16.10","f16.10","f16.5","f16.5","f16.5 &
                    ","f16.5","f16.5)

    ! ! looping through the nodes
    ! do i = 1,Nx
    !     do j = 1,Ny
    !         write(unit = 1, fmt = 50) X(j,i),Y(j,i),0.0,u(j,i),v(j,i),p(j,i), &
    !                             rho(j,i),T(j,i),Mach(j,i)
    !     end do
    ! end do

    ! looping through the nodes
    do i = 1,Nx
        do j = 1,Ny
            ! populating CSVFile_line
            CSVFile_line%X = X(j,i)
            CSVFile_line%Y = Y(j,i)
            CSVFile_line%Z = 0.0
            CSVFile_line%u = u(j,i)
            CSVFile_line%v = v(j,i)
            CSVFile_line%p = p(j,i)
            CSVFile_line%rho = rho(j,i)
            CSVFile_line%T = T(j,i)
            CSVFile_line%Mach = Mach(j,i)

            write(unit = 1, fmt = 50) CSVFile_line
        end do
    end do

    ! closing file
    close(unit = 1)

    print *,"written data to file"

end subroutine write_csv

! resume simulation subroutine-------------------------------------------------
subroutine read_prevSolFile()

    use parameters
    use modelVars

    implicit none

    ! using derived datatype to read a csv file line
    Type :: csv_data
        real(kind=rkd) :: X
        real(kind=rkd) :: Y
        real(kind=rkd) :: Z
        real(kind=rkd) :: u
        real(kind=rkd) :: v
        real(kind=rkd) :: p
        real(kind=rkd) :: rho
        real(kind=rkd) :: T
        real(kind=rkd) :: Mach
    end type csv_data

    ! declaring local variables
    character(len = 100) :: junk
    integer(kind=ikd) :: i,j
    type(csv_data) :: CSVFile_line

    print *,"Resume func called"

    ! opening file to read
    open(unit = 1, file="solution_files_backup/data.csv")

    ! reading header and disposing
    read(unit = 1, fmt = '(A)') junk

    ! looping through to get node values and assigning to field variables
    do i = 1,Nx
        do j = 1,Ny
            read(unit = 1, fmt=*) CSVFile_line
            X(j,i) = CSVFile_line%X
            Y(j,i) = CSVFile_line%Y
            u(j,i) = CSVFile_line%u
            v(j,i) = CSVFile_line%v
            p(j,i) = CSVFile_line%p
            rho(j,i) = CSVFile_line%rho
            T(j,i) = CSVFile_line%T
        end do
    end do

    ! closing file
    close(unit=1)

end subroutine read_prevSolFile
