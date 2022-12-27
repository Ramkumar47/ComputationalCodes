!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: main program file
! description:
!    it contains the main program snippet
!------------------------------------------------------------------------------

! main program begin
program main

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring local variables
    integer(kind=ikd) :: icount = 0

    ! calling initializer subroutine
    call initializer()

    call write_csv()
    print *,"End"

end program main
