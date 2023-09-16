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

    ! initializing flow field variables based on fresh or resume simulation
    if (resume_simulation .eq. 0) then ! fresh start of simulation
        ! generating grid
        call generateGrid()

        ! initializing flow field primitive variables
        p = P_inf
        rho = P_inf/R/T_inf
        u = M_inf*sqrt(g*R*T_inf)
        ! u = 0.0
        v = 0
        T = T_inf
        e = Cv*T
    elseif (resume_simulation .eq. 1) then ! resume simulation
        call read_prevSolFile()
    else
        print *,"invalid value in variable : resume_simulation"
        ERROR stop
    endif

    call apply_bc()

    ! calling subroutine to initialize k and mu
    call compute_k_mu()

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
    mu = mu0*(T/T0)**(3.0/2.0)*(T0+110.0)/(T+110.0)

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
    ! U5 = rho*(e + (u**2+v**2)/2.0)
    U5 = rho*(Cv*T + (u**2+v**2)/2.0)

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
    ! E5 = rho*u*(e+(u**2+v**2)/2.0) + u*p - u*Txx - v*Txy + qx
    E5 = rho*u*(Cv*T+(u**2+v**2)/2.0) + u*p - u*Txx - v*Txy + qx

    ! computing F's
    F1 = rho*v
    F2 = rho*u*v - Txy
    F3 = rho*v**2 + p - Tyy
    ! F5 = rho*v*(e+(u**2+v**2)/2.0) + v*p - u*Txy - v*Tyy + qy
    F5 = rho*v*(Cv*T+(u**2+v**2)/2.0) + v*p - u*Txy - v*Tyy + qy

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
    real(kind=rkd), dimension(Ny,Nx) :: dT_CFL, a

    ! computing speed of sound
    a = sqrt(g*R*T)

    ! calculating CFL timesteps
    dT_CFL = 1.0/(abs(u)/deltaX + abs(v)/deltaY + a*sqrt(1.0/deltaX**2 +  &
            1.0/deltaY**2) + 2.0*mu/rho*(1.0/deltaX**2 + 1.0/deltaY**2))

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
    convergenceResidual = maxval(abs(rho_old - rho))

    ! updating rho
    rho_old = rho

end subroutine check_convergence

! resume simulation subroutine-------------------------------------------------
subroutine read_prevSolFile()

    use parameters
    use modelVars

    implicit none

    ! using derived datatype to read a csv file line
    Type :: csv_data
        real(kind=rkd) :: X
        real(kind=rkd) :: Y
        real(kind=rkd) :: Z
        real(kind=rkd) :: u
        real(kind=rkd) :: v
        real(kind=rkd) :: p
        real(kind=rkd) :: rho
        real(kind=rkd) :: T
        real(kind=rkd) :: Mach
    end type csv_data

    ! declaring local variables
    character(len = 100) :: junk
    integer(kind=ikd) :: i,j
    type(csv_data) :: CSVFile_line

    print *,"Reading data from previous solution file"

    ! opening file to read
    open(unit = 1, file="solution_files/data.csv")

    ! reading header and disposing
    read(unit = 1, fmt = '(A)') junk

    ! looping through to get node values and assigning to field variables
    do i = 1,Nx
        do j = 1,Ny
            read(unit = 1, fmt=*) CSVFile_line
            X(j,i) = CSVFile_line%X
            Y(j,i) = CSVFile_line%Y
            u(j,i) = CSVFile_line%u
            v(j,i) = CSVFile_line%v
            p(j,i) = CSVFile_line%p
            rho(j,i) = CSVFile_line%rho
            T(j,i) = CSVFile_line%T
        end do
    end do

    ! closing file
    close(unit=1)

end subroutine read_prevSolFile
