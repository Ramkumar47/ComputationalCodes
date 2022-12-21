!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: initialization and calculation file
! description:
!    it contains subroutines related to computation fields initialization
!    and calculation
!------------------------------------------------------------------------------

! initializer subroutine
! definition-------------------------------------------------------------------
subroutine initializer()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! generating grid
    call generateGrid()

    ! initializing flow field primitive variables
    p = P_inf
    rho = P_inf/R/T_inf
    u = 0
    v = 0
    T = T_inf
    e = Cv*T

    ! calling subroutine to initialize k and mu
    call compute_k_mu()

    ! calling subroutine to populate differentiation matrices
    call populate_diffMatrices()

    ! calling subroutie to compute U's
    call compute_Us()

    print *,"initialization done"

end subroutine initializer

! k and mu computation
! subroutine-------------------------------------------------------------------
subroutine compute_k_mu()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! computing mu using sutherlands equation
    mu = mu0*(T/T0)**(3.0/2.0)*(T0+110)/(T+110)

    ! computing thermal conductivity k using Prandtl number
    k = mu*Cp/Pr

end subroutine compute_k_mu

! computing U's i.e. conservative variable
! values-----------------------------------------------------------------------
subroutine compute_Us()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! computing Us
    U1 = rho
    U2 = rho*u
    U3 = rho*v
    U5 = rho*(e + (u**2+v**2)/2.0)

end subroutine compute_Us

! computing primitive variables from U's conservative
! variables--------------------------------------------------------------------
subroutine compute_primitives()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! computing primitive variables
    rho = U1
    u = U2/U1
    v = U3/U1
    e = U5/U1 - (u**2 + v**2)/2.0
    T = e/Cv
    p = rho*R*T

end subroutine compute_primitives

! computing E & F conservative variables from
! primitives-------------------------------------------------------------------
subroutine compute_E_F()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! computing E's
    E1 = rho*u
    E2 = rho*u**2 + p - Txx
    E3 = rho*u*v - Txy
    E5 = rho*u*(e+(u**2+v**2)/2) + u*p - u*Txx - v*Txy + qx

    ! computing F's
    F1 = rho*v
    F2 = rho*u*v - Txy
    F3 = rho*v**2 + p - Tyy
    F5 = rho*v*(e+(u**2+v**2)/2) + u*p - u*Txy - v*Tyy + qy

end subroutine compute_E_F

! computing shear stresses and heat
! fluxes-----------------------------------------------------------------------
subroutine compute_tau_q()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! assuming that the derivatives are already computed

    ! computing shear stresses
    Txx = -2.0/3.0*mu*(dudx + dvdy) + 2.0*mu*dudx
    Tyy = -2.0/3.0*mu*(dudx + dvdy) + 2.0*mu*dvdy
    Txy = mu*(dudy + dvdx)

    ! computing heat flux
    qx = -k*dTdx
    qy = -k*dTdy

end subroutine compute_tau_q

! computing deltaT using CFL
! equation---------------------------------------------------------------------
subroutine compute_deltaT()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! declaring new local variables used in calculation
    real(kind=rkd), dimension(Nx,Ny) :: dT_CFL, a

    ! computing speed of sound
    a = sqrt(g*R*T)

    ! calculating CFL timesteps
    dT_CFL = (abs(u)/deltaX + abs(v)/deltaY + a*sqrt(1.0/deltaX**2 +  &
            1.0/deltaY**2) + 2*mu/rho*(1.0/deltaX**2 + 1.0/deltaY**2))**(-1.0)

    ! taking minimum of CFL timesteps as the chosen timestep
    deltaT = minval(K_num*dT_CFL)

end subroutine compute_deltaT

! subroutine to check convergence of
! solution---------------------------------------------------------------------
subroutine check_convergence()

    ! importing needed modules
    use parameters
    use modelVars

    ! overriding automatic variable type assignment
    implicit none

    ! computing residual
    convergenceResidual = minval(abs(rho_old - rho))

    ! updating rho
    rho_old = rho

end subroutine check_convergence
