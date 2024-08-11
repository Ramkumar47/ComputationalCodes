program main

    implicit none

    integer, parameter :: ikd = selected_int_kind(8), rkd = selected_real_kind(8,8)
    integer, parameter :: dp = kind(1.0d0)

    real(kind=dp), dimension(10) :: rn1,rn2,z0,z1
    real(kind=dp), parameter :: pi = 4.0*atan(1.0)
    integer :: i

    call random_number(rn1)
    call random_number(rn2)

    z0 = sqrt(-2.0*log(rn1))*cos(2.0*pi*rn2)
    z1 = sqrt(-2.0*log(rn1))*sin(2.0*pi*rn2)


    print *,z0
    print *,"\n"
    print *,rn2

    open(unit=1,file="test.csv",status="replace")

    do i = 1,10
        write(unit=1,fmt=*) z0(i), rn1(i),rn2(i)
    end do

    close(unit=1)

end program main
