!------------------------------------------------------------------------------
! supersonic laminar flow over flat plate computation
! developed by Ramkumar
!
! filetype: parameters module
! description:
!    it contains definitions of parametric variables used in computation
!------------------------------------------------------------------------------

! parameters module definition
module parameters

    ! overriding automatic variable type assignment
    implicit none

    ! defining global types for real and integer variables
    integer, parameter :: ikd = selected_int_kind(8)
    integer, parameter :: rkd = selected_real_kind(8,8)

    ! freestream mach number
    real(kind=rkd), parameter :: M_inf = 4.0

    ! freestream pressure and temperature
    real(kind=rkd), parameter :: P_inf = 101325.0 , T_inf = 288.16

    ! ratio of specific heats and gas constant
    real(kind=rkd), parameter :: g = 1.4, R = 287.0

    ! flow Prandtl number
    real(kind=rkd), parameter :: Pr = 0.7

    ! reference viscosity and temperature
    real(kind=rkd), parameter :: mu0 = 1.789e-5, T0 = 288.16

    ! Courant number
    real(kind=rkd), parameter :: K_num = 0.5

    ! Convergence residual value
    real(kind=rkd), parameter :: convergenceValue = 1e-8

    ! number of grid points
    integer(kind=ikd), parameter :: Nx = 100, Ny = 100

    ! domain length and height
    real(kind=rkd), parameter :: L_x = 1e-5, L_y = 7.90569e-6

    ! max simulation time and timestep count
    real(kind=rkd), parameter :: maxSimTime = 1.0
    integer(kind=ikd), parameter :: maxTSCount = 10000

    ! restart/resume simulation from saved data.csv file
    ! 1 - yes; 0 - no
    integer(kind=ikd), parameter :: resume_simulation = 0

    ! file write type
    ! current options are : "csv", "visit", "hdf5"
    character(len = 10) :: fileType = "hdf5"


    ! computing derived parameters---------------------------------------------
    ! specific heats at constant pressure and volume
    real(kind=rkd), parameter :: Cp = g*R/(g-1.0), Cv = R/(g-1.0)

    ! space steps along x and y
    real(kind=rkd), parameter :: deltaX = L_x/float(Nx-1)
    real(kind=rkd), parameter :: deltaY = L_y/float(Ny-1)

end module parameters
