!------------------------------------------------------------------------------
! single composed neurons curve fit program : subroutines definition
!------------------------------------------------------------------------------

! write data to file
subroutine write_data()

    use parameters
    use variables

    implicit none

    ! opening new file pointer
    open(unit=1,file = "estimation.csv", status="replace")

    ! writing data to file
    write(unit=1,fmt="(A)") "x y y_pred"
    do i = 1,N_size
        write(unit=1, fmt=*) x(i),y(i),y_pred(i)
    end do

    ! closing file
    close(unit=1)

end subroutine write_data
