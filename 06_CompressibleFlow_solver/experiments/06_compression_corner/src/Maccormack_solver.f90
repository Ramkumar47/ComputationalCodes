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
    call compute_ddx(u,"backward",dudx) ! backward differencing in x direction
    call compute_ddx(v,"backward",dvdx)
    call compute_ddx(T,"backward",dTdx)
    call compute_ddy(u,"central",dudy) ! central differencing in y direction
    call compute_ddy(v,"central",dvdy)

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
    call compute_ddx(u,"central",dudx) ! central differencing in x direction
    call compute_ddx(v,"central",dvdx)
    call compute_ddy(T,"backward",dTdy) ! backward differencing in y direction
    call compute_ddy(u,"backward",dudy)
    call compute_ddy(v,"backward",dvdy)

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
    ! forward differencing in x direction
    call compute_ddx(E1,"forward",dE1dx)
    call compute_ddx(E2,"forward",dE2dx)
    call compute_ddx(E3,"forward",dE3dx)
    call compute_ddx(E5,"forward",dE5dx)

    ! forward differencing in y direction
    call compute_ddy(F1,"forward",dF1dy)
    call compute_ddy(F2,"forward",dF2dy)
    call compute_ddy(F3,"forward",dF3dy)
    call compute_ddy(F5,"forward",dF5dy)

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
    call compute_ddx(u,"forward",dudx) ! forward differencing in x direction
    call compute_ddx(v,"forward",dvdx)
    call compute_ddx(T,"forward",dTdx)
    call compute_ddy(u,"central",dudy) ! central differencing in y direction
    call compute_ddy(v,"central",dvdy)

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
    call compute_ddx(u,"central",dudx) ! central differencing in x direction
    call compute_ddx(v,"central",dvdx)
    call compute_ddy(T,"forward",dTdy) ! forward differencing in y direction
    call compute_ddy(u,"forward",dudy)
    call compute_ddy(v,"forward",dvdy)

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
    ! backward differencing in x direction
    call compute_ddx(E1,"backward",dE1dx)
    call compute_ddx(E2,"backward",dE2dx)
    call compute_ddx(E3,"backward",dE3dx)
    call compute_ddx(E5,"backward",dE5dx)

    ! backward differencing in y direction
    call compute_ddy(F1,"backward",dF1dy)
    call compute_ddy(F2,"backward",dF2dy)
    call compute_ddy(F3,"backward",dF3dy)
    call compute_ddy(F5,"backward",dF5dy)

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
