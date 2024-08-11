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
    do i = 1,N_data
        write(unit=1, fmt=*) x(i),y(i),y_pred(i)
    end do

    ! closing file
    close(unit=1)

end subroutine write_data

! reading training data
subroutine read_training_data()

    use parameters
    use variables

    implicit none

    ! opening file to read data
    open(unit = 1, file = datafile_name, status = "old")

    ! reading data to variable
    do i = 1,N_data
        read(unit=1, fmt=*) x(i),y(i)
    end do

    ! closing file
    close(unit=1)

    print *,"training data read done"

end subroutine read_training_data

! saving loss value
subroutine save_loss_values()

    use parameters
    use variables

    implicit none

    ! opening file to write loss value
    open(unit=1, file = "loss.csv", status = "replace")

    ! writing loss values to file
    do i = 1,N_epochs
        write(unit=1, fmt=*) lossValues(i)
    end do

    ! closing file
    close(unit=1)

    print *,"saved loss values"

end subroutine save_loss_values
