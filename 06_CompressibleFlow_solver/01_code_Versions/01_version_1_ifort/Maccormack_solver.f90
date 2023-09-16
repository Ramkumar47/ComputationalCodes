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
    use differentiation

    ! overriding automatic variable type assignment
    implicit none

    ! declaring needed local variables
    real(kind=rkd), dimension(Ny,Nx) :: U1s,U2s,U3s,U5s

    ! taking a copy of initial U's to be used in corrector step
    U1s = U1; U2s = U2; U3s = U3; U5s = U5

    ! predictor step-----------------------------------------------------------
    ! computing needed derivatives for E's
    dudx = matmul(u,Mddx_backward)
    dudy = matmul(Mddy_central,u)
    dvdx = matmul(v,Mddx_backward)
    dvdy = matmul(Mddy_central,v)
    dTdx = matmul(T,Mddx_backward)

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
    dudx = matmul(u,Mddx_central)
    dudy = matmul(Mddy_backward,u)
    dvdx = matmul(v,Mddx_central)
    dvdy = matmul(Mddy_backward,v)
    dTdy = matmul(Mddy_backward,T)

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
    dE1dx = matmul(E1,Mddx_forward)
    dE2dx = matmul(E2,Mddx_forward)
    dE3dx = matmul(E3,Mddx_forward)
    dE5dx = matmul(E5,Mddx_forward)

    dF1dy = matmul(Mddy_forward,F1)
    dF2dy = matmul(Mddy_forward,F2)
    dF3dy = matmul(Mddy_forward,F3)
    dF5dy = matmul(Mddy_forward,F5)

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
    dudx = matmul(u,Mddx_forward)
    dudy = matmul(Mddy_central,u)
    dvdx = matmul(v,Mddx_forward)
    dvdy = matmul(Mddy_central,v)
    dTdx = matmul(T,Mddx_forward)

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
    dudx = matmul(u,Mddx_central)
    dudy = matmul(Mddy_forward,u)
    dvdx = matmul(v,Mddx_central)
    dvdy = matmul(Mddy_forward,v)
    dTdy = matmul(Mddy_forward,T)

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
    dE1dx = matmul(E1,Mddx_backward)
    dE2dx = matmul(E2,Mddx_backward)
    dE3dx = matmul(E3,Mddx_backward)
    dE5dx = matmul(E5,Mddx_backward)

    dF1dy = matmul(Mddy_backward,F1)
    dF2dy = matmul(Mddy_backward,F2)
    dF3dy = matmul(Mddy_backward,F3)
    dF5dy = matmul(Mddy_backward,F5)

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
