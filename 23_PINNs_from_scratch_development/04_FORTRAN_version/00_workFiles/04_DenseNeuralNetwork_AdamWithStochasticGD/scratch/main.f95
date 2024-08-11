program main

    implicit none

    integer, parameter :: ikd = selected_int_kind(8), rkd = selected_real_kind(8,8)

    real(kind=rkd), dimension(5) :: randomNumbers
    integer(kind=ikd), dimension(5) :: randomIntegers
    integer(kind=ikd), dimension(3) :: indices = (/1,2,4/)


    call random_number(randomNumbers)


    randomIntegers = floor(randomNumbers*10)

    print *,sum(randomIntegers(indices))
    print *,randomIntegers

end program main
