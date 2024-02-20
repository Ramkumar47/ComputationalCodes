!------------------------------------------------------------------------------
! Particle Swarm Optimization
! subroutines definition
!------------------------------------------------------------------------------

! writing data to file
subroutine writeData()

    use parameters
    use modelVariables

    implicit none

    50 format(f12.5,",",f12.5,",",f12.5)

    write(unit=1,fmt=50) gbest(1),gbest(2),f_gbest

end subroutine writeData

! initializer subroutine
subroutine initializer()
    use parameters
    use modelVariables

    implicit none

    integer(kind=ikd) :: i,j
    integer(kind=ikd),dimension(1) :: tmp1
    real(kind=rkd) :: tmp

    ! initializing PSO variables
    call random_number(x)
    call random_number(v)
    call random_number(Pbest)
    call random_number(Gbest)

    x = x*(x_bc(2) - x_bc(1)) + x_bc(1)
    v = v*(v_bc(2) - v_bc(1)) + v_bc(1)
    Pbest = Pbest*(x_bc(2) - x_bc(1)) + x_bc(1)
    Gbest = Gbest*(x_bc(2) - x_bc(1)) + x_bc(1)

    ! evaluating objective function
    do i = 1,Np
        call f_obj(x(i,:),tmp)
        f_eval(i) = tmp
        f_pbest(i) = tmp
    end do

    ! getting minimum value location
    tmp1 = minloc(f_eval) ! returns an array of size 1, not scalar
    i = tmp1(1)

    ! initializing Gbest
    Gbest = Pbest(i,:)

    ! opening file for writing computed data
    open(unit = 1,file = filename, status="replace")
    write(unit = 1,fmt=*) "x_best,y_best,f_eval"

end subroutine initializer

! velocity update subroutine
subroutine updateVelocity()

    use parameters
    use modelVariables

    implicit none

    integer(kind=ikd) :: i,j

    ! updating random weights
    call random_number(r1)
    call random_number(r2)

    ! looping through particles
    do i = 1,Np
        do j = 1,Nd
            v_np1(i,j) = v(i,j)*w +c1*r1(i,j)*(Pbest(i,j) - x(i,j)) + c2*r2(i,j)*(Gbest(j)-x(i,j))
        end do
    end do

end subroutine updateVelocity

! position update subroutine
subroutine updatePosition()

    use parameters
    use modelVariables

    implicit none

    integer(kind=ikd) :: i,j

    x_np1 = x + v_np1

end subroutine updatePosition

! pbest and gbest computing subroutine
subroutine computePbestGbest()

    use parameters
    use modelVariables

    implicit none

    integer(kind=ikd) :: i
    integer(kind=rkd),dimension(1) :: idx
    real(kind=rkd) :: f_np1

    ! looping to update pbests
    do i = 1,Np
        ! computing objective function at new x
        call f_obj(x_np1(i,:),f_np1)

        ! updating Pbest
        if (f_np1 < f_pbest(i)) then
            Pbest(i,:) = x_np1(i,:)
            f_pbest(i) = f_np1
        end if
        f_eval(i) = f_np1

        x(i,:) = x_np1(i,:)
        v(i,:) = v_np1(i,:)

    end do

    ! getting minimum value location
    idx = minloc(f_pbest) ! returns an array of size 1, not scalar
    i = idx(1)

    ! initializing Gbest
    Gbest = Pbest(i,:)
    f_gbest = f_pbest(i)

end subroutine computePbestGbest
