!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: Maccormack solver file
! description:
!    it contains the Maccormack solver related subroutine(s)
!------------------------------------------------------------------------------

! Maccormack solver subroutine definition
subroutine Maccormack_solver()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring needed local variables
    real(kind=rkd), dimension(Ny,Nx) :: U1s,U2s,U3s,U5s
    integer(kind=ikd) :: i,j

    ! taking a copy of initial U's to be used in corrector step
    U1s = U1; U2s = U2; U3s = U3; U5s = U5

    ! predictor step-----------------------------------------------------------

    ! computing needed derivatives for E's
    do i = 2,Nx ! backward differencing in x direction
        do j = 2,Ny-1 ! central differencing in y direction
            dudx(j,i) = (u(j,i) - u(j,i-1))/deltaX
            dudy(j,i) = (u(j+1,i) - u(j-1,i))/2.0/deltaY
            dvdx(j,i) = (v(j,i) - v(j,i-1))/deltaX
            dvdy(j,i) = (v(j+1,i) - v(j-1,i))/2.0/deltaY
            dTdx(j,i) = (T(j,i) - T(j,i-1))/deltaX
        end do
        dudy(1,:) = (u(2,:) - u(1,:))/deltaY
        dvdy(1,:) = (v(2,:) - v(1,:))/deltaY
        dudy(Ny,:) = (u(Ny,:) - u(Ny-1,:))/deltaY
        dvdy(Ny,:) = (v(Ny,:) - v(Ny-1,:))/deltaY
    end do
    dudx(:,1) = (u(:,2) - u(:,1))/deltaX
    dvdx(:,1) = (v(:,2) - v(:,1))/deltaX

    ! computing shear stresses
    Txx = -2.0/3.0*mu*(dudx + dvdy) + 2.0*mu*dudx
    Txy = mu*(dudy + dvdx)

    ! computing heat flux
    qx = -k*dTdx

    ! computing E's
    E1 = rho*u
    E2 = rho*u**2 + p - Txx
    E3 = rho*u*v - Txy
    E5 = rho*u*(e+(u**2+v**2)/2.0) + u*p - u*Txx - v*Txy + qx

    ! computing needed derivatives for F's
    do i = 2,Nx-1 ! central differencing in x direction
        do j = 2,Ny ! backward differencing in y direction
            dudx(j,i) = (u(j,i+1) - u(j,i-1))/deltaX/2.0
            dudy(j,i) = (u(j,i) - u(j-1,i))/deltaY
            dvdx(j,i) = (v(j,i+1) - v(j,i-1))/deltaX/2.0
            dvdy(j,i) = (v(j,i) - v(j-1,i))/deltaY
            dTdy(j,i) = (T(j,i) - T(j-1,i))/deltaY
        end do
        dudx(:,1) = (u(:,2) - u(:,1))/deltaX
        dvdx(:,1) = (v(:,2) - v(:,1))/deltaX
        dudx(:,Nx) = (u(:,Nx) - u(:,Nx-1))/deltaX
        dvdx(:,Nx) = (v(:,Nx) - v(:,Nx-1))/deltaX
    end do
    dudy(1,:) = (u(2,:) - u(1,:))/deltaY
    dvdy(1,:) = (v(2,:) - v(1,:))/deltaY

    ! computing shear stresses
    Tyy = -2.0/3.0*mu*(dudx + dvdy) + 2.0*mu*dvdy
    Txy = mu*(dudy + dvdx)

    ! computing heat flux
    qy = -k*dTdy

    ! computing F's
    F1 = rho*v
    F2 = rho*u*v - Txy
    F3 = rho*v**2 + p - Tyy
    F5 = rho*v*(e+(u**2+v**2)/2.0) + v*p - u*Txy - v*Tyy + qy

    ! computing derivatives of F and E
    do i = 1,Nx-1 ! forward differencing in x direction
        dE1dx(:,i) = (E1(:,i+1) - E1(:,i))/deltaX
        dE2dx(:,i) = (E2(:,i+1) - E2(:,i))/deltaX
        dE3dx(:,i) = (E3(:,i+1) - E3(:,i))/deltaX
        dE5dx(:,i) = (E5(:,i+1) - E5(:,i))/deltaX
    end do
    dE1dx(:,Nx) = (E1(:,Nx) - E1(:,Nx-1))/deltaX
    dE2dx(:,Nx) = (E2(:,Nx) - E2(:,Nx-1))/deltaX
    dE3dx(:,Nx) = (E3(:,Nx) - E3(:,Nx-1))/deltaX
    dE5dx(:,Nx) = (E5(:,Nx) - E5(:,Nx-1))/deltaX

    do j = 1,Ny-1 ! forward differencing in y direction
        dF1dy(j,:) = (F1(j+1,:) - F1(j,:))/deltaY
        dF2dy(j,:) = (F2(j+1,:) - F2(j,:))/deltaY
        dF3dy(j,:) = (F3(j+1,:) - F3(j,:))/deltaY
        dF5dy(j,:) = (F5(j+1,:) - F5(j,:))/deltaY
    end do
    dF1dy(Ny,:) = (F1(Ny,:) - F1(Ny-1,:))/deltaY
    dF2dy(Ny,:) = (F2(Ny,:) - F2(Ny-1,:))/deltaY
    dF3dy(Ny,:) = (F3(Ny,:) - F3(Ny-1,:))/deltaY
    dF5dy(Ny,:) = (F5(Ny,:) - F5(Ny-1,:))/deltaY

    ! computing dUdt's
    dU1dt = -dE1dx - dF1dy
    dU2dt = -dE2dx - dF2dy
    dU3dt = -dE3dx - dF3dy
    dU5dt = -dE5dx - dF5dy

    ! computing barred U's
    U1 = U1 + dU1dt*deltaT
    U2 = U2 + dU2dt*deltaT
    U3 = U3 + dU3dt*deltaT
    U5 = U5 + dU5dt*deltaT

    ! computing back the primitive variables for corrector step
    call compute_primitives()

    call apply_bc()

    call compute_k_mu()

    ! corrector step-----------------------------------------------------------
    ! computing needed derivatives for E's
    do i = 1,Nx-1 ! forward differencing in x direction
        do j = 2,Ny-1 ! central differencing in y direction
            dudx(j,i) = (u(j,i+1) - u(j,i))/deltaX
            dudy(j,i) = (u(j+1,i) - u(j-1,i))/2.0/deltaY
            dvdx(j,i) = (v(j,i+1) - v(j,i))/deltaX
            dvdy(j,i) = (v(j+1,i) - v(j-1,i))/2.0/deltaY
            dTdx(j,i) = (T(j,i+1) - T(j,i))/deltaX
        end do
        dudy(1,:) = (u(2,:) - u(1,:))/deltaY
        dvdy(1,:) = (v(2,:) - v(1,:))/deltaY
        dudy(Ny,:) = (u(Ny,:) - u(Ny-1,:))/deltaY
        dvdy(Ny,:) = (v(Ny,:) - v(Ny-1,:))/deltaY
    end do
    dudx(:,Nx) = (u(:,Nx) - u(:,Nx-1))/deltaX
    dvdx(:,Nx) = (v(:,Nx) - v(:,Nx-1))/deltaX

    ! computing shear stresses
    Txx = -2.0/3.0*mu*(dudx + dvdy) + 2.0*mu*dudx
    Txy = mu*(dudy + dvdx)

    ! computing heat flux
    qx = -k*dTdx

    ! computing E's
    E1 = rho*u
    E2 = rho*u**2 + p - Txx
    E3 = rho*u*v - Txy
    E5 = rho*u*(e+(u**2+v**2)/2.0) + u*p - u*Txx - v*Txy + qx

    ! computing needed derivatives for F's
    do i = 2,Nx-1 ! central differencing in x direction
        do j = 1,Ny-1 ! forward differencing in y direction
            dudx(j,i) = (u(j,i+1) - u(j,i-1))/deltaX/2.0
            dudy(j,i) = (u(j+1,i) - u(j,i))/deltaY
            dvdx(j,i) = (v(j,i+1) - v(j,i-1))/deltaX/2.0
            dvdy(j,i) = (v(j+1,i) - v(j,i))/deltaY
            dTdy(j,i) = (T(j+1,i) - T(j,i))/deltaY
        end do
        dudx(:,1) = (u(:,2) - u(:,1))/deltaX
        dvdx(:,1) = (v(:,2) - v(:,1))/deltaX
        dudx(:,Nx) = (u(:,Nx) - u(:,Nx-1))/deltaX
        dvdx(:,Nx) = (v(:,Nx) - v(:,Nx-1))/deltaX
    end do
    dudy(Ny,:) = (u(Ny,:) - u(Ny-1,:))/deltaY
    dvdy(Ny,:) = (v(Ny,:) - v(Ny-1,:))/deltaY

    ! computing shear stresses
    Tyy = -2.0/3.0*mu*(dudx + dvdy) + 2.0*mu*dvdy
    Txy = mu*(dudy + dvdx)

    ! computing heat flux
    qy = -k*dTdy

    ! computing F's
    F1 = rho*v
    F2 = rho*u*v - Txy
    F3 = rho*v**2 + p - Tyy
    F5 = rho*v*(e+(u**2+v**2)/2.0) + v*p - u*Txy - v*Tyy + qy

    ! computing derivatives of F and E
    do i = 2,Nx ! backward differencing in x direction
        dE1dx(:,i) = (E1(:,i) - E1(:,i-1))/deltaX
        dE2dx(:,i) = (E2(:,i) - E2(:,i-1))/deltaX
        dE3dx(:,i) = (E3(:,i) - E3(:,i-1))/deltaX
        dE5dx(:,i) = (E5(:,i) - E5(:,i-1))/deltaX
    end do
    dE1dx(:,1) = (E1(:,2) - E1(:,1))/deltaX
    dE2dx(:,1) = (E2(:,2) - E2(:,1))/deltaX
    dE3dx(:,1) = (E3(:,2) - E3(:,1))/deltaX
    dE5dx(:,1) = (E5(:,2) - E5(:,1))/deltaX

    do j = 2,Ny ! backward differencing in y direction
        dF1dy(j,:) = (F1(j,:) - F1(j-1,:))/deltaY
        dF2dy(j,:) = (F2(j,:) - F2(j-1,:))/deltaY
        dF3dy(j,:) = (F3(j,:) - F3(j-1,:))/deltaY
        dF5dy(j,:) = (F5(j,:) - F5(j-1,:))/deltaY
    end do
    dF1dy(1,:) = (F1(2,:) - F1(1,:))/deltaY
    dF2dy(1,:) = (F2(2,:) - F2(1,:))/deltaY
    dF3dy(1,:) = (F3(2,:) - F3(1,:))/deltaY
    dF5dy(1,:) = (F5(2,:) - F5(1,:))/deltaY

    ! computing dUdt's
    dU1dt_bar = -dE1dx - dF1dy
    dU2dt_bar = -dE2dx - dF2dy
    dU3dt_bar = -dE3dx - dF3dy
    dU5dt_bar = -dE5dx - dF5dy

    ! computing barred U's
    U1 = U1s + 0.5*(dU1dt+dU1dt_bar)*deltaT
    U2 = U2s + 0.5*(dU2dt+dU2dt_bar)*deltaT
    U3 = U3s + 0.5*(dU3dt+dU3dt_bar)*deltaT
    U5 = U5s + 0.5*(dU5dt+dU5dt_bar)*deltaT

    ! computing back the primitive variables for corrector step
    call compute_primitives()

    call apply_bc()

    call compute_k_mu()

end subroutine Maccormack_solver
