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
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! computing postprocessing variables
    Mach = sqrt((u**2+v**2)/(g*R*T))

    ! checking file type to write
    if (fileType == "csv") then
        call write_csv()
    elseif (fileType == "visit") then
        call write_visit()
    elseif (fileType == "hdf5") then
        call write_hdf5()
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
    write(unit = 1, fmt = '(A)') "X,Y,Z,u,v,p,rho,T,Mach"

    ! format specifier
    50 format(f16.10","f16.10","f16.10","f16.10","f16.5","f16.5","f16.5 &
                    ","f16.5","f16.5)

    ! looping through the nodes
    do i = 1,Nx
        do j = 1,Ny
            write(unit = 1, fmt = 50) X(j,i),Y(j,i),0.0,u(j,i),v(j,i),p(j,i), &
                                rho(j,i),T(j,i),Mach(j,i)
        end do
    end do

    ! closing file
    close(unit = 1)

    print *,"written data to file"

end subroutine write_csv

! visit file writer subroutine
! definition-------------------------------------------------------------------
subroutine write_visit()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! creating new directory to store the computed data
    call system("rm -rf solution_files_visit")
    call system("mkdir solution_files_visit")

    ! writing point3D files
    call write_point3D(u,"u")
    call write_point3D(v,"v")
    call write_point3D(p,"p")
    call write_point3D(rho,"rho")
    call write_point3D(T,"T")
    call write_point3D(Mach,"Mach")

    contains

        subroutine write_point3D(field,fieldName)

            implicit none

            character(len=*),intent(in) :: fieldName
            real(kind=rkd),dimension(Ny,Nx), intent(in) :: field
            integer(kind=ikd) :: i,j


            ! preparing fileName
            character(len=50) :: fileName
            write(fileName,'(A)') "solution_files_visit/"//fieldName//".3D"

            print *,"writing file : ",fileName

            ! opening file and writing header
            open(unit = 1, file=fileName)
            write(unit = 1, fmt='(A)') "X Y "//fieldName
            write(unit = 1, fmt='(A)') "#coordflag xyv"

            ! preparing format to store values
            50 format(es14.8" "es14.8" "es14.8)

            ! writing values to file
            do i = 1,Nx
                do j = 1,Ny
                    write(unit = 1, fmt=50) X(j,i),Y(j,i),field(j,i)
                end do
            end do

            ! closing file
            close(unit = 1)

        end subroutine write_point3D

end subroutine write_visit

! HDF5 file writer subroutine
! definition-------------------------------------------------------------------
subroutine write_hdf5()

    ! imporing needed modules
    use parameters
    use modelVars
    use hdf5

    ! overriding automatic variable type assignment
    implicit none


    !the dataset filename
    character(len=50), parameter :: filename = "solution_files_hdf5/data.h5"

    !dataset rank is 2
    integer :: rank = 2

    integer(HID_T) :: file_id       ! File identifier
    integer(HID_T) :: dset_id       ! Dataset identifier
    integer(HID_T) :: dataspace     ! Dataspace identifier
    integer(HID_T) :: memspace      ! Memory dataspace identifier
    integer(HID_T) :: crp_list      ! Dataset creation property identifier

    !dataset dimensions at creation time
    integer(hsize_t), dimension(1:2) :: dims = (/Nx,Ny/)

    ! variables for reading and writing
    real, dimension(Nx,Ny)  :: data1
    integer(hsize_t), dimension(1:2) :: data_dims

    !flag to check operation success
    integer :: error

    !initialize fortran predefined datatypes
    call h5open_f(error)

    !create a new file using default properties.
    call h5fcreate_f(filename, H5F_ACC_TRUNC_F, file_id, error)

    !create the data space for writing solution fields
    call h5screate_simple_f(RANK, dims, dataspace, error)

    ! writing Mach field-------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "Mach", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(Mach) ! need to transpose for proper display

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)

    ! writing u field----------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "u", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(u)

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)

    ! writing v field----------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "v", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(v)

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)

    ! writing p field----------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "p", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(p)

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)

    ! writing rho field----------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "rho", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(rho)

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)

    ! writing T field----------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "T", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(T)

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)

    ! writing X field----------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "X", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(X)

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)

    ! writing Y field----------------------------------------------------------
    !create a dataset to store each single variable
    call h5dcreate_f(file_id, "Y", H5T_NATIVE_REAL, dataspace, &
       dset_id, error)

   ! taking a copy of field variable due to datatype inconsistency
    data1 = transpose(Y)

    !write data array to dataset
    call h5dwrite_f(dset_id, H5T_NATIVE_REAL, data1, dims, error)


    !close the objects that were opened.
    call h5sclose_f(dataspace, error)
    call h5dclose_f(dset_id, error)
    call h5fclose_f(file_id, error)


    !close fortran predefined datatypes
    call h5close_f(error)

    print *,"written HDF5 file"

end subroutine write_hdf5
