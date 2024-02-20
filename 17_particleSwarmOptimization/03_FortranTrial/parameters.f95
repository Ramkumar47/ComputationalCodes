!------------------------------------------------------------------------------
! Particle Swarm Optimization
! Parameter variables definition
!------------------------------------------------------------------------------

module parameters

    implicit none

    ! defining data type
    integer, parameter :: ikd = selected_int_kind(8), rkd =selected_real_kind(8,8)

    ! number of particles and design variables
    integer(kind=ikd), parameter :: Np = 101, Nd = 2

    ! bounding values
    real(kind=rkd),parameter,dimension(2) :: x_bc = (/-4.5,4.5/), v_bc = (/-0.1,0.1/)

    ! PSO weights
    real(kind=rkd),parameter :: w = 0.7, c1 = 0.2, c2 = 0.2

    ! maximum number of iterations
    integer(kind=ikd), parameter :: N_itr = 100

    ! output filename
    character(len=*), parameter :: filename = "computed_data.csv"

    contains

        ! objective function subroutine
        subroutine f_obj(xi,fval)

            implicit none

            real(kind=rkd), dimension(Nd), intent(in) :: xi
            real(kind=rkd), intent(out) :: fval
            integer(kind=ikd) :: i

            ! evalutating the function ! sphere function
            fval = 0
            do i = 1,Nd
                fval = fval + xi(i)**2
            end do

            ! ! evalutating the function ! Beale function
            ! fval = (1.5-xi(1)+xi(1)*xi(2))**2 + (2.25 -xi(1)+xi(1)*xi(2)**2)**2 &
            !     + (2.625-xi(1)+xi(1)*xi(2)**3)**2

            ! ! evalutating the function ! Booth function
            ! fval = (xi(1)+2*xi(2)-7)**2+(2*xi(1)+xi(2)-5)**2

        end subroutine f_obj

end module parameters
